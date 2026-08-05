#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blog → Instagram 自動發文 script v1
- 檢查 jekyll-blog/_posts/ 有冇新 GitHub 新聞（front matter 有 creator_github + fb_message）
- 有 → 自動 POST 去 IG（封面圖 + fb_message caption + hashtags）
- 記錄已發佈文章，避免重複發佈

用法：python3 ig-auto-post.py
"""
import json
import os
import re
import sys
import fcntl
import time
import urllib.request
import urllib.parse
import datetime

# ---------- 設定 ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JEKYLL_DIR = os.path.dirname(BASE_DIR)
POSTS_DIR = os.path.join(JEKYLL_DIR, "_posts")
SECRETS_DIR = os.path.expanduser("~/.openclaw/workspace/.secrets/ig")
STATE_FILE = os.path.join(BASE_DIR, "ig_posted_state.json")
LOCK_FILE = os.path.join(BASE_DIR, ".ig-auto-post.lock")

IG_TOKEN = open(os.path.join(SECRETS_DIR, "ig_token.txt")).read().strip()
IG_USER_ID = open(os.path.join(SECRETS_DIR, "ig_user_id.txt")).read().strip()
# og:image 用 github.io（FB/IG crawler 可達；custom domain 唔可靠）
BLOG_BASE = "https://hongkpng855-lang.github.io/blog"
API = "https://graph.instagram.com/v25.0"
HASHTAGS = "#AI #開源 #GitHub #LLM #人工智能"


def log(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def acquire_lock():
    """同一時間只允許一個實例（防止重複 post）"""
    lock_fd = open(LOCK_FILE, "w")
    try:
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        log("⚠️ 另一個 ig-auto-post.py 實例執行緊，跳過")
        sys.exit(0)
    lock_fd.write(str(os.getpid()))
    lock_fd.flush()
    return lock_fd


def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE) as f:
                return json.load(f)
        except Exception:
            return {"posted": []}
    return {"posted": []}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def parse_front_matter(path):
    info = {"title": None, "description": None, "image": None, "categories": None, "creator_github": None, "fb_message": None}
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.S)
        if m:
            fm = m.group(1)
            t = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            img = re.search(r'^image:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            cg = re.search(r'^creator_github:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            fbm = re.search(r'^fb_message:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            if t: info["title"] = t.group(1).strip().strip('"\'')
            if img: info["image"] = img.group(1).strip().strip('"\'')
            if cg: info["creator_github"] = cg.group(1).strip().strip('"\'')
            if fbm: info["fb_message"] = fbm.group(1).strip().strip('"\'').replace("\\n", "\n")
        return info
    except Exception:
        return info


def ig_api(path, params, method="GET"):
    url = f"{API}/{path}"
    if method == "GET":
        url += "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url)
    else:
        req = urllib.request.Request(url, data=urllib.parse.urlencode(params).encode(), method="POST")
    try:
        return json.loads(urllib.request.urlopen(req, timeout=60).read().decode())
    except Exception as e:
        return {"_error": str(e)}


def ig_post_image(image_url, caption):
    """兩步：create media container → publish"""
    r = ig_api(f"{IG_USER_ID}/media", {
        "image_url": image_url,
        "caption": caption,
        "access_token": IG_TOKEN,
    }, "POST")
    if "id" not in r:
        return False, str(r)
    time.sleep(10)  # 等 IG 處理圖片
    r2 = ig_api(f"{IG_USER_ID}/media_publish", {
        "creation_id": r["id"],
        "access_token": IG_TOKEN,
    }, "POST")
    if "id" in r2:
        return True, r2["id"]
    return False, str(r2)


def main():
    lock_fd = acquire_lock()
    log("=== Blog → Instagram 自動發文檢查 (v1) ===")
    first_run = not os.path.exists(STATE_FILE)
    state = load_state()
    posted = set(state.get("posted", []))

    if not os.path.isdir(POSTS_DIR):
        log(f"ERROR: 搵唔到 posts 目錄 {POSTS_DIR}")
        sys.exit(1)

    posts = sorted(os.listdir(POSTS_DIR))

    if first_run:
        state["posted"] = [p for p in posts if p.endswith(".md")]
        save_state(state)
        log(f"首次執行：已標記 {len(state['posted'])} 篇現有文章為已處理（唔會發佈舊文）")
        return

    new_posts = [p for p in posts if p.endswith(".md") and p not in posted]
    if not new_posts:
        log("冇新文章 ✅")
        return

    log(f"發現 {len(new_posts)} 篇新文章，開始發佈...")
    success_count = 0

    for post in new_posts:
        info = parse_front_matter(os.path.join(POSTS_DIR, post))

        # 只發 GitHub 新聞（有 creator_github + fb_message）
        if not info.get("creator_github") or not info.get("fb_message"):
            posted.add(post)
            log(f"⏭️ 跳過（非 GitHub 新聞或冇 fb_message）：{post}")
            continue
        if not info.get("image"):
            posted.add(post)
            log(f"⏭️ 冇封面圖：{post}")
            continue

        image = info["image"]
        img_url = image if image.startswith("http") else BLOG_BASE + image
        caption = info["fb_message"] + "\n\n" + HASHTAGS

        ok, result = ig_post_image(img_url, caption)
        if ok:
            posted.add(post)
            success_count += 1
            log(f"✅ 已發佈：{post}（{result}）")
            log(f"   圖片：{img_url}")
        else:
            log(f"❌ 發佈失敗：{post} → {result}")

    state["posted"] = sorted(posted)
    save_state(state)
    log(f"完成：成功 {success_count}/{len(new_posts)} 篇")
    if success_count < len(new_posts):
        sys.exit(1)


if __name__ == "__main__":
    main()
