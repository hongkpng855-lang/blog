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
FONT_EN = os.path.join(FONT_DIR, "AlfaSlabOne-Regular.ttf")       # 英文 Slab Serif（unwire 風格）
FONT_ZH = os.path.join(FONT_DIR, "NotoSansCJKsc-Black.otf")      # 中文 Heavy/Black（unwire 風格）
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


def smart_crop(img):
    """智能 crop：分析內容區（非白色像素），裁走留白 + scrollbar（2026-08-10 用戶要求 README cap 得好啲）"""
    import numpy as np
    gray = img.convert('L')
    arr = np.array(gray)
    w, h = img.size
    content = arr < 245  # 非白色 = 內容
    row_c = content.mean(axis=1)
    col_c = content.mean(axis=0)

    def find_bounds(arr_c, threshold=0.001):
        active = arr_c > threshold
        idx = np.where(active)[0]
        if len(idx) == 0:
            return 0, len(arr_c)
        return int(idx[0]), int(idx[-1])

    top, bottom = find_bounds(row_c)
    left, right = find_bounds(col_c)
    # 加返少量 padding（唔好切到貼邊內容）
    pad = 30
    top = max(0, top - pad)
    left = max(0, left - pad)
    bottom = min(h, bottom + pad)
    right = min(w, right + pad)
    return img.crop((left, top, right, bottom))


def make_cover(bg, title_zh, title_en, out):
    img = load_bg(bg)
    # 智能 crop：裁走留白 + scrollbar（GitHub README 截圖適用）
    img = smart_crop(img)
    # 統一 1080x1080 正方形（IG/FB 最佳比例，2026-08-10 用戶要求）
    tw, th = 1080, 1080
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
    start = int(h * 0.55)
    for i in range(start, h):
        t = (i - start) / (h - start)
        od.line([(0, i), (w, i)], fill=(0, 0, 0, int(60 + 195 * (t ** 1.5))))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)

    font_en = ImageFont.truetype(FONT_EN, 30)
    font_zh = ImageFont.truetype(FONT_ZH, 96)

    # ===== unwire 排版（正方形佈局，文字區塊喺底部三分一） =====
    zh_lines = [ln.strip() for ln in title_zh.split("|") if ln.strip()] if "|" in title_zh else [title_zh]
    # 文字區塊底部對齊：英文標題喺底部三分一（y ~700）
    if title_en:
        draw_center(draw, 640, title_en.upper(), font_en, (10, 10, 12), w, spacing=6, outline=GOLD, stroke=3)
        draw.line([(w // 2 - 110, 700), (w // 2 + 110, 700)], fill=GOLD, width=4)

    # 中文標題喺分隔線下方
    y = 720
    for i, ln in enumerate(zh_lines):
        if len(zh_lines) == 2 and i == 1:
            draw_center(draw, y, ln, font_zh, (0, 0, 0), w, outline=GOLD, stroke=6)
        else:
            draw_center(draw, y, ln, font_zh, WHITE, w, shadow=True)
        y += 140

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
