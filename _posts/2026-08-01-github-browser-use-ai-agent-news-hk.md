---
layout: post
title: "🔥 10.7 萬人 Star 嘅開源神器：browser-use 教 AI 自己上網做嘢"
date: 2026-08-01 18:05:00 +0800
categories: 技術
tags: [GitHub, 開源, AI Agent, browser-use, 自動化, Python, 科技新聞, 香港, auto-publish, github-news]
image: /assets/images/posts/github-browser-use-shot1.png
description: "GitHub 又出爆紅 project！browser-use 短短時間已經 10.7 萬星——佢令 AI Agent 可以好似人咁用瀏覽器：開網頁、撳掣、打字、填表、抽資料，全部自動化。呢篇新聞式介紹睇下佢點解咁受歡迎、點樣上手。"
author: "陳志豪 Eric Chan"
---

# 🔥 10.7 萬人 Star 嘅開源神器：browser-use 教 AI 自己上網做嘢

> **GitHub 今日最紅嘅開源 project，唔係框架、唔係模型 — 係一個教 AI「自己上網」嘅工具。**

**107,458 個 star**、每日更新、MIT 開源免費 — 呢個叫 **browser-use** 嘅 Python 套件，令 AI Agent 可以好似人咁操作瀏覽器：開頁、撳掣、打字、填 form、抽數據，你淨係用文字描述個任務，佢就幫你做完。

我睇完佢成個 README，話你知呢個 project 有咩咁把炮。

---

## <svg class="ui-icon"><use href="#ui-chart"/></svg>新聞重點速覽

<div class="ui-stat-grid">
  <div class="ui-stat"><span class="ui-stat-num">107,460</span><span class="ui-stat-label">⭐ Stars</span></div>
  <div class="ui-stat"><span class="ui-stat-num">11.8K</span><span class="ui-stat-label">Forks</span></div>
  <div class="ui-stat"><span class="ui-stat-num">134</span><span class="ui-stat-label">Releases</span></div>
  <div class="ui-stat"><span class="ui-stat-num">318</span><span class="ui-stat-label">Contributors</span></div>
  <div class="ui-stat"><span class="ui-stat-num">Python</span><span class="ui-stat-label">語言</span></div>
  <div class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">License</span></div>
</div>

> 更新頻率：日日更新（今日都有 commit）

![browser-use GitHub 主頁（107k stars）]({{ '/assets/images/posts/github-browser-use-shot1.png' | relative_url }})

---

## <svg class="ui-icon"><use href="#ui-robot"/></svg>呢個 project 係咩？

一句講晒：**Browser Use 令 AI Agent 可以用網頁瀏覽器，同你一樣咁操作。**

以往 AI Agent 做嘢多數局限喺 API 同文字，但現實世界好多嘢係喺網頁上面：填 job application、登入後台、抽社交媒體數據、訂機票… API 唔一定俾你，但**瀏覽器一定得**。

Browser Use 就係嗰條橋：你話俾佢知想做咩，佢自己開瀏覽器、搵元素、撳掣、填資料、攞結果。

**官方示範任務：**
- **填表**：「幫我填呢份求職申請，用我嘅履歷資料。」
- **抽數據**：「抽我 followers 嘅結構化數據，輸出做 CSV。」

![browser-use README 內容（功能示範）]({{ '/assets/images/posts/github-browser-use-shot3.png' | relative_url }})

---

## <svg class="ui-icon"><use href="#ui-rocket"/></svg>點解咁多人 Star？

1. **真係解決到問題** — AI Agent 最缺就係「同現實世界互動」嘅能力，browser 就係個入口
2. **易上手** — Python 幾行 code 就跑到，唔使複雜設定
3. **生態做得好** — 官方 Cloud 服務、文件齊、Discord 社群活躍、仲有 MCP 支援（可以直接俾 Claude 用）
4. **開放** — MIT License，免費商用，仲有 134 個 releases 日日修 bug

![browser-use 專案統計（Releases/Contributors/Languages）]({{ '/assets/images/posts/github-browser-use-shot2.png' | relative_url }})

---

## <svg class="ui-icon"><use href="#ui-download"/></svg>點樣開始用

```bash
pip install browser-use
```

基本用法（官方例子）：

```python
from browser_use import Agent
from langchain_openai import ChatOpenAI

agent = Agent(
    task="Search for a flight from Hong Kong to Tokyo and return the best price",
    llm=ChatOpenAI(model="gpt-4o"),
)

await agent.run()
```

就係咁簡單 — 一個 task 一句話，AI 自己上網搞掂。進階可以配 Playwright 自訂、加自己嘅 browser profile、接 MCP 俾 Claude 用。

---

## <svg class="ui-icon"><use href="#ui-link"/></svg>出處

<div class="ui-note"><svg class="ui-icon"><use href="#ui-link"/></svg><strong>GitHub 官方 repo</strong>：https://github.com/browser-use/browser-use

官方文件：https://docs.browser-use.com ｜ Cloud 服務：https://cloud.browser-use.com</div>

---

## <svg class="ui-icon"><use href="#ui-bulb"/></svg>我嘅睇法

<div class="ui-tip"><svg class="ui-icon"><use href="#ui-bulb"/></svg><strong>「AI 自己上網」呢個方向，係 2026 年 AI Agent 落地最重要嘅一步。</strong>唔好睇少呢類工具 — 當 AI 可以操作瀏覽器，佢就由「識傾偈」進化到「識做嘢」：幫你填表、訂嘢、睇資料、monitor 網站。107k 星只係開始。</div>

> **「試過先講」** — 呢個我睇完 README 即刻想試，你都可以 😄
