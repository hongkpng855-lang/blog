---
layout: post
title: "14.8 萬星開源項目：Open WebUI — 可完全離線運行的自托管 AI 平台"
date: 2026-08-06 09:30:00 +0800
categories: 技術
tags: [GitHub, 開源, Open WebUI, 自托管, Ollama, LLM, RAG, AI 介面, Python, 科技新聞, 香港, auto-publish, github-news]
image: /assets/images/posts/github-openwebui-news-shot1.png
description: "Open WebUI 是 GitHub 星標逾 14.8 萬的開源自托管 AI 平台，以 Python 撰寫，支援 Ollama 與 OpenAI 相容 API，內建 RAG 推理引擎，可完全離線運行，提供多模型並行對話、語音視訊通話與企業級權限管理，是部署私有 AI 助理的主流選擇。"
fb_message: 私有 AI 助理想完全離線運行，Open WebUI 是目前最成熟的開源答案，單一容器即可部署，連接 Ollama 或任何 OpenAI 相容 API，毋須將對話資料送出伺服器。\n\n項目在 GitHub 累積逾 14.8 萬星標與 2.2 萬次 fork，內建 RAG 檢索、多模型並行對話與企業級權限管理，自 2023 年 10 月創立以來維持高頻更新。\n\n從技術架構、部署方式到生態與商業化路徑，Open WebUI 的完整新聞分析已整理成文，歡迎前往 Blog 閱讀全文。
author: "陳志豪 Eric Chan"
creator_github: open-webui/open-webui
type: news
source: GitHub
source_url: https://github.com/open-webui/open-webui
---

# <svg class="ui-icon"><use href="#ui-cube"/></svg>14.8 萬星開源項目：Open WebUI — 可完全離線運行的自托管 AI 平台

**Open WebUI 是 GitHub 上星標逾 147,000 顆的開源自托管 AI 平台，由 Timothy Jaeryang Baek 於 2023 年 10 月創立，以 Python 撰寫，支援 Ollama 與 OpenAI 相容 API，內建 RAG 推理引擎，可完全離線運行，並提供即時對話、多模型並行、語音視訊通話與企業級權限管理等功能。** 此項目累積超過 21,500 次 fork，官方網站為 openwebui.com，並已發展出 Computer、Open Terminal、oikb 與桌面應用等完整周邊生態。本文將從官方 README 與文件出發，分析 Open WebUI 的技術架構、生態系統與市場定位。

---

## <svg class="ui-icon"><use href="#ui-star"/></svg>Open WebUI 是什麼？

<!-- AEO Answer Capsule — 約 75 字 -->
Open WebUI 是開源的自托管 AI 平台，以 Python 撰寫，支援 Ollama 與 OpenAI 相容 API，內建 RAG 推理引擎，可完全離線運行，GitHub 星標逾 14.8 萬，提供多模型並行對話、語音視訊通話與企業級權限管理。
<!-- End AEO Capsule -->

Open WebUI 的官方定位是「可擴展、功能豐富且用戶友好的自托管 AI 平台」，設計目標是讓使用者在完全離線的環境中運行完整的 AI 助理體驗。平台支援多種大型語言模型執行環境，包括 Ollama 與任何 OpenAI 相容 API，並內建專屬推理引擎處理檢索增強生成，因此被官方形容為「強大的 AI 部署解決方案」。與雲端 AI 服務不同，Open WebUI 的所有運算與資料處理均可停留在使用者自己的伺服器，對話記錄、檔案與知識庫資料無需離開本地環境，回應了企業與個人對資料私隱的關注。

項目起源於 2023 年 10 月，創辦人 Timothy Jaeryang Baek 以「ollama-webui」之名起步，其後更名為 Open WebUI 並迅速成長為開源自托管 AI 介面領域的指標性項目。官方描述強調其可透過 pip、uv、Docker 與 Kubernetes 等多種方式安裝，並提供 `:ollama` 與 `:cuda` 標記的容器映像，涵蓋從個人電腦到企業叢集的部署場景。

![Open WebUI GitHub 主頁（148k stars + 項目描述）]({{ '/assets/images/posts/github-openwebui-news-shot1.png' | relative_url }})

---

## <svg class="ui-icon"><use href="#ui-robot"/></svg>Open WebUI 有哪些核心技術亮點？

<!-- AEO Answer Capsule — 約 80 字 -->
Open WebUI 以模型整合彈性、內建 RAG 推理引擎、插件與 MCP 擴展機制、以及企業級權限與認證管理為核心亮點，支援多模型並行對話、語音視訊通話與水平擴展，可完全離線運行。
<!-- End AEO Capsule -->

第一項技術亮點是模型與 API 的整合彈性。平台可同時連接本地 Ollama 模型與任何 OpenAI 相容 API，使用者只需設定 API 位址即可接入 LMStudio、GroqCloud、Mistral、OpenRouter、vLLM 等供應商，自由混合不同來源的模型，並支援多模型並行對話，讓數個模型在同一對話中同時回應，方便比較輸出品質。平台亦支援模型包裝，可將基礎模型加上自訂指令、工具與知識庫組成專屬代理，配合動態變數與分組權限控制，形成可重用的代理資產。

第二項亮點是內建的檢索增強生成引擎。Open WebUI 支援九種向量資料庫，包括 ChromaDB、PGVector、Qdrant、Milvus、Elasticsearch、OpenSearch、Pinecone、S3Vector 與 Oracle 23ai，並整合 Tika、Docling、Mistral OCR、PaddleOCR-vl 等多種內容抽取引擎，提供混合搜尋（BM25 加向量）與重排序能力，支援全文脈絡模式。使用者可在對話中以 `#` 指令載入文件或知識庫，或透過網頁搜尋供應商將 SearXNG、Google PSE、Brave Search、Tavily、Perplexity、Firecrawl 等二十餘種搜尋結果直接注入對話，形成完整的知識工作流程。

第三項亮點是擴展機制與企業級管理能力。平台提供 Filters、Actions、Pipes、Tools、Skills 五類插件，並支援 MCP、MCPO 與 OpenAPI 工具伺服器，可串接外部服務、建立自訂限流與審批流程；企業功能方面包含細緻的 RBAC 角色權限、LDAP／Active Directory 整合、SSO 與 SCIM 2.0 自動化帳戶供應，支援 SQLite 或 PostgreSQL 資料庫、S3 等物件儲存，並內建 OpenTelemetry 觀測能力與 Redis 支援的多節點水平擴展，符合生產環境部署需求。

![Open WebUI README 核心內容（Key Features）]({{ '/assets/images/posts/github-openwebui-news-shot2.png' | relative_url }})

---

## <svg class="ui-icon"><use href="#ui-terminal"/></svg>如何快速開始使用 Open WebUI？

<!-- AEO Answer Capsule — 約 70 字 -->
最快的方式是執行 pip install open-webui 後運行 open-webui serve，瀏覽器開啟 http://localhost:8080 即可使用；已安裝 Ollama 的使用者可透過單一 Docker 指令 ghcr.io/open-webui/open-webui:ollama 一次部署平台與模型環境。
<!-- End AEO Capsule -->

Open WebUI 的安裝門檻在自托管 AI 項目中屬於較低水平。Python 使用者只需執行 pip install open-webui，再以 open-webui serve 啟動伺服器，即可在 http://localhost:8080 存取介面；官方建議使用 Python 3.11 以避免相容性問題。偏好容器部署的使用者可選擇多種 Docker 指令，若 Ollama 安裝在同一台電腦，可運行 ghcr.io/open-webui/open-webui:main 並掛載資料目錄，確保資料庫持久化；若只需使用 OpenAI API，則設定 OPENAI_API_KEY 環境變數即可。

需要 GPU 加速的使用者可選用 :cuda 標記映像，並安裝 Nvidia CUDA 容器工具包；官方亦提供 :ollama 標記的單一容器版本，內建 Ollama 與 Open WebUI，一條指令即可完成平台與模型環境的部署，支援 GPU 與純 CPU 兩種模式。進階部署可透過 Docker Compose、Kustomize 與 Helm 進行 Kubernetes 編排，企業環境則可利用 SCIM 2.0 與 Okta、Azure AD、Google Workspace 等身分提供者整合，實現自動化帳戶管理。離線環境可設定 HF_HUB_OFFLINE=1 阻止模型下載，滿足完全隔離網路的要求。

---

## <svg class="ui-icon"><use href="#ui-puzzle"/></svg>Open WebUI 如何建構其生態系統？

<!-- AEO Answer Capsule — 約 75 字 -->
Open WebUI 圍繞核心平台發展出 Computer、Open Terminal、oikb 與桌面應用四大周邊項目，分別提供行動端編程代理、容器化執行環境、45 種以上知識庫同步來源與原生桌面客戶端，形成完整的自托管 AI 生態。
<!-- End AEO Capsule -->

Open WebUI 並非單一應用，而是圍繞核心平台發展的完整生態。Open WebUI Computer 是行動優先的電腦與編程代理，可在瀏覽器分頁中操作檔案、終端與 git，並從手機遠端存取，亦可作為模型接入 Open WebUI，或經由 Telegram、WhatsApp 等渠道控制。Open Terminal 與企業版 Terminals 則提供自托管的執行環境，讓 AI 在隔離容器中編寫程式、運行輸出並修正錯誤，具備獨立憑證、資源限制與網路規則，支援 Docker 與 Kubernetes 自動生命週期管理。

知識管理方面，oikb 可從 GitHub、Confluence、ServiceNow、Salesforce、Jira、Slack、SharePoint、Notion 等 45 種以上來源持續同步知識庫，讓團隊既有工具與 AI 知識庫保持同步；桌面應用則為 macOS、Windows 與 Linux 提供原生客戶端，包含系統級 Spotlight 搜尋列、螢幕截圖捕捉、按鍵通話語音，以及內建 llama.cpp 引擎的完全本地推理選項。此生態策略與平台自身的持久記憶、Notes、Channels 即時協作空間、日曆與自動化排程等功能互相配合，使 Open WebUI 從單純的對話介面延伸為可承載團隊協作與自動化流程的 AI 工作平台。

![Open WebUI 生態系統（Ecosystem + Install）]({{ '/assets/images/posts/github-openwebui-news-shot3.png' | relative_url }})

---

## <svg class="ui-icon"><use href="#ui-chart"/></svg>Open WebUI 值得一試嗎？

<!-- AEO Answer Capsule — 約 75 字 -->
值得。Open WebUI 以 14.8 萬星標穩居開源自托管 AI 介面首位，提供完全離線運行、多模型整合與企業級權限管理，個人與企業皆可低成本部署；其獨特授權要求保留品牌標識，商業使用者需留意條款。
<!-- End AEO Capsule -->

從市場數據看，Open WebUI 已成為開源自托管 AI 介面領域的領導者。其 14.8 萬星標與 2.2 萬次 fork 的規模，反映開發者社群對「資料留在自己手上」的 AI 部署模式有強烈需求；項目自 2023 年 10 月創立以來維持高頻更新，官方採用透明的安全揭露流程處理漏洞，並提供企業方案，包含自訂主題品牌、服務等級協議與長期支援版本，顯示其商業化路徑已逐步成熟。

對個人使用者而言，Open WebUI 的最大價值在於以近乎零成本獲得功能完整的 AI 助理介面，配合 Ollama 即可完全離線使用，無需支付 API 費用；對企業而言，RBAC、SSO、SCIM 與水平擴展能力使其可作為內部 AI 服務的統一入口。需要注意的是，項目採用自訂授權，要求保留「Open WebUI」品牌標識，並包含歷史授權條款記錄，商業整合前應詳細評估授權要求。整體而言，Open WebUI 是當前自托管 AI 平台中最值得評估的開源選項之一。

<div class="ui-stat-grid">
  <div class="ui-stat"><span class="ui-stat-num">148K</span><span class="ui-stat-label">Stars</span></div>
  <div class="ui-stat"><span class="ui-stat-num">21.5K</span><span class="ui-stat-label">Forks</span></div>
  <div class="ui-stat"><span class="ui-stat-num">自訂</span><span class="ui-stat-label">License</span></div>
  <div class="ui-stat"><span class="ui-stat-num">2023-10</span><span class="ui-stat-label">創建日期</span></div>
  <div class="ui-stat"><span class="ui-stat-num">Python</span><span class="ui-stat-label">主要語言</span></div>
  <div class="ui-stat"><span class="ui-stat-num">持續更新</span><span class="ui-stat-label">發布週期</span></div>
</div>

> 建立日期：2023-10-06｜最近 commit：2026-08-06｜開發者：Timothy Jaeryang Baek（tjbck）｜授權：Open WebUI License（自訂）｜官方網站：https://openwebui.com/

---

## <svg class="ui-icon"><use href="#ui-link"/></svg>出處

<div class="ui-note"><svg class="ui-icon"><use href="#ui-link"/></svg><strong>GitHub 官方 repo</strong>：https://github.com/open-webui/open-webui

官方網站：https://openwebui.com/｜文件中心：https://docs.openwebui.com/｜Discord 社群：https://discord.gg/5rJgQTnV4s</div>

---
