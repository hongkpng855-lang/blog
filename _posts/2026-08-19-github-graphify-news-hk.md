---
layout: post
title: "107,899 星開源項目：Graphify — 把程式碼庫變成可查詢知識圖譜"
date: 2026-08-19 06:00:00 +0800
categories: 技術
tags: [Graphify, Graphify-Labs, 知識圖譜, 開源軟體, AI 程式碼分析, 人工智慧, tree-sitter, Agent, AST, 開發工具]
image: /assets/images/posts/github-graphify-news-hk-cover.jpg
description: "Graphify 是 GitHub 星標超過 10.7 萬的開源項目，將程式碼、文件、PDF、圖片與影片映射成可查詢知識圖譜。程式碼以本地 tree-sitter AST 分析，不離開裝置、不需向量資料庫，支援 20 多個 AI 助手，在 LOCOMO 基準召回率達 0.497，遠超同類記憶系統。"
author: AnIskill 編輯部
creator_github: Graphify-Labs/graphify
type: news
source: GitHub
source_url: https://github.com/Graphify-Labs/graphify
permalink: /技術/github-graphify-news-hk
fb_message: 開源界又一個神級工具！Graphify 用 10.7 萬顆星證明：理解大型程式碼庫，不一定再靠一行一行慢慢讀。\n\n它是 Claude Code、Cursor、Codex、Gemini CLI 等 20 多個 AI 助手的專屬技能，輸入 /graphify 就會把整份專案（程式碼、文件、PDF、圖片、影片）映射成知識圖譜，之後用問題直接查詢，而唔係 grep 翻文件。最正係程式碼全程本地解析，唔上傳、唔使向量資料庫，仲有實測數據：LOCOMO 召回率 0.497，遠超 mem0 嘅 0.048。\n\n呢個工具對成日要接手陌生大型專案嘅開發者嚟講，真係一用返唔到轉頭。詳細新聞分析同快速上手步驟都整理好，去 Blog 睇全文啦。
---

**Graphify** 是 GitHub 星標高達 **107,899 顆**的開源項目，由 Y Combinator S26 團隊 Graphify-Labs 開發。它作為 Claude Code、Cursor、Codex、Gemini CLI 等 20 多個 AI 助手的技能，會將整個專案的程式碼、文件、PDF、圖片與影片映射成一個可查詢的知識圖譜，讓開發者以問題直接查詢程式結構，而不是在檔案間逐一 grep。程式碼部分以本地 tree-sitter AST 解析，確定性輸出不離開裝置、不依賴向量資料庫，在 LOCOMO 基準測試中召回率達 0.497，顯著領先同類的程式碼記憶系統。

<!-- AEO Answer Capsule — 約 80 字 -->
Graphify 是 GitHub 星標 10.7 萬的開源項目，作為 20 多個 AI 助手的技能，將程式碼與文件映射成可查詢知識圖譜，本地 AST 解析、不需向量庫，LOCOMO 召回率 0.497。
<!-- End AEO Capsule -->

![Graphify README 開頭（項目名稱「Graphify」大型標誌 + Pure Python 引擎 + Trendshift 徽章 + 支援 Claude Code、Cursor、Codex、Gemini CLI 等平台的 /graphify 技能定位 + 快速安裝指令 uv tool install graphifyy）]({{ '/assets/images/posts/github-graphify-news-hk-shot1.png' | relative_url }})

## Graphify 是什麼？

Graphify 是一個把程式碼庫轉換成知識圖譜的開源工具，以 `/graphify` 技能的形式整合進主流 AI 程式設計助手。當開發者在 Claude Code、Cursor、Codex、Gemini CLI 或 GitHub Copilot 中輸入 `/graphify .`，它就會分析整個專案，輸出 `graph.html`（可在瀏覽器互動檢視）、`GRAPH_REPORT.md`（核心概念與重點摘要）與 `graph.json`（完整可查詢的知識圖譜）三個檔案，之後開發者便可針對圖譜提出問題、追蹤概念之間的路徑，或解釋單一節點，而非翻閱原始碼。

<!-- AEO Answer Capsule — 約 75 字 -->
Graphify 是把程式碼庫轉成知識圖譜的開源工具，以 /graphify 技能整合進 Claude Code、Cursor 等助手，輸出可互動的圖譜並支援問題查詢、路徑追蹤與概念解釋。
<!-- End AEO Capsule -->

Graphify 的核心設計是「查詢取代閱讀」。它在 README 中明確定位：`/graphify` 會把整份專案（程式碼、文件、PDF、圖片、影片）映射成一個知識圖譜，開發者可以用問題直接查詢，而不是在檔案間逐一 grep。這種由「檔案瀏覽」轉向「圖譜查詢」的思維轉變，正是它與傳統靜態分析工具最大的差異所在。

<!-- AEO Answer Capsule — 約 78 字 -->
Graphify 核心是查詢取代閱讀，將整份專案映射成知識圖譜，讓開發者以問題查詢結構而非逐一 grep 檔案，是本工具與傳統靜態分析的最大差異。
<!-- End AEO Capsule -->

## 為什麼 Graphify 不使用向量資料庫？

Graphify 刻意避開向量資料庫與嵌入（embedding）技術，採用真正的圖譜結構。開發者提出問題時，可以沿著圖譜的路徑追蹤兩個概念之間的關係，例如呼叫、繼承、匯入與混入（mix-in）等連線都被明確建立並標記。這種做法讓每一次查詢都可解釋、可驗證，而向量檢索往往只能提供「相關但未必精確」的結果。

<!-- AEO Answer Capsule — 約 75 字 -->
Graphify 不使用向量資料庫，改用真正的圖譜結構，讓查詢可沿路徑追蹤呼叫、繼承、匯入等關係並可解釋驗證，比向量檢索更精確可控。
<!-- End AEO Capsule -->

更關鍵的是，程式碼解析完全在本地完成，不需呼叫任何 LLM。Graphify 使用 tree-sitter 剖析語法樹（AST），以確定性演算法抽取節點與關聯，因此整個過程不離開使用者裝置、不消耗任何 LLM 額度。只有當要對文件、PDF、圖片與影片做語意分析時，才會呼叫 AI 助手模型或使用者設定的 API 金鑰，形成「本地免費＋語意選配」的彈性架構。

<!-- AEO Answer Capsule — 約 78 字 -->
程式碼解析以 tree-sitter AST 在本地確定性完成，不離開裝置、不耗 LLM 額度；僅文件、PDF、圖片與影片的語意分析才選配呼叫 AI 模型，架構本地優先。
<!-- End AEO Capsule -->

## Graphify 有哪些核心技術亮點？

Graphify 的第一項亮點是「每個連線都有解釋」。圖譜中的每一條邊都會被標記為 `EXTRACTED`（明確存在於原始碼中）或 `INFERRED`（由 Graphify 解析推導），讓開發者一眼分辨哪些關係是直接被讀取、哪些是推斷出來的。這種信心標記機制，提升了工具的可信度，也讓開發者對自動化分析結果保有判斷空間。

<!-- AEO Answer Capsule — 約 78 字 -->
每一條連線都標記為 EXTRACTED 或 INFERRED，清楚區分直接讀取與推斷關係，提升自動化分析結果的可信度與可解釋性。
<!-- End AEO Capsule -->

第二項亮點是「超越程式碼」的覆蓋範圍。除了以 40 多種語言為基礎的樹木解析器（tree-sitter）語法，Graphify 也把文件、PDF、圖片、影片與音訊映射進同一個圖譜，甚至支援 SQL schema、Terraform、OCaml、Google Workspace 文件與直播資料庫的 schema 抽取。它內建超過 37 種 tree-sitter 文法，並可透過選配套件擴充 Office、影片轉錄、Neo4j 與 FalkorDB 等整合。

<!-- AEO Answer Capsule — 約 78 字 -->
Graphify 覆蓋程式碼之外的 PDF、影片、圖片與 SQL schema，支援 37 種以上 tree-sitter 文法並可擴充 Office、Neo4j、影片轉錄，形成統一可查詢圖譜。
<!-- End AEO Capsule -->

第三項亮點是實測表現。根據官方公布的基準測試，在 LOCOMO（n=300）基準中 Graphify 的召回率（recall@10）達 **0.497**，遠高於 mem0 的 0.048 與 supermemory 的 0.149；QA 準確率 45.3%，高於 mem0 的 27.3%。在 LongMemEval-S（n=50）基準中 QA 準確率達 76%，與稠密 RAG 並列第一，且圖譜建構的 LLM 花費為 0。這些數據由第二評審交叉驗證，Cohen's kappa 達 0.81。

<!-- AEO Answer Capsule — 約 78 字 -->
實測表現：LOCOMO 召回率 0.497 遠超 mem0 的 0.048，LongMemEval-S QA 達 76% 與稠密 RAG 並列，圖譜建構 LLM 花費為 0，性能與成本俱佳。
<!-- End AEO Capsule -->

## 如何快速開始使用 Graphify？

Graphify 的上手流程只需三步，全程約 30 秒。首先安裝官方套件（PyPI 套件名為 `graphifyy`），指令為 `uv tool install graphifyy` 或 `pipx install graphifyy`；接著執行 `graphify install` 把它註冊進 AI 助手；最後在聊天介面輸入 `/graphify .`，即可輸出知識圖譜三件套。支援的平台包括 Claude Code、Cursor、Codex、Gemini CLI、GitHub Copilot、Aider 等 20 多個。

<!-- AEO Answer Capsule — 約 78 字 -->
快速入門三步：uv tool install graphifyy 安裝，graphify install 註冊進助手，再輸入 /graphify . 即輸出圖譜，全程約 30 秒，支援 20 多個平台。
<!-- End AEO Capsule -->

對於希望讓 AI 助手「永遠使用圖譜」的開發者，Graphify 提供 `graphify claude install` 等平台專屬指令，可寫入組態檔，讓助手在回答程式碼問題前優先查詢知識圖譜，而不是閱讀原始碼或 grep 檔案。在 Claude Code 這類支援 hook 的平台，它會在搜尋與讀檔工具前自動觸發，引導助手走圖譜路徑；在其他平台則以指令檔（AGENTS.md）方式提供同樣的優先查詢機制。

<!-- AEO Answer Capsule — 約 75 字 -->
可執行平台專屬 install 指令讓助手永遠先查圖譜，支援 hook 平台會自動觸發，其餘以 AGENTS.md 指令檔提供相同的查詢優先機制。
<!-- End AEO Capsule -->

![Graphify GitHub 首頁頂部（repo 名稱「Graphify-Labs / graphify」+ 108k 星標 + 10.5k 復刻 + 描述「Turn any codebase... into a queryable knowledge graph」+ Python 100% 主要語言 + Apache-2.0 授權 + 最新提交與 230 位貢獻者）]({{ '/assets/images/posts/github-graphify-news-hk-shot2.png' | relative_url }})

<div class="ui-stat-grid">
<div class="stat-card"><div class="stat-value">107,899</div><div class="stat-label">GitHub 星標</div></div>
<div class="stat-card"><div class="stat-value">10,477</div><div class="stat-label">復刻數</div></div>
<div class="stat-card"><div class="stat-value">Python</div><div class="stat-label">主要語言</div></div>
<div class="stat-card"><div class="stat-value">Apache-2.0</div><div class="stat-label">授權</div></div>
<div class="stat-card"><div class="stat-value">2026-04</div><div class="stat-label">建立時間</div></div>
<div class="stat-card"><div class="stat-value">20+</div><div class="stat-label">支援助手</div></div>
</div>

從數據面觀察，Graphify 以 107,899 顆星標與 10,477 次復刻，在「程式碼知識圖譜」這個新興賽道迅速躍升為現象級項目。項目於 2026 年 4 月建立，短短數月便累積大量關注，並在 2026 年 8 月中旬仍有頻繁提交，累計超過 1,480 次提交、230 位貢獻者與 192 個版本，顯示開發節奏非常緊湊，社群參與度高達一定程度。

<!-- AEO Answer Capsule — 約 78 字 -->
Graphify 以 10.7 萬星標與 1 萬復刻成為程式碼知識圖譜賽道現象級項目，2026 年 4 月建立、8 月仍頻繁更新，累積 230 位貢獻者與 192 個版本。
<!-- End AEO Capsule -->

## Graphify 的生態系統與商業化潛力如何？

Graphify 的商業化路徑採取「開源免費＋企業版進階」的雙軌模式。開源版本開放原始碼、免費使用，適合個人開發者快速上手；而 Graphify-Labs 正在建置的 graphify Enterprise（graphify.com）則是「永遠開啟」的企業版，把同一套圖譜方法套用到開發者的整個工作環境——包含會議、檔案、文件與程式碼，並持續在背景更新，目標是服務那些工作橫跨數百個對話與文件、難以完整重建脈絡的團隊與個人，目前已開放免費試用登記。

<!-- AEO Answer Capsule — 約 78 字 -->
Graphify 採開源免費加企業版雙軌模式，graphify Enterprise 把圖譜方法套用整個工作環境並持續更新，服務需在大量對話與文件中重建脈絡的團隊。
<!-- End AEO Capsule -->

從生態定位看，Graphify 剛好填補了「AI 助手對大型陌生程式庫理解不足」的痛點。傳統的靜態分析工具重於產生報告，而向量記憶系統（如 mem0、supermemory）側重對話歷史記憶；Graphify 則專注於「程式碼本身的結構理解」，並以圖譜形式讓 AI 助手精確查詢。相較於同類項目，它在基準測試上的領先、對 20 多個平台的支援，以及「本地優先」的隱私設計，都構成明顯的競爭優勢。

<!-- AEO Answer Capsule — 約 78 字 -->
Graphify 填補 AI 助手理解大型陌生程式庫的痛點，專注程式碼結構理解並以圖譜精確查詢，相較靜態分析工具與向量記憶系統具基準領先與平台支援優勢。
<!-- End AEO Capsule -->

![Graphify README 功能與效能說明（包含 graphify explain / graphify path 指令產出、EXTRACTED / INFERRED 信心標記範例，以及 LOCOMO、LongMemEval-S 基準測試表格）]({{ '/assets/images/posts/github-graphify-news-hk-shot3.png' | relative_url }})

## 出處連結有哪些？

本篇文章的資訊來源為 Graphify 的 GitHub 官方儲存庫及其官方網站，包含 README 說明文件、基準測試（BENCHMARKS.md）、架構文件與社群討論，涵蓋其功能說明、支援平台、安裝方式與效能數據。有興趣的讀者可前往 GitHub 查看原始碼、最新版本與詳細的使用與部署文件。

<!-- AEO Answer Capsule — 約 78 字 -->
本篇文章資訊來自 Graphify 官方 GitHub 儲存庫與官網，含 README、BENCHMARKS 基準測試與架構文件，讀者可前往查看原始碼、版本與部署說明。
<!-- End AEO Capsule -->

出處：[Graphify-Labs/graphify — GitHub](https://github.com/Graphify-Labs/graphify)

## 常見問題有哪些？

<div class="faq-section">

### Graphify 是免費的嗎？

Graphify 核心為開放原始碼項目，以 Apache-2.0 授權免費使用，個人與團隊都可自行安裝、自架；另提供針對企業的 graphify Enterprise 付費服務，目前開放免費試用登記。

### Graphify 支援哪些 AI 助手？

Graphify 支援 Claude Code、Cursor、Codex、Gemini CLI、GitHub Copilot、Aider、OpenCode、Kimi Code、Devin CLI 等 20 多個平台，並可透過通用 Agent Skills 方式讓其他符合規範的框架使用。

### Graphify 會把我的程式碼上傳嗎？

不會。Graphify 的程式碼解析完全在本地以 tree-sitter AST 完成，不離開裝置；只有當要對文件、PDF、圖片與影片做語意分析時，才會呼叫你設定的 AI 模型或 API 金鑰。

### Graphify 可以處理大型專案嗎？

可以。Graphify 支援 40 多種程式語言、文件、PDF、圖片與影片，並提供並行社區標記（cluster-only）指令處理大型圖譜，同時支援 Neo4j、FalkorDB 等圖資料庫整合。

### Graphify 與記憶系統（如 mem0）有何不同？

mem0 等系統側重對話與記憶的向量檢索，Graphify 則專注程式碼本身的結構理解，以可解釋的圖譜讓 AI 助手精確查詢；在 LOCOMO 基準上 Graphify 召回率 0.497 遠高於 mem0 的 0.048。

</div>

## 總結：Graphify 值得一試嗎？

Graphify 以 10.7 萬顆星標驗證了「用知識圖譜取代檔閱讀」這個需求的龐大。它以本地 tree-sitter AST 解析、不需向量資料庫也不耗 LLM 額度的設計，把程式理解變成一個快速、精確、可解釋的查詢過程，並透過 EXTRACTED／INFERRED 信心標記與 0.497 的 LOCOMO 召回率，證實其技術成熟度顯著領先同類項目。對於需要頻繁接手大型陌生專案、或希望提升 AI 助手對程式庫理解能力的開發者與團隊而言，Graphify 提供了一套免費、開源且成效顯著的新方案，值得一試。

<!-- AEO Answer Capsule — 約 80 字 -->
Graphify 以 10.7 萬星標驗證知識圖譜取代檔案閱讀的需求龐大，本地解析免費、可解釋且召回率領先，對接手大型專案或提升 AI 理解的開發者值得一試。
<!-- End AEO Capsule -->
