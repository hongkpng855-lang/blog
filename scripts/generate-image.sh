#!/bin/bash
# ~/.openclaw/workspace/scripts/generate-image.sh

PROMPT="$1"
OUTPUT_FILE="$2"
BLOG_DIR="$HOME/.openclaw/workspace/jekyll-blog"

if [ -z "$PROMPT" ] || [ -z "$OUTPUT_FILE" ]; then
  echo "用法: $0 <prompt> <output_filename>"
  exit 1
fi

cd "$BLOG_DIR/assets/images/posts" || exit 1

echo "🎨 提交生成請求..."
job_response=$(curl -s --max-time 30 -X POST https://aihorde.net/api/v2/generate/async \
  -H "apikey: 0000000000" \
  -H "Content-Type: application/json" \
  -d "{
    \"prompt\": \"$PROMPT\",
    \"params\": {
      \"width\": 512,
      \"height\": 512,
      \"steps\": 20,
      \"cfg_scale\": 7
    },
    \"models\": [\"stable_diffusion\"]
  }")

# Extract job ID using python (since jq may not be available)
job_id=$(echo "$job_response" | python3 -c "import sys, json; print(json.load(sys.stdin)['id'])")
if [ -z "$job_id" ]; then
  echo "❌ 無法取得 Job ID: $job_response"
  exit 1
fi
echo "📝 Job ID: $job_id"

echo "⏳ 等待生成..."
while true; do
  status=$(curl -s --max-time 30 -H "apikey: 0000000000" \
    "https://aihorde.net/api/v2/generate/check/$job_id")
  # Use python to parse done
  done=$(echo "$status" | python3 -c "import sys, json; print(json.load(sys.stdin).get('done', False))")
  if [ "$done" = "True" ] || [ "$done" = "true" ]; then
    echo "✅ 生成完成！"
    break
  fi
  wait_time=$(echo "$status" | python3 -c "import sys, json; print(json.load(sys.stdin).get('wait_time', 0))")
  echo "⏳ 預計等待 ${wait_time} 秒..."
  sleep 5
done

echo "📥 下載圖片..."
image_url=$(curl -s --max-time 30 -H "apikey: 0000000000" \
  "https://aihorde.net/api/v2/generate/status/$job_id" \
  | python3 -c "import sys, json; print(json.load(sys.stdin)['generations'][0]['img'])")
if [ -z "$image_url" ]; then
  echo "❌ 無法取得圖片 URL"
  exit 1
fi

curl -sL --max-time 30 -o "$OUTPUT_FILE" "$image_url"

echo "✅ 圖片已儲存至: $BLOG_DIR/assets/images/posts/$OUTPUT_FILE"