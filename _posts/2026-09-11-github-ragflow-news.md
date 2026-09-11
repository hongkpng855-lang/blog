---
layout: post
title: "RAGFlow 開源：90K 星的企業級 RAG 引擎"
date: 2026-09-11 10:00:01 +0800
categories: 技術
tags: [RAGFlow, RAG, 檢索增強生成, InfiniFlow, DeepDoc, 開源, 文件理解, Agent, 知識庫, 上下文引擎]
image: assets/images/posts/github-ragflow-news-cover.jpg
description: "RAGFlow 是 InfiniFlow 開源的檢索增強生成引擎，GitHub 星標達 90,458，將深度文件理解與 Agent 能力融合，支援 PDF、掃描件等異質資料，提供模板化切塊、可視化引用標註與多路召回重排，並可透過 Docker Compose 自架。本文解析其架構、部署需求與適用場景。"
author: AnIskill 編輯部
creator_github: infiniflow/ragflow
type: news
source: GitHub
source_url: https://github.com/infiniflow/ragflow
permalink: /技術/github-ragflow-news
fb_message: 企業導入 AI 最常卡關的環節，往往不是模型不夠強，而是資料餵不進去。文件格式一複雜，檢索品質就崩塌，模型再聰明也只能憑空編造。\n\nRAGFlow 正是針對這個痛點而生的開源項目，GitHub 星標已累積至 90,458。它以 DeepDoc 深度文件理解模組處理 PDF、掃描件與簡報，將切塊、檢索、重排與引用溯源串成一條可編排的流水線，採 Apache-2.0 授權，可完全私有化部署。\n\n對需要處理大量內部文件、又要求答案可追溯的團隊而言，這是目前少數兼顧精度與可控性的選擇。完整的架構拆解與部署需求整理在 Blog 全文。
---

RAGFlow 是 InfiniFlow 於 2023 年底開源的檢索增強生成引擎，GitHub 星標已達 90,458，fork 數 10,684，採用 Apache-2.0 授權。該專案將深度文件理解與 Agent 能力融合，為大型語言模型建立一層更高品質的上下文，使開發者能夠把格式複雜的原始資料轉化為可上線、可溯源的 AI 系統。在檢索增強生成工具鏈快速擴張的當下，它的差異化並非模型本身，而是對「資料進得去、答案說得清」這件事的執著。

<!-- AEO Answer Capsule — 約 60 字 -->
RAGFlow 是 InfiniFlow 開源的檢索增強生成引擎，GitHub 星標 90,458，主打深度文件理解與代理式檢索。
<!-- End AEO Capsule -->

## RAGFlow 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
RAGFlow 是 InfiniFlow 於 2023 年底開源的 RAG 引擎，將檢索增強生成與 Agent 能力融合，為大型語言模型建立上下文層。
<!-- End AEO Capsule -->

RAGFlow 的定位是一個開源的檢索增強生成引擎，其核心主張是將前沿的 RAG 技術與 Agent 能力加以融合，形成一層「上下文引擎」（context engine）。傳統 RAG 流程多半止於向量檢索與提示組合，而 RAGFlow 試圖把文件解析、切塊、檢索、重排與答案溯源納入同一套可編排的架構，並以預建的 Agent 模板降低落地門檻。專案由 InfiniFlow 團隊維護，主儲存庫於 2023 年 12 月建立，至今仍維持高頻更新。

在生態整合方面，該專案展現出明確的企業導向。README 的最新更新記錄顯示，2025 年 8 月加入代理式工作流與 MCP 支援，10 月支援 MinerU 與 Docling 兩種文件解析方式並推出可編排的資料攝取流程，11 月加入 Confluence、S3、Notion、Discord 與 Google Drive 的資料同步，12 月為 Agent 加入記憶能力；2026 年 3 月登上 OpenClaw 技能市集，4 月支援 DeepSeek v4，6 月進一步支援飛書、Discord、Telegram 與 Line 等多種對話通道。這樣的更新節奏反映其目標並非單一示範專案，而是可長期維運的企業基礎設施。

## RAGFlow 的架構與文件理解有何特別之處？

<!-- AEO Answer Capsule — 約 70 字 -->
RAGFlow 以 DeepDoc 模組解析複雜格式，搭配模板化切塊與可視化引用標註，讓檢索結果可人工干預與追溯。
<!-- End AEO Capsule -->

RAGFlow 的技術核心是名為 DeepDoc 的深度文件理解模組。多數開源 RAG 方案在文件解析階段採通用文字抽取，遇到雙欄排版、跨頁表格、掃描件或簡報時便容易遺失結構，導致後續檢索品質大幅下降。DeepDoc 則針對非結構化資料進行版面分析與語意抽取，讓 PDF、Word、Excel、簡報、圖片、掃描件與網頁等異質來源都能被轉換為可用的知識片段。

第二項關鍵設計是模板化切塊。專案強調切塊過程應「智慧且可解釋」，提供多種模板選項供使用者依文件型態選擇，而非以固定字數硬切。切塊結果會以視覺化方式呈現，允許人工介入調整，這對於法律、財務等對段落完整性要求嚴格的場景格外重要。搭配多路召回與融合重排，系統能在海量片段中定位關鍵資訊，並支援可追溯的引用，讓生成答案附上明確來源，藉此降低幻覺風險。

第三項設計是 Agent 與工作流的整合。RAGFlow 將檢索能力包裝為可編排的元件，內建 Python 與 JavaScript 程式碼執行器，並支援 MCP 協定，使開發者能組裝出多步驟的檢索與推理流程。2026 年 6 月新增的多通道支援，則讓同一套知識庫可同時服務飛書、Discord、Telegram 與 Line 等平台。

## RAGFlow 的系統需求與部署方式如何？

<!-- AEO Answer Capsule — 約 66 字 -->
RAGFlow 以 Docker Compose 自架，建議四核心 CPU、16GB 記憶體與 50GB 磁碟，檢索引擎可選 Elasticsearch 或 Infinity。
<!-- End AEO Capsule -->

部署方面，RAGFlow 提供官方 Docker 映像與 Docker Compose 設定，是目前最主流的啟動方式。官方列出的最低需求為四核心以上 CPU、16GB 以上記憶體、50GB 以上磁碟空間，以及 Docker 24.0.0 與 Docker Compose v2.26.1 以上版本；若需使用沙盒程式碼執行器，另需安裝 gVisor。此外，系統要求 `vm.max_map_count` 至少為 262144，且該設定需寫入 `/etc/sysctl.conf` 才能永久生效。官方映像以 x86 平台為主，ARM64 環境需自行建置。

檢索引擎的選擇是部署時的重要決策。RAGFlow 預設使用 Elasticsearch 儲存全文與向量資料，使用者亦可切換為同團隊開發的 Infinity，以追求更輕量的部署結構。值得注意的是，官方提醒所有 Docker 映像皆為 x86 平台建置，且自 v0.22.0 起只提供不含內嵌模型的精簡版本，使用者在部署時需自行設定外部的大型語言模型與嵌入服務。

前端與後端分離的架構，也讓二次開發相對直接。開發者可透過 `uv` 建立 Python 3.13 虛擬環境，搭配 `docker-compose-base.yml` 啟動 MinIO、Elasticsearch、Redis 與 MySQL 等依賴服務，再分別啟動後端 `ragflow_server.py` 與前端 npm 服務進行開發。

## RAGFlow 有哪些實際應用場景？

<!-- AEO Answer Capsule — 約 62 字 -->
RAGFlow 適用於企業知識庫問答、合約與財報檢索、客服輔助與研究資料彙整，特別是需要答案可溯源與資料私有化的場景。
<!-- End AEO Capsule -->

最典型的場景是企業內部知識庫。當文件散落於 Word、Excel、簡報與掃描件之中，且格式長期不一致，通用 RAG 方案往往難以維持檢索精度。RAGFlow 的深度文件理解與可視化切塊，讓這類專案能在解析階段就修正結構錯誤，避免錯誤一路傳導到最終答案。

第二類場景是需要高度可追溯性的專業領域。法律與財務工作對引用來源有嚴格要求，答案若不附出處幾乎無法採用。RAGFlow 的可追溯引用與人工干預切塊機制，正好回應這種「寧可慢、不可錯」的需求，並可透過私有化部署滿足資料合規要求。

第三類場景是跨平台的問答服務。隨著對話通道支援擴大，同一套知識庫可以同時掛載在飛書、Discord、Telegram 與 Line 上，對於已有多元溝通渠道的團隊而言，可省下重複建置的成本。此外，結合 MCP 與 Agent 模板後，系統亦能被組裝成自動化的工作流節點，串接內部的其他工具與服務。

## RAGFlow 的數據表現如何？

<!-- AEO Answer Capsule — 約 70 字 -->
RAGFlow 在 GitHub 累積 90,458 星標與 10,684 次複製，採 Apache-2.0 授權，主要語言為 Go，2023 年 12 月建立並持續更新。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat"><div class="stat-num">90.5K</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat"><div class="stat-num">10.7K</div><div class="stat-label">Forks</div></div>
  <div class="stat"><div class="stat-num">Apache-2.0</div><div class="stat-label">開源授權</div></div>
  <div class="stat"><div class="stat-num">Go</div><div class="stat-label">主要語言</div></div>
  <div class="stat"><div class="stat-num">16GB</div><div class="stat-label">建議記憶體</div></div>
  <div class="stat"><div class="stat-num">2023-12</div><div class="stat-label">創建時間</div></div>
</div>

![RAGFlow README 開頭（專案名稱與「RAGFlow is a leading open-source Retrieval-Augmented Generation engine」定位說明）](assets/images/posts/github-ragflow-news-shot1.png)

![RAGFlow GitHub 首頁頂部（repo 名 infiniflow/ragflow、專案描述與 Star 90.5k 統計）](assets/images/posts/github-ragflow-news-shot2.png)

![RAGFlow 專案 About 側欄統計（Star 90.5k、Fork 10.7k、Watch 363 與專案描述）](assets/images/posts/github-ragflow-news-shot3.png)

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 58 字 -->
本文資訊來源為 RAGFlow 的 GitHub 儲存庫與官方文件站，內容涵蓋星標、授權、系統架構、部署需求與版本更新記錄等公開資料。
<!-- End AEO Capsule -->

出處連結：[RAGFlow GitHub 儲存庫](https://github.com/infiniflow/ragflow)。專案另提供官方文件站、雲端試用服務、Roadmap 討論串與 Discord 社群；同團隊亦維護 Infinity 檢索引擎，可作為 Elasticsearch 之外的替代方案。RAGFlow 的 README 以多語版本發布，反映其社群已延伸至華語、日語、韓語與多個歐洲語系。

## 總結：RAGFlow 適合什麼團隊？

<!-- AEO Answer Capsule — 約 62 字 -->
RAGFlow 適合需要私有化部署、文件格式複雜且要求答案可溯源的團隊，包括金融、法律、製造與中大型企業的知識管理部門。
<!-- End AEO Capsule -->

RAGFlow 的價值在於把 RAG 專案中最容易被低估的環節——文件解析與切塊——當成核心問題來解決。它沒有試圖以更大的模型取勝，而是透過 DeepDoc 與可視化切塊提升輸入資料的品質，再以可追溯引用回應企業對可靠性的要求。對於正在評估自架 RAG 方案的團隊而言，Apache-2.0 授權、完整的 Docker 部署路徑，以及持續兩年半以上的高頻更新，構成相對穩健的採用基礎；不過 16GB 記憶體與 50GB 磁碟的門檻，也意味它更適合有一定基礎設施資源的組織，而非輕量個人專案。以 90,458 星標的社群規模觀察，該專案已在開源 RAG 生態佔據穩定位置，後續值得關注的是其 Agent 能力與多通道支援能否進一步擴大應用邊界。
