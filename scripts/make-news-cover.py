#!/usr/bin/env python3
"""
make-news-cover.py — 新聞封面專業生成器（v1.0，2026-08-10）
用法:
  python3 make-news-cover.py --bg <背景圖路徑或URL> --title-zh "中文標題" --title-en "English Title" --sub "副標題" --out <輸出路徑> [--watermark "AnIskill"]

流程:
  1. 背景圖: 可傳本地路徑或 URL（自動下載）
  2. 底部漸層遮罩（保障文字可讀性）
  3. 英文標題（細、金色、字距闊）+ 分隔線 + 中文標題（大、白色、粗體）+ 副標題
  4. 右下角水印（半透明，品牌名）
  5. 輸出 1200x630 或原圖比例 JPG

文字100%由程式渲染 → 保證唔會變形/亂碼（AI 生成文字先會變形）
"""
import argparse, os, sys, urllib.request, tempfile

from PIL import Image, ImageDraw, ImageFont

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "fonts")
FONT_BOLD = os.path.join(FONT_DIR, "NotoSansCJKsc-Bold.otf")
FONT_REG = os.path.join(FONT_DIR, "NotoSansCJKsc-Regular.otf")
BRAND_COLOR = (201, 168, 76)   # 金 #C9A84C
WHITE = (255, 255, 255)


def load_bg(bg):
    """背景圖：本地路徑或 URL"""
    if bg.startswith("http://") or bg.startswith("https://"):
        req = urllib.request.Request(bg, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=60).read()
        tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
        tmp.write(data)
        tmp.close()
        path = tmp.name
    else:
        path = bg
    return Image.open(path).convert("RGB"), path


def draw_center_text(draw, y, text, font, fill, w, letter_spacing=0):
    """畫置中文字（支援字距）"""
    if letter_spacing == 0:
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((w - tw) / 2, y), text, font=font, fill=fill)
        return
    # 字距模式：逐字畫
    total_w = 0
    char_widths = []
    for ch in text:
        bbox = draw.textbbox((0, 0), ch, font=font)
        cw = bbox[2] - bbox[0]
        char_widths.append(cw)
        total_w += cw + letter_spacing
    total_w -= letter_spacing
    x = (w - total_w) / 2
    for ch, cw in zip(text, char_widths):
        draw.text((x, y), ch, font=font, fill=fill)
        x += cw + letter_spacing


def make_cover(bg, title_zh, title_en, sub, out, watermark=""):
    img, _ = load_bg(bg)
    # 統一輸出尺寸: 1200x630（新聞封面標準），背景 cover crop
    target_w, target_h = 1200, 630
    iw, ih = img.size
    scale = max(target_w / iw, target_h / ih)
    img = img.resize((int(iw * scale), int(ih * scale)), Image.LANCZOS)
    img = img.crop(((img.width - target_w) // 2, (img.height - target_h) // 2,
                    (img.width - target_w) // 2 + target_w, (img.height - target_h) // 2 + target_h))
    w, h = img.size

    # 底部漸層遮罩（最後 55% 漸黑，保障文字可讀）
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    start = int(h * 0.42)
    for i in range(start, h):
        t = (i - start) / (h - start)
        alpha = int(40 + 215 * (t ** 1.5))
        od.line([(0, i), (w, i)], fill=(0, 0, 0, alpha))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)

    # ===== 字體 =====
    font_en = ImageFont.truetype(FONT_BOLD, 26)      # 英文標題
    font_zh = ImageFont.truetype(FONT_BOLD, 52)      # 中文標題
    font_sub = ImageFont.truetype(FONT_REG, 22)      # 副標題
    font_wm = ImageFont.truetype(FONT_BOLD, 20)      # 水印

    # ===== 排版（由底向上） =====
    # 1. 副標題（最底）— 可選
    sub_y = h - 34 - 22
    if sub:
        draw_center_text(draw, sub_y, sub, font_sub, (230, 230, 230), w)

    # 2. 中文標題（副標題之上）
    zh_y = sub_y - 30 - 52 if sub else h - 60 - 52
    # 多行處理
    zh_lines, line = [], ""
    for ch in title_zh:
        line += ch
        if len(line) >= 12:
            zh_lines.append(line); line = ""
    if line: zh_lines.append(line)
    if len(zh_lines) > 1:
        zh_y = sub_y - 30 - 52 * len(zh_lines)
    for i, ln in enumerate(zh_lines):
        draw_center_text(draw, zh_y + i * 62, ln, font_zh, WHITE, w)

    # 3. 分隔線（中英之間）
    line_y = zh_y - 22
    draw.line([(w // 2 - 70, line_y), (w // 2 + 70, line_y)], fill=BRAND_COLOR, width=3)

    # 4. 英文標題（最上，金色，字距）
    en_y = line_y - 40
    if title_en:
        draw_center_text(draw, en_y, title_en.upper(), font_en, BRAND_COLOR, w, letter_spacing=4)

    # ===== 水印（右下角）— 預設冇，傳 watermark 先顯示 =====
    if watermark:
        wm_text = f"◆ {watermark}"
        bbox = draw.textbbox((0, 0), wm_text, font=font_wm)
        wm_w = bbox[2] - bbox[0]
        draw.text((w - wm_w - 18, h - 18 - 20), wm_text, font=font_wm, fill=(255, 255, 255, 160))

    img.save(out, quality=93)
    print(f"✅ 封面完成: {out} ({w}x{h})")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--bg", required=True, help="背景圖路徑或 URL")
    ap.add_argument("--title-zh", required=True, help="中文標題")
    ap.add_argument("--title-en", default="", help="英文標題")
    ap.add_argument("--sub", default="", help="副標題")
    ap.add_argument("--out", required=True, help="輸出路徑")
    ap.add_argument("--watermark", default="", help="水印文字（預設冇）")
    args = ap.parse_args()
    make_cover(args.bg, args.title_zh, args.title_en, args.sub, args.out, args.watermark)
