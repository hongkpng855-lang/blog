#!/usr/bin/env python3
"""
make-cover.py — 統一封面生成器 v2.0（2026-08-10 用戶確認最終版）
背景圖（截圖 / AI 生成圖）+ unwire 式文字排版（金色英文置頂 + 分隔線 + 白色大字 + 金色描邊強調）

用法:
  python3 make-cover.py --bg <背景圖路徑或URL> --title-zh "中文標題|第二行(可選)" --title-en "English" --out <輸出.jpg>

規則（2026-08-10 用戶確認）:
  - 冇水印、冇日期、冇來源
  - 文字 100% 程式渲染（Noto Sans CJK）→ 唔變形唔亂碼
  - 中文標題用 | 斷行（唔好斬開英文單字）
  - GitHub 新聞: bg = 第一張截圖
  - 外媒新聞: bg = AI 生成背景（原文圖參考，prompt 加 no text）
"""
import argparse, os, sys, urllib.request, tempfile
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "fonts")
FONT_BOLD = os.path.join(FONT_DIR, "NotoSansCJKsc-Bold.otf")
FONT_REG = os.path.join(FONT_DIR, "NotoSansCJKsc-Regular.otf")
GOLD = (201, 168, 76)
WHITE = (255, 255, 255)


def load_bg(bg):
    if bg.startswith("http://") or bg.startswith("https://"):
        req = urllib.request.Request(bg, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=60).read()
        tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
        tmp.write(data)
        tmp.close()
        return Image.open(tmp.name).convert("RGB")
    return Image.open(bg).convert("RGB")


def draw_center(draw, y, text, font, fill, w, spacing=0, outline=None, stroke=0, shadow=False):
    total, widths = 0, []
    for ch in text:
        bbox = draw.textbbox((0, 0), ch, font=font)
        cw = bbox[2] - bbox[0]
        widths.append(cw)
        total += cw + spacing
    total -= spacing
    x = (w - total) / 2
    for ch, cw in zip(text, widths):
        if shadow:
            draw.text((x + 3, y + 3), ch, font=font, fill=(0, 0, 0, 190))
        if outline:
            draw.text((x, y), ch, font=font, fill=outline, stroke_width=stroke, stroke_fill=outline)
            draw.text((x, y), ch, font=font, fill=fill)
        else:
            draw.text((x, y), ch, font=font, fill=fill)
        x += cw + spacing


def make_cover(bg, title_zh, title_en, out):
    img = load_bg(bg)
    # 統一 1200x630，cover crop
    tw, th = 1200, 630
    iw, ih = img.size
    scale = max(tw / iw, th / ih)
    img = img.resize((int(iw * scale), int(ih * scale)), Image.LANCZOS)
    img = img.crop(((img.width - tw) // 2, (img.height - th) // 2,
                    (img.width - tw) // 2 + tw, (img.height - th) // 2 + th))
    w, h = img.size

    # 全畫面微暗 + 底部漸層（保留背景但保障文字可讀）
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle([(0, 0), (w, h)], fill=(0, 0, 0, 55))
    start = int(h * 0.45)
    for i in range(start, h):
        t = (i - start) / (h - start)
        od.line([(0, i), (w, i)], fill=(0, 0, 0, int(60 + 195 * (t ** 1.5))))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)

    font_en = ImageFont.truetype(FONT_BOLD, 30)
    font_zh = ImageFont.truetype(FONT_BOLD, 82)

    # ===== unwire 排版 =====
    if title_en:
        draw_center(draw, 130, title_en.upper(), font_en, GOLD, w, spacing=6, shadow=True)
        draw.line([(w // 2 - 90, 195), (w // 2 + 90, 195)], fill=GOLD, width=3)

    zh_lines = [ln.strip() for ln in title_zh.split("|") if ln.strip()] if "|" in title_zh else [title_zh]
    total_h = len(zh_lines) * 120
    y = (h - total_h) // 2 + 30
    for i, ln in enumerate(zh_lines):
        if len(zh_lines) == 2 and i == 1:
            draw_center(draw, y, ln, font_zh, (0, 0, 0), w, outline=GOLD, stroke=5)
        else:
            draw_center(draw, y, ln, font_zh, WHITE, w, shadow=True)
        y += 120

    img.save(out, quality=93)
    print(f"✅ 封面完成: {out} ({w}x{h})")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--bg", required=True, help="背景圖路徑或 URL")
    ap.add_argument("--title-zh", required=True, help="中文標題（| 斷行）")
    ap.add_argument("--title-en", default="", help="英文標題")
    ap.add_argument("--out", required=True, help="輸出路徑")
    args = ap.parse_args()
    make_cover(args.bg, args.title_zh, args.title_en, args.out)
