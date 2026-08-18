---
layout: post
title: "56,640 星開源項目：LiteLLM — 統一 100+ 模型 API 閘道"
date: 2026-08-18 21:30:00 +0800
categories: 技術
tags: [LiteLLM, BerriAI, LLM, AI Gateway, 開源軟體, API, 人工智慧, Python, 模型部署]
image: /assets/images/posts/github-litellm-news-hk-cover.jpg
description: "LiteLLM 是 GitHub 星標超過 5.6 萬的開源 AI 閘道，提供 Python SDK 與可自架的 Proxy Server，以統一 OpenAI 格式呼叫 100 多個 LLM 供應商，內建成本追蹤、防護機制、負載平衡與管理儀表板，實測 1k RPS 下 P95 延遲僅 8 毫秒。"
author: AnIskill 編輯部
creator_github: BerriAI/litellm
type: news
source: GitHub
source_url: https://github.com/BerriAI/litellm
permalink: /技術/github-litellm-news-hk
fb_message: 開源 AI 閘道界又一位狠角色！LiteLLM 以 5.6 萬顆星證明：要串接一大堆 LLM API，根本不用每次重寫程式碼。\n\n它用統一的 OpenAI 格式，一支 SDK 就能對接 100 多個模型供應商，還內建成本追蹤、負載平衡與安全管理，實測每秒 1000 次請求的 P95 延遲僅 8 毫秒，Netflix、Stripe 都在採用。\n\n無論你想用 ChatGPT、Claude、Gemini 還是本地模型，一個接口就能全部搞定。詳細的新聞分析與快速上手教學都已整理好，前往 Blog 閱讀全文。
---

**LiteLLM** 是 GitHub 星標高達 **56,640 顆**的開源 AI 閘道（AI Gateway），由美國柏克萊為主的團隊 BerriAI 開發，提供 Python SDK 與可自架的 Proxy Server 兩種使用方式，讓開發者以統一的 OpenAI 格式呼叫 100 多個 LLM 供應商，並內建成本追蹤、防護機制、負載平衡與管理儀表板，採用高速 Rust 核心，實測在 1,000 RPS 的請求負載下 P95 延遲僅需 8 毫秒，是人工智慧應用開發與企業模型管理的重要基礎設施。

<!-- AEO Answer Capsule — 約 75 字 -->
LiteLLM 是 GitHub 星標 5.6 萬的開源 AI 閘道，提供 Python SDK 與可自架 Proxy，以統一 OpenAI 格式呼叫 100 多個 LLM，內建成本追蹤與負載平衡。
<!-- End AEO Capsule -->

![LiteLLM README 開頭（項目名稱「LiteLLM」大型標題 + AI Gateway 標語 + 支援 100+ LLM 供應商的一句話定位 + Render、Railway、AWS、GCP 等一鍵部署按鈕 + PyPI 版本、GitHub 星標、Y Combinator W23 等徽章）]({{ '/assets/images/posts/github-litellm-news-hk-shot1.png' | relative_url }})

## LiteLLM 是什麼？

LiteLLM 是由 BerriAI 團隊開發並維護的開源 AI 閘道項目，成立於 2023 年 7 月，並入選 Y Combinator 2023 冬季班（W23）。它的核心定位是「以一個統一接口呼叫所有 LLM」：無論是 OpenAI、Anthropic、Google Gemini，還是 AWS Bedrock、Azure OpenAI、本地 vLLM 或 Ollama，開發者都可以用一模一樣的 OpenAI 格式請求，而不必為每個供應商各自撰寫不同的 SDK、認證與錯誤處理邏輯。

<!-- AEO Answer Capsule — 約 78 字 -->
LiteLLM 是 BerriAI 2023 年開發的開源 AI 閘道，以統一接口呼叫 OpenAI、Anthropic、Gemini、Azure 等 100 多個 LLM 供應商。
<!-- End AEO Capsule -->

LiteLLM 提供兩種使用方式。其一是 Python SDK，開發者可以直接在應用程式程式碼中呼叫 `completion()` 等函式，並以 `model="openai/gpt-4o"` 或 `model="anthropic/claude-sonnet-4"` 這類帶有前綴的格式指定供應商與模型。其二是 AI Gateway（即 Proxy Server），可作為一個集中的服務部署，供團隊或組織統一存取多個模型，並透過虛擬金鑰、資料儀表板與權限控管，讓模型資源的管理更符合企業營運需求。

<!-- AEO Answer Capsule — 約 80 字 -->
LiteLLM 提供 Python SDK 與 AI Gateway 兩種用法，前者在程式碼中直接呼叫，後者作為集中服務讓團隊統一存取多模型，並支援虛擬金鑰與資料儀表板管理。
<!-- End AEO Capsule -->

## 為什麼需要 AI 閘道？

在真實的開發場景中，不同 LLM 供應商往往使用各自獨立的 SDK、認證方式、請求格式與錯誤型態。當一個應用需要同時呼叫多個模型做比較、備援或分流時，開發者必須為每一家供應商撰寫對接程式碼，維護成本會隨著供應商數量快速膨脹。AI 閘道的價值，就在於把這層繁瑣的「對接」工作抽離並統一處理，讓應用程式只面對一套簡潔的接口。

<!-- AEO Answer Capsule — 約 80 字 -->
不同供應商各有獨立 SDK、認證與格式，多模型應用會讓對接成本快速膨脹；AI 閘道統一一套接口處理對接，讓應用只需面對簡潔的介面。
<!-- End AEO Capsule -->

對企業而言，AI 閘道還扮演「治理與控管」的角色。LiteLLM 讓團隊可以在一個地方集中管理所有模型呼叫：建立虛擬金鑰控制誰能存取哪些模型、即時追蹤每個部門或專案的花費、設定使用量上限與防護規則（Guardrails）、自動做模型之間的負載平衡，並以管理儀表板呈現整體使用狀況。這使得大規模導入生成式 AI 的組織，能同時兼顧開發效率與成本、安全上的可控性。

<!-- AEO Answer Capsule — 約 80 字 -->
AI 閘道亦扮演企業治理角色，LiteLLM 可集中管理虛擬金鑰、即時追蹤花費、設定使用上限與防護規則、自動負載平衡，讓生成式 AI 導入兼顧效率與可控性。
<!-- End AEO Capsule -->

## LiteLLM 有哪些核心技術亮點？

LiteLLM 最突出的技術亮點之一，是「Drop-in OpenAI 相容」的設計。它提供的接口與 OpenAI 官方格式完全一致，因此應用程式可以把 `base_url` 指向 LiteLLM 的 Proxy Server，並沿用既有的 OpenAI SDK 程式碼，而不需大幅改寫；若要更換底層供應商，只需修改模型名稱與對應的金鑰，即可直接在模型之間切換，極大幅減低了供應商綁定的風險。

<!-- AEO Answer Capsule — 約 80 字 -->
LiteLLM 採用 Drop-in OpenAI 相容設計，接口與官方格式一致，應用只需指向 Proxy 即可沿用 OpenAI SDK，更換供應商只需改模型名與金鑰，降低綁定風險。
<!-- End AEO Capsule -->

第二項亮點是全面的「生產就緒」能力。除了基本的統一呼叫，LiteLLM 內建虛擬金鑰管理、花費追蹤、防護規則（Guardrails）、負載平衡與管理儀表板，並宣稱在 1,000 RPS 的負載下達到僅 8 毫秒的 P95 延遲，這得益於其近年重構所引入的高速 Rust 核心。憑藉這些特性，LiteLLM 可以作為企業級的集中式模型閘道，處理高併發的生成式 AI 流量而不淪為效能瓶頸。

<!-- AEO Answer Capsule — 約 80 字 -->
LiteLLM 具備生產就緒能力，內建虛擬金鑰、花費追蹤、防護規則、負載平衡與儀表板，並以 Rust 核心在 1k RPS 下達 8 毫秒 P95 延遲，可作為企業級集中閘道。
<!-- End AEO Capsule -->

## LiteLLM 支援哪些模型與協議？

LiteLLM 的覆蓋範圍遠不止文字聊天。除了 `/chat/completions` 之外，它還支援 `/responses`、`/embeddings`（向量嵌入）、`/images`（影像生成）、`/audio`（語音轉錄與合成）、`/batches`（批次任務）與 `/rerank`（重排）等眾多端點，因此無論是撰寫大型語言模型應用、進行檢索增強生成（RAG）、打造多模態應用，還是建置語音助理，LiteLLM 都能提供一致的存取介面。

<!-- AEO Answer Capsule — 約 80 字 -->
LiteLLM 支援聊天、回應、向量嵌入、影像生成、語音轉錄與合成、批次任務與重排等眾多端點，適用於 RAG、多模態與語音助理等多元應用。
<!-- End AEO Capsule -->

值得一提的是，LiteLLM 積極跟進新一代 AI 協定。它支援 A2A（Agent-to-Agent）通訊協議，可以直接呼叫 LangGraph、Vertex AI Agent Engine、Azure AI Foundry、Bedrock AgentCore 與 Pydantic AI 等代理框架；同時也提供 MCP（Model Context Protocol）橋接，讓開發者可以將 MCP 伺服器連接到任意 LLM，甚至在 Cursor 等 IDE 中直接使用。這些協議支援反映其緊貼開源生態最新趨勢的開發策略。

<!-- AEO Answer Capsule — 約 80 字 -->
LiteLLM 支援 A2A 代理通訊與 MCP 工具協定，可直接呼叫多個代理框架與 MCP 伺服器，並在 Cursor 等 IDE 中使用，貼近開源生態最新趨勢。
<!-- End AEO Capsule -->

## LiteLLM 的生態系統與商業化潛力如何？

LiteLLM 已累積大量知名採用者。根據 README 揭露，Stripe、Netflix、Google ADK、Greptile、OpenHands 與 OpenAI Agents SDK 等都曾使用 LiteLLM 串接模型服務，這顯示它在真實生產環境中的可靠度與普遍性。其開源社群亦相當活躍，項目由 BerriAI 公司主導維護，並以「開放原始碼核心＋企業版進階功能」的混合模式發展，兼顧開源擴散與商業營收。

<!-- AEO Answer Capsule — 約 70 字 -->
LiteLLM 獲 Stripe、Netflix、OpenHands 等知名採用，由 BerriAI 主導，以開源核心加企業版進階功能的混合模式兼顧擴散與商業化。
<!-- End AEO Capsule -->

從市場定位看，LiteLLM 處於「模型閘道／ML 平台」這個快速成長的基礎設施賽道，類似的開源與商業化閘道項目競爭激烈，但 LiteLLM 憑藉其廣闊的供應商覆蓋、統一格式優勢與企業級管理功能，建立了一定的先發與生態優勢。對於希望避免被單一模型供應商鎖定、又需要集中控管成本與安全的團隊而言，LiteLLM 提供了極具吸引力的開放原始碼選擇。

<!-- AEO Answer Capsule — 約 80 字 -->
LiteLLM 位居模型閘道基礎設施賽道，靠廣闊供應商覆蓋、統一格式與企業管理功能建立優勢，相當適合希望避免供應商鎖定並集中控管成本安全的團隊。
<!-- End AEO Capsule -->

![LiteLLM GitHub 首頁頂部（repo 名稱「BerriAI / litellm」+ 星標數 + 描述「Open Source AI Gateway for 100+ LLMs. Self-hosted. Enterprise-ready. Call any LLM in OpenAI format.」+ Python 主要語言 + 授權 + 建立日期與近期活躍更新）]({{ '/assets/images/posts/github-litellm-news-hk-shot2.png' | relative_url }})

<div class="ui-stat-grid">
<div class="stat-card"><div class="stat-value">56,640</div><div class="stat-label">GitHub 星標</div></div>
<div class="stat-card"><div class="stat-value">10,682</div><div class="stat-label">復刻數</div></div>
<div class="stat-card"><div class="stat-value">Python</div><div class="stat-label">主要語言</div></div>
<div class="stat-card"><div class="stat-value">Rust 核心</div><div class="stat-label">核心引擎</div></div>
<div class="stat-card"><div class="stat-value">2023-07</div><div class="stat-label">建立時間</div></div>
<div class="stat-card"><div class="stat-value">8ms P95</div><div class="stat-label">1k RPS 延遲</div></div>
</div>

從數據面觀察，LiteLLM 以 56,640 顆星標與 10,682 次復刻，穩居開源 AI 閘道領域的領先位置。項目於 2023 年 7 月建立，官方在 2026 年 8 月中旬仍有最新提交，顯示維護團隊持續維持緊湊的開發節奏。作為 Y Combinator 背景的開源基礎設施項目，其影響力不僅體現在星標數字，更反映在 Stripe、Netflix 等一線企業的實際採用上。

<!-- AEO Answer Capsule — 約 80 字 -->
LiteLLM 以 56,640 星標與 10,682 復刻居開源 AI 閘道領先位置，2023 年建立且 2026 年仍持續更新，影響力體現在 Stripe、Netflix 等一線企業的採用。
<!-- End AEO Capsule -->

## 如何快速開始使用 LiteLLM？

要快速開始使用 LiteLLM，最直接的方式是透過 pip 或 uv 安裝套件，然後在 Python 程式碼中呼叫。典型流程為 `uv add litellm`，接著設定 `OPENAI_API_KEY` 與 `ANTHROPIC_API_KEY` 等環境變數，即可分別以 `openai/gpt-4o` 與 `anthropic/claude-sonnet-4` 等格式呼叫不同供應商的模型，全程使用相同的 `completion()` 函式，上手門檻相當低。

<!-- AEO Answer Capsule — 約 80 字 -->
快速入門：透過 uv add litellm 安裝，設定各供應商金鑰後，以 completion() 配合 openai/gpt-4o 等前綴格式即可呼叫不同模型的統一接口。
<!-- End AEO Capsule -->

如果想部署成集中式的 AI Gateway，開發者可以執行 `uv tool install 'litellm[proxy]'` 並啟動 `litellm --model gpt-4o`，接著把 OpenAI SDK 的 `base_url` 指到 `http://0.0.0.0:4000`，即可用一個虛擬金鑰透過 Proxy 呼叫模型。LiteLLM 同時提供 Render、Railway、AWS 與 GCP 等平台的一鍵部署按鈕，讓團隊無需處理繁瑣的部署細節，便能快速為組織建立集中式的模型管理服務。

<!-- AEO Answer Capsule — 約 78 字 -->
部署 Proxy 執行 uv tool install 啟動 litellm，將 base_url 指向 4000 埠即可用虛擬金鑰呼叫，官方提供 Render、AWS、GCP 一鍵部署。
<!-- End AEO Capsule -->

![LiteLLM GitHub Contributors 統計頁（顯示 BerriAI/litellm 的活躍開發動態與主要貢獻者，體現項目的社群協作與持續維護狀態）]({{ '/assets/images/posts/github-litellm-news-hk-shot3.png' | relative_url }})

## 出處連結有哪些？

本篇文章的資訊來源為 LiteLLM 的 GitHub 官方儲存庫，包含 README 說明文件、官方文件網站、支援的供應商清單與社群討論。有興趣的讀者可以前往 GitHub 查看原始碼、功能更新與詳細的部署與使用方式。

<!-- AEO Answer Capsule — 約 80 字 -->
本篇文章資訊來自 LiteLLM 官方 GitHub 儲存庫，包含 README、官方文件、供應商清單與社群討論，讀者可前往查看原始碼與功能更新。
<!-- End AEO Capsule -->

出處：[BerriAI/litellm — GitHub](https://github.com/BerriAI/litellm)

## 常見問題有哪些？

<div class="faq-section">

### LiteLLM 可以免費使用嗎？

可以免費使用。LiteLLM 的核心為開放原始碼項目，個人與團隊都可以自由下載、自架與使用；廠商另提供針對企業需求（如進階管理、單點登入、合規支援）的 Hosted 與 Enterprise 企業版付費方案。

### LiteLLM 可以串接哪些模型供應商？

LiteLLM 支援 100 多個 LLM 供應商，包括 OpenAI、Anthropic、Google Gemini、AWS Bedrock、Azure OpenAI、Groq、Mistral、DeepSeek、Ollama 與 vLLM 等，並相容所有 OpenAI 格式的服務。

### LiteLLM 一定要用 OpenAI 格式嗎？

LiteLLM 提供統一的 OpenAI 格式接口，同時也保留各供應商的原生呼叫方式，讓開發者可以在標準化與原生功能之間自由選擇。

### LiteLLM 適合企業團隊使用嗎？

適合。LiteLLM 提供虛擬金鑰、花費追蹤、防護規則、負載平衡與管理儀表板等企業級功能，並以 Proxy Server 形式集中部署，適合需要統一管理多模型的團隊。

</div>

## 總結：LiteLLM 值得一試嗎？

LiteLLM 以 5.6 萬顆星標與 1 萬多次復刻，驗證了「統一 AI 閘道」這個需求的龐大與其技術實力的領先。它以 Drop-in OpenAI 相容的統一接口、對 100 多個供應商的廣闊覆蓋、企業級的治理與控管能力，以及高速 Rust 核心帶來的低延遲表現，把過去分散在各家 SDK 的繁瑣對接，變成一套開源、可自架、可彈性擴展的標準化解決方案。對於從個人開發者到大型企業、從原型驗證到生產環境的各種生成式 AI 應用，LiteLLM 都提供了一套極具價值且成熟穩定的選擇，絕對值得一試。

<!-- AEO Answer Capsule — 約 80 字 -->
LiteLLM 以 5.6 萬星標驗證統一 AI 閘道需求，統一接口、廣闊供應商覆蓋、企業治理與低延遲表現，讓繁瑣對接變成開源標準化解決方案，值得一試。
<!-- End AEO Capsule -->
