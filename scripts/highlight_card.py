#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make-highlight-card.py — 文章「最精彩一段」金句卡（2026-10-01 用戶要求）

IG / FB 發文除咗封面，加多一張金句卡：抽出文章最精彩嗰段文字，
排成 1080x1080 深藍金字卡（同封面同尺寸，IG carousel / FB 多圖都夾得埋）。

用法：
  python3 make-highlight-card.py --post _posts/2026-10-01-xxx.md \
      --out assets/images/posts/highlights/2026-10-01-xxx-highlight.jpg
  python3 make-highlight-card.py --post _posts/2026-10-01-xxx.md --print-only

作為模組用（fb/ig script import）：
  from importlib.machinery import SourceFileLoader
  hl = SourceFileLoader("mhlc", "scripts/make-highlight-card.py").load_module()
  text = hl.extract_highlight(post_path)   # 抽金句文字
  hl.make_card(text, out_path)             # 生成卡
"""
import argparse
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "fonts")
FONT_CJK_BOLD = os.path.join(FONT_DIR, "NotoSansCJKsc-Bold.otf")
FONT_LATIN = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

NAVY_TOP = (14, 20, 38)
NAVY_BOT = (30, 47, 84)
GOLD = (201, 168, 76)
WHITE = (245, 246, 248)
W = H = 1080

# 「有金句感」嘅轉折 / 洞察字眼（出現越多、越似值得獨立抽出來嘅一句）
CONTRAST = ["但", "然而", "其實", "真正", "或許", "往往", "不只", "不是", "而是",
            "反而", "卻", "值得", "關鍵", "難題", "盲點", "矛盾"]


# ---------- 文字抽取 ----------

def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if m:
        return m.group(1), text[m.end():]
    return "", text


def _fb_first_para(fm):
    m = re.search(r'^fb_message:\s*["\']?(.+?)["\']?\s*$', fm, re.M)
    if not m:
        return ""
    v = m.group(1).replace("\\n", "\n").strip().strip('"\'')
    return v.split("\n\n")[0].strip()


def _trim(p, limit=150):
    p = p.strip().strip('"\'')
    if len(p) <= limit:
        return p
    cut = p[:limit]
    for sep in "。！？":
        idx = cut.rfind(sep)
        if idx >= 40:
            return cut[:idx + 1]
    return cut.rstrip() + "…"


def extract_paragraphs(body):
    """文章正文 → 候選段落清單（已剝 capsule / 圖片 / HTML / 標題）"""
    # 移除 AEO capsule（連入面嘅文字）
    body = re.sub(r"<!--\s*AEO Answer Capsule.*?<!--\s*End AEO Capsule\s*-->",
                  "", body, flags=re.S | re.I)
    # 移除其餘 HTML 註解
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    # 移除圖片 + HTML tag
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)
    body = re.sub(r"<[^>]+>", "", body)

    paras = []
    for raw in re.split(r"\n\s*\n", body):
        p = re.sub(r"\s+", " ", raw).strip()
        if not p:
            continue
        if p[0] in "#|-*>" and not p.startswith(">"):
            continue
        p = p.lstrip("> ").strip()
        if not p or len(p) < 35:
            continue
        if "http" in p or "{{" in p or "%}" in p:
            continue
        paras.append(p)
    return paras


def extract_highlight(post_path, fallback_fb=True):
    """回傳（金句文字, 來源）。優先抽正文最精彩一段，冇就退去 fb_message 首段。"""
    text = _read(post_path)
    fm, body = _front_matter(text)
    paras = extract_paragraphs(body)

    best, best_score = None, -1
    for i, p in enumerate(paras):
        score = 0
        if 45 <= len(p) <= 135:
            score += 3
        elif len(p) <= 175:
            score += 1
        hits = sum(1 for w in CONTRAST if w in p)
        score += min(6, hits * 2)
        if p.endswith(("。", "？", "！")):
            score += 1
        if i < 4:
            score += 1
        if score > best_score:
            best, best_score = p, score

    if best:
        return _trim(best), "body"
    if fallback_fb:
        fb = _fb_first_para(fm)
        if fb:
            return _trim(fb, 130), "fb_message"
    return "", "none"


# ---------- 繪圖 ----------

def _wrap(draw, text, font, max_w):
    lines, cur = [], ""
    for ch in text:
        if draw.textlength(cur + ch, font=font) <= max_w:
            cur += ch
        else:
            lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines


def make_card(text, out, domain="aniskill.esgov.org"):
    if not text:
        raise ValueError("冇金句文字，唔可以生成卡")

    img = Image.new("RGB", (W, H), NAVY_TOP)
    d = ImageDraw.Draw(img)
    # 垂直漸層
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=(
            int(NAVY_TOP[0] + (NAVY_BOT[0] - NAVY_TOP[0]) * t),
            int(NAVY_TOP[1] + (NAVY_BOT[1] - NAVY_TOP[1]) * t),
            int(NAVY_TOP[2] + (NAVY_BOT[2] - NAVY_TOP[2]) * t)))
    # 右上角金色柔光
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(ov).ellipse([W - 360, -300, W + 260, 320], fill=(201, 168, 76, 26))
    img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(img)

    # 引號裝飾
    try:
        fq = ImageFont.truetype(FONT_LATIN, 170)
        d.text((72, 34), "\u201C", font=fq, fill=GOLD)
        d.text((W - 190, H - 350), "\u201D", font=fq, fill=GOLD)
    except Exception:
        pass

    # 自動字級：揀最大而唔爆版嘅 size
    max_w = W - 240
    lines = None
    font = None
    lh = 0
    for size in range(68, 33, -2):
        f = ImageFont.truetype(FONT_CJK_BOLD, size)
        ls = _wrap(d, text, f, max_w)
        if len(ls) <= 7 and len(ls) * int(size * 1.55) <= 560:
            lines, font, lh = ls, f, int(size * 1.55)
            break
    if lines is None:
        font = ImageFont.truetype(FONT_CJK_BOLD, 34)
        lines = _wrap(d, text, font, max_w)
        lh = int(34 * 1.55)

    total = len(lines) * lh
    y = (H - total) // 2 - 4
    for ln in lines:
        tw = d.textlength(ln, font=font)
        d.text(((W - tw) / 2, y), ln, font=font, fill=WHITE)
        y += lh

    # 底部金線 + domain
    d.line([(W / 2 - 90, H - 186), (W / 2 + 90, H - 186)], fill=GOLD, width=5)
    try:
        fdom = ImageFont.truetype(FONT_LATIN, 36)
    except Exception:
        fdom = ImageFont.load_default()
    tw = d.textlength(domain, font=fdom)
    d.text(((W - tw) / 2, H - 160), domain, font=fdom, fill=GOLD)

    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    img.save(out, "JPEG", quality=92)
    return out


# ---------- 模組介面（供 fb-auto-post / ig-auto-post / publish-queue 使用）----------

HIGHLIGHT_REL_DIR = "assets/images/posts/highlights"


def card_rel_path(slug):
    """金句卡喺 jekyll root 之下嘅相對路徑"""
    return f"{HIGHLIGHT_REL_DIR}/{slug}-highlight.jpg"


def build_card(post_path, jekyll_dir, slug, only_if_missing=True):
    """生成金句卡，回傳相對路徑（抽唔到文字回 None）。

    only_if_missing=True（預設）：已有卡就唔重生（可重入，避免覆寫／重複 commit）。
    """
    rel = card_rel_path(slug)
    out = os.path.join(jekyll_dir, rel)
    if only_if_missing and os.path.exists(out):
        return rel
    text, _src = extract_highlight(post_path)
    if not text:
        return None
    make_card(text, out)
    return rel


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--post", required=True, help="文章 markdown 路徑")
    ap.add_argument("--out", help="輸出 JPG 路徑")
    ap.add_argument("--domain", default="aniskill.esgov.org")
    ap.add_argument("--print-only", action="store_true", help="只印抽到嘅文字，唔出圖")
    args = ap.parse_args()

    text, src = extract_highlight(args.post)
    print(f"[來源：{src}] {len(text)} 字")
    print(text)
    if args.print_only:
        return
    if not args.out:
        ap.error("需要 --out 或者 --print-only")
    if not text:
        print("⚠️ 抽唔到金句文字，唔生成卡", file=sys.stderr)
        sys.exit(1)
    out = make_card(text, args.out, args.domain)
    print(f"✅ 金句卡完成: {out} ({W}x{H})")


if __name__ == "__main__":
    main()
