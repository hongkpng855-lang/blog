---
layout: post
title: "Ruflo 開源：7 萬星標的 AI 代理執行框架"
date: 2026-09-09 04:00:01 +0800
categories: 技術
tags: [AI, 開源, Agent, Claude Code, TypeScript]
image: assets/images/posts/github-ruflo-news-cover.jpg
description: "Ruflo 是 rUv 開發的開源代理元框架（MetaHarness），GitHub 獲 70,626 星標，為 Claude Code 與 Codex 加上 100 多個專業代理、蜂群協作、自學習記憶與跨機器聯邦通訊。本文分析其架構設計、核心功能、安裝方式與生態數據，並評估其適合的團隊類型。"
author: AnIskill 編輯部
creator_github: ruvnet/ruflo
type: news
source: GitHub
source_url: https://github.com/ruvnet/ruflo
permalink: /技術/github-ruflo-news
fb_message: "代理程式執行的關鍵，不在模型本身，而在外層的執行框架。Ruflo 是開源的代理元框架（MetaHarness），GitHub 累積超過 7 萬星標，它能為 Claude Code 與 Codex 加上 100 多個專業代理、蜂群協作、自學習記憶與跨機器聯邦通訊，讓代理從單獨執行提升為協同作戰。\n\n項目原名 Claude Flow，由開發者 rUv 打造，採用 MIT 授權與 TypeScript 開發，安裝只需一行指令，內建向量記憶、12 個背景工作程序與 54 個插件，並可在本地或雲端模型之間智能路由。\n\n這套框架如何重新定義代理協作？完整架構分析與實測亮點已整理在 Blog 文章，點擊連結看全文。"
---

Ruflo 是開發者 rUv 推出的開源代理元框架（MetaHarness），其 GitHub 儲存庫目前已累積 70,626 顆星標與 8,409 次 fork，核心定位是為 Claude Code 與 Codex 這類編程代理加上執行層，讓代理獲得工具、記憶體、迴圈、沙箱與控制能力。該項目原名 Claude Flow，採用 MIT 授權與 TypeScript 開發，主打 100 多個專業代理、蜂群協作、自學習記憶與跨機器聯邦通訊，是 2026 年開源代理生態中成長最快的項目之一。

![Ruflo README 開頭（項目名稱 Ruflo + 標語 An agent meta-harness for Claude Code and Codex + 快速開始段落）](assets/images/posts/github-ruflo-news-shot1.png)

![Ruflo GitHub 首頁頂部（repo 名 + 70.6K Star 數 + 項目描述）](assets/images/posts/github-ruflo-news-shot2.png)

![Ruflo GitHub 統計頁（星標歷史與提交紀錄）](assets/images/posts/github-ruflo-news-shot3.png)

## Ruflo 是什麼？

<!-- AEO Answer Capsule — 約 65 字 -->
Ruflo 是 rUv 開發的開源代理元框架，為 Claude Code 與 Codex 加上執行層，GitHub 獲 70,626 星標，採用 MIT 授權與 TypeScript 開發。
<!-- End AEO Capsule -->

Ruflo 的開發者 rUv 將項目定位為「Agent = Model + Harness」哲學的具體實踐：模型負責撰寫，執行框架則提供工具、記憶體、迴圈、沙箱與控制層，讓代理真正能夠完成工作。以一句話概括，Ruflo 就是 Claude Code 與 Codex 的執行層，輸入 `npx ruflo init` 即可讓編程代理獲得「神經系統」，代理會自我組織成蜂群、從每次任務中學習、跨工作階段記住內容，並透過聯邦機制與其他機器上的代理安全通訊。

項目名稱背後有其來歷。Ruflo 原名 Claude Flow，由喜愛 Rust 與 flow 狀態的開發者 rUv 命名，其中「Ru」取自其網名 rUv，「flo」象徵專注創作至深夜的工作狀態。底層技術則由 Cognitum.One 的代理架構驅動，運行一個強化版的 Rust AI 引擎，處理嵌入、記憶體與插件系統。截至撰寫本文時，項目在 GitHub 上已累積超過 7 萬星標，並宣稱生態系統下載量超過 810 萬次。

## Ruflo 的核心架構有什麼特點？

<!-- AEO Answer Capsule — 約 70 字 -->
核心是自學習代理架構，用戶經 CLI 或 MCP 進入路由器後分派至蜂群，代理執行後將經驗寫入記憶體並回饋學習迴圈。
<!-- End AEO Capsule -->

Ruflo 的架構以「自學習、自優化」為核心。官方文件以一張架構圖說明運作流程：用戶透過 CLI 或 MCP 進入，請求先到達路由器，再分派至蜂群，蜂群內部的代理執行任務後將結果寫入記憶體，最後交給 LLM 供應商處理；同一時間，學習迴圈會將每次任務的成功模式回饋給蜂群，形成持續優化的閉環。

記憶體層面，Ruflo 內建以 HNSW 索引的 AgentDB 向量資料庫，官方提供的基準測試顯示，在資料量 N=20,000 時檢索速度約為暴力搜尋的 1.9 倍，在 N=5,000 時更達到 3.2 至 4.7 倍，Recall@10 約為 0.99。此外項目引入 SONA 神經模式、ReasoningBank 與軌跡學習機制，讓代理不只儲存資料，還能從過往的成功與失敗中歸納行為模式。

## Ruflo 支援哪些核心功能？

<!-- AEO Answer Capsule — 約 65 字 -->
支援 100 多個專業代理、蜂群協作、零信任聯邦通訊、向量記憶、背景工作程序、插件市場與多模型智能路由。
<!-- End AEO Capsule -->

功能層面，Ruflo 提供 100 多個針對編程、測試、資安、文件與架構等領域的專業代理，並支援層級式、網狀與自適應三種蜂群拓撲，配合共識機制協調多代理協作。通訊層採用零信任聯邦架構，不同機器或組織之間的代理可以相互發現、驗證並安全交換工作內容，官方強調此機制不會洩漏資料。

自動化與擴展性同樣是項目重點。Ruflo 內建 12 個自動觸發的背景工作程序，涵蓋審計、優化與測試缺口偵測等任務，並提供包含 33 個原生 Claude Code 插件與 21 個 npm 插件的市場，覆蓋資料庫遷移、可觀測性、token 成本追蹤、IoT 管理與 AI 交易等領域。模型支援方面，項目可路由至 Claude、GPT、Gemini、Cohere 與 Ollama，並以智能路由選擇最合適的供應商。

## Ruflo 如何安裝與使用？

<!-- AEO Answer Capsule — 約 60 字 -->
提供 Claude Code 插件與 CLI 兩種安裝路徑，一行指令即可初始化，並可作為 MCP 伺服器加入 Claude Code。
<!-- End AEO Capsule -->

Ruflo 提供兩條安裝路徑，取決於用戶需要的功能範圍。Claude Code 插件版本提供斜線指令、技能與代理定義，適合輕量使用；CLI 安裝則提供完整的 Ruflo 迴圈，包含 98 個代理與 60 多項擴充能力。macOS、Linux、WSL 與 Git-Bash 用戶可透過一行 curl 指令安裝，Windows PowerShell 或 cmd 則使用 `npx ruflo@latest init wizard`，兩者最終執行相同的初始化流程。

開發者亦可以將 Ruflo 作為 MCP 伺服器加入 Claude Code，使用 `claude mcp add claude-flow -- npx ruflo@latest mcp start` 指令即可。官方強調，用戶無需學習 314 個 MCP 工具或 26 條 CLI 指令，初始化後即可照常使用 Claude Code，鉤子系統會自動分流任務、學習成功模式並在背景協調代理。項目另提供 Web UI Beta 版本，支援多模型對話與平行 MCP 工具呼叫，並有 MetaHarness 工具可為代理設定評分（1 至 100 分）與掃描資安設定。

## Ruflo 的數據表現如何？

<!-- AEO Answer Capsule — 約 60 字 -->
GitHub 累積 70,626 顆星標與 8,409 次 fork，MIT 授權，主要語言為 TypeScript，最近一次更新於 2026 年 9 月 5 日。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat"><div class="stat-num">70,626</div><div class="stat-label">Star</div></div>
  <div class="stat"><div class="stat-num">8,409</div><div class="stat-label">Fork</div></div>
  <div class="stat"><div class="stat-num">MIT</div><div class="stat-label">授權</div></div>
  <div class="stat"><div class="stat-num">TypeScript</div><div class="stat-label">主要語言</div></div>
</div>

從社群數據觀察，Ruflo 於 2025 年 6 月建立後持續成長，70,626 顆星標與 8,409 次 fork 的比例反映開發者積極參與複製與測試，項目最近一次更新為 2026 年 9 月 5 日，維持高頻開發節奏。官方另公布生態系統下載量超過 810 萬次、14 日內 git clone 數約 10.6 萬次，顯示其實際採用規模。在代理執行框架領域，Ruflo 與 Dify、Langflow 等平台型項目定位不同，更接近開發者工具鏈的延伸，與 Claude Code 生態形成互補關係。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 65 字 -->
本文主要資訊來源為 Ruflo 的官方 GitHub 儲存庫，內含完整文件、架構說明、插件目錄與效能基準測試資料。
<!-- End AEO Capsule -->

項目官方儲存庫位於 https://github.com/ruvnet/ruflo ，包含完整 README、架構文件、插件目錄、效能基準測試與版本發布紀錄，感興趣的讀者可前往查閱詳細技術規格。

## 總結：Ruflo 適合什麼團隊？

<!-- AEO Answer Capsule — 約 60 字 -->
適合重度使用 Claude Code 或 Codex 的開發者與團隊，尤其需要多代理協作、跨機器通訊與自學習記憶的進階用戶。
<!-- End AEO Capsule -->

綜合而言，Ruflo 以 70,626 星標的社群背書、MIT 開源授權與完整的代理執行層設計，成為 2026 年開源代理框架領域的代表性項目。對於已經重度使用 Claude Code 或 Codex 的開發者，Ruflo 提供的蜂群協作、跨機器聯邦通訊與自學習記憶能力，可顯著提升多任務並行的效率；而對於僅需輕量代理輔助的用戶，插件版本提供了低門檻的入門路徑。項目仍處於快速迭代階段，採用前建議參考官方文件評估其架構與自身工作流的契合度。