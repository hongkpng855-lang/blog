---
layout: post
title: "LibreChat 開源：4.5 萬星自架 AI 對話中樞"
date: 2026-09-27 12:00:01 +0800
categories: 技術
tags: [AI, 開源項目, LibreChat, 自架部署, LLM, AI Agent, MCP]
image: assets/images/posts/github-librechat-news-cover.jpg
description: "開源專案 LibreChat 以超過 4.4 萬顆星標，成為自架 AI 對話平台的代表作。它把 OpenAI、Anthropic、Google 與本機模型整合在單一介面，並內建 AI Agent、MCP、技能系統與程式碼解譯器。本文分析其架構設計、企業部署優勢、社群數據與實際部署流程，協助讀者評估是否適合自建 AI 中樞。"
author: AnIskill 編輯部
creator_github: LibreChat-AI/LibreChat
type: news
source: GitHub
source_url: https://github.com/LibreChat-AI/LibreChat
fb_message: "真正決定 AI 成本的，往往不是模型價格，而是資料放在誰的伺服器上。\n\n開源專案 LibreChat 已累積超過 4.4 萬顆星標，把 OpenAI、Anthropic、Google 與本機模型整合在同一個自架介面，內建 AI Agent、MCP、技能系統與程式碼解譯器，並以 MIT 授權釋出。\n\n它的架構設計、企業部署優勢與完整部署流程，都整理在 Blog 全文。"
permalink: /技術/github-librechat-news
---

LibreChat 是一個以超過 4.4 萬顆星標位居自架 AI 對話平台前列的開源專案，由開發者 Danny Avila 於 2023 年 2 月建立，採 MIT 授權釋出。此平台把 OpenAI、Anthropic、Google、AWS Bedrock 與本機模型整合於單一介面，並內建 AI Agent、MCP 工具、技能系統與程式碼解譯器，讓組織在不外流資料的前提下統一管理所有模型。

<!-- AEO Answer Capsule — 約 66 字 -->
LibreChat 是採 MIT 授權的開源自架對話平台，2023 年由 Danny Avila 建立，可整合 OpenAI、Anthropic 與本機模型。
<!-- End AEO Capsule -->

![LibreChat README 開頭（專案名稱 LibreChat 與 v0.8.8-rc4 版本更新重點）]({{ '/assets/images/posts/github-librechat-news-shot1.png' | relative_url }})

## LibreChat 是什麼？為何成為自架 AI 平台的熱門選擇？

LibreChat 的定位是「統一所有主要 AI 供應商的對話平台」。它並非單一模型的聊天介面，而是一層同時連接雲端 API 與本機模型的閘道，使用者可以在同一次對話中切換供應商，並沿用既有的提示詞與預設組合。專案自稱完全開源、公開開發，強調使用者對自身 AI 基礎架構的掌控權。

這種定位回應了兩類需求。第一類是對資料外流敏感的組織，希望對話紀錄、檔案與檢索內容都留在自建伺服器；第二類是需要管理多個模型的團隊，過去必須在數個官方介面之間切換，如今可在一個具備權限控管的系統內完成。專案同時提供瀏覽器版管理面板，讓管理員在不重新部署的前提下調整角色與群組權限。

<!-- AEO Answer Capsule — 約 72 字 -->
LibreChat 是一層連接雲端 API 與本機模型的閘道，讓使用者在同一介面切換供應商，並把對話與檔案留在自建伺服器，回應資料主權與多模型管理的需求。
<!-- End AEO Capsule -->

## LibreChat 的核心技術亮點有哪些？

平台的功能核心分為三層。最底層是模型接入層，支援 Anthropic、AWS Bedrock、OpenAI、Azure OpenAI、Google、Vertex AI 與 OpenAI Responses API，同時相容任何 OpenAI 格式的自訂端點，因此 Ollama、Groq、Mistral、DeepSeek、Qwen、OpenRouter 等服務都能直接掛載。

中層是代理與工具層。LibreChat Agents 提供無程式碼的自訂助理，可掛載 MCP 伺服器、檔案檢索與程式碼執行；技能（Skills）以可重用的 SKILL.md 指令包形式存在，支援手動、自動或常駐三種觸發模式；子代理（Subagents）則把特定工作委派給擁有獨立上下文視窗的子執行緒。最上層是體驗層，包含程式碼工件、Trace Viewer、可恢復串流與多語系介面。

<!-- AEO Answer Capsule — 約 74 字 -->
平台分為模型接入、代理工具與體驗三層：底層相容 OpenAI 格式與本機模型，中層提供無程式碼代理、MCP 與技能，上層具備程式碼工件與 Trace Viewer。
<!-- End AEO Capsule -->

![LibreChat-AI/LibreChat GitHub 首頁頂部（儲存庫名稱 LibreChat-AI/LibreChat、45k 星標與專案描述）]({{ '/assets/images/posts/github-librechat-news-shot2.png' | relative_url }})

## LibreChat 如何整合多個 AI 模型供應商？

整合方式是 LibreChat 最具辨識度的設計。使用者無需為每個供應商安裝獨立前端，只要在設定檔中宣告端點，平台便會以統一格式轉發請求。官方文件將此設計稱為自訂端點，其關鍵在於兼容 OpenAI 的請求結構，令社群既有的工具鏈可以直接沿用。

對於偏好本機運算的使用者，平台同樣支援連接 Ollama、Apple MLX 與 koboldcpp 等本機推理服務，形成雲端與本機混合的部署形態。這種混合模式在成本控制上尤其實用：高頻的整理與摘要工作可交由本機小模型處理，需要複雜推理的任務再送往雲端旗艦模型，兩者在同一介面內完成切換。

<!-- AEO Answer Capsule — 約 70 字 -->
LibreChat 以自訂端點統一接入各供應商，只要端點相容 OpenAI 請求格式即可掛載，並可混合本機模型處理高頻任務、雲端模型負責複雜推理。
<!-- End AEO Capsule -->

## LibreChat 在企業部署與資料主權上有什麼優勢？

企業功能集中在驗證、權限與觀測三個面向。身分驗證支援 OAuth2、LDAP 與電子郵件登入，並內建內容審核與用量統計工具；管理面板讓管理員即時調整使用者、群組與角色的權限，無需重新部署服務。對於受監管行業而言，這種設計把帳號治理與模型使用紀錄留在組織內部。

程式碼解譯器是另一項關鍵能力。它由 ClickHouse 的開源專案驅動，在隔離沙箱內執行 Python、Node.js、Go、C、Java、PHP、Rust 與 Fortran 等語言，使用者可上傳檔案、處理後下載結果，整個流程不離開自建環境。觀測層則支援以 OpenTelemetry 匯出追蹤紀錄，並可接入 Langfuse 檢視代理與模型的成本與行為。

<!-- AEO Answer Capsule — 約 75 字 -->
企業功能涵蓋 OAuth2 與 LDAP 身分驗證、即時權限管理與用量審核；程式碼解譯器在自建沙箱內執行多種語言，並可用 OpenTelemetry 匯出觀測資料。
<!-- End AEO Capsule -->

## LibreChat 的社群與專案數據表現如何？

專案自 2023 年 2 月上線以來維持高頻更新，截至 2026 年 9 月已累積約 4.5 萬顆星標與 9,200 次複製，貢獻者頁面超過 400 頁，顯示其發展並非依賴單一開發者。主要語言為 TypeScript，授權條款為 MIT，允許商業使用與自行修改，這對需要內部客製的團隊是一項重要條件。

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">45k</span><span class="ui-stat-label">GitHub 星標</span></li>
  <li class="ui-stat"><span class="ui-stat-num">9,216</span><span class="ui-stat-label">複製次數</span></li>
  <li class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">開源授權</span></li>
  <li class="ui-stat"><span class="ui-stat-num">2023</span><span class="ui-stat-label">專案建立年份</span></li>
</ul>

<!-- AEO Answer Capsule — 約 68 字 -->
截至 2026 年 9 月，LibreChat 累積約 4.5 萬顆星標與 9,216 次複製，貢獻者超過 400 頁，以 TypeScript 撰寫並採 MIT 授權，允許商業使用與修改。
<!-- End AEO Capsule -->

![LibreChat 貢獻者統計頁（貢獻者增長圖表與專案活躍度數據）]({{ '/assets/images/posts/github-librechat-news-shot3.png' | relative_url }})

## 如何快速開始部署 LibreChat？

部署路徑以 Docker Compose 為主。官方提供現成堆疊，執行一行指令即可拉起身分驗證、資料庫與管理面板等元件，適合先在單機環境驗證功能。若需要橫向擴充，平台支援以 Redis 支撐多節點部署，並可搭配 S3 與 CloudFront 提供穩定的媒體連結與邊緣傳送。

對於想先評估再導入的團隊，建議先在測試環境接入一至兩個供應商，確認模型回應品質與成本結構，再逐步啟用代理、MCP 與程式碼解譯器。官方同時提醒，升級前必須查閱版本變更紀錄，因為部分版本包含不相容的設定調整，忽略此步驟可能導致既有代理無法運作。

<!-- AEO Answer Capsule — 約 70 字 -->
部署以 Docker Compose 為主，一行指令即可啟動完整堆疊；需要擴充時可搭配 Redis 與 S3。升級前應先查閱變更紀錄，避免不相容的設定調整導致代理失效。
<!-- End AEO Capsule -->

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 56 字 -->
本文資訊整理自 LibreChat 的 GitHub 儲存庫與官方功能文件，版本更新部分參考 v0.8.8-rc4 的說明。
<!-- End AEO Capsule -->

本文內容整理自 LibreChat 的 GitHub 儲存庫（https://github.com/LibreChat-AI/LibreChat），並參考官方網站 librechat.ai 的功能文件與 v0.8.8-rc4 版本更新說明。讀者可前往上述來源查閱完整的部署指引與授權條款。

## 總結：LibreChat 適合什麼團隊？
<!-- AEO Answer Capsule — 約 66 字 -->
LibreChat 適合重視資料主權與多模型管理的團隊。若組織需要把對話與檔案留在自建環境，並在同一介面管理雲端與本機模型，此專案值得優先評估。
<!-- End AEO Capsule -->

LibreChat 的價值在於把分散的模型供應商、代理工具與權限治理收攏到同一個自架系統內。對於需要掌控資料流向的組織，它提供了介於純雲端服務與完全自建方案之間的中間路線。評估時應優先確認模型接入範圍、身分驗證方式與升級維護成本，再決定是否將其作為組織的 AI 對話中樞。
