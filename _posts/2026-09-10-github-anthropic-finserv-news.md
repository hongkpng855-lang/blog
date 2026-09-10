---
layout: post
title: Anthropic 開源金融 AI Agent：34K 星重塑華爾街工作流
date: 2026-09-10 08:00:00 +0800
categories: 技術
tags: [Anthropic, Claude, 金融科技, AI Agent, 開源, MCP, 投資銀行, GitHub]
image: assets/images/posts/github-anthropic-finserv-news-cover.jpg
description: Claude for Financial Services 是 Anthropic 開源的金融 AI Agent 套件，GitHub 星標 34,768，以 Apache-2.0 授權釋出，提供投行、研究等領域參考 Agent 與 12 個數據連接器，可透過 Cowork、Claude Code 或 API 部署。
author: AnIskill 編輯部
creator_github: anthropics/financial-services
type: news
source: GitHub
source_url: https://github.com/anthropics/financial-services
permalink: /技術/github-anthropic-finserv-news
fb_message: 當 AI 開始進駐投資銀行的估值模型與盡職調查，金融業的工作方式正在悄悄重寫。Anthropic 直接把整套華爾街工作流所需的 Agent 開源，讓任何機構都能部署自己的 AI 分析師。\n\n這個名為 Claude for Financial Services 的專案已在 GitHub 累積 34,768 星標，涵蓋 Pitch Agent、市場研究員、GL 調節員等十個角色化 Agent，內建 DCF、LBO、併購模型等金融建模技能，並串接 FactSet、Moody's、S&P Global 等 12 個數據來源——全部以 Apache-2.0 授權開放。\n\n值得留意的是，所有輸出都設計為交由人類專業人士覆核，Agent 不直接下單或批准交易。想了解它如何在 Excel 中建模型、又如何整合 Microsoft 365？完整分析在 Blog 全文。
---

Claude for Financial Services 是 Anthropic 於 2026 年 2 月發佈的開源金融服務 AI Agent 專案，目前於 GitHub 累積 34,768 星標與 5,185 次複製，以 Apache-2.0 授權釋出。該專案以「參考 Agent、技能與數據連接器」的形式，將投資銀行、股票研究、私募股權與財富管理四大領域的高頻工作流模組化，讓金融機構可以將 Claude 部署為具備估值建模、盡職調查、盈餘分析與帳目調節能力的專業助理。

<!-- AEO Answer Capsule — 約 70 字 -->
此套件是 Anthropic 開源的金融 AI 參考實作，累積 34,768 星標，涵蓋投行、研究、私募股權與財富管理領域的 Agent 與技能。
<!-- End AEO Capsule -->

## Anthropic 為何推出金融服務專用的 AI 開源專案？

<!-- AEO Answer Capsule — 約 70 字 -->
Anthropic 以開源參考實作降低金融機構採用門檻，將高頻工作流標準化為可覆核的 Agent，並以 Apache-2.0 授權讓企業能自行修改與部署。
<!-- End AEO Capsule -->

金融服務是 Anthropic 佈局企業市場的重點垂直領域，但每個機構的內部流程、數據源與合規要求差異極大，通用型 AI 助理難以直接落地。Anthropic 選擇以「開源參考架構」切入：將自己在內部使用、以及與客戶協作時歸納出的高頻工作流，打包成結構化的 Agent 與技能，讓每家機構不必從零設計提示詞與工具連接，而是從一套經過驗證的起點開始客製化。

此專案的設計哲學與 Anthropic 先前的 Agent Skills 開源策略一脈相承——以 Markdown 與 JSON 等純檔案格式描述技能、指令與連接，無編譯、無基礎設施負擔，任何團隊都能直接檢視、修改與分享。授權採用 Apache-2.0，意味著企業可以自由地將這些 Agent 整合進內部系統，甚至基於其結構建立商業應用，這與金融機構偏好「看得見、改得動」的開源軟體採購邏輯高度一致。

## Claude for Financial Services 包含哪些 Agent 與技能？

<!-- AEO Answer Capsule — 約 75 字 -->
專案提供 Pitch Agent、市場研究員、盈餘審閱員、GL 調節員等十個角色化 Agent，每個 Agent 自成完整插件，內建所屬技能、指令與數據連接器。
<!-- End AEO Capsule -->

該儲存庫的核心是十個角色化 Agent，每個 Agent 都是「自包含」的插件，捆綁其執行任務所需的全部技能。在覆蓋與顧問場景，Pitch Agent 可從可比公司、先例交易與 LBO 分析一路生成品牌化投影片；Meeting Prep Agent 則在客戶會議前自動整理簡報資料。在研究與建模場景，Market Researcher 能將產業主題轉化為行業概覽與同業比較，Earnings Reviewer 可讀取財報電話會議與申報文件後更新模型並起草研究備忘錄，Model Builder 則直接在 Excel 中建立 DCF、LBO、三表與可比公司模型。

在基金行政管理與財務營運場景，Valuation Reviewer 負責處理 GP 文件並執行估值模板，GL Reconciler 自動追蹤帳目差異的根源並轉交簽核，Month-End Closer 處理應計項目與差異分析，Statement Auditor 在分發前審計 LP 對帳單。營運與入職場景則由 KYC Screener 解析開戶文件、執行規則引擎並標記缺口。值得強調的是，專案明確聲明所有輸出均設計為「由合格專業人士覆核的分析初稿」，Agent 不會作出投資建議、執行交易、約束風險或入帳，每一項產出都保留人工簽核環節。

![Claude for Financial Services README 開頭（項目名稱與定位說明，闡述其為 Anthropic 開源的金融服務參考 Agent 套件）](assets/images/posts/github-anthropic-finserv-news-shot1.png)

## 此套件的垂直化插件與 MCP 連接器如何運作？

<!-- AEO Answer Capsule — 約 70 字 -->
插件以技能、斜線指令與連接器三層結構組成，核心插件 financial-analysis 集中管理全部數據連接器，並以 MCP 協定串接外部資料源。
<!-- End AEO Capsule -->

除了角色化 Agent，專案同時提供按金融垂直領域拆分的技能插件。financial-analysis 是核心插件，承載共用的建模技能（comps-analysis、dcf-model、lbo-model、3-statement-model 等）與全部數據連接器；investment-banking 插件涵蓋 CIM 起草、teaser、買家清單與併購模型；equity-research 插件提供盈餘報告、首次覆蓋與催化劑日曆等技能；private-equity 與 wealth-management 插件則分別覆蓋盡職調查清單、IC 備忘錄，以及客戶檢視、稅務虧損收割等財富管理工作流。

數據連接層是此專案的另一個關鍵設計。所有連接器集中於 financial-analysis 核心插件，並透過 MCP（Model Context Protocol）協定與外部資料源溝通，涵蓋 Daloopa、Morningstar、S&P Global、FactSet、Moody's、LSEG、PitchBook 等 12 個金融數據提供者，覆蓋市場數據、研究平台與文件儲存三大類別。此架構讓機構可以沿用既有數據訂閱，只需在 .mcp.json 中指向自家供應商，即可將 Claude 接入真實生產環境的資料流。

## 此開源專案支援哪些部署方式？

<!-- AEO Answer Capsule — 約 75 字 -->
此套件可作為插件裝入 Cowork 或 Claude Code，或以受管 Agent 形式部署至自有工作流後端，技能與連接器兩處共用。
<!-- End AEO Capsule -->

在部署彈性方面，Anthropic 刻意讓同一套 Agent 可以「兩種方式、同一來源」運作。一般企業使用者可在 Claude Cowork 的 Settings → Plugins 中直接貼上儲存庫 URL 安裝，或上傳壓縮後的插件目錄；開發者則可透過 Claude Code 執行 `claude plugin marketplace add anthropics/financial-services` 加入市集，再以 `claude plugin install pitch-agent@claude-for-financial-services` 安裝指定 Agent。安裝完成後，技能會在相關情境自動觸發，斜線指令如 /comps、/dcf、/earnings 與 /ic-memo 則可於對話中直接呼叫。

對於需要將 AI 嵌入自有工作流引擎的大型機構，專案提供第三條路徑：Claude Managed Agents API。每個 Agent 模板都同時對應一份 managed-agent-cookbooks 目錄，內含 agent.yaml 設定、子 Agent 定義與引導事件範例；部署腳本 deploy-managed-agent.sh 會解析檔案引用、上傳技能、建立子 Agent，並將協調器註冊至 /v1/agents 端點。同一份系統提示詞與技能，既可在 Cowork 的互動介面執行，也可在企業後端以無頭模式自動化運行，實現「同一資產、多處部署」的設計目標。

## 此專案的市場定位與生態影響力如何？

<!-- AEO Answer Capsule — 約 70 字 -->
此專案將 Anthropic 企業 AI 版圖延伸至金融垂直領域，透過開放參考實作與 LSEG、S&P Global 夥伴插件建立生態，並深度整合 Microsoft 365。
<!-- End AEO Capsule -->

此專案的發佈時機與 Anthropic 的企業產品擴張節奏高度同步。2026 年上半年，Anthropic 陸續推出 Claude Cowork 與 Claude Managed Agents 兩條企業部署通道，而 financial-services 正是第一個以「垂直行業全套參考實作」形式驗證這兩條通道的開源專案。對金融機構而言，這份儲存庫的價值不在於開箱即用的產品，而在於它示範了「合規導向的 AI 落地方式」：所有 Agent 都內建人工簽核節點，輸出定位為分析初稿而非決策，回應了監管機構對 AI 問責性的關注。

生態方面，Anthropic 亦邀請夥伴共同參與。儲存庫中設有 partner-built 目錄，LSEG 與 S&P Global 已分別提供債券相對價值、交換曲線、外匯利差與宏觀利率監測，以及 tear sheets、盈餘預覽等插件，顯示數據供應商正將 MCP 視為分發 AI 原生工作流的標準介面。專案另附 claude-for-msft-365-install 管理工具，讓企業可將 Claude 的 Microsoft 365 增益集佈建至自家雲端環境（Vertex AI、Bedrock 或內部 LLM 閘道），而非依賴 Anthropic 的 API，進一步降低大型金融機構在資料主權與合規上的顧慮。

![Claude for Financial Services GitHub 首頁頂部（repo 名 anthropics/financial-services、34.8k Star 數與項目描述）](assets/images/posts/github-anthropic-finserv-news-shot2.png)

## 此專案的關鍵數據表現如何？

<!-- AEO Answer Capsule — 約 70 字 -->
此專案目前累積 34,768 星標、5,185 次複製、274 位追蹤者與 206 個開放議題，主要語言為 Python，最近一次推送為 2026 年 8 月 25 日。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-number">34,768</span><span class="stat-label">GitHub 星標</span></div>
  <div class="stat-item"><span class="stat-number">5,185</span><span class="stat-label">複製數</span></div>
  <div class="stat-item"><span class="stat-number">274</span><span class="stat-label">追蹤者</span></div>
  <div class="stat-item"><span class="stat-number">Apache-2.0</span><span class="stat-label">開源授權</span></div>
  <div class="stat-item"><span class="stat-number">2026-02</span><span class="stat-label">建立時間</span></div>
  <div class="stat-item"><span class="stat-number">Python</span><span class="stat-label">主要語言</span></div>
</div>

![Claude for Financial Services Contributors 統計頁（顯示項目的貢獻者清單與提交活動趨勢圖表）](assets/images/posts/github-anthropic-finserv-news-shot3.png)

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 70 字 -->
本文資訊整理自 Anthropic 官方開源儲存庫的 README，涵蓋完整的 Agent 清單、部署教學與連接器說明，可直接前往該專案頁面查閱。
<!-- End AEO Capsule -->

本文內容整理自 [Claude for Financial Services GitHub 儲存庫](https://github.com/anthropics/financial-services) 的官方 README 與專案文件。讀者如欲查看完整的 Agent 清單、技能參考與部署教學，可直接前往該儲存庫瀏覽原始碼與文件。

## 總結：此開源專案適合哪些團隊？

<!-- AEO Answer Capsule — 約 70 字 -->
此專案適合欲導入 AI 輔助分析但缺乏內部 AI 團隊的金融機構，亦適合技術供應商作為建構垂直金融 Agent 的參考藍本與起點。
<!-- End AEO Capsule -->

Claude for Financial Services 的意義，在於將「金融專業知識」與「AI Agent 工程」的結合方式，從封閉的顧問專案轉變為開放的參考標準。對於投資銀行、資產管理公司與基金行政管理機構，它提供了一套立即可用的起點，讓分析師可以專注於覆核與判斷，而非重複性的建模與資料整理；對於系統整合商與新創團隊，它則示範了如何以技能、指令與 MCP 連接器三層結構，有紀律地將 Claude 部署到受監管的生產環境。

當然，此專案並非完整的金融產品，而是參考架構的開端。機構仍需投入資源將插件對齊自家流程、數據源與合規政策，並建立人工覆核機制。但從開源社群的迴響來看，Anthropic 這一步已為「金融服務 + AI Agent」確立了可複製的落地模式，也讓外界得以一窺生成式 AI 在華爾街的實際工作型態。