#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GSC 題材信號查詢（2026-08-24 建立）

背景：
- 用戶要求「由即使少少嘅開始」— 哪怕篇文章得 1-3 個瀏覽，都好過 0 個瀏覽，呢個就係題材方向信號
- 淨係 focus 現役科技 Blog（aniskill.esgov.org），唔理其他網站
- FB/IG 而家零 followers 零互動，唔可以當指標，唯一有信號係 GSC 搜索數據

功能：
1. 查 GSC（sc-domain:esgov.org）filter 淨係 aniskill.esgov.org 嘅 pages + queries
2. 統計有 clicks 嘅文章（>=1 click 都係信號）、有曝光冇點擊嘅反例
3. 按 URL 分類題材（技術/投資/健康/學習/生活），計每個題材嘅總 clicks / impressions
4. 輸出信號報告到 memory/topic-signals/YYYY-MM-DD.md + 更新 latest.md
5. 純 Python stdlib，零依賴，零 model token

用法：python3 scripts/gsc-topic-signals.py [--days 30] [--min-impressions 10]
"""
import argparse
import datetime
import json
import os
import sys
import time
import urllib.parse
import urllib.request

# ============ 路徑 ============
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JEKYLL_DIR = os.path.dirname(BASE_DIR)
WORKSPACE = os.path.dirname(JEKYLL_DIR)
HERMES_DIR = os.path.expanduser("~/.hermes")
SIGNAL_DIR = os.path.join(WORKSPACE, "memory", "topic-signals")

GSC_SITE = "sc-domain:esgov.org"
BLOG_HOST = "aniskill.esgov.org"

# ============ GSC token ============
def get_access_token():
    """Refresh Google OAuth token（用 ~/.hermes 嘅憑證）"""
    sec = json.load(open(os.path.join(HERMES_DIR, "google_client_secret.json")))["installed"]
    tok = json.load(open(os.path.join(HERMES_DIR, "google_token.json")))
    data = urllib.parse.urlencode({
        "client_id": sec["client_id"],
        "client_secret": sec["client_secret"],
        "refresh_token": tok["refresh_token"],
        "grant_type": "refresh_token",
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data)
    resp = json.loads(urllib.request.urlopen(req, timeout=30).read())
    return resp["access_token"]


def gsc_query(body, at, retries=3):
    """Call GSC searchAnalytics/query API"""
    payload = json.dumps(body).encode()
    req = urllib.request.Request(
        f"https://www.googleapis.com/webmasters/v3/sites/{urllib.parse.quote(GSC_SITE, safe='')}/searchAnalytics/query",
        data=payload,
        headers={"Authorization": "Bearer " + at, "Content-Type": "application/json"},
    )
    for i in range(retries):
        try:
            return json.loads(urllib.request.urlopen(req, timeout=30).read())
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(2)
    return {}


# ============ 題材分類 ============
def classify_slug(page):
    """由 URL 路徑判斷題材分類"""
    path = urllib.parse.unquote(page)
    path = path.replace(f"https://{BLOG_HOST}", "").replace(f"http://{BLOG_HOST}", "")
    lower = path.lower()
    if "/技術/" in lower or "/tech/" in lower or "/技術" in lower:
        return "技術(AI/開源新聞)"
    if "/投資/" in lower or "/investment/" in lower:
        return "投資"
    if "/健康/" in lower or "/health/" in lower:
        return "健康"
    if "/學習/" in lower or "/learning/" in lower:
        return "學習"
    if "/生活/" in lower or "/life/" in lower:
        return "生活"
    return "其他"


def short_name(page):
    """將 page URL 轉做短名稱（slug）"""
    path = urllib.parse.unquote(page).replace(f"https://{BLOG_HOST}", "")
    path = path.replace(f"http://{BLOG_HOST}", "")
    # 攞最後一段
    parts = [p for p in path.split("/") if p]
    if not parts:
        return path
    slug = parts[-1].replace(".html", "")
    if len(slug) > 60:
        slug = slug[:60] + "…"
    return slug


# ============ 主流程 ============
def main():
    parser = argparse.ArgumentParser(description="GSC 題材信號查詢")
    parser.add_argument("--days", type=int, default=30, help="查詢日數（預設 30）")
    parser.add_argument("--min-impressions", type=int, default=10, help="有曝光冇點擊嘅最低曝光門檻（預設 10）")
    parser.add_argument("--top", type=int, default=40, help="顯示 top N 有流量文章（預設 40）")
    args = parser.parse_args()

    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=args.days)
    start_str = start_date.strftime("%Y-%m-%d")
    end_str = end_date.strftime("%Y-%m-%d")

    os.makedirs(SIGNAL_DIR, exist_ok=True)
    at = get_access_token()

    # 1. 攞全部 pages（分頁）
    all_rows = []
    start_row = 0
    while True:
        r = gsc_query({
            "startDate": start_str, "endDate": end_str,
            "dimensions": ["page"], "rowLimit": 100, "startRow": start_row, "type": "web",
            "dimensionFilterGroups": [{"filters": [{"dimension": "page", "operator": "includingRegex",
                                                     "expression": BLOG_HOST.replace(".", "\\.")}]}],
        }, at)
        rows = r.get("rows", [])
        if not rows:
            break
        all_rows.extend(rows)
        start_row += len(rows)
        if len(rows) < 100:
            break
        if start_row > 3000:  # 安全上限
            break

    # 2. 攞 top queries
    q_rows = []
    try:
        rq = gsc_query({
            "startDate": start_str, "endDate": end_str,
            "dimensions": ["query"], "rowLimit": 20, "type": "web",
            "dimensionFilterGroups": [{"filters": [{"dimension": "page", "operator": "includingRegex",
                                                     "expression": BLOG_HOST.replace(".", "\\.")}]}],
        }, at)
        q_rows = rq.get("rows", [])
    except Exception:
        q_rows = []

    # 3. 分類整理
    with_clicks = [x for x in all_rows if x["clicks"] >= 1]
    with_clicks.sort(key=lambda x: -x["clicks"])
    zero_clicks = [x for x in all_rows if x["clicks"] == 0 and x["impressions"] >= args.min_impressions]
    zero_clicks.sort(key=lambda x: -x["impressions"])

    # 題材統計
    topic_stats = {}
    for row in all_rows:
        cat = classify_slug(row["keys"][0])
        s = topic_stats.setdefault(cat, {"clicks": 0, "impressions": 0, "pages": 0})
        s["clicks"] += row["clicks"]
        s["impressions"] += row["impressions"]
        s["pages"] += 1

    total_clicks = sum(x["clicks"] for x in all_rows)
    total_impressions = sum(x["impressions"] for x in all_rows)

    # 4. 組報告
    lines = []
    lines.append(f"# 📡 GSC 題材信號報告（{end_str}）")
    lines.append("")
    lines.append(f"> 查詢範圍：**{start_str} → {end_str}**（{args.days} 日）｜對象：**{BLOG_HOST}**（淨係現役科技 Blog）")
    lines.append(f"> 生成：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("## 📊 總覽")
    lines.append("")
    lines.append(f"- 總點擊（clicks）：**{total_clicks}**")
    lines.append(f"- 總曝光（impressions）：**{total_impressions}**")
    lines.append(f"- 有流量文章：**{len(with_clicks)} 篇**（clicks ≥ 1）")
    lines.append(f"- 有曝光冇點擊：**{len(zero_clicks)} 篇**（曝光 ≥ {args.min_impressions}）")
    lines.append("")
    lines.append("### 題材分佈")
    lines.append("")
    lines.append("| 題材 | 總點擊 | 總曝光 | 文章數 |")
    lines.append("|---|---|---|---|")
    for cat, s in sorted(topic_stats.items(), key=lambda x: -x[1]["clicks"]):
        lines.append(f"| {cat} | {s['clicks']} | {s['impressions']} | {s['pages']} |")
    lines.append("")

    lines.append("## 🏆 有流量文章（題材信號，由高到低）")
    lines.append("")
    if with_clicks:
        lines.append("| 點擊 | 曝光 | CTR | 排名 | 題材 | 文章 |")
        lines.append("|---|---|---|---|---|---|")
        for row in with_clicks[:args.top]:
            k = row["keys"][0]
            lines.append(f"| {row['clicks']} | {row['impressions']} | {row['ctr']*100:.1f}% | {row['position']:.1f} | {classify_slug(k)} | {short_name(k)} |")
    else:
        lines.append("（呢段期間冇任何點擊 — 全部題材零信號）")
    lines.append("")

    lines.append("## ⚠️ 有曝光但零點擊（反例 — 題材有人見到但唔吸引撳）")
    lines.append("")
    if zero_clicks:
        lines.append("| 曝光 | 排名 | 題材 | 文章 |")
        lines.append("|---|---|---|---|")
        for row in zero_clicks[:20]:
            k = row["keys"][0]
            lines.append(f"| {row['impressions']} | {row['position']:.1f} | {classify_slug(k)} | {short_name(k)} |")
    else:
        lines.append("（冇）")
    lines.append("")

    lines.append("## 🔍 用戶搜索關鍵字（queries）")
    lines.append("")
    if q_rows:
        lines.append("| 點擊 | 曝光 | CTR | 排名 | 關鍵字 |")
        lines.append("|---|---|---|---|---|")
        for row in q_rows:
            lines.append(f"| {row['clicks']} | {row['impressions']} | {row['ctr']*100:.1f}% | {row['position']:.1f} | {row['keys'][0]} |")
    else:
        lines.append("（冇數據）")
    lines.append("")

    lines.append("## 🎯 發文方向結論")
    lines.append("")
    # 簡單結論：邊個題材最強
    if topic_stats:
        best = max(topic_stats.items(), key=lambda x: x[1]["clicks"])
        lines.append(f"- 最強題材：**{best[0]}**（{best[1]['clicks']} clicks / {best[1]['impressions']} impressions）")
    if zero_clicks:
        worst = zero_clicks[0]["keys"][0]
        lines.append(f"- 避開/改用教學角度：**{short_name(worst)}**（曝光 {zero_clicks[0]['impressions']} 但 0 點擊）")
    lines.append("- 大廠 AI 動作 + 知名開源工具（有人會搜嘅名）＞ 冷門新 project")
    lines.append("- 有曝光冇點擊 = 標題/內容唔夠吸引 → 換角度寫或者唔寫")
    lines.append("")

    # 5. 寫檔
    report_date = end_str
    report_path = os.path.join(SIGNAL_DIR, f"{report_date}.md")
    latest_path = os.path.join(SIGNAL_DIR, "latest.md")
    content = "\n".join(lines)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(content)
    with open(latest_path, "w", encoding="utf-8") as f:
        f.write(content)

    # 6. 顯示精簡版（畀 cron / agent 睇）
    print(f"=== GSC 題材信號（{start_str} → {end_str}）===")
    print(f"總點擊 {total_clicks} / 總曝光 {total_impressions} / 有流量文章 {len(with_clicks)} 篇")
    if topic_stats:
        print("題材分佈：")
    for cat, s in sorted(topic_stats.items(), key=lambda x: -x[1]["clicks"]):
        print(f"  {cat}: {s['clicks']} clicks / {s['impressions']} impressions / {s['pages']} 篇")
    if with_clicks:
        print("\n有流量文章 top 10：")
        for row in with_clicks[:10]:
            print(f"  {row['clicks']} clicks: {short_name(row['keys'][0])}")
    if zero_clicks:
        print(f"\n反例（有曝光冇點擊，top 5）：")
        for row in zero_clicks[:5]:
            print(f"  {row['impressions']} impr: {short_name(row['keys'][0])}")
    print(f"\n完整報告：{report_path}")
    print(f"最新：{latest_path}")


if __name__ == "__main__":
    main()