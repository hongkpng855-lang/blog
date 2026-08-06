#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blog → Instagram 自動發文 script v2（2026-08-06）
- 檢查 jekyll-blog/_posts/ 有冇新 GitHub 新聞（front matter 有 creator_github + fb_message）
- 有 → 自動 POST 去 IG：
  * caption 最頂 = Blog 文章連結（用戶要求：文章最上面放返 blog 連結）
  * 圖片 = 文章全部圖片（封面 + 正文所有圖），2 張以上用 Carousel（最多 10 張）
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
# 圖片用 github.io（IG crawler 可達；custom domain 唔可靠）
IMG_BASE = "https://hongkpng855-lang.github.io/blog/"
# caption 內嘅文章連結用 custom domain（用戶要求 2026-08-06）
LINK_BASE = "https://aniskill.esgov.org/"
API = "https://graph.instagram.com/v25.0"
HASHTAGS = "#AI #開源 #GitHub #LLM #人工智能"
MAX_CAROUSEL = 10  # IG Carousel 上限


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
    info = {"title": None, "description": None, "image": None, "categories": None,
            "creator_github": None, "fb_message": None}
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
        m = re.match(r"^---\s*\n(.*?)\n---", content, re.S)
        if m:
            fm = m.group(1)
            t = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            img = re.search(r'^image:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            c = re.search(r'^categories:\s*(.+?)\s*$', fm, re.M)
            cg = re.search(r'^creator_github:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            fbm = re.search(r'^fb_message:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            if t: info["title"] = t.group(1).strip().strip('"\'')
            if img: info["image"] = img.group(1).strip().strip('"\'')
            if c:
                cat = c.group(1).strip().strip('"\'')
                if cat and not cat.startswith("["):
                    info["categories"] = cat
            if cg: info["creator_github"] = cg.group(1).strip().strip('"\'')
            if fbm: info["fb_message"] = fbm.group(1).strip().strip('"\'').replace("\\n", "\n")
        return info
    except Exception:
        return info


def get_post_url(filename, categories):
    """從 filename + categories 推斷文章 URL（Jekyll permalink: /:categories/:year/:month/:day/:title）"""
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$", filename)
    if m:
        y, mo, d, slug = m.groups()
        if categories:
            return f"{LINK_BASE}{categories}/{y}/{mo}/{d}/{slug}.html"
        return f"{LINK_BASE}{y}/{mo}/{d}/{slug}.html"
    return LINK_BASE


def get_absolute_image(image_path):
    """將相對圖片路徑轉做絕對 URL"""
    if not image_path:
        return None
    if image_path.startswith("http"):
        return image_path
    image_path = image_path.lstrip("/")
    return f"{IMG_BASE}{image_path}"


def extract_content_images(md_content):
    """從 markdown 正文抽取所有圖片路徑（去重、保留順序）"""
    images = []
    # 1) Liquid 語法：![alt]({{ '/path' | relative_url }})
    for m in re.finditer(r'!\[[^\]]*\]\(\{\{\s*[\'"]([^\'"]+)[\'"]\s*\|\s*relative_url\s*\}\}\)', md_content):
        p = m.group(1).strip()
        if p not in images:
            images.append(p)
    # 2) 純 markdown：![alt](path)
    for m in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', md_content):
        p = m.group(1).strip()
        if p.startswith("{{") or p.startswith("<") or p.startswith("http"):
            continue
        if p not in images:
            images.append(p)
    # 3) <img src="...">
    for m in re.finditer(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', md_content):
        p = m.group(1).strip()
        if p not in images:
            images.append(p)
    return images


def build_image_list(post_path, info):
    """封面 + 正文全部圖片 → 絕對 URL 清單（去重、最多 10 張）"""
    with open(post_path, encoding="utf-8") as f:
        content = f.read()

    raw = []
    if info.get("image"):
        raw.append(info["image"])  # 封面（front matter image）排最前
    raw.extend(extract_content_images(content))

    # 去重（保留順序）
    seen, urls = set(), []
    for p in raw:
        if p in seen:
            continue
        seen.add(p)
        # IG 唔支援 SVG → 跳過
        if p.lower().endswith((".svg", ".gif")):
            continue
        url = get_absolute_image(p)
        if url and url not in urls:
            urls.append(url)
    return urls[:MAX_CAROUSEL]


def build_caption(post_url, fb_message):
    """caption：Blog 連結放最頂 → fb_message → hashtags"""
    return f"📄 完整文章：{post_url}\n\n{fb_message}\n\n{HASHTAGS}"


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
    """單圖：兩步 create media container → publish"""
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


def ig_post_carousel(image_urls, caption):
    """Carousel：每張圖 create item container → create CAROUSEL container → publish"""
    children = []
    for i, url in enumerate(image_urls):
        r = ig_api(f"{IG_USER_ID}/media", {
            "image_url": url,
            "is_carousel_item": "true",
            "access_token": IG_TOKEN,
        }, "POST")
        if "id" not in r:
            return False, f"第 {i + 1}/{len(image_urls)} 張圖 create 失敗：{r}"
        children.append(r["id"])
        log(f"   ⏳ Carousel 圖片容器 {i + 1}/{len(image_urls)} ok（{url}）")
        time.sleep(3)  # 避免 rate limit
    r = ig_api(f"{IG_USER_ID}/media", {
        "media_type": "CAROUSEL",
        "children": ",".join(children),
        "caption": caption,
        "access_token": IG_TOKEN,
    }, "POST")
    if "id" not in r:
        return False, f"Carousel container 失敗：{r}"
    time.sleep(15)  # 等 IG 處理
    r2 = ig_api(f"{IG_USER_ID}/media_publish", {
        "creation_id": r["id"],
        "access_token": IG_TOKEN,
    }, "POST")
    if "id" in r2:
        return True, r2["id"]
    return False, str(r2)


def main():
    lock_fd = acquire_lock()
    log("=== Blog → Instagram 自動發文檢查 (v2: 全圖 Carousel + 連結置頂) ===")
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

        img_urls = build_image_list(os.path.join(POSTS_DIR, post), info)
        if not img_urls:
            posted.add(post)
            log(f"⏭️ 冇圖片：{post}")
            continue

        post_url = get_post_url(post, info["categories"])
        caption = build_caption(post_url, info["fb_message"])
        log(f"📝 {post}")
        log(f"   連結：{post_url}")
        log(f"   圖片：{len(img_urls)} 張 → {'Carousel' if len(img_urls) > 1 else '單圖'}")

        if len(img_urls) == 1:
            ok, result = ig_post_image(img_urls[0], caption)
        else:
            ok, result = ig_post_carousel(img_urls, caption)

        if ok:
            posted.add(post)
            success_count += 1
            log(f"✅ 已發佈：{post}（{result}）")
            # Story 同步（2026-08-06 用戶要求：出埋 Story，引導 copy 連結去出處）
            if img_urls:
                post_story_for(post, info, img_urls[0], post_url)
        else:
            log(f"❌ 發佈失敗：{post} → {result}")

    state["posted"] = sorted(posted)
    save_state(state)
    log(f"完成：成功 {success_count}/{len(new_posts)} 篇")
    if success_count < len(new_posts):
        sys.exit(1)


if __name__ == "__main__":
    main()


# ==================== Story 功能（2026-08-06 用戶要求） ====================
# 每篇 feed post 出完之後，自動出一個 Story：
#   - 1080x1920 圖（封面置中 + 底部 URL bar）
#   - caption 引導：撳 copy 連結去返出處
# ⚠️ IG API 唔支援 Link Sticker → 用「caption 完整 URL + copy 指示」策略

STORY_DIR = os.path.join(JEKYLL_DIR, "assets/images/posts/stories")

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

STORY_W, STORY_H = 1080, 1920
FONT_CJK = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
FONT_LATIN = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def _font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def make_story_image(cover_local_path, domain_short, out_path):
    """封面圖 → 1080x1920 Story 圖（navy 背景 + 封面置中 + 底部 URL bar）"""
    if not HAS_PIL:
        return False
    bg = Image.new("RGB", (STORY_W, STORY_H), "#1B2A4A")
    try:
        cover = Image.open(cover_local_path).convert("RGB")
    except Exception:
        return False
    # 封面 fit 入 1080 闊，置中偏上（留位俾頂部標題同底部 bar）
    scale = min(STORY_W / cover.width, (STORY_H - 420) / cover.height)
    nw, nh = int(cover.width * scale), int(cover.height * scale)
    cover = cover.resize((nw, nh), Image.LANCZOS)
    bg.paste(cover, ((STORY_W - nw) // 2, 160))
    d = ImageDraw.Draw(bg)
    # 頂部標題
    f_title = _font(FONT_CJK, 54)
    title = "📰 新文章發佈"
    tw = d.textlength(title, font=f_title)
    d.text(((STORY_W - tw) / 2, 60), title, fill="#C9A84C", font=f_title)
    # 底部 URL bar
    d.rectangle([0, STORY_H - 260, STORY_W, STORY_H], fill="#0E1626")
    f_url = _font(FONT_LATIN, 46)
    f_hint = _font(FONT_CJK, 34)
    url_text = f"🔗 {domain_short}"
    uw = d.textlength(url_text, font=f_url)
    d.text(((STORY_W - uw) / 2, STORY_H - 220), url_text, fill="#FFFFFF", font=f_url)
    hint = "完整文章連結喺 Story 底部 👇"
    hw = d.textlength(hint, font=f_hint)
    d.text(((STORY_W - hw) / 2, STORY_H - 140), hint, fill="#C9A84C", font=f_hint)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    bg.save(out_path, "JPEG", quality=88)
    return True


def git_push_file(file_path):
    """將 Story 圖 commit + push 去 blog repo（等 GitHub Pages 可以 serve）"""
    import subprocess
    try:
        subprocess.run(["git", "add", file_path], cwd=JEKYLL_DIR, check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", f"Story 圖 {os.path.basename(file_path)}"], cwd=JEKYLL_DIR, check=True, capture_output=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=JEKYLL_DIR, check=True, capture_output=True, timeout=120)
        return True
    except Exception as e:
        log(f"⚠️ Story 圖 push 失敗：{e}")
        return False


def wait_url_ready(url, timeout_s=180):
    """等 GitHub Pages build + 圖片 200 OK"""
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        try:
            r = urllib.request.urlopen(url, timeout=15)
            if r.status == 200:
                return True
        except Exception:
            pass
        time.sleep(10)
    return False


def ig_post_story(image_url, caption):
    """Story：create container（media_type=STORIES）→ publish"""
    r = ig_api(f"{IG_USER_ID}/media", {
        "image_url": image_url,
        "media_type": "STORIES",
        "caption": caption,
        "access_token": IG_TOKEN,
    }, "POST")
    if "id" not in r:
        return False, str(r)
    time.sleep(8)
    r2 = ig_api(f"{IG_USER_ID}/media_publish", {
        "creation_id": r["id"],
        "access_token": IG_TOKEN,
    }, "POST")
    if "id" in r2:
        return True, r2["id"]
    return False, str(r2)


def post_story_for(post_file, info, cover_url, post_url):
    """完整 Story 流程：生成圖 → push → 等 200 → 發佈"""
    if not HAS_PIL:
        log("⏭️ 冇 PIL，跳過 Story")
        return
    # 封面本地路徑（由 github.io URL 反推）
    rel = cover_url.replace(IMG_BASE, "")
    cover_local = os.path.join(JEKYLL_DIR, rel)
    if not os.path.exists(cover_local):
        log(f"⏭️ Story：搵唔到本地封面 {cover_local}")
        return
    slug = post_file.replace(".md", "")
    out_path = os.path.join(STORY_DIR, f"{slug}-story.jpg")
    domain_short = LINK_BASE.replace("https://", "").rstrip("/")
    if not make_story_image(cover_local, domain_short, out_path):
        log("⏭️ Story：生成圖片失敗")
        return
    if not git_push_file(out_path):
        return
    story_url = f"{IMG_BASE}assets/images/posts/stories/{slug}-story.jpg"
    if not wait_url_ready(story_url):
        log(f"⚠️ Story 圖片等唔到 200：{story_url}")
        return
    caption = f"📌 完整文章：{post_url}\n\n👉 撳 copy 呢條連結，就可以去返出處！"
    ok, result = ig_post_story(story_url, caption)
    if ok:
        log(f"✅ Story 已發佈：{post_file}（{result}）")
    else:
        log(f"⚠️ Story 發佈失敗：{post_file} → {result}")
