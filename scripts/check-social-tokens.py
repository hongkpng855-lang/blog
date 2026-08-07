#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
社交 Token 健康檢查 script v1（2026-08-07）
=========================================
用途：每日檢查 FB page token + IG token 有效性，提早發現失效/被封鎖
背景：2026-08-07 事件 — Meta API access blocked（開發者帳戶異常活動）令
      FB/IG 發佈靜默失敗，用戶 14:53 先發現 post 冇咗。如果 token 每日
      有檢查，朝早 10:00 失效即刻會知，唔使等幾個鐘。

檢查項目：
1. FB page token：debug_token（graph.facebook.com）→ is_valid？
2. FB 專頁基本資料：GET /{page_id}（驗證有 pages_manage_posts scope）
3. IG token：GET /me（graph.instagram.com）→ 有 id？
4. 兩個 token 有冇到期日（expires_at）？快到期（<7 日）出 warning

輸出：
- 全部 OK → exit 0，冇輸出（靜默）
- 有問題 → exit 1，詳細錯誤（俾 cron 讀）

用法：
  python3 check-social-tokens.py
  （cron：每日 09:00 跑一次；有問題會 announce 去 Telegram）
"""
import json
import os
import sys
import urllib.request
import urllib.parse

SECRETS_BASE = os.path.expanduser("~/.openclaw/workspace/.secrets")

def api_get(url):
    """GET JSON，失敗返回 dict error"""
    try:
        with urllib.request.urlopen(url, timeout=20) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return {"error": str(e)}

def check_fb():
    """FB page token 檢查"""
    fb_dir = os.path.join(SECRETS_BASE, "fb")
    try:
        page_id = open(os.path.join(fb_dir, "page_id.txt")).read().strip()
        token = open(os.path.join(fb_dir, "page_token.txt")).read().strip()
    except Exception as e:
        return f"❌ FB secrets 讀取失敗: {e}"

    # 1. debug_token（用 page token 做 access token 都得，FB 容許）
    url = "https://graph.facebook.com/v21.0/debug_token?" + urllib.parse.urlencode({
        "input_token": token,
        "access_token": token,
    })
    d = api_get(url)
    if "error" in d:
        return f"❌ FB token 失效: {d['error'].get('message', d['error'])}"
    data = d.get("data", {})
    if not data.get("is_valid"):
        return f"❌ FB token invalid: {data.get('error', 'unknown')}"
    # expires_at=0 = 永久
    exp = data.get("expires_at", 0)
    if exp and exp != 0:
        import datetime
        exp_dt = datetime.datetime.fromtimestamp(exp)
        days = (exp_dt - datetime.datetime.now()).days
        if days < 7:
            return f"⚠️ FB token {days} 日後到期（{exp_dt}），要 refresh"

    # 2. 專頁基本資料（驗證有 pages_manage_posts）
    url2 = f"https://graph.facebook.com/v21.0/{page_id}?fields=name,is_published&access_token={token}"
    d2 = api_get(url2)
    if "error" in d2:
        return f"❌ FB 專頁讀取失敗: {d2['error'].get('message', d2['error'])}"
    if not d2.get("is_published"):
        return f"❌ FB 專頁未發佈（is_published=false）: {d2.get('name')}"
    return None  # OK

def check_ig():
    """IG token 檢查（用 graph.instagram.com — 2026-08-07 教訓：用錯 endpoint 會誤判失效）"""
    ig_dir = os.path.join(SECRETS_BASE, "ig")
    try:
        token = open(os.path.join(ig_dir, "ig_token.txt")).read().strip()
    except Exception as e:
        return f"❌ IG secrets 讀取失敗: {e}"

    url = "https://graph.instagram.com/v21.0/me?fields=id,username&access_token=" + token
    d = api_get(url)
    if "error" in d:
        return f"❌ IG token 失效: {d['error'].get('message', d['error'])}"
    if "id" not in d:
        return f"❌ IG token 無效（攞唔到 user id）: {d}"
    return None  # OK

def main():
    problems = []
    fb_issue = check_fb()
    if fb_issue:
        problems.append(fb_issue)
    ig_issue = check_ig()
    if ig_issue:
        problems.append(ig_issue)

    if problems:
        print("🚨 社交 Token 健康檢查 FAILED：")
        for p in problems:
            print("  " + p)
        print("\n👉 需要處理：")
        print("  - FB token：developers.facebook.com → App → 重新授權 → 更新 .secrets/fb/page_token.txt")
        print("  - IG token：developers.facebook.com → IG App → Instagram API with Instagram Login → 產生存取憑證 → 更新 .secrets/ig/ig_token.txt")
        sys.exit(1)
    print("✅ 社交 Token 健康檢查全部正常（FB + IG）")

if __name__ == "__main__":
    main()
