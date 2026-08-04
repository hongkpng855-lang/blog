#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blog → Facebook 自動發文 script v5
- 檢查 jekyll-blog/_posts/ 有冇新文章（相對 state 檔案）
- 有 → 自動 POST 去 Facebook 專頁（精簡版內容 + 封面圖卡片 + Blog 連結，引流去 Blog）
- 記錄已發佈文章，避免重複發佈

用法：python3 fb-auto-post.py
"""
import json
import os
import re
import sys
import urllib.request
import urllib.parse
import datetime

# ---------- 設定 ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# script 喺 jekyll-blog/scripts/ 入面
JEKYLL_DIR = os.path.dirname(BASE_DIR)
POSTS_DIR = os.path.join(JEKYLL_DIR, "_posts")
SECRETS_DIR = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", ".secrets", "fb")
STATE_FILE = os.path.join(BASE_DIR, "fb_posted_state.json")

PAGE_ID = open(os.path.join(SECRETS_DIR, "page_id.txt")).read().strip()
PAGE_TOKEN = open(os.path.join(SECRETS_DIR, "page_token.txt")).read().strip()
BLOG_BASE = "https://aniskill.esgov.org/"

def log(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)

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
    """解析 Jekyll front matter，攞 title / description / image / categories / creator_github"""
    info = {"title": None, "description": None, "image": None, "categories": None, "creator_github": None}
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.S)
        if m:
            fm = m.group(1)
            t = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            d = re.search(r'^description:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            img = re.search(r'^image:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            c = re.search(r'^categories:\s*(.+?)\s*$', fm, re.M)
            cg = re.search(r'^creator_github:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            if t: info["title"] = t.group(1).strip().strip('"\'')
            if d: info["description"] = d.group(1).strip().strip('"\'')
            if img: info["image"] = img.group(1).strip().strip('"\'')
            if c:
                cat = c.group(1).strip()
                if cat.startswith("["):
                    cat = re.sub(r"[\[\]\s]", "", cat)
                    cat = cat.split(",")[0]
                info["categories"] = cat
            if cg: info["creator_github"] = cg.group(1).strip().strip('"\'')
        return info, content
    except Exception:
        return info, ""

def extract_excerpt(content, max_len=280):
    """攞正文前 2 段做精簡版內容（front matter 之後）"""
    body = re.sub(r"^---\s*\n.*?\n---\s*\n?", "", content, flags=re.S)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    body = re.sub(r"<svg.*?</svg>", "", body, flags=re.S)
    body = re.sub(r"<[^>]+>", "", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    paras = [p.strip() for p in body.split("\n\n") if p.strip()]

    excerpt = ""
    for p in paras:
        if p.startswith("#") or p.startswith(">"):
            continue
        if excerpt == "" and len(p) < 20:
            continue
        excerpt += p + "\n\n"
        if len(excerpt) >= max_len:
            break
    excerpt = excerpt.strip()
    if len(excerpt) > max_len:
        excerpt = excerpt[:max_len - 3].rstrip() + "..."
    return excerpt

def get_post_url(filename, categories):
    """從 filename + categories 推斷文章 URL（Jekyll permalink: /:categories/:year/:month/:day/:title）"""
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$", filename)
    if m:
        y, mo, d, slug = m.groups()
        if categories:
            return f"{BLOG_BASE}{categories}/{y}/{mo}/{d}/{slug}.html"
        return f"{BLOG_BASE}{y}/{mo}/{d}/{slug}.html"
    return BLOG_BASE

def get_absolute_image(image_path):
    """將相對圖片路徑轉做絕對 URL"""
    if not image_path:
        return None
    if image_path.startswith("http"):
        return image_path
    image_path = image_path.lstrip("/")
    return f"{BLOG_BASE}{image_path}"

def fb_post_link(message, link):
    """POST 連結卡片去 Facebook（Facebook 自動抓 og:image 做封面圖）"""
    url = f"https://graph.facebook.com/v21.0/{PAGE_ID}/feed"
    params = {
        "message": message,
        "link": link,
        "access_token": PAGE_TOKEN,
    }
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(url, data=data)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode())
            if "id" in result:
                return True, result["id"]
            return False, str(result)
    except Exception as e:
        return False, str(e)

def main():
    log("=== Blog → Facebook 自動發文檢查 (v5: 精簡內容+封面，引流去 Blog) ===")
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
        log("之後新增嘅文章會自動發佈 ✅")
        return

    new_posts = [p for p in posts if p.endswith(".md") and p not in posted]

    if not new_posts:
        log(f"冇新文章（已發佈 {len(posted)} 篇）✅")
        return

    log(f"發現 {len(new_posts)} 篇新文章，開始發佈...")
    success_count = 0

    for post in new_posts:
        path = os.path.join(POSTS_DIR, post)
        info, content = parse_front_matter(path)
        title = info["title"] or os.path.basename(post)
        desc = info["description"] or ""
        excerpt = extract_excerpt(content)

        # 組合精簡版內容：description + 正文摘要
        body_text = excerpt if excerpt else desc
        if desc and desc not in body_text:
            body_text = f"{desc}\n\n{excerpt}"

        image_url = get_absolute_image(info["image"])
        url = get_post_url(post, info["categories"])

        # 帖文：標題 + 精簡內容 + Blog 連結卡片（FB 自動抓 og:image 封面）
        # ⚠️ 唔加任何外部連結（GitHub 出處等）——將 FB 流量引流去 Blog
        message = f"{title}\n\n{body_text}"
        ok, result = fb_post_link(message, url)

        if ok:
            posted.add(post)
            success_count += 1
            log(f"✅ 已發佈：{post}（{result}）")
            log(f"   標題：{title}")
            log(f"   URL：{url}")
            log(f"   封面圖：{image_url}")
        else:
            log(f"❌ 發佈失敗：{post} → {result}")

    state["posted"] = sorted(posted)
    save_state(state)
    log(f"完成：成功 {success_count}/{len(new_posts)} 篇")
    if success_count < len(new_posts):
        sys.exit(1)

if __name__ == "__main__":
    main()
