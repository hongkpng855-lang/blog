#!/usr/bin/env python3
"""批量將 GitHub 新聞封面轉成 unwire 式（截圖背景 + 標題文字）"""
import os, re, glob, subprocess, sys

BLOG = "/home/hongk/.openclaw/workspace/jekyll-blog"
POSTS = os.path.join(BLOG, "_posts")
SCRIPT = os.path.join(BLOG, "scripts", "make-cover.py")


def parse_title(title):
    """title: '9.6 萬星開源項目：Deep-Live-Cam — 一張照片實時換臉'
    → (stars, name, desc)"""
    m = re.match(r'^([\d.]+ 萬星開源項目)[：:]\s*(.+?)\s*[—–-]\s*(.+)$', title)
    if m:
        return m.group(1), m.group(2).strip(), m.group(3).strip()
    # fallback: 冇星數格式
    m2 = re.match(r'^(.+?)[—–-]\s*(.+)$', title)
    if m2:
        return "", m2.group(1).strip(), m2.group(2).strip()
    return "", title, ""


def build_zh(name, desc, stars):
    """中文標題：第一行描述（截 10 字），第二行星數"""
    line1 = desc
    if len(line1) > 10:
        line1 = line1[:10]
    parts = []
    if line1:
        parts.append(line1)
    if stars:
        parts.append(stars.replace(" ", ""))
    return "|".join(parts) if parts else name


def main():
    files = sorted(glob.glob(os.path.join(POSTS, "*.md")), reverse=True)
    done, skipped = [], []
    for f in files:
        content = open(f, encoding='utf-8').read()
        m_img = re.search(r'^image:\s*(\S+)', content, re.M)
        if not m_img or 'shot1.png' not in m_img.group(1):
            continue
        m_title = re.search(r'^title:\s*"([^"]+)"', content, re.M)
        m_gh = re.search(r'^creator_github:\s*(\S+)', content, re.M)
        if not m_title or not m_gh:
            skipped.append(os.path.basename(f))
            continue
        title = m_title.group(1)
        repo = m_gh.group(1).split('/')[-1]
        stars, name, desc = parse_title(title)
        slug = os.path.basename(f).replace('.md', '')

        # 英文標題 = 項目名（大寫），簡化
        en = repo.replace('-', ' ').replace('_', ' ').title() if repo else name
        en = re.sub(r'\s+', ' ', en).strip()

        zh = build_zh(name, desc, stars)
        shot1 = m_img.group(1).lstrip('/')  # assets/images/posts/xxx-shot1.png
        bg = os.path.join(BLOG, shot1)
        out = os.path.join(BLOG, "assets", "images", "posts", f"{slug}-cover.jpg")

        if not os.path.exists(bg):
            skipped.append(f"{os.path.basename(f)} (冇 shot1: {bg})")
            continue

        # 生成封面
        r = subprocess.run(["python3", SCRIPT, "--bg", bg,
                            "--title-zh", zh, "--title-en", en, "--out", out],
                           capture_output=True, text=True)
        if r.returncode != 0:
            skipped.append(f"{os.path.basename(f)} (make-cover fail: {r.stderr[:100]})")
            continue

        # 更新 front matter image
        new_content = content.replace(
            f"image: {m_img.group(1)}",
            f"image: /assets/images/posts/{slug}-cover.jpg", 1)
        open(f, 'w', encoding='utf-8').write(new_content)
        done.append(os.path.basename(f))

    print(f"✅ 完成 {len(done)} 篇")
    if skipped:
        print(f"⚠️ 跳過 {len(skipped)} 篇:")
        for s in skipped:
            print(f"   {s}")


if __name__ == "__main__":
    main()
