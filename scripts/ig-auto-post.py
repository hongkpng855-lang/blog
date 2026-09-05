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
# 圖片用 custom domain HTTPS 直連（2026-09-04 修正：github.io 會 301 redirect 去非 HTTPS custom domain，IG crawler 唔跟，HTTP 400；HTTPS 直連實測 OK）
IMG_BASE = "https://aniskill.esgov.org/"
# caption 內嘅文章連結用 custom domain（用戶要求 2026-08-06）
LINK_BASE = "https://aniskill.esgov.org/"
API = "https://graph.instagram.com/v25.0"
HASHTAGS = "#AI #開源 #GitHub #LLM #人工智能"
# IG 對 custom domain 嘅圖有時拎唔到（可能 cache 咗 build 未完時嘅 404）→ fallback 用 raw.githubusercontent.com 直連（2026-09-05 實測 OK）
RAW_IMG_BASE = "https://raw.githubusercontent.com/hongkpng855-lang/blog/main/"
MAX_CAROUSEL = 10  # IG Carousel 上限
# 發文後自動補第一條留言（2026-08-08 新增，link in first comment 引流）
# 改呢度就可以改留言內容；{url} 會自動換成文章連結
FIRST_COMMENT_TEMPLATE = "📌 完整文章：{url}\n\n🔗 撳入去睇完整教學！"


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
            "creator_github": None, "fb_message": None, "permalink": None, "type": None}
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
            perm = re.search(r'^permalink:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            tp = re.search(r'^type:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
            if t: info["title"] = t.group(1).strip().strip('"\'')
            if img: info["image"] = img.group(1).strip().strip('"\'')
            if c:
                cat = c.group(1).strip().strip('"\'')
                if cat and not cat.startswith("["):
                    info["categories"] = cat
            if cg: info["creator_github"] = cg.group(1).strip().strip('"\'')
            if fbm: info["fb_message"] = fbm.group(1).strip().strip('"\'').replace("\\n", "\n")
            if perm: info["permalink"] = perm.group(1).strip().strip('"\'')
            if tp: info["type"] = tp.group(1).strip().strip('"\'')
        return info
    except Exception:
        return info


def get_post_url(filename, info):
    """推斷文章 URL：
    - 有 front matter permalink（無日期格式）→ LINK_BASE + permalink
    - 冇 → 舊格式 /:categories/:year/:month/:day/:title.html
    """
    if info.get("permalink"):
        return LINK_BASE + info["permalink"].lstrip("/")
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$", filename)
    if m:
        y, mo, d, slug = m.groups()
        if info.get("categories"):
            return f"{LINK_BASE}{info['categories']}/{y}/{mo}/{d}/{slug}.html"
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


def ig_post_comment(media_id, comment):
    """喺自己嘅 IG post 下面補第一條留言（link in first comment）"""
    r = ig_api(f"{media_id}/comments", {
        "message": comment,
        "access_token": IG_TOKEN,
    }, "POST")
    if "id" in r:
        return True, r["id"]
    return False, str(r)


def raw_fallback_url(image_url):
    """custom domain 圖拎唔到 → 轉 raw.githubusercontent.com 直連（IG crawler 實測 OK）"""
    if image_url.startswith(IMG_BASE):
        return image_url.replace(IMG_BASE, RAW_IMG_BASE)
    return None


def ig_post_image(image_url, caption):
    """單圖：兩步 create media container → publish（失敗自動試 raw fallback）"""
    candidates = [image_url]
    fb = raw_fallback_url(image_url)
    if fb:
        candidates.append(fb)
    last_err = "未嘗試"
    for cand in candidates:
        if cand != image_url:
            log(f"   🔁 custom domain 拎圖失敗，改用 raw 直連重試：{cand}")
        r = ig_api(f"{IG_USER_ID}/media", {
            "image_url": cand,
            "caption": caption,
            "access_token": IG_TOKEN,
        }, "POST")
        if "id" not in r:
            last_err = str(r)
            continue
        time.sleep(10)  # 等 IG 處理圖片
        r2 = ig_api(f"{IG_USER_ID}/media_publish", {
            "creation_id": r["id"],
            "access_token": IG_TOKEN,
        }, "POST")
        if "id" in r2:
            return True, r2["id"]
        return False, str(r2)
    return False, last_err


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
    log("=== Blog → Instagram 自動發文檢查 (v3: GitHub 新聞 + 外媒/AI 新聞 (type: news) + 全圖 Carousel + 連結置頂) ===")
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

        # 只發新聞文章（GitHub 新聞有 creator_github，或外媒/AI 新聞有 type: news）+ fb_message
        is_news = info.get("type") == "news" or bool(info.get("creator_github"))
        if not is_news or not info.get("fb_message"):
            posted.add(post)
            log(f"⏭️ 跳過（非新聞文章或冇 fb_message）：{post}")
            continue

        # ⚠️ 雙保險：即使 state 檔意外被清，都檢查 IG 上有冇相同標題嘅 post（2026-08-08 用戶要求防重複）
        # 注意：IG caption 開頭係「📄 完整文章：{url}」唔係 title → 用「包含 title」判斷，唔可以 startswith（2026-08-08 修正）
        try:
            check_url = f"https://graph.instagram.com/v21.0/{IG_USER_ID}/media?fields=caption&limit=30&access_token={IG_TOKEN}"
            with urllib.request.urlopen(check_url, timeout=20) as resp:
                existing = json.loads(resp.read().decode()).get("data", [])
            title_key = (info["title"] or "").strip()[:25]
            dup = any(
                title_key and title_key in (p.get("caption") or "")
                for p in existing
            )
            if dup:
                posted.add(post)
                log(f"⏭️ 跳過（IG 已有相同標題嘅 post）：{post}")
                continue
        except Exception as e:
            log(f"⚠️ 重複檢查失敗（照發，靠 state 檔）：{e}")


        img_urls = build_image_list(os.path.join(POSTS_DIR, post), info)
        if not img_urls:
            posted.add(post)
            log(f"⏭️ 冇圖片：{post}")
            continue

        post_url = get_post_url(post, info)
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
            # 發文後自動補第一條留言（2026-08-08 用戶要求：自己 post 留言）
            comment = FIRST_COMMENT_TEMPLATE.format(url=post_url)
            okc, cres = ig_post_comment(result, comment)
            if okc:
                log(f"💬 已留言：{post}（comment id {cres}）")
            else:
                log(f"⚠️ 留言失敗（唔影響發文）：{cres}")
            # Story 同步（2026-08-06 用戶要求：出埋 Story，引導 copy 連結去出處）
            if img_urls:
                post_story_for(post, info, img_urls, post_url)
        else:
            log(f"❌ 發佈失敗：{post} → {result}")

    state["posted"] = sorted(posted)
    save_state(state)
    log(f"完成：成功 {success_count}/{len(new_posts)} 篇")
    if success_count < len(new_posts):
        sys.exit(1)


# ==================== Story 功能（2026-08-06 用戶要求） ====================
# 每篇 feed post 出完之後，自動出一個 Story：
#   - 1080x1920 圖（封面置中 + 底部 URL bar）
#   - caption 引導：撳 copy 連結去返出處
# ⚠️ IG API 唔支援 Link Sticker → 用「caption 完整 URL + copy 指示」策略

STORY_DIR = os.path.join(JEKYLL_DIR, "assets/images/posts/stories")

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
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


def make_story_image(cover_local_paths, domain_short, out_path):
    """封面圖 → 1080x1920 Story 圖（blur 背景填滿成張 + 前景 1-2 張圖 + 底部 URL bar）

    cover_local_paths: list，最多 2 張圖
    2026-08-06 用戶要求：
    - 之前：一張截圖只佔半個內容，下邊加多一張
    - 而家（16:45）：README 截圖要好似其他圖片咁佔據晒成張 → 用 IG 標準
      blur 背景填充：背景 = 第一張圖放大模糊 + 暗化，前景 = 清晰原圖置中
    """
    if not HAS_PIL:
        return False
    covers = []
    for pth in cover_local_paths[:2]:
        try:
            covers.append(Image.open(pth).convert("RGB"))
        except Exception:
            continue
    if not covers:
        return False
    # ---- 背景：第一張圖 cover 填滿成張 + blur + 暗化 ----
    bg_cover = covers[0].resize((STORY_W, STORY_H), Image.LANCZOS)
    # 保持比例 cover（crop 中間，避免變形）
    scale = max(STORY_W / covers[0].width, STORY_H / covers[0].height)
    bw, bh = int(covers[0].width * scale), int(covers[0].height * scale)
    bg_cover = covers[0].resize((bw, bh), Image.LANCZOS)
    bg_cover = bg_cover.crop(((bw - STORY_W) // 2, (bh - STORY_H) // 2,
                              (bw - STORY_W) // 2 + STORY_W, (bh - STORY_H) // 2 + STORY_H))
    bg_cover = bg_cover.filter(ImageFilter.GaussianBlur(14))
    # 暗化 overlay，令前景突出 + 文字可讀
    dark = Image.new("RGB", (STORY_W, STORY_H), (10, 16, 32))
    bg = Image.blend(bg_cover, dark, alpha=0.30)
    d = ImageDraw.Draw(bg)
    # ---- 頂部標題（半透明底）----
    f_title = _font(FONT_CJK, 54)
    title = "📰 新文章發佈"
    d.rounded_rectangle([40, 30, STORY_W - 40, 130], radius=24, fill=(0, 0, 0, 90))
    tw = d.textlength(title, font=f_title)
    d.text(((STORY_W - tw) / 2, 55), title, fill="#C9A84C", font=f_title)
    # ---- 前景：單張 shot1（README）fit 全闊，置中；背景已有 blur 版填滿成張 ----
    # 2026-08-06 16:45 用戶要求：README 截圖要好似其他圖片咁佔據晒成張
    # → IG 標準做法：背景 = 同一張圖 blur 放大填滿，前景 = 清晰原圖置中
    cover = covers[0]
    scale = min(STORY_W / cover.width, (STORY_H - 320) / cover.height)
    nw, nh = int(cover.width * scale), int(cover.height * scale)
    c = cover.resize((nw, nh), Image.LANCZOS)
    bg.paste(c, ((STORY_W - nw) // 2, (STORY_H - nh) // 2))
    # ---- 底部 URL bar（半透明）----
    bottom_bar_h = 260
    bar = Image.new("RGBA", (STORY_W, bottom_bar_h), (10, 18, 38, 235))
    bg.paste(bar, (0, STORY_H - bottom_bar_h), bar)
    d = ImageDraw.Draw(bg)
    f_url = _font(FONT_LATIN, 46)
    f_hint = _font(FONT_CJK, 34)
    url_text = f"🔗 {domain_short}"
    uw = d.textlength(url_text, font=f_url)
    d.text(((STORY_W - uw) / 2, STORY_H - 225), url_text, fill="#FFFFFF", font=f_url)
    hint = "完整文章連結喺 Story 底部 👇"
    hw = d.textlength(hint, font=f_hint)
    d.text(((STORY_W - hw) / 2, STORY_H - 150), hint, fill="#C9A84C", font=f_hint)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    bg.save(out_path, "JPEG", quality=88)
    return True


def git_push_file(file_path):
    """將 Story 圖 commit + push 去 blog repo（等 GitHub Pages 可以 serve）
    2026-08-07 修正：commit 回傳「nothing to commit」（圖已 commit 過）時
    照樣當成功，唔好因為重複 commit 失敗而跳過 Story 發佈。"""
    import subprocess
    try:
        subprocess.run(["git", "add", file_path], cwd=JEKYLL_DIR, check=True, capture_output=True)
        cp = subprocess.run(["git", "commit", "-m", f"Story 圖 {os.path.basename(file_path)}"],
                            cwd=JEKYLL_DIR, capture_output=True, timeout=60)
        # 如果冇嘢可 commit（already committed），唔當錯誤
        out = (cp.stdout or b"").decode() + (cp.stderr or b"").decode()
        if cp.returncode != 0 and "nothing to commit" not in out and "nothing added" not in out:
            raise Exception(out.strip() or f"commit exit {cp.returncode}")
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


def post_story_for(post_file, info, img_urls, post_url):
    """完整 Story 流程：生成圖（頭兩張）→ push → 等 200 → 發佈"""
    if not HAS_PIL:
        log("⏭️ 冇 PIL，跳過 Story")
        return
    # 封面本地路徑（由 github.io URL 反推），攞頭兩張
    cover_locals = []
    for u in img_urls[:2]:
        rel = u.replace(IMG_BASE, "")
        lp = os.path.join(JEKYLL_DIR, rel)
        if os.path.exists(lp):
            cover_locals.append(lp)
    if not cover_locals:
        log("⏭️ Story：搵唔到本地封面圖")
        return
    slug = post_file.replace(".md", "")
    out_path = os.path.join(STORY_DIR, f"{slug}-story.jpg")
    domain_short = LINK_BASE.replace("https://", "").rstrip("/")
    if not make_story_image(cover_locals, domain_short, out_path):
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


if __name__ == "__main__":
    main()
