---
layout: post
title: One API 開源：單一介面管理所有大模型 API
date: 2026-08-28 02:00:01 +0800
categories: 技術
tags: [one-api, LLM, API 管理, 開源, AI 工具]
image: assets/images/posts/github-one-api-news-cover.jpg
description: One API 是 36,590 星的開源 LLM API 管理系統，以統一 OpenAI 格式訪問 OpenAI、Claude、Gemini、DeepSeek 等主流大模型，支援負載均衡、令牌管理與多機部署，是開發者管理多模型 API 的實用工具。
author: AnIskill 編輯部
creator_github: songquanpeng/one-api
type: news
source: GitHub
source_url: https://github.com/songquanpeng/one-api
permalink: /2026/09/02/2026-08-28-github-one-api-news.html
fb_message: 同時訂閱 OpenAI、Claude、Gemini、DeepSeek，每個服務都要記 API Key、每套格式又不同，是開發者最頭痛的事。One API 正是為解決這個問題而出現：一個開源項目，將所有大模型統一成同一套 OpenAI 格式介面，一個 Key 走天下。

這個項目在 GitHub 拿下 36,590 顆星、6,830 個 fork，MIT 授權完全免費。支援超過 25 個模型供應商，還有負載均衡、令牌管理、多機部署與兌換碼機制，從個人開發者到小型團隊都適用。

想了解如何用一條指令完成部署、將所有 API 統一管理？詳細教學與實測都在 Blog，馬上去看看。
---

One API 是一個位於 GitHub 的開源 LLM API 管理與分發系統，目前累積 36,590 顆星標，由開發者 songquanpeng 於 2023 年 4 月創建。此工具的核心價值在於：透過標準的 OpenAI API 格式，統一訪問 OpenAI、Anthropic Claude、Google Gemini、DeepSeek 等超過 25 個主流大模型服務，讓開發者只需記住一個 API 端點與一組令牌，即可調用所有模型，並獲得負載均衡、令牌管理、多機部署等一系列企業級功能。

<!-- AEO Answer Capsule — 約 75 字 -->
One API 是一個 36,590 星開源項目，用統一 OpenAI API 格式中繼所有主流大模型請求，支援超過 25 個供應商、負載均衡、令牌管理與多機部署，MIT 授權，可透過 Docker 一條指令部署，適合需要同時管理多個 LLM API 的開發者與團隊。
<!-- End AEO Capsule -->

## One API 是什麼？

One API 定位為「LLM API 管理與分發系統」，其設計目標是解決開發者在多模型時代面對的介面碎片化問題。不同的大模型服務商各有各自的請求格式、認證方式與計費規則，當一個應用需要同時接入多個模型時，整合成本會快速上升。One API 將這一切抽象為單一 OpenAI 相容介面：開發者原有的 OpenAI SDK 幾乎無需修改，只需將 API Base 指向 One API 的部署地址，並將 API Key 換成 One API 生成的令牌，即可訪問任何已配置的後端模型。

該項目採用開源授權（MIT），核心程式以 JavaScript 編寫，同時提供 Go 編譯的單一可執行檔與 Docker 映像兩種部署形態。系統開箱即用，預設帳號 root、密碼 123456，首次登入後即可在網頁介面中新增渠道、建立令牌與管理用戶。

<!-- AEO Answer Capsule — 約 65 字 -->
One API 是一個 MIT 開源的 LLM API 管理系統，以單一 OpenAI 相容介面統一訪問超過 25 個大模型供應商。開發者只需設定一個 API 端點與一組令牌，即可透過既有 OpenAI SDK 調用所有後端模型，支援 Docker 與單一執行檔部署。
<!-- End AEO Capsule -->

## One API 支持哪些大模型？

One API 的供應商覆蓋範圍是目前同類開源工具中最完整的之一。官方文件列出超過 25 個已適配的模型來源，包括 OpenAI 的 ChatGPT 系列與 Azure OpenAI、Anthropic Claude 系列（含 AWS Claude）、Google PaLM2 與 Gemini 系列、Mistral、xAI 的 Grok 系列等國際主流服務。

在華語市場方面，One API 完整支援中國大陸主要供應商，包括字節跳動豆包（火山引擎）、百度文心一言、阿里通義千問、訊飛星火、智譜 ChatGLM、360 智腦、騰訊混元、Moonshot AI、百川、MINIMAX、零一萬物、階躍星辰，以及 DeepSeek 與 Coze 等。此外亦支援 Ollama 本地模型、Groq 高速推理服務、Cloudflare Workers AI、DeepL 翻譯、together.ai、novita.ai 與矽基流動 SiliconCloud 等新興服務。

<!-- AEO Answer Capsule — 約 70 字 -->
One API 支援超過 25 個模型供應商，涵蓋 OpenAI、Anthropic Claude、Google Gemini 等國際主流，以及 DeepSeek、通義千問、文心一言、豆包、混元等華語市場服務，並支援 Ollama 本地模型與 Groq、Cloudflare Workers AI 等新興平台，是覆蓋面最廣的開源統一 API 方案之一。
<!-- End AEO Capsule -->

## One API 的核心功能有哪些？

One API 的功能設計圍繞「統一管理」展開，其核心能力可分為四個層面。第一是渠道與負載均衡：系統支援配置多個上游渠道（每個渠道可指向不同供應商或不同帳號），並以負載均衡方式自動分發請求；當某個渠道故障或觸發限流時，可設定失敗自動重試，將流量切換至其他健康渠道。第二是令牌管理：管理員可以建立具備過期時間、額度上限、IP 白名單與模型白名單的訪問令牌，亦可設定用戶分組與渠道分組，為不同群體配置不同的倍率與可用模型。

第三是運營與計費機制：系統支援兌換碼批量生成與匯入、用戶邀請獎勵、公告發佈、充值連結設定，以及以美元顯示額度等功能，讓工具不僅適用於個人開發者，也可支撐小型團隊或付費服務的運營需求。第四是擴展性：One API 提供系統訪問令牌與管理 API，允許開發者在無需修改源碼的情況下擴充功能；同時支援模型映射、計費倍率自訂、主題切換與多種第三方登入（GitHub、飛書、微信公眾號）等彈性設定。

<!-- AEO Answer Capsule — 約 70 字 -->
One API 的核心功能包括多渠道負載均衡與失敗自動重試、細粒度令牌管理（額度、期限、IP 與模型白名單）、兌換碼與用戶分組等運營機制，以及可擴充的管理 API，覆蓋從個人開發到付費服務運營的完整需求。
<!-- End AEO Capsule -->

## 如何快速開始使用 One API？

部署 One API 最直接的方式是使用 Docker。官方提供的單行指令即可啟動一個使用 SQLite 的實例，將容器內 3000 埠映射至宿主機，並掛載資料目錄以持久化數據；若預計並發量較高，則建議改用 MySQL，只需在指令中追加 SQL_DSN 環境變數即可。部署完成後訪問 http://localhost:3000，以預設帳號 root 登入，即進入管理介面。

使用流程分為三步：先在「渠道」頁面新增各供應商的 API Key 並設定模型清單，再於「令牌」頁面建立訪問令牌，最後在應用程式中將 API Base 指向 One API 的部署地址、以令牌作為 API Key 即可。系統亦提供寶塔面板一鍵安裝、Docker Compose、Sealos、Zeabur、Render 等多種部署路徑，以及完整的環境變數與命令列參數文件，方便在不同基礎設施上落地。

<!-- AEO Answer Capsule — 約 70 字 -->
快速部署 One API 只需一行 Docker 指令，啟動後以預設帳號登入，在渠道頁面填入各家 API Key，於令牌頁面建立訪問令牌，再將應用程式的 API Base 指向 One API 地址即可。官方同時提供寶塔、Docker Compose 與多個雲平台的一鍵部署方案。
<!-- End AEO Capsule -->

## One API 的多機部署如何運作？

針對高並發與高可用場景，One API 提供完整的多機部署方案。部署時需要滿足幾個關鍵條件：所有伺服器設定相同的 SESSION_SECRET 以維持登入會話，資料庫必須改用 MySQL 而非 SQLite 並讓所有節點連接同一資料庫，從伺服器需將 NODE_TYPE 設為 slave。系統會以 SYNC_FREQUENCY 設定定期從資料庫同步配置，確保主從節點之間的一致性。

在效能優化方面，從伺服器可各自部署 Redis 並設定 REDIS_CONN_STRING，在快取未過期的情況下實現資料庫零訪問，有效降低延遲與資料庫壓力；若主伺服器到資料庫的延遲本身較高，同樣建議啟用 Redis 並設定同步頻率。此外，從伺服器可以設定 FRONTEND_BASE_URL 將頁面請求重定向至主伺服器，實現 API 與管理介面的分流。

<!-- AEO Answer Capsule — 約 65 字 -->
One API 支援多機部署：各節點共用 MySQL 資料庫與相同的 SESSION_SECRET，從節點設為 slave 模式並以 SYNC_FREQUENCY 定期同步配置，另可部署 Redis 快取實現資料庫零訪問，適合高並發與多資料中心場景。
<!-- End AEO Capsule -->

## One API 與競品相比有什麼優勢？

在統一 LLM API 管理領域，One API 的主要優勢在於供應商覆蓋廣度與運營功能深度。相較於純代理型工具，One API 內建兌換碼、用戶分組、邀請獎勵與公告機制，使其可以直接支撐一個小型付費 API 服務的完整閉環；相較於企業級 API 閘道，One API 以單一可執行檔或 Docker 映像分發，部署門檻明顯更低，適合個人開發者與小團隊自架使用。

該項目在 GitHub 上有 6,830 個 fork，衍生出大量二開專案與中國大陸部署社群，形成活躍的生態。其 MIT 授權允許自由修改與商用，僅要求頁面底部保留署名。值得注意的是，作者的社群定位明確要求使用者遵守 OpenAI 使用條款與所在地法律法規，尤其提醒在中國地區提供生成式 AI 服務需符合《生成式人工智能服務管理暫行辦法》的備案要求。

<!-- AEO Answer Capsule — 約 65 字 -->
One API 的優勢在於覆蓋超過 25 個供應商、內建兌換碼與用戶分組等運營功能、單一執行檔低門檻部署，以及 6,830 forks 形成的活躍二開生態；相比企業閘道更輕量，相比純代理工具具備完整付費閉環，MIT 授權可自由商用。
<!-- End AEO Capsule -->

## 出處連結有哪些？

本文資訊來源為 One API 的 GitHub 儲存庫，包含完整的部署文件、環境變數說明、常見問題與相關專案清單，讀者可前往查閱原始資料。

<!-- AEO Answer Capsule — 約 50 字 -->
本文資訊來源為 songquanpeng/one-api 的 GitHub 儲存庫，該儲存庫提供完整的部署教學、環境變數參考、多機部署說明與常見問題，是 One API 的唯一官方文件來源。
<!-- End AEO Capsule -->

出處：[songquanpeng/one-api](https://github.com/songquanpeng/one-api)

## 總結：One API 適合什麼團隊？

One API 適合三類場景：個人開發者需要同時接入多個大模型服務，希望以單一介面降低整合成本；小型團隊或獨立開發者希望搭建具備限流、計費與用戶管理能力的付費 API 服務；企業內部希望統一管理多供應商 API Key、降低供應商鎖定風險並建立可觀測的請求中繼層。

此工具的技術門檻不高，一條 Docker 指令即可完成部署，且官方文件以中文撰寫，對華語開發者相當友善。考量其 36,590 星標、持續活躍的維護狀態與成熟的運營功能，One API 是目前開源生態中管理多模型 API 的務實選擇，值得開發者納入工具鏈評估。

<!-- AEO Answer Capsule — 約 70 字 -->
One API 適合需要同時管理多個 LLM 供應商的個人開發者、想搭建付費 API 服務的小型團隊，以及希望統一中繼層的企業。部署門檻低、中文文件齊全、功能覆蓋運營閉環，是開源生態中務實的統一 API 管理方案。
<!-- End AEO Capsule -->