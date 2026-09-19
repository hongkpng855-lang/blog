#!/usr/bin/env bash
# 開機補跑（2026-09-20 建立）
#
# 背景：部機夜晚會熄/瞓，系統 crontab 追唔到排程 → publish-queue 漏跑（例：9/20
#       00:00–06:00 四個時段全冇跑，佇列積壓）。
# 作用：開機後等網絡通 → 補跑 publish-queue，最多 3 篇、每篇隔 15 分鐘，
#       令積壓文章可以追返。
# 用法（crontab）：@reboot /home/hongk/.openclaw/workspace/jekyll-blog/scripts/reboot-catchup.sh
set -u

BLOG_DIR="/home/hongk/.openclaw/workspace/jekyll-blog"
LOG="$BLOG_DIR/logs/publish-queue.log"
PY="/usr/bin/python3"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] [reboot-catchup] $*" >>"$LOG"; }

cd "$BLOG_DIR" || exit 0

# 開機後 cron 即刻行，等系統/網絡穩定
sleep 120

# 等網絡（最多 5 分鐘），未有網就唔好硬跑（會 push 失敗）
for _ in $(seq 1 30); do
  if curl -sS -m 10 -o /dev/null "https://hongkpng855-lang.github.io/blog/" 2>/dev/null; then
    NET_OK=1
    break
  fi
  sleep 10
done

if [ "${NET_OK:-0}" != "1" ]; then
  log "⚠️ 網絡未通，放棄今次開機補跑（等下個整點 cron）"
  exit 0
fi

log "🔄 開機補跑開始（最多 3 篇，每篇隔 900 秒）"
"$PY" "$BLOG_DIR/scripts/publish-queue.py" --max 3 --gap 900 >>"$LOG" 2>&1
log "🔄 開機補跑結束 rc=$?"
