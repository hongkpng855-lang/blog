#!/usr/bin/env python3
"""批量將全部文章封面轉 1080x1080 正方形（2026-08-10 用戶要求）"""
import os, re, glob, subprocess, sys

BLOG = "/home/hongk/.openclaw/workspace/jekyll-blog"
POSTS = os.path.join(BLOG, "_posts")
SCRIPT = os.path.join(BLOG, "scripts", "make-cover.py")
TMP = "/home/hongk/.openclaw/workspace/.tmp-orig-news"


def parse_title(title):
    m = re.match(r'^([\d.]+ 萬星開源項目)[：:]\s*(.+?)\s*[—–-]\s*(.+)$', title)
    if m:
        return m.group(1), m.group(2).strip(), m.group(3).strip()
    m2 = re.match(r'^(.+?)[—–-]\s*(.+)$', title)
    if m2:
        return "", m2.group(1).strip(), m2.group(2).strip()
    return "", title, ""


def build_zh(name, desc, stars):
    line1 = desc
    if len(line1) > 10:
        line1 = line1[:10]
    parts = []
    if line1:
        parts.append(line1)
    if stars:
        parts.append(stars.replace(" ", ""))
    return "|".join(parts) if parts else name


def regen_cover(f, bg, title, repo, dry=False):
    """用 make-cover.py 重新生成 1080x1080 封面"""
    stars, name, desc = parse_title(title)
    zh = build_zh(name, desc, stars)
    en = repo.replace('-', ' ').replace('_', ' ').title() if repo else name
    en = re.sub(r'\s+', ' ', en).strip()
    slug = os.path.basename(f).replace('.md', '')
    out = os.path.join(BLOG, "assets", "images", "posts", f"{slug}-cover.jpg")
    if not os.path.exists(bg):
        return f"❌ {slug}: 背景圖唔存在 {bg}"
    r = subprocess.run(["python3", SCRIPT, "--bg", bg, "--title-zh", zh,
                        "--title-en", en, "--out", out], capture_output=True, text=True)
    if r.returncode != 0:
        return f"❌ {slug}: {r.stderr[:80]}"
    return f"✅ {slug}"


def crop_square(f, img_path, dry=False):
    """將現有封面 crop 成 1080x1080 正方形"""
    from PIL import Image
    import io
    if img_path.lower().endswith('.svg'):
        return f"⏭️ {os.path.basename(f)}: SVG 跳過（PIL 唔支持）"
    path = os.path.join(BLOG, img_path.lstrip('/'))
    if not os.path.exists(path):
        return f"❌ {os.path.basename(f)}: 封面唔存在 {img_path}"
    try:
        raw = open(path, 'rb').read()
        # 檢查係咪假 webp（實際 SVG 內容）
        if raw[:5].startswith(b'<svg') or raw[:5].startswith(b'<?xml'):
            import cairosvg
            png = cairosvg.svg2png(bytestring=raw, output_width=1080, output_height=1080)
            img = Image.open(io.BytesIO(png)).convert("RGB")
            if img.size != (1080, 1080):
                img = img.resize((1080, 1080), Image.LANCZOS)
            img.save(path.replace('.webp', '.jpg'), quality=92)
            # 更新文章 front matter 指返 jpg
            _update_fm(f, img_path, img_path.replace('.webp', '.jpg'))
            return f"✅ {os.path.basename(f)} (SVG→JPG 正方形)"
        img = Image.open(io.BytesIO(raw)).convert("RGB")
        if img.size == (1080, 1080):
            return f"⏭️ {os.path.basename(f)}: 已係正方形"
        w, h = img.size
        side = min(w, h)
        left = (w - side) // 2
        top = int((h - side) * 0.35)  # 偏上 crop（封面文字通常喺中下）
        top = max(0, min(top, h - side))
        img = img.crop((left, top, left + side, top + side)).resize((1080, 1080), Image.LANCZOS)
        if path.lower().endswith('.webp'):
            img.save(path.replace('.webp', '.jpg'), quality=92)
            _update_fm(f, img_path, img_path.replace('.webp', '.jpg'))
        else:
            img.save(path, quality=92)
        return f"✅ {os.path.basename(f)}"
    except Exception as e:
        return f"❌ {os.path.basename(f)}: {type(e).__name__} {str(e)[:60]}"


def _update_fm(f, old_img, new_img):
    c = open(f, encoding='utf-8').read()
    c2 = c.replace(old_img, new_img)
    if c2 != c:
        open(f, 'w', encoding='utf-8').write(c2)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    files = sorted(glob.glob(os.path.join(POSTS, "*.md")), reverse=True)
    gh_done = other_done = gh_skip = other_skip = 0
    gh_fail, other_fail = [], []

    for f in files:
        c = open(f, encoding='utf-8').read()
        m_img = re.search(r'^image:\s*(\S+)', c, re.M)
        m_gh = re.search(r'^creator_github:\s*(\S+)', c, re.M)
        m_title = re.search(r'^title:\s*"([^"]+)"', c, re.M)
        if not m_img or not m_title:
            continue
        img = m_img.group(1).strip('"\'')
        base = os.path.basename(f).replace('.md', '')
        title = m_title.group(1)

        # GitHub 新聞：用 shot1 做背景重新生成（unwire 式）
        if m_gh:
            # shot1 檔名有多種命名（有/冇 -hk 後綴），直接 scan 目錄匹配
            shot1 = None
            for cand in [f"{base}-shot1.png", f"{base}-shot1.jpg"]:
                p = os.path.join(BLOG, "assets", "images", "posts", cand)
                if os.path.exists(p):
                    shot1 = p
                    break
            if not shot1:
                # 最後 fallback：glob 掃描 github-*{project}*-shot1.*
                m2 = re.search(r'github-([a-z0-9-]+?)-news(?:-hk)?$', base)
                proj = m2.group(1) if m2 else None
                if proj:
                    import glob as _glob
                    cands = _glob.glob(os.path.join(BLOG, "assets", "images", "posts", f"github-*{proj}*-shot1.*"))
                    if cands:
                        shot1 = cands[0]
            if shot1:
                r = regen_cover(f, shot1, title, m_gh.group(1).split('/')[-1])
                if r.startswith("✅"):
                    gh_done += 1
                else:
                    gh_fail.append(r)
            else:
                gh_skip += 1
                other_fail.append(f"❌ {base}: 搵唔到 shot1 檔")
            continue

        # 外媒新聞（type: news 但冇 shot1）：用 AI 背景
        if re.search(r'^type:\s*news', c, re.M):
            m2 = re.search(r'(news-[a-z0-9-]+-hk)', base)
            news_key = m2.group(1) if m2 else base
            bg_map = {
                "news-claude-code-auto-mode-hk": os.path.join(TMP, "claude-ref-cover.jpg"),
                "news-deepmind-weathernext-cyclone-hk": os.path.join(TMP, "weather-ref-cover.jpg"),
            }
            bg = bg_map.get(news_key)
            if bg and os.path.exists(bg):
                r = regen_cover(f, bg, title, "AnIskill News")
                if r.startswith("✅"):
                    gh_done += 1
                else:
                    gh_fail.append(r)
            else:
                other_fail.append(f"❌ {base}: 冇 AI 背景")
            continue

        # 其他文章：crop 正方形
        r = crop_square(f, img)
        if r.startswith("✅"):
            other_done += 1
        elif r.startswith("⏭️"):
            other_skip += 1
        else:
            other_fail.append(r)

    print(f"\n=== 完成 ===")
    print(f"GitHub/新聞重新生成（unwire 式）: {gh_done} 篇")
    print(f"其他文章 crop 正方形: {other_done} 篇（{other_skip} 已係）")
    if gh_fail:
        print(f"⚠️ GitHub/新聞失敗 {len(gh_fail)}:")
        for x in gh_fail: print(f"  {x}")
    if other_fail:
        print(f"⚠️ 其他失敗 {len(other_fail)}:")
        for x in other_fail[:15]: print(f"  {x}")


if __name__ == "__main__":
    main()
