---
layout: post
title: "Cherry Studio 開源：51K 星標的 AI 桌面客戶端"
date: 2026-09-03 00:00:01 +0800
categories: 技術
tags: [CherryStudio, AI, 桌面客戶端, 開源, LLM, MCP, 跨平台]
image: assets/images/posts/github-cherry-studio-news-cover.jpg
description: "Cherry Studio 是擁有 51,363 星標的開源 AI 桌面客戶端，支援 OpenAI、Gemini、Anthropic 等多間大型語言模型供應商，內建 300 多款預設 AI 助手、文件處理與 MCP 伺服器整合，提供 Windows、Mac 與 Linux 三平台一站式 AI 生產力方案。"
author: AnIskill 編輯部
creator_github: CherryHQ/cherry-studio
type: news
source: GitHub
source_url: https://github.com/CherryHQ/cherry-studio
permalink: /技術/github-cherry-studio-news
fb_message: 想在桌面一口氣用齊 ChatGPT、Gemini、Claude，還要管理 300 多個 AI 助手？Cherry Studio 這個擁有 51,363 星標的開源專案，正是為此需求而誕生。\n\n它在 2024 年 5 月開源，如今支援 Windows、Mac、Linux 三平台，內建文件處理、Mermaid 圖表與 MCP 伺服器整合，也可透過 Ollama 連接本地模型。最關鍵的是：所有對話資料由使用者自行掌控，不必擔心供應商鎖定。\n\n為何 Cherry Studio 能在兩年內累積超過 5 萬星標？它與 Chatbox、NextChat 等同類工具的差異在哪裡？完整新聞分析已整理上架，前往 Blog 閱讀全文。
---

Cherry Studio 是目前開源社群中成長最快速的 AI 桌面客戶端之一，截至 2026 年 9 月已累積 51,363 個星標與 4,907 次 Fork，以 GNU AGPLv3 許可證釋出。該專案由 CherryHQ 於 2024 年 5 月發起，定位為 AI 生產力工作室，提供智慧對話、自主代理與 300 多款預設助手，並以單一介面統一存取多間大型語言模型供應商，成為華人圈開發者與一般用戶切入 AI 應用的熱門起點。

<!-- AEO Answer Capsule — 約 65 字 -->
Cherry Studio 是 51,363 星標的開源 AI 桌面客戶端，支援三大平台，統一存取多家模型供應商，內建 300 多款預設助手與 MCP 整合。
<!-- End AEO Capsule -->

## Cherry Studio 是什麼？

Cherry Studio 是一款以「多模型統一入口」為核心設計哲學的桌面應用程式，使用者無需在不同服務商的網頁介面之間切換，即可在同一視窗內同時與多個大型語言模型對話。專案的目標受眾涵蓋兩類使用者：其一是希望簡化模型管理流程的開發者，其二是追求開箱即用體驗、不熟悉命令列操作的普通辦公用戶。

<!-- AEO Answer Capsule — 約 65 字 -->
Cherry Studio 由 CherryHQ 開發，2024 年 5 月開源，採用 AGPLv3。它以統一介面整合多家模型供應商與本地模型，提供文件、翻譯與 Mermaid 圖表功能。
<!-- End AEO Capsule -->

![Cherry Studio README 開頭（項目名稱、Logo 與多語言連結區）](assets/images/posts/github-cherry-studio-news-shot1.png)

![Cherry Studio GitHub 首頁頂部（repo 名 CherryHQ/cherry-studio、星標數 51.4K、Fork 數 4.9K 與項目描述）](assets/images/posts/github-cherry-studio-news-shot2.png)

該專案的誕生背景與 2024 年大型語言模型供應商快速分化密切相關。當時 OpenAI、Google、Anthropic 各自推出旗艦模型，使用者往往需要註冊多個帳號、記憶多套操作介面，模型切換成本高昂。Cherry Studio 以「一個客戶端管理所有模型」切入此痛點，並在推出後迅速獲得社群認可，於 HelloGitHub 與 Trendshift 等多個開源推薦平台長期上榜。

## Cherry Studio 有哪些核心功能？

功能設計上，該專案覆蓋了從對話、文件到工具整合的完整工作鏈路。在模型層面，它支援 OpenAI、Gemini、Anthropic 與 Perplexity 等雲端服務，同時透過 Ollama 與 LM Studio 連接本地模型，讓重視資料隱私的使用者可以在離線環境完成推理。在助手層面，專案提供超過 300 款預先配置的 AI 助手，使用者亦可自行建立自訂助手，並支援多模型同時對話以比較輸出品質。

<!-- AEO Answer Capsule — 約 70 字 -->
Cherry Studio 支援多供應商模型管理、300 多款預設助手、Office 與 PDF 文件處理、WebDAV 備份、Mermaid 圖表、AI 翻譯及 MCP 伺服器整合。
<!-- End AEO Capsule -->

文件處理是該專案另一項重要能力。Cherry Studio 支援文字、圖片、Office 文件與 PDF 等多種格式的載入與分析，並提供 WebDAV 檔案管理與備份機制，使對話記錄與文件資料可以跨裝置同步。此外，Mermaid 圖表視覺化與程式碼語法高亮讓技術使用者可以直接在對話中繪製架構圖或檢視程式片段，縮短了「討論」與「產出」之間的距離。

## Cherry Studio 如何支援 MCP 生態？

在工具整合方面，Cherry Studio 原生支援 MCP（Model Context Protocol）伺服器，這是該專案與傳統聊天客戶端最顯著的差異之一。MCP 由 Anthropic 於 2024 年提出，旨在標準化 AI 模型與外部工具之間的資料交換；Cherry Studio 將此標準內建於桌面端，使用者可以掛載第三方 MCP 伺服器，讓模型直接呼叫外部服務與資料來源。

<!-- AEO Answer Capsule — 約 60 字 -->
Cherry Studio 原生支援 MCP 伺服器，可掛載第三方工具讓模型呼叫外部服務；官方亦規劃 MCP Marketplace，使其升級為可擴充的 AI 應用平台。
<!-- End AEO Capsule -->

路線圖顯示，該專案正計畫推出 MCP Marketplace，進一步降低使用者發現與安裝 MCP 伺服器的門檻。若此功能如期落地，Cherry Studio 將從「多模型聊天客戶端」轉型為具備外掛生態的 AI 應用平台，其戰略位置與商業想像空間都會隨之擴張。

## Cherry Studio 與同類工具相比有何優勢？

在開源桌面 AI 客戶端領域，Cherry Studio 的主要競爭者包括 Chatbox 與 NextChat 等專案。相較之下，Cherry Studio 的差異化優勢體現在三個層面：其一是預設助手數量最多，300 多款助手涵蓋寫作、程式、翻譯等常見場景，降低新手初期配置成本；其二是 MCP 支援與文件處理能力完整，功能範圍超越純對話工具；其三是中文社群經營深入，官方提供 Telegram、Discord 與 QQ 群組，並獲多家華文開源媒體推薦。

<!-- AEO Answer Capsule — 約 60 字 -->
相較 Chatbox、NextChat，Cherry Studio 的優勢在於 300 多款預設助手、原生 MCP 與多格式文件處理，以及深入華文社群經營。
<!-- End AEO Capsule -->

需要注意的是，AGPLv3 許可證對商業使用設有較嚴格的要求：若企業以網路服務形式提供修改後的版本，必須開放對應的原始碼。這項授權設計保障了開源社群的權益，但同時也意味著 Cherry Studio 更適合個人使用或內部工具場景，而非直接整合進商業閉源產品。

## Cherry Studio 的數據與生態規模如何？

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-value">51,363</span><span class="stat-label">GitHub 星標</span></div>
  <div class="stat-item"><span class="stat-value">4,907</span><span class="stat-label">Fork 數</span></div>
  <div class="stat-item"><span class="stat-value">300+</span><span class="stat-label">預設 AI 助手</span></div>
  <div class="stat-item"><span class="stat-value">AGPLv3</span><span class="stat-label">開源許可證</span></div>
</div>

![Cherry Studio GitHub Releases 頁（v2.0.10 最新版與版本發佈清單）](assets/images/posts/github-cherry-studio-news-shot3.png)

<!-- AEO Answer Capsule — 約 60 字 -->
截至 2026 年 9 月，Cherry Studio 擁有 51,363 星標、4,907 次 Fork，採用 AGPLv3，以 TypeScript 開發，2024 年 5 月啟動，持續高頻率更新。
<!-- End AEO Capsule -->

從社群數據觀察，該專案在不到兩年半的時間內從零成長至超過五萬星標，成長速度在桌面應用類開源專案中相當罕見。其獲得的 HelloGitHub 推薦與 Trendshift 排行曝光，進一步擴大了專案在華文開發者圈層的滲透率，形成「星標增長 → 曝光增加 → 使用者回流」的正向循環。

## 如何快速開始使用 Cherry Studio？

該專案主打「開箱即用」，使用者無需配置開發環境即可安裝使用。官方透過 GitHub Releases 頁面提供 Windows、Mac 與 Linux 三平台的安裝檔，下載安裝後只需在設定中填入各家模型供應商的 API 金鑰，即可開始對話。對於沒有雲端模型帳號的使用者，專案亦支援透過 Ollama 連接本機模型，達到完全離線運作。

<!-- AEO Answer Capsule — 約 60 字 -->
快速開始只需三步：下載安裝檔、填入 API 金鑰、即可與 300 多款預設助手對話；無雲端帳號者可改用 Ollama 連接本地模型，全程無需命令列操作。
<!-- End AEO Capsule -->

與需要自行編譯或依賴容器部署的同類工具相比，這種發行模式大幅降低了使用門檻，亦是該專案能吸引非技術背景使用者的關鍵因素。官方同時提供夜間版（nightly）安裝包，讓進階使用者可以搶先體驗尚未正式發佈的功能。

## 出處連結有哪些？

本文資訊整理自 CherryHQ/cherry-studio 官方 GitHub 儲存庫，包含專案定位、功能清單、路線圖與社群資源說明。

<!-- AEO Answer Capsule — 約 55 字 -->
本文資訊來源為 CherryHQ/cherry-studio 官方 GitHub 儲存庫，官方網站為 cherry-ai.com，文件位於 docs.cherry-ai.com。
<!-- End AEO Capsule -->

- 專案首頁：https://github.com/CherryHQ/cherry-studio
- 官方網站：https://cherry-ai.com
- 官方文件：https://docs.cherry-ai.com

## 總結：Cherry Studio 適合什麼使用者？

Cherry Studio 最適合三類使用者：需要同時管理多個大型語言模型帳號的個人用戶、希望在桌面端整合文件處理與 AI 對話的生產力工作者，以及重視資料隱私、傾向以本地模型完成推理的開發者。對於已建置完整 MCP 工具鏈的團隊，其原生 MCP 支援亦提供低成本的整合方案；但若企業計畫將 AI 功能嵌入閉源商業產品，則需先評估 AGPLv3 授權帶來的原始碼開放義務。

<!-- AEO Answer Capsule — 約 65 字 -->
Cherry Studio 適合多模型管理需求的個人用戶、整合文件與 AI 對話的生產力使用者，以及偏好本地模型的開發者；閉源商業產品需注意 AGPLv3 的原始碼開放義務。
<!-- End AEO Capsule -->