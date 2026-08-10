#!/usr/bin/env bash
# github-readme-shot.sh — 自動截 GitHub README 開頭做封面背景（V15 流程，2026-08-10）
# 用 browser (CDP) 開頁 → 加大 viewport → scroll 去 README → 隱藏右欄 → 截圖
# 用法: bash github-readme-shot.sh <repo_url> <output_path>
# 例: bash github-readme-shot.sh https://github.com/huggingface/transformers /tmp/readme.png

REPO_URL="$1"
OUT="$2"
if [ -z "$REPO_URL" ] || [ -z "$OUT" ]; then
  echo "用法: $0 <repo_url> <output_path>"
  exit 1
fi

# 用 Node CDP script（連 browser）截圖
node /home/hongk/.openclaw/workspace/jekyll-blog/scripts/cdp-readme-shot.mjs "$REPO_URL" "$OUT" 2>&1

if [ -f "$OUT" ]; then
  echo "✅ 截圖完成: $OUT"
  python3 - "$OUT" <<'PYEOF'
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L')
import statistics
pixels = list(im.resize((50, 50)).getdata())
avg = statistics.mean(pixels)
std = statistics.stdev(pixels)
print(f"  平均亮度: {avg:.0f} / 標準差: {std:.0f}")
if std < 8:
    print("  ⚠️ 圖太單調（可能空白/未 render），請檢查")
PYEOF
else
  echo "❌ 截圖失敗"
  exit 1
fi
