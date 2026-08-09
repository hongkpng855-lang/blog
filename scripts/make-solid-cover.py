#!/usr/bin/env python3
"""
make-solid-cover.py — 底色式新聞封面（unwire.hk 風格，v1.0，2026-08-10）
用法:
  python3 make-solid-cover.py --title-zh "中文標題" --title-en "English" --out <輸出路徑> [--bg-color "#17181C"] [--accent "#E8A33D"]

風格:
  - 深色純色背景（預設炭黑 #17181C）
  - 大字標題：可選「實心 + 空心描邊」混合（unwire 風格）
  - 英文標題細字置頂 + 金色分隔線
  - 冇水印、冇日期、冇來源（簡潔）
"""
import argparse, os
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "fonts")
FONT_BOLD = os.path.join(FONT_DIR, "NotoSansCJKsc-Bold.otf")
FONT_REG = os.path.join(FONT_DIR, "NotoSansCJKsc-Regular.otf")


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def draw_outline_text(draw, x, y, text, font, fill, outline_color, stroke_width=4):
    """空心描邊文字（unwire 風格）"""
    draw.text((x, y), text, font=font, fill=outline_color,
              stroke_width=stroke_width, stroke_fill=outline_color)
    draw.text((x, y), text, font=font, fill=fill)


def draw_center(draw, y, text, font, fill, w, spacing=0, outline=None, stroke=0):
    total = 0
    widths = []
    for ch in text:
        bbox = draw.textbbox((0, 0), ch, font=font)
        cw = bbox[2] - bbox[0]
        widths.append(cw)
        total += cw + spacing
    total -= spacing
    x = (w - total) / 2
    for ch, cw in zip(text, widths):
        if outline:
            draw_outline_text(draw, x, y, ch, font, fill, outline, stroke)
        else:
            draw.text((x, y), ch, font=font, fill=fill)
        x += cw + spacing
    return total


def smart_split(title):
    """智能斷行：支援 | 手動標記；否則喺空格/完整詞之間斷，唔斬英文單字"""
    if "|" in title:
        return [ln.strip() for ln in title.split("|") if ln.strip()]
    # 自動：每行上限 8 字，優先在空格斷
    max_len = 8
    words = title.split()
    lines, cur = [], ""
    for wd in words:
        if not cur:
            cur = wd
        elif len(cur) + 1 + len(wd) <= max_len:
            cur += " " + wd
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    # 如果任何一行仲超過 max_len（長英文詞/長中文），強行按字切
    final = []
    for ln in lines:
        while len(ln) > max_len:
            # 搵最後一個空格切（冇就切 max_len）
            cut = ln.rfind(" ", 0, max_len + 1)
            if cut <= 0:
                cut = max_len
            final.append(ln[:cut])
            ln = ln[cut:].strip()
        if ln:
            final.append(ln)
    return final


def make_cover(title_zh, title_en, out, bg_color="#17181C", accent="#E8A33D"):
    w, h = 1200, 630
    bg = hex_to_rgb(bg_color)
    accent_rgb = hex_to_rgb(accent)
    img = Image.new("RGB", (w, h), bg)
    draw = ImageDraw.Draw(img)

    font_en = ImageFont.truetype(FONT_BOLD, 30)
    font_zh = ImageFont.truetype(FONT_BOLD, 88)   # 大字標題

    # ===== 英文標題（頂部，金色，字距） =====
    if title_en:
        draw_center(draw, 150, title_en.upper(), font_en, accent_rgb, w, spacing=6)
        # 分隔線
        draw.line([(w//2 - 90, 215), (w//2 + 90, 215)], fill=accent_rgb, width=3)

    # ===== 中文標題（大字，置中） =====
    zh_lines = smart_split(title_zh)

    # 多行：第一行實心白字，第二行空心描邊（unwire 混合風格）
    total_h = len(zh_lines) * 120
    y = (h - total_h) // 2 + 30
    for i, ln in enumerate(zh_lines):
        if len(zh_lines) == 2 and i == 1:
            # 第二行：空心描邊（金色邊 + 黑字）
            draw_center(draw, y, ln, font_zh, bg, w, outline=accent_rgb, stroke=5)
        elif len(zh_lines) == 2 and i == 0:
            # 第一行：實心白
            draw_center(draw, y, ln, font_zh, (255, 255, 255), w)
        else:
            draw_center(draw, y, ln, font_zh, (255, 255, 255), w)
        y += 120

    # 底部細橫線裝飾
    draw.line([(100, h - 60), (w - 100, h - 60)], fill=(60, 60, 70), width=1)
    # 左上角品牌點綴
    draw.rectangle([(60, 60), (60 + 14, 60 + 14)], fill=accent_rgb)

    img.save(out, quality=93)
    print(f"✅ 底色封面完成: {out} ({w}x{h})")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--title-zh", required=True, help="中文標題")
    ap.add_argument("--title-en", default="", help="英文標題")
    ap.add_argument("--out", required=True, help="輸出路徑")
    ap.add_argument("--bg-color", default="#17181C", help="背景色")
    ap.add_argument("--accent", default="#E8A33D", help="強調色")
    args = ap.parse_args()
    make_cover(args.title_zh, args.title_en, args.out, args.bg_color, args.accent)
