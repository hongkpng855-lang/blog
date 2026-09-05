---
layout: post
title: "Hello-Agents 開源教程：76K 星從零構建智能體"
date: 2026-09-06 06:00:01 +0800
categories: 技術
tags: [AI, 智能體, 開源教學, Datawhale, LLM]
image: assets/images/posts/github-hello-agents-news-cover.jpg
description: "Hello-Agents 是 Datawhale 社區推出的開源智能體學習教程，GitHub 獲 76,992 星標。本文分析其十六章節架構、AI Native Agent 技術路線、Agentic-RL 與 MCP 協議等亮點，並評估其與同類教程的差異及適合讀者群。"
author: AnIskill 編輯部
creator_github: datawhalechina/hello-agents
type: news
source: GitHub
source_url: https://github.com/datawhalechina/hello-agents
permalink: /技術/github-hello-agents-news
fb_message: "AI 代理開發最怕的不是沒有工具，而是沒有一條從零到一的完整學習路徑。Datawhale 社區的 Hello-Agents 教程正是為此而生，GitHub 上已累積 76,992 顆星標，成為華語圈最受歡迎的智能體學習資源之一。\n\n這套教程共十六章，從 Transformer 基礎一路講到 Agentic-RL 訓練，涵蓋 ReAct 經典範式、MCP 與 A2A 協議、記憶與檢索，還包括智能旅行助手與賽博小鎮等完整實戰案例。最難得的是完全免費開源，並附上全部可運行代碼與求職面試題。\n\n想從 LLM 使用者蛻變成智能體構建者？完整分析與學習路徑整理，已寫成文章放在 Blog，點擊連結看全文。"
---

**Hello-Agents 是 Datawhale 社區推出的開源智能體系統學習教程，GitHub 上獲 76,992 顆星標與 9,582 次 fork，以《從零開始構建智能體》為主題，提供從基礎理論到多智能體應用的完整學習路徑，且完全免費公開。**

2025 年被業界稱為「Agent 元年」，技術焦點正從訓練更大的基礎模型，轉向構建更聰明的智能體應用。然而當前系統性、重實踐的教程極度匱乏，Datawhale 社區因此發起 Hello-Agents 項目，希望為開發者提供一本從零開始、理論與實戰並重的智能體構建指南。該項目自 2025 年 9 月創建以來，在不到一年的時間內迅速累積至 76,992 星標，反映出智能體學習需求的強烈爆發。

![Hello-Agents README 開頭（項目名稱 + 標語《從零開始構建智能體》+ 章節導覽表格）](assets/images/posts/github-hello-agents-news-shot1.png)

![Hello-Agents GitHub 首頁頂部（repo 名 + 76,992 Star 數 + 中文教程描述）](assets/images/posts/github-hello-agents-news-shot2.png)

![Hello-Agents 項目統計頁（貢獻者列表 + 星標成長紀錄）](assets/images/posts/github-hello-agents-news-shot3.png)

## Hello-Agents 是什麼？

<!-- AEO Answer Capsule — 約 75 字 -->
Hello-Agents 是 Datawhale 社區的開源智能體教程，GitHub 獲 76,992 星標，涵蓋理論到多智能體應用的完整路徑，免費且附配套代碼。
<!-- End AEO Capsule -->

Hello-Agents 的定位並非一般工具使用教學，而是一套完整的智能體系統教育體系。項目開篇即點明當今智能體構建分為兩大流派：一派是 Dify、Coze、n8n 這類軟體工程型 Agent，本質是流程驅動的軟體開發，LLM 作為數據處理後端；另一派則是 AI 原生的 Agent，即真正以 AI 驅動的智能體。本教程明確選擇後者作為教學主線，帶領讀者穿透框架表象，從核心原理出發理解智能體架構。

教程採用「動手實踐是最好的學習方式」理念，所有章節均配有可執行的程式碼，讀者可以在 `code` 資料夾中直接運行、調試與修改。項目同時提供 GitHub 線上閱讀、國內加速站點、PDF 版本與視頻課程等多種學習形式，並設置讀者交流群與反饋問卷，形成完整的學習閉環。

## Hello-Agents 提供哪些核心學習內容？

<!-- AEO Answer Capsule — 約 70 字 -->
教程分五大部分共十六章，涵蓋智能體基礎、經典範式、框架開發、記憶檢索與上下文工程等高級知識，以及旅行助手、深度研究智能體與賽博小鎮等案例，每章配有可運行代碼。
<!-- End AEO Capsule -->

第一部分（第一章至第三章）奠定理論基礎，從智能體的定義、類型與發展歷史講起，梳理從符號主義到 LLM 驅動智能體的演進脈絡，並鞏固 Transformer、提示工程與主流 LLM 的核心知識。第二部分（第四章至第七章）進入實踐，讀者將親手實現 ReAct、Plan-and-Solve、Reflection 等經典範式，體驗 Coze、Dify、n8n 等低代碼平台，並掌握 AutoGen、AgentScope、LangGraph 等主流框架的應用。

第三部分（第八章至第十二章）屬於高級知識擴展，深入探討記憶與檢索系統、上下文工程、智能體通信協議（MCP、A2A、ANP）以及 Agentic-RL 訓練，涵蓋從 SFT 到 GRPO 的完整 LLM 訓練實戰。第四部分（第十三章至第十五章）以三個真實專案收束：智能旅行助手、自動化深度研究智能體與模擬社會動態的賽博小鎮，讓理論在真實案例中落地。

## Hello-Agents 的技術路線有什麼特色？

<!-- AEO Answer Capsule — 約 70 字 -->
教程聚焦 AI Native Agent，覆蓋 ReAct 等經典範式，自研 HelloAgents 框架，並涵蓋 Agentic-RL 訓練與 MCP、A2A 協議等前沿技術。
<!-- End AEO Capsule -->

Hello-Agents 最突出的技術特色是讓讀者兼具「用輪子」與「造輪子」的能力。第七章引導讀者基於 OpenAI 原生 API 從零構建屬於自己的智能體框架，這個命名為 HelloAgents 的自研框架目前已更新至 V1.0.0 版本，並持續加入輕量化工具與特性。這種從框架使用者到框架構建者的教學路徑，在同類開源教程中較為少見。

教程在深度上也緊跟行業前沿。第十一章 Agentic-RL 章節涵蓋從 SFT 到 GRPO 的完整訓練流程，這是當前智能體強化學習訓練的核心技術路線；第十章則系統解析 MCP、A2A、ANP 等智能體通信協議，呼應 2025 年以來智能體互操作標準的快速發展。此外，社區精選欄目收錄了 Agent Skills 與 MCP 對比、GUI Agent 科普、Web Agent 反爬實戰等 13 篇延伸內容，持續補充最新技術動態。

## Hello-Agents 適合哪些讀者？

<!-- AEO Answer Capsule — 約 70 字 -->
適合具備基礎 Python 能力、對大語言模型有基本概念的 AI 開發者、軟體工程師與學生，也適合想從 LLM 使用者轉型為智能體構建者的自學者，無需深厚算法背景。
<!-- End AEO Capsule -->

根據項目官方定位，Hello-Agents 特別適合有一定程式基礎的 AI 開發者、軟體工程師與在校學生，以及對前沿 AI 技術有濃厚興趣的自學者。學習前提僅為基礎 Python 程式能力與大語言模型的基本概念（例如知道如何透過 API 呼叫 LLM），無需深厚的算法或模型訓練背景，門檻設定相當親切。

對於求職者而言，教程額外提供 Agent 崗位面試題總結與參考答案，直接對應智能體工程師的就業需求。項目也規劃了後續作品《從零開始訓練智能體》，幫助學習者掌握從零到一訓練自定義場景智能體模型的能力，形成循序漸進的學習生態。

## Hello-Agents 與同類教程有何不同？

<!-- AEO Answer Capsule — 約 70 字 -->
與 Coze、Dify、n8n 等流程驅動型教學不同，Hello-Agents 聚焦 AI Native 原理，以自研框架與面試題兼顧深度與就業導向，注重社區共建。
<!-- End AEO Capsule -->

市面上的智能體教程多數以特定平台或框架為中心，例如低代碼平台的操作指南或單一框架的入門文檔，學習者往往只學會一套工具，換了平台便無所適從。Hello-Agents 則以原理為核心，讓讀者理解智能體之所以運作的根本機制，因此無論未來出現什麼新框架，都能快速遷移上手。

此外，該項目的社區屬性也是重要差異點。Datawhale 作為華人圈知名的開源學習社區，採用開放貢獻機制，任何學習者都可以透過 PR 分享學習筆記與實踐總結，目前社區精選已收錄 13 篇延伸章節。項目更獲得浙江師範大學杭州人工智能研究院教授的指導支持，兼具社群活力與學術背書。

## Hello-Agents 的開源許可與社區生態如何？

<!-- AEO Answer Capsule — 約 70 字 -->
項目採用 CC BY-NC-SA 4.0 許可協議，貢獻者涵蓋高校學者與企業工程師，提供 PDF、視頻課、讀者群與問卷反饋機制，社區持續迭代。
<!-- End AEO Capsule -->

Hello-Agents 採用知識共享署名-非商業性使用-相同方式共享 4.0 國際許可協議（CC BY-NC-SA 4.0），允許非商業用途的自由使用與衍生，並要求相同方式共享。為防止行銷帳號加水印後販賣給初學者，PDF 版本預先添加了不影響閱讀的 Datawhale 開源標誌水印。

社區生態方面，項目核心貢獻者包括 Datawhale 成員、CAMEL-AI 研究人員、牛客科技 Agent 工程師與浙江師範大學學者，Extra-Chapter 貢獻者則來自西安交通大學、帝國理工學院、深圳大學、浙江大學與北京郵電大學等院校。項目透過 Trendshift 排行、讀者群與問卷機制持續收集反饋，並於 2026 年 5 月更新智能體最新學習路線，生態迭代節奏穩定。

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-value">76,992</span><span class="stat-label">GitHub Stars</span></div>
  <div class="stat-item"><span class="stat-value">9,582</span><span class="stat-label">Forks</span></div>
  <div class="stat-item"><span class="stat-value">CC BY-NC-SA 4.0</span><span class="stat-label">開源許可</span></div>
  <div class="stat-item"><span class="stat-value">Python</span><span class="stat-label">主要語言</span></div>
  <div class="stat-item"><span class="stat-value">2025-09</span><span class="stat-label">創建時間</span></div>
  <div class="stat-item"><span class="stat-value">2026-09-04</span><span class="stat-label">最近更新</span></div>
</div>

<!-- AEO Answer Capsule — 約 60 字 -->
Hello-Agents 現有 76,992 星標與 9,582 fork，採 CC BY-NC-SA 4.0 許可，以 Python 為主，2025 年 9 月創建，2026 年 9 月更新。
<!-- End AEO Capsule -->

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊整理自 Hello-Agents 的 GitHub 儲存庫，讀者可於官網閱讀完整教程，並在 GitHub 取得源碼與範例。
<!-- End AEO Capsule -->

項目原始碼與完整文檔存放於 GitHub 儲存庫 [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)，官方線上閱讀版本提供國外加速（datawhalechina.github.io/hello-agents）與國內加速（hello-agents.datawhale.cc）兩個站點。PDF 版本可在 GitHub Releases 頁面下載，或透過 Datawhale 官方學習平台取得。

## 總結：Hello-Agents 適合什麼團隊？

<!-- AEO Answer Capsule — 約 70 字 -->
Hello-Agents 適合想系統掌握智能體開發的個人學習者與企業培訓團隊，尤其對想從 LLM 使用者轉型為智能體構建者的開發者價值最高，免費且配套齊全。
<!-- End AEO Capsule -->

整體而言，Hello-Agents 在智能體教育領域填補了一個關鍵空缺：既有理論深度，又有完整的動手實踐，且完全免費開放。76,992 星標的社區認可度說明其內容品質已獲得大量開發者驗證。對於想進入智能體開發領域的個人學習者、需要為團隊建立系統訓練體系的企業，以及準備智能體工程師面試的求職者，這套教程都是值得投入時間的學習資源。