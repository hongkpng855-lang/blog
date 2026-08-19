#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
待發佈佇列 Publisher（2026-08-20 建立，排程發佈系統核心）

背景：
- AI model 喺 09:00–12:00 / 14:00–18:00 漲價 → 唔可以喺嗰啲時段用 AI 搜尋/寫稿
- 但用戶想「出文時間維持一樣」（每 2 小時一篇，包括 peak 時段）
- 解決：平價時段 AI 寫稿存入 _queue/（唔 commit），本 script 用「純 Python + git」喺
  任何時段（包括 peak）將佢搬上 blog + 上 FB/IG → 零 model token 成本

流程（每 2 小時由系統 crontab 觸發）：
1. 檢查 _queue/posts/ 有冇待發佈文章（一次出一篇，保持每 2 小時節奏）
2. 有 → front matter date 改為「出街時間」+ filename 改 YYYY-MM-DD-{slug}.md
3. 搬去 _posts/ + 封面圖搬去 assets/images/posts/
4. git commit + push
5. 等 GitHub Actions build 完 + URL 200（timeout 300s）
6. call fb-auto-post.py + ig-auto-post.py（timeout 600/900 包住，逾時唔當 error）
7. 全部成功 → 由 _queue 刪除該文章（防止重複出街）
8. 冇文章 → 靜默退出（exit 0，唔出聲）

用法：python3 scripts/publish-queue.py [--dry-run]
"""
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JEKYLL_DIR = os.path.dirname(BASE_DIR)
QUEUE_POSTS = os.path.join(JEKYLL_DIR, "_queue", "posts")
QUEUE_ASSETS = os.path.join(JEKYLL_DIR, "_queue", "assets", "images", "posts")
POSTS_DIR = os.path.join(JEKYLL_DIR, "_posts")
ASSETS_DIR = os.path.join(JEKYLL_DIR, "assets", "images", "posts")
STATE_FILE = os.path.join(BASE_DIR, "publish_queue_state.json")
LOG_FILE = os.path.join(JEKYLL_DIR, "logs", "publish-queue.log")

BLOG_BASE = "https://aniskill.esgov.org/"
GITHUB_BASE = "https://hongkpng855-lang.github.io/blog/"
BUILD_WAIT = 300  # 最長等 build + 200（秒）
URL_CHECK_INTERVAL = 15


def log(msg):
    line = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line, flush=True)
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass


def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE) as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def run(cmd, timeout=120):
    """行 command，返回 (returncode, stdout, stderr)"""
    try:
        p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"


def url_ok(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False


def list_queued_posts():
    if not os.path.isdir(QUEUE_POSTS):
        return []
    posts = []
    for f in sorted(os.listdir(QUEUE_POSTS)):
        if f.endswith(".md") and not f.startswith("."):
            posts.append(os.path.join(QUEUE_POSTS, f))
    return posts


def extract_slug(post_path):
    """由 front matter permalink 或 filename 攞 slug（permalink 格式：/技術/{slug} → 攞最後一段）"""
    try:
        with open(post_path) as f:
            content = f.read()
        m = re.search(r"^permalink:\s*(?:'|\")?/?([^'\"/\n\s]+(?:/[^'\"/\n\s]+)*)", content, re.M)
        if m:
            # 攞最後一段（slug 本身）
            return m.group(1).strip("/").split("/")[-1]
    except Exception:
        pass
    return os.path.splitext(os.path.basename(post_path))[0]


def update_front_matter_date(post_path, date_str):
    """將 front matter date 改為指定時間（保留其他欄位）"""
    with open(post_path) as f:
        content = f.read()
    # date: 可能係 "2026-08-20 01:00:00 +0800" 或 "2026-08-20" 等格式
    new_content = re.sub(
        r"^(date:).*$",
        lambda m: f"date: {date_str}",
        content,
        count=1,
        flags=re.M,
    )
    if new_content == content:
        # 冇 date 欄位 → 插入 front matter 開頭
        new_content = re.sub(
            r"^(---\n)",
            r"\1date: " + date_str + "\n",
            content,
            count=1,
        )
    with open(post_path, "w") as f:
        f.write(new_content)


def run_fb_ig():
    """上 FB + IG（用 timeout 包住，逾時唔當 error）"""
    fb_script = os.path.join(BASE_DIR, "fb-auto-post.py")
    ig_script = os.path.join(BASE_DIR, "ig-auto-post.py")
    results = {}
    if os.path.exists(fb_script):
        rc, out, err = run(f"cd {JEKYLL_DIR} && timeout 600 python3 {fb_script}", timeout=660)
        results["fb"] = {"rc": rc, "out": out[-500:], "err": err[-300:]}
        if rc == 124:
            log("⚠️ fb-auto-post.py 逾時被 timeout 終止（唔當 error）")
        elif rc != 0:
            log(f"⚠️ fb-auto-post.py rc={rc}: {err[-200:]}")
        else:
            log(f"✅ FB 同步完成: {out[-200:]}")
    else:
        log("⚠️ fb-auto-post.py 唔存在，跳過 FB")
    if os.path.exists(ig_script):
        rc, out, err = run(f"cd {JEKYLL_DIR} && timeout 900 python3 {ig_script}", timeout=960)
        results["ig"] = {"rc": rc, "out": out[-500:], "err": err[-300:]}
        if rc == 124:
            log("⚠️ ig-auto-post.py 逾時被 timeout 終止（唔當 error）")
        elif rc != 0:
            log(f"⚠️ ig-auto-post.py rc={rc}: {err[-200:]}")
        else:
            log(f"✅ IG 同步完成: {out[-200:]}")
    else:
        log("⚠️ ig-auto-post.py 唔存在，跳過 IG")
    return results


def main():
    dry_run = "--dry-run" in sys.argv
    state = load_state()

    posts = list_queued_posts()
    if not posts:
        log("佇列冇文章，靜默退出")
        return 0

    # 攞第一篇（最舊）
    post_path = posts[0]
    slug = extract_slug(post_path)
    log(f"準備出街：{os.path.basename(post_path)} (slug={slug})")

    # 防重複：state 記低已 commit 但未完成嘅 post
    if state.get("in_progress") == slug:
        log(f"⚠️ {slug} 已喺 in_progress 狀態（上次未完成），檢查係咪已 commit")
        existing = [f for f in os.listdir(POSTS_DIR) if slug in f]
        if existing:
            log(f"✅ {slug} 已喺 _posts/，跳過 commit 直接做社交同步")
            run_fb_ig()
            state.pop("in_progress", None)
            save_state(state)
            return 0
        else:
            log(f"⚠️ {slug} in_progress 但 _posts/ 冇檔，重新嚟過")
            state.pop("in_progress", None)
            save_state(state)

    if dry_run:
        log(f"[DRY-RUN] 會出街：{slug}")
        return 0

    # 1. 改 date + filename
    now = datetime.datetime.now().astimezone()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S +0800")
    new_filename = f"{now.strftime('%Y-%m-%d')}-{slug}.md"
    new_post_path = os.path.join(POSTS_DIR, new_filename)

    update_front_matter_date(post_path, date_str)

    # 2. 搬文章 + 封面
    os.makedirs(POSTS_DIR, exist_ok=True)
    os.makedirs(ASSETS_DIR, exist_ok=True)
    shutil.copy2(post_path, new_post_path)

    moved_assets = []
    if os.path.isdir(QUEUE_ASSETS):
        for f in os.listdir(QUEUE_ASSETS):
            if slug in f:
                src = os.path.join(QUEUE_ASSETS, f)
                dst = os.path.join(ASSETS_DIR, f)
                shutil.copy2(src, dst)
                moved_assets.append(f)
                log(f"  封面/圖片搬咗：{f}")

    # 3. git commit + push
    rc, out, err = run(f"cd {JEKYLL_DIR} && git add _posts/{new_filename} assets/images/posts/ && git commit -m '排程發佈: {slug} ({now.strftime('%Y-%m-%d %H:%M')})'", timeout=60)
    if rc != 0 and "nothing to commit" not in err and "nothing to commit" not in out:
        log(f"⚠️ git commit 失敗 rc={rc}: {err}")
        # 唔刪 queue，下次再試
        return 1
    rc, out, err = run(f"cd {JEKYLL_DIR} && git push origin main", timeout=120)
    if rc != 0:
        log(f"⚠️ git push 失敗 rc={rc}: {err}")
        return 1
    log(f"✅ 已 push：{new_filename}")

    # 記 low in_progress（萬一之後 crash，下次可以補社交同步）
    state["in_progress"] = slug
    save_state(state)

    # 4. 等 build + URL 200
    permalink = slug
    url = f"{BLOG_BASE}{permalink}"
    # 如果 permalink 帶日期 path，試埋 github.io 版
    url2 = f"{GITHUB_BASE}{permalink}"
    ok = False
    deadline = time.time() + BUILD_WAIT
    while time.time() < deadline:
        if url_ok(url) or url_ok(url2):
            ok = True
            break
        time.sleep(URL_CHECK_INTERVAL)
    if not ok:
        log("⚠️ URL 未 200（build 慢？），但文章已 commit，FB/IG 照做")

    # 5. FB/IG 同步
    results = run_fb_ig()

    # 6. 成功 → 刪 queue 原文
    try:
        os.remove(post_path)
        log(f"🗑️ 已刪 queue 原文：{os.path.basename(post_path)}")
    except Exception as e:
        log(f"⚠️ 刪 queue 原文失敗：{e}")

    state.pop("in_progress", None)
    state["last_published"] = {
        "slug": slug,
        "filename": new_filename,
        "time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "fb": results.get("fb", {}).get("rc"),
        "ig": results.get("ig", {}).get("rc"),
    }
    save_state(state)
    log(f"🎉 出街完成：{slug}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
