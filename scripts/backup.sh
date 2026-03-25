#!/bin/bash

# Jekyll 部落格備份腳本
# 用途：建立專案備份，包含時間戳記

# 設定
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BACKUP_BASE="$HOME/.openclaw/workspace/backups/jekyll-blog"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="$BACKUP_BASE/backup_$DATE"

# 顏色輸出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}========================================${NC}"
echo -e "${YELLOW}Jekyll 部落格備份腳本${NC}"
echo -e "${YELLOW}========================================${NC}"
echo ""

# 建立備份目錄
echo -e "${YELLOW}[1/4] 建立備份目錄...${NC}"
mkdir -p "$BACKUP_DIR"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ 備份目錄已建立：$BACKUP_DIR${NC}"
else
    echo -e "${RED}✗ 無法建立備份目錄${NC}"
    exit 1
fi

# 複製專案檔案
echo -e "${YELLOW}[2/4] 複製專案檔案...${NC}"
rsync -av --exclude='.git' --exclude='node_modules' --exclude='.jekyll-cache' "$PROJECT_DIR/" "$BACKUP_DIR/"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ 專案檔案已備份${NC}"
else
    echo -e "${RED}✗ 檔案備份失敗${NC}"
    exit 1
fi

# 記錄備份資訊
echo -e "${YELLOW}[3/4] 記錄備份資訊...${NC}"
echo "備份時間: $(date)" > "$BACKUP_DIR/backup_info.txt"
echo "專案路徑: $PROJECT_DIR" >> "$BACKUP_DIR/backup_info.txt"
echo "Git 分支: $(cd $PROJECT_DIR && git branch --show-current 2>/dev/null || echo 'N/A')" >> "$BACKUP_DIR/backup_info.txt"
echo "Git 提交: $(cd $PROJECT_DIR && git rev-parse --short HEAD 2>/dev/null || echo 'N/A')" >> "$BACKUP_DIR/backup_info.txt"
echo -e "${GREEN}✓ 備份資訊已記錄${NC}"

# 清理舊備份（保留最近 10 個）
echo -e "${YELLOW}[4/4] 清理舊備份...${NC}"
cd "$BACKUP_BASE"
ls -t | tail -n +11 | xargs -r rm -rf
BACKUP_COUNT=$(ls -d backup_* 2>/dev/null | wc -l)
echo -e "${GREEN}✓ 目前保留 $BACKUP_COUNT 個備份${NC}"

# 完成訊息
echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}備份完成！${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "備份位置: ${YELLOW}$BACKUP_DIR${NC}"
echo -e "備份大小: ${YELLOW}$(du -sh $BACKUP_DIR | cut -f1)${NC}"
echo ""

# 可選：自動推送到 GitHub（需要 git 認證）
read -p "是否要建立 Git tag 並推送？(y/N): " push_choice
if [[ "$push_choice" =~ ^[Yy]$ ]]; then
    cd "$PROJECT_DIR"
    git tag -a "backup_$DATE" -m "自動備份 $(date)"
    git push origin --tags
    echo -e "${GREEN}✓ Git tag 已建立並推送${NC}"
fi

exit 0
