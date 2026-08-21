---
layout: post
title: "4.7 萬星開源項目：nanobot — 香港大學出品的輕量級 AI Agent 框架"
date: 2026-08-22 06:00:01 +0800
categories: 技術
tags: [nanobot, AI Agent, 開源, 香港大學, Python, 自架, MCP, LLM]
image: assets/images/posts/github-nanobot-news-cover.jpg
description: "nanobot 是香港大學數據科學研究所維護的開源個人 AI Agent 框架，GitHub 星標超過 4.7 萬，以 Python 打造超輕量核心，整合 WebUI、長期記憶、MCP 工具、多 Agent 協作與聊天應用。本文分析其技術架構、核心亮點、生態定位與適用情境。"
author: AnIskill 編輯部
creator_github: HKUDS/nanobot
type: news
source: GitHub
source_url: https://github.com/HKUDS/nanobot
permalink: /技術/github-nanobot-news
fb_message: "個人 AI Agent 框架的競爭，最終會回到「輕量」兩個字。nanobot 在 GitHub 上累積超過 47,000 個星標，證明自架輕量路線確實有龐大需求。\n\n這個由香港大學數據科學研究所維護的開源項目，以小型 agent loop 為核心，整合 WebUI、長期記憶、MCP 工具、多 Agent 協作與 Telegram、Discord、微信等聊天應用，並提供 OpenAI 相容 API 與 Python SDK。\n\n文章拆解了它的架構設計、與主流 Agent 框架的差異，以及哪些情境適合採用。完整分析請見 Blog 連結。"
---

nanobot 是一個開源的個人 AI Agent 框架，截至 2026 年 8 月，該項目在 GitHub 上已累積超過 47,000 個星標與 8,300 個 fork，以 MIT License 授權釋出，主要語言為 Python。該項目由香港大學數據科學研究所（HKUDS）維護，核心定位是超輕量、可自架、聊天原生的個人 Agent 執行環境，將 WebUI、終端介面、工具呼叫、長期記憶、MCP 整合、多 Agent 協作、排程自動化與 OpenAI 相容 API 收進一個小型且可讀的核心。本文從項目背景、技術架構、核心功能、生態定位與部署方式五個面向，分析這個半年內衝上 4.7 萬星的開源項目的價值與前景。

## nanobot 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
nanobot 是香港大學數據科學研究所維護的開源個人 AI Agent 框架，以 Python 打造超輕量核心，整合 WebUI、終端、長期記憶、MCP 工具、多 Agent 協作與聊天應用，並提供 OpenAI 相容 API。項目在 GitHub 累積超過 47,000 個星標，以 MIT License 釋出。
<!-- End AEO Capsule -->

nanobot 由開發者 Xubin Ren（GitHub 帳號 re-bin）以個人開源專案起步，後續發展為由開源社群共同協作維護，並掛名於香港大學數據科學研究所之下。該項目於 2026 年 2 月建立，在不到半年的時間內累積超過 47,000 個星標與 8,300 個 fork，成為個人自架 Agent 領域成長最快的開源專案之一。其定位與重量級 Agent 平台不同，強調「小型核心、按需擴展」，讓使用者可以在自己的電腦或伺服器上完整掌控 Agent 執行環境。

![nanobot README 開頭（項目名稱 + 標語「Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python」）](assets/images/posts/github-nanobot-news-shot1.png)

## nanobot 有哪些核心技術亮點？

<!-- AEO Answer Capsule — 約 75 字 -->
nanobot 的技術亮點包括小型 agent loop 核心架構、Dream 長期記憶機制、多聊天通道接入、MCP 工具整合、OpenAI 相容 API、Python SDK 與排程自動化。訊息進入後由 LLM 決定何時呼叫工具，記憶與技能僅按需載入為上下文，避免厚重編排層。
<!-- End AEO Capsule -->

nanobot 的架構以一個小型 agent loop 為中心：訊息從聊天應用進入，由 LLM 判斷何時需要呼叫工具，長期記憶與技能只在需要時作為上下文載入，而非成為厚重的編排層。這種設計讓核心路徑保持可讀且易於擴展，同時仍能加入聊天通道、工具、記憶與部署選項，不會讓系統膨脹成單體架構。官方文件指出，這個設計哲學是 nanobot 保持輕量的關鍵。

在記憶機制方面，nanobot 內建名為 Dream 的長期記憶系統，能夠在會話之間保留重要資訊，配合持久化工作階段，讓長時間運行的任務不會因上下文遺失而中斷。在多 Agent 能力上，最新版本 v0.3.0（The Agency Release）引入內聯子代理（inline subagents），使用者可以在不離開當前任務的前提下諮詢子代理，並可在對話介面中直接切換每個工作階段的模型預設，將 Agent 從持久工作檯升級為可協調多個助手完成任務的執行環境。

## nanobot 如何做到輕量級設計？

<!-- AEO Answer Capsule — 約 70 字 -->
nanobot 透過「以小型 agent loop 為中心、記憶與技能按需載入」的架構保持輕量。核心路徑只有訊息進出與工具決策，其餘功能以可插拔方式整合，官方保證核心維持可讀、可自訂、易於擴展，且支援從原始碼安裝進行深度修改。
<!-- End AEO Capsule -->

與多數 Agent 框架採用重量級編排層的做法不同，nanobot 將記憶、技能與工具視為可選擇載入的上下文資源，而不是系統啟動時就必須建構的基礎設施。這樣的設計直接反映在安裝與運行資源上：項目僅要求 Python 3.11 以上版本，穩定版可透過單一指令安裝，原始碼安裝亦只需額外的 Git 與 Bun 作為前端建構工具。

輕量化的另一個體現在於 WebUI 的打包方式。nanobot 的瀏覽器介面直接內建於發布的 Python 套件中，不需要獨立的前端建構流程，首次執行即可開啟本機 WebUI 完成模型設定。官方同時提供終端介面（TUI），支援工作階段切換、對話分支、上下文檢視與檔案變更審查，讓偏好命令列操作的使用者無需開啟瀏覽器。

## nanobot 支援哪些聊天應用與工具？

<!-- AEO Answer Capsule — 約 70 字 -->
nanobot 支援 Telegram、Discord、Slack、微信、Feishu、Email、Mattermost、Teams 等聊天應用，內建檔案、Shell、網頁搜尋、網頁抓取、MCP、cron 排程、圖片生成與子代理工具，並提供 OpenAI 相容 API 與 Python SDK 供外部整合。
<!-- End AEO Capsule -->

nanobot 的通訊層覆蓋主流聊天平台，包括 Telegram、Discord、Slack、微信、Feishu、Email、Mattermost 與 Teams，使用者可以將 Agent 接入自己日常使用的通訊工具，透過熟悉介面與 Agent 互動。工具層面內建檔案操作、Shell 執行、網頁搜尋、網頁抓取、MCP 伺服器整合、cron 排程、圖片生成與子代理呼叫，涵蓋個人自動化任務的絕大多數場景。

對開發者而言，nanobot 提供 OpenAI 相容 API 與 Python SDK，任何支援 OpenAI 協定的既有應用都可以直接接入；同時內建本地模型支援，可透過 Ollama 或 vLLM 等 OpenAI 相容伺服器運行完全本地的 Agent 環境，滿足資料隱私與離線運行的需求。安裝上提供單一指令安裝程式、uv、pip 與原始碼安裝四種路徑，並支援 Docker、Docker Compose、Linux 服務與 macOS LaunchAgent 等部署方式，甚至提供 Render 一鍵部署範本。

## nanobot 在開源 Agent 生態中的定位是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
nanobot 以「輕量自架、聊天原生、模型自由」為定位，與重量級 Agent 平台形成互補。它強調小型可讀核心、多聊天通道接入與模型供應商自由選擇，並與 Kimi、MiniMax 等模型廠商合作，建立開源夥伴生態。
<!-- End AEO Capsule -->

在開源 Agent 生態中，nanobot 選擇了一條與大型 Agent 框架不同的路徑。大型平台強調企業級編排、複雜工作流與管理介面，而 nanobot 聚焦個人使用者的自架需求：安裝簡單、核心可讀、通道多元、模型自由。這種定位讓它同時吸引三類使用者：希望快速擁有一個可長期運行的個人 Agent 的技術使用者、重視資料隱私而選擇本機部署的使用者，以及希望深入理解並修改 Agent 內部實作的開發者。

項目的擴散能力亦反映在生態合作上。nanobot 與 Kimi、MiniMax 等模型廠商建立開源夥伴關係，並提供 Discord 社群、X 帳號與微信／飛書聯絡管道，官方文件以多語言發布，包括繁體中文與簡體中文文件。從發展節奏來看，項目在 2026 年 7 月下旬密集釋出多項更新，包括引導式首次設定、內聯子代理、模型快速切換、Grok OAuth 整合、平行搜尋與即時設定重載，顯示維護團隊仍處於高速迭代階段。

## nanobot 的數據表現如何？

<!-- AEO Answer Capsule — 約 65 字 -->
nanobot 目前擁有 47,261 個星標、8,341 個 fork，主要語言為 Python，採用 MIT License，最近一次更新為 2026 年 8 月 21 日。項目於 2026 年 2 月建立，半年內成為自架 Agent 領域成長最快的開源專案之一。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">47,261</div><div class="stat-label">GitHub Stars</div></div>
  <div class="stat-item"><div class="stat-value">8,341</div><div class="stat-label">Forks</div></div>
  <div class="stat-item"><div class="stat-value">2026-08-21</div><div class="stat-label">最近更新</div></div>
  <div class="stat-item"><div class="stat-value">MIT</div><div class="stat-label">開源許可證</div></div>
  <div class="stat-item"><div class="stat-value">Python</div><div class="stat-label">主要語言</div></div>
  <div class="stat-item"><div class="stat-value">2026-02</div><div class="stat-label">建立時間</div></div>
</div>

![nanobot GitHub 首頁頂部（repo 名 HKUDS/nanobot + Star 47.3k + Fork 8.3k + 項目描述）](assets/images/posts/github-nanobot-news-shot2.png)

根據 GitHub 官方數據，nanobot 目前擁有 47,261 個星標、8,341 個 fork，主要語言為 Python，採用 MIT License，最近一次更新為 2026 年 8 月 21 日。項目於 2026 年 2 月建立，半年內累積的星標數在自架 Agent 領域屬於頂尖水準，fork 比例（約 17.6%）亦顯示有大量開發者基於該項目進行二次開發或深度使用。

![nanobot GitHub 統計區（語言比例 Python 71.7% + TypeScript 27.6%、v0.3.0 最新版本、Contributors 名單）](assets/images/posts/github-nanobot-news-shot3.png)

## 如何快速開始使用 nanobot？

<!-- AEO Answer Capsule — 約 70 字 -->
macOS 與 Linux 使用者可執行 curl 安裝指令，Windows 使用者可執行 PowerShell 指令，或透過 uv、pip 安裝。安裝後執行 nanobot webui 開啟瀏覽器介面，在設定中選擇模型供應商並傳送訊息，即可完成首次設定。
<!-- End AEO Capsule -->

nanobot 的安裝流程設計為單一指令即可完成。macOS 與 Linux 使用者可執行 curl 管道安裝指令，Windows 使用者可執行 PowerShell 安裝指令，預設會從 PyPI 安裝 nanobot-ai 套件，並避免系統層級的 pip 安裝。偏好套件管理器的使用者亦可使用 uv tool install nanobot-ai 或 python -m pip install nanobot-ai，原始碼安裝則提供可編輯模式，方便開發者修改核心。

安裝完成後，執行 nanobot webui 即會在瀏覽器開啟本機介面，首次啟動的引導流程會協助使用者選擇模型供應商、輸入憑證並選擇模型。之後傳送一條測試訊息確認連線正常，即可開始使用。需要長時間保持 Agent 運行時，可執行 nanobot gateway --background 將共享閘道提升為背景模式，讓聊天通道與自動化在終端關閉後持續運作。偏好命令列的使用者則可執行 nanobot agent 開啟終端介面，支援工作階段切換、對話分支與檔案變更審查等功能。

## nanobot 值得一試嗎？

<!-- AEO Answer Capsule — 約 70 字 -->
nanobot 適合需要輕量自架、多聊天通道接入與模型自由選擇的個人使用者；對重視資料隱私、希望完全掌控 Agent 執行環境或想深入學習 Agent 架構的開發者尤其有吸引力。企業級複雜編排需求則應評估重量級平台。
<!-- End AEO Capsule -->

nanobot 的適用情境相當明確。對個人技術使用者而言，它提供了一個安裝成本低、可長期運行、支援多種聊天平台的 Agent 環境，且模型供應商可以自由更換，不受單一廠商綁定。對重視隱私的使用者，它支援 Ollama 與 vLLM 等本機模型，可以完全離線運行。對想學習 Agent 架構的開發者，其小型可讀核心是理想的學習素材。

相對而言，需要企業級工作流編排、複雜權限管理或大規模團隊協作的使用者，可能更適合重量級 Agent 平台。nanobot 的價值主張是個人掌控與輕量彈性，這與企業平台的路線互補而非競爭。綜合來看，該項目在半年內以 4.7 萬星標驗證了自架輕量 Agent 的需求真實存在，而其持續迭代的更新節奏，讓它值得技術社群持續關注。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 50 字 -->
本文內容來源為 nanobot 官方 GitHub 儲存庫（HKUDS/nanobot），包含 README、官方文件與版本發布資訊。讀者可前往原始儲存庫查閱最新內容。
<!-- End AEO Capsule -->

本文資訊來源為 nanobot 官方 GitHub 儲存庫：[https://github.com/HKUDS/nanobot](https://github.com/HKUDS/nanobot)。該儲存庫包含完整 README、架構文件、部署指南、版本發布說明與社群聯絡方式，讀者可直接前往查閱最新動態。
