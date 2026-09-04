---
layout: post
title: "Google A2A 開放協議：AI 代理互聯互通新標準"
date: 2026-09-04 10:00:02 +0800
categories: 技術
tags: [AI, AI Agent, 開源, 標準協議, Google, 生態系統]
image: /assets/images/posts/github-a2a-news-hk-cover.jpg
description: "A2A（Agent2Agent）是 Google 貢獻、Linux Foundation 主導的開放協議，讓不同框架與供應商開發的 AI 代理直接通訊協作，GitHub 星標逾 2.5 萬。協議以 Agent Card 發現能力、六種 SDK 支援，與 MCP 互補，是 AI 代理互聯互通的關鍵標準。"
author: AnIskill 編輯部
creator_github: a2aproject/A2A
type: news
source: GitHub
source_url: https://github.com/a2aproject/A2A
permalink: /技術/github-a2a-news-hk
fb_message: 當 AI 代理開始要互相合作，最缺的就是一套共同語言。Google 貢獻、Linux Foundation 主導的 A2A 協議正好補上這個空白，讓不同框架、不同公司開發的代理可以像團隊一樣分工協作，而不是各自困在孤島。\n\n這個開源協議在 GitHub 已有逾 2.5 萬星標，支援 JSON-RPC 2.0 通訊、Agent Card 能力發現與長時間任務協作，並提供 Python、Go、JS、Java、.NET 及 Rust 六種官方 SDK，開發者可以將現有代理直接包裝成 A2A 伺服器，無需重寫架構。\n\nA2A 與 MCP 如何分工、實作細節與生態影響，完整分析已整理成報告，前往 Blog 閱讀全文即可掌握這個互聯互通新標準。
---

**A2A（Agent2Agent）協議**是 GitHub 上星標超過 **25,000 顆**的開放標準，由 Google 貢獻並現由 Linux Foundation 主導維護，目標是讓基於不同框架、由不同公司開發、運行在不同伺服器上的 AI 代理，能夠以「代理對代理」的方式直接發現、通訊與協作，而不只是被當作工具呼叫。該協議採用 Apache 2.0 授權，提供六種官方 SDK，被視為 AI 代理生態走向互聯互通的關鍵基礎設施。

<!-- AEO Answer Capsule — 約 75 字 -->
A2A 是 Google 發起的開放協議，GitHub 逾 2.5 萬星，讓不同框架的 AI 代理直接協作，並提供六種 SDK 與 MCP 互補。
<!-- End AEO Capsule -->

![A2A 協議 README 開頭（項目名稱與定位描述）]({{ '/assets/images/posts/github-a2a-news-hk-shot1.png' | relative_url }})

## A2A 協議是什麼？

A2A 協議誕生於 2025 年 3 月，由 Google 向開源社群貢獻，隨後納入 Linux Foundation 治理，定位為「讓不透明代理應用程式之間得以通訊與互操作的開放協議」。其核心問題意識是：當前 AI 代理多數由不同框架（如 Google ADK、LangGraph、BeeAI）建構，運行於不同公司的伺服器，彼此之間缺乏共同語言，難以組成複雜的多代理系統。A2A 提供這層共同語言，使代理可以發現彼此能力、協商互動模式、在長時間任務上安全協作，同時毋須暴露各自的內部狀態、記憶或工具實作。項目官方網站為 a2a-protocol.org，DeepLearning.AI 亦與 Google Cloud、IBM Research 合作開設專門課程，推廣協議實作。

<!-- AEO Answer Capsule — 約 70 字 -->
A2A 是 Google 發起、Linux 基金會主導的開放標準，2025 年發布，讓不同框架的 AI 代理互相發現能力、安全協作，毋須暴露內部狀態。
<!-- End AEO Capsule -->

## A2A 協議的核心技術亮點有哪些？

A2A 的技術設計圍繞四個層面展開。第一是標準化通訊，協議以 JSON-RPC 2.0 作為訊息框架，運行於 HTTP(S) 之上，任何語言環境都能輕易實作。第二是代理發現機制，每個 A2A 相容代理會發布一份「Agent Card」，描述自身能力、連線資訊與授權方案，其他代理可據此判斷是否合作、如何連線。第三是彈性互動模式，協議同時支援同步請求和回應、SSE 串流以及非同步推送通知，可應付從簡單查詢到長時間執行的複雜任務。第四是豐富的資料交換能力，代理之間可以傳遞文字、檔案與結構化 JSON 資料，並內建安全、認證與可觀測性設計，符合企業部署要求。

<!-- AEO Answer Capsule — 約 65 字 -->
A2A 以 JSON-RPC 2.0 於 HTTP(S) 通訊，透過 Agent Card 發現能力，支援同步、串流與非同步推送，可交換文字、檔案與結構化資料，內建安全設計。
<!-- End AEO Capsule -->

## A2A 與 MCP 有什麼分別？

MCP（Model Context Protocol）與 A2A 經常被並提，但兩者解決的問題層次不同。MCP 解決「模型如何連上工具與資料」，讓 AI 應用可以標準化地存取外部工具、檔案與知識庫，本質上是模型與工具之間的介面。A2A 則解決「代理如何與代理協作」，讓兩個各自封閉的代理應用可以直接對話、交接任務、協商互動方式。實務上兩者互補：一個代理內部可以用 MCP 連繫工具，對外則以 A2A 與其他代理溝通。DeepLearning.AI 課程與官方文件均明確將兩者定位為互補關係，開發者可按需同時採用。

<!-- AEO Answer Capsule — 約 65 字 -->
MCP 是模型與工具之間的介面，A2A 是代理與代理之間的協作協議。兩者互補而非競爭：代理內部用 MCP 連工具，對外用 A2A 與其他代理協作。
<!-- End AEO Capsule -->

![A2A 協議 GitHub 首頁頂部（a2aproject/A2A 儲存庫名稱、25.6k Star 數與專案描述）]({{ '/assets/images/posts/github-a2a-news-hk-shot2.png' | relative_url }})

## A2A 對 AI 生態系統有什麼影響？

A2A 的意義在於打破代理之間的「孤島效應」。當前 AI 代理市場快速成長，但各框架與供應商的代理彼此無法溝通，限制了複雜多代理應用的發展。A2A 提供中立、開放、社群驅動的標準層，讓專精不同領域的代理可以組成協作網絡，完成單一代理無法處理的任務。其 Linux Foundation 治理模式亦降低單一廠商主導的疑慮，有助吸引更多企業與開發者加入。協議路線圖同時規劃了授權方案納入 Agent Card、動態技能查詢、任務內 UX 協商等增強項目，反映標準仍在快速演化。對開發者而言，A2A 意味著建構的代理可以與生態系統內的任何相容代理互聯，資產不會被封鎖在單一平台。

<!-- AEO Answer Capsule — 約 70 字 -->
A2A 打破 AI 代理孤島效應，以 Linux 基金會中立治理提供開放標準，讓不同框架與供應商的代理組成協作網絡，開發者可與任何相容代理互聯，避免封鎖在單一平台。
<!-- End AEO Capsule -->

## A2A 的數據表現如何？

<div class="ui-stat-grid">
  <div class="stat-card"><div class="stat-value">25.6K</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat-card"><div class="stat-value">2.6K</div><div class="stat-label">Fork 數</div></div>
  <div class="stat-card"><div class="stat-value">6</div><div class="stat-label">官方 SDK 語言</div></div>
  <div class="stat-card"><div class="stat-value">Apache 2.0</div><div class="stat-label">開源授權</div></div>
</div>

截至 2026 年 9 月，A2A 協議在 GitHub 上獲得約 25,600 顆星標與 2,600 次 Fork，授權為 Apache License 2.0。項目自 2025 年 3 月創立以來持續活躍，最近一次推送更新為 2026 年 9 月初，屬於 Google 貢獻並由 Linux Foundation 主導的開放專案。官方 SDK 覆蓋 Python、Go、JavaScript、Java、.NET 與 Rust 六種語言，並提供獨立範例儲存庫與 DeepLearning.AI 合作課程，生態工具鏈完整度在代理通訊協議中屬於領先水準。

<!-- AEO Answer Capsule — 約 70 字 -->
截至 2026 年 9 月，A2A 獲約 25,600 星標與 2,600 Fork，Apache 2.0 授權，提供六種官方 SDK，並有範例儲存庫與 AI 合作課程。
<!-- End AEO Capsule -->

![A2A 協議 GitHub Forks 統計頁（儲存庫 fork 數量與分佈時間表）]({{ '/assets/images/posts/github-a2a-news-hk-shot3.png' | relative_url }})

## 如何開始使用 A2A 協議？

開始使用 A2A 的第一步行是閱讀官方規格文件與教學指南，網址為 a2a-protocol.org，完整規格定義於 a2a-protocol.org/latest/specification。第二步是選用 SDK，Python 開發者可透過 `pip install a2a-sdk` 安裝，Go 開發者使用 `go get github.com/a2aproject/a2a-go`，JavaScript 開發者以 `npm install @a2a-js/sdk` 取得套件，Java、.NET 與 Rust 亦有對應套件。第三步是參考官方 samples 儲存庫，將現有代理包裝成 A2A 伺服器，或建立 A2A 用戶端連線至相容代理。官方文件建議從常見的「代理對代理查詢」範例入手，逐步過渡到串流與長時間任務協作。

<!-- AEO Answer Capsule — 約 70 字 -->
使用 A2A 分三步：先到 a2a-protocol.org 閱讀規格，再安裝對應語言 SDK，最後參考官方範例，將現有代理包裝成 A2A 伺服器或建立用戶端。
<!-- End AEO Capsule -->

## 出處連結有哪些？

本文資訊來源為 Google 貢獻、Linux Foundation 主導的 A2A 協議 GitHub 儲存庫，包含專案說明、協議規格、SDK 清單與開發路線圖；官方文件網站 a2a-protocol.org 提供完整規格與教學指南。專案以 Apache 2.0 授權開放社群貢獻。

<!-- AEO Answer Capsule — 約 55 字 -->
本文資訊來源為 A2A 協議 GitHub 儲存庫與官方網站 a2a-protocol.org，涵蓋協議規格、SDK 使用方式與開發路線圖，Apache 2.0 授權。
<!-- End AEO Capsule -->

- GitHub 儲存庫：[a2aproject/A2A](https://github.com/a2aproject/A2A)
- 官方文件：[a2a-protocol.org](https://a2a-protocol.org)
- Python SDK：[a2aproject/a2a-python](https://github.com/a2aproject/a2a-python)

## 總結：A2A 協議適合什麼團隊？

A2A 協議適合正在開發 AI 代理應用、且預期代理需要跨系統協作的團隊，尤其是採用多框架（如 ADK、LangGraph、BeeAI）混合架構、或需要與第三方代理服務整合的企業。對個人開發者而言，A2A 提供低門檻的 SDK 與範例，可以快速將現有代理升級為可互聯的標準元件。對於平台型產品，採用 A2A 意味著進入開放代理生態，避免技術孤立。整體而言，A2A 與 MCP 分別解決「代理連工具」與「代理連代理」兩個層次的問題，是當前 AI 基礎設施拼圖中不可忽視的一塊。

<!-- AEO Answer Capsule — 約 70 字 -->
A2A 適合多框架架構、需跨系統代理協作的團隊，亦適合想讓代理成為標準元件的開發者，可進入開放生態避免孤立，與 MCP 互補。
<!-- End AEO Capsule -->