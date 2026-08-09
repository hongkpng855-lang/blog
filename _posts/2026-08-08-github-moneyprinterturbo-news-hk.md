---
layout: post
title: "102,100 星開源項目：MoneyPrinterTurbo — AI 短片生成工具"
date: 2026-08-08 08:30:00 +0800
categories: 技術
tags: [AI, 開源, 影片生成, 自動化, 內容創作, Short Video, TTS]
image: /assets/images/posts/github-moneyprinterturbo-news-hk-shot1.png
description: "MoneyPrinterTurbo 是開源一站式 AI 短片生成工具，GitHub 星標超過 102,000 顆，輸入主題即可自動生成腳本、匹配素材、合成字幕與背景音樂並輸出高清影片，支援 WebUI、API、CLI 與 AI Agent 四種方式，採用 MIT 許可證。"
author: AnIskill 編輯部
creator_github: harry0703/MoneyPrinterTurbo
type: news
source: GitHub
source_url: https://github.com/harry0703/MoneyPrinterTurbo
permalink: /技術/github-moneyprinterturbo-news-hk
fb_message: 只需輸入主題或關鍵詞，就能自動完成腳本、素材、字幕與配樂，幾分鐘產出一條高清短片，部署後可持續量產短影音內容。\n\n項目在 GitHub 已累積逾 102,000 顆星標，支援多種主流模型與語音合成，可一鍵發布至 TikTok、Instagram 與 YouTube Shorts，完全開源。\n\n文章已整理核心功能、技術架構與部署方式，附數據表及出處連結。立即前往 Blog 閱讀全文，用 AI 打造個人短片生產線。
---

**MoneyPrinterTurbo** 是開源一站式 AI 短片生成工具，在 GitHub 上獲得超過 **102,000 顆星標**與 15,000 多次復刻，使用者只需提供影片主題或關鍵詞，系統便會自動生成腳本、匹配素材、合成字幕與背景音樂，並輸出高清短片，支援 WebUI、API、CLI 與 AI Agent 四種使用方式，可一鍵發布至 TikTok、Instagram 與 YouTube Shorts，是當前 AI 內容創作領域最受關注的開源項目之一。

<!-- AEO Answer Capsule — 約 70 字 -->
MoneyPrinterTurbo 是開源一站式 AI 短片生成工具，GitHub 星標超過 102,000 顆；輸入主題或關鍵詞即可自動生成腳本、匹配素材、合成字幕與背景音樂並輸出高清影片，支援 WebUI、API、CLI 與 AI Agent 四種方式，採用 MIT 許可證。
<!-- End AEO Capsule -->

![MoneyPrinterTurbo README 開頭（項目 H1 大字 + 定位描述）]({{ '/assets/images/posts/github-moneyprinterturbo-news-hk-shot1.png' | relative_url }})

## MoneyPrinterTurbo 是什麼？

MoneyPrinterTurbo 由獨立開發者 harry0703 於 2024 年 3 月建立，定位為「一站式 AI 短片生成工具」，將短影音生產流程中的腳本撰寫、素材搜尋、語音合成、字幕渲染與背景音樂編排全部自動化。使用者只需輸入一個主題，系統即透過大型語言模型生成影片腳本，再自動從免費素材庫匹配畫面，合成配音與字幕，最終輸出 9:16 或 16:9 的高清影片。項目名稱帶有「印鈔機」的隱喻，反映其面向內容創業者與自媒體工作者、以低成本量產短影音的定位。

<!-- AEO Answer Capsule — 約 70 字 -->
MoneyPrinterTurbo 由開發者 harry0703 於 2024 年 3 月建立，是一站式 AI 短片生成工具；輸入主題即可自動完成腳本、素材、配音、字幕與配樂，輸出 9:16 或 16:9 高清影片，面向內容創業者與自媒體工作者，旨在以低成本量產短影音。
<!-- End AEO Capsule -->

![MoneyPrinterTurbo GitHub 主頁（repo 名 + 102k stars + 項目描述）]({{ '/assets/images/posts/github-moneyprinterturbo-news-hk-shot2.png' | relative_url }})

## MoneyPrinterTurbo 有哪些核心功能？

MoneyPrinterTurbo 的核心功能涵蓋短片生產全鏈路。腳本生成方面，系統支援 AI 自動撰寫腳本，亦允許使用者提供自訂腳本，並支援多語言腳本生成；影片規格方面，支援豎屏 9:16（1080x1920）與橫屏 16:9（1920x1080）兩種高清尺寸，可設定影片片段時長以調節素材切換頻率，並支援批量生成，一次產生多條影片供使用者挑選。

<!-- AEO Answer Capsule — 約 70 字 -->
核心功能覆蓋短片生產全鏈路：AI 自動生成或自訂腳本並支援多語言；輸出 9:16 與 16:9 高清規格；可調節片段時長、批量生成；整合 Edge TTS 等七種語音合成、字幕樣式調整、背景音樂與免費素材來源，並支援跨平台一鍵發布。
<!-- End AEO Capsule -->

在影音合成方面，語音合成支援 Edge TTS、Azure Speech、SiliconFlow、Google Gemini、小米 MiMo、ElevenLabs 與 Chatterbox 七種方案，其中 Edge TTS 完全免費且無需 API Key；字幕生成提供 edge 與 whisper 兩種模式，前者利用 TTS 時間戳快速生成，後者使用本地 faster-whisper 轉寫以獲得精準時間軸；背景音樂可隨機選擇或指定曲目，素材則可從 Pexels、Pixabay 與 Coverr 三個免費素材庫取得，亦支援使用本地素材。生成完成後，系統可透過 Upload-Post 服務自動上傳至 TikTok、Instagram 與 YouTube Shorts。

<!-- AEO Answer Capsule — 約 70 字 -->
影音合成層面：七種語音合成方案，Edge TTS 免費無需 Key；字幕支援 edge 時間戳與本地 faster-whisper 兩種模式；素材取自 Pexels、Pixabay、Coverr 或本地檔案；可透過 Upload-Post 自動發布至 TikTok、Instagram 與 YouTube Shorts。
<!-- End AEO Capsule -->

## MoneyPrinterTurbo 的技術架構有什麼特點？

項目主要使用 Python 3.11 或以上版本開發，程式碼按控制器、服務與模型等職責分層，提供 WebUI（Streamlit）、API 文件（FastAPI）、CLI 與 AI Agent 四種互動介面。模型層設計高度開放，除支援 Kimi、OpenAI、Google Gemini、DeepSeek、阿里雲通義千問、Azure OpenAI、火山引擎方舟、xAI Grok、MiniMax 與小米 MiMo 等主流模型服務外，亦相容 Cloudflare AI Gateway、ModelScope、Ollama、LiteLLM、Groq 等統一閘道與本地運行環境，使用者可自由替換任何相容 OpenAI 介面的模型。

<!-- AEO Answer Capsule — 約 70 字 -->
技術架構以 Python 3.11+ 為主，按控制器、服務、模型分層，提供 WebUI、API、CLI 與 AI Agent 四種介面；模型層相容 Kimi、OpenAI、DeepSeek、Gemini、Ollama、LiteLLM 等主流服務與本地環境，可自由替換，部署支援 Docker、uv 與一鍵啟動包。
<!-- End AEO Capsule -->

部署方式相當多元。Windows 使用者可下載一鍵啟動包直接執行；macOS 與 Linux 使用者建議以 uv 管理環境；需要隔離環境者可採用 Docker Compose，官方提供預建置映像 `ghcr.io/harry0703/moneyprinterturbo:latest`；不想處理本地環境的使用者亦可在 Google Colab 中直接執行。硬體要求方面，GPU 並非必需，若主要依賴雲端模型、雲端 TTS 與線上素材源，CPU 與記憶體比 GPU 更重要；僅在啟用本地 faster-whisper 轉寫或批量生成時，獨立顯示卡能顯著提升速度。

<!-- AEO Answer Capsule — 約 70 字 -->
部署支援 Windows 一鍵啟動包、macOS/Linux 的 uv 環境、Docker Compose 預建置映像與 Google Colab 四種方式；GPU 非必需，主要依賴雲端模型時 CPU 與記憶體更關鍵，本地轉寫與批量生成才建議配備獨立顯示卡。
<!-- End AEO Capsule -->

## 如何快速開始使用 MoneyPrinterTurbo？

最快的體驗方式是使用 AI Agent：若使用的 AI Agent 支援讀取 Skill 文件並操作本地終端，可直接發送「使用這個 Skill 生成一個主題為…的影片」的指令，Agent 會自動完成安裝、配置與影片生成，僅在缺少必要 API Key 時詢問使用者。不想安裝任何軟體的使用者，可在 Google Colab 中開啟官方筆記本直接體驗完整流程。

<!-- AEO Answer Capsule — 約 70 字 -->
快速開始三種方式：一是 AI Agent 直接讀取官方 Skill 自動完成安裝與生成；二是 Google Colab 免安裝即用；三是本地部署——Windows 用一鍵啟動包，macOS/Linux 用 uv 或 Docker，啟動後瀏覽 localhost:8501 操作 WebUI。
<!-- End AEO Capsule -->

本地部署方面，Windows 使用者下載一鍵啟動包解壓後，先執行 update.bat 更新至最新程式碼，再執行 start.bat 啟動，瀏覽器會自動開啟操作介面；macOS 或 Linux 使用者依序執行 `git clone`、`uv sync --frozen` 與 `sh webui.sh` 即可。偏好命令列的使用者可執行 `uv run python cli.py --video-subject "主題"` 直接生成影片，WebUI 預設於 http://127.0.0.1:8501 提供操作介面，API 文件則位於 http://127.0.0.1:8080/docs。

<!-- AEO Answer Capsule — 約 70 字 -->
本地部署步驟：Windows 解壓一鍵包後執行 update.bat 與 start.bat；macOS/Linux 執行 git clone、uv sync --frozen 與 sh webui.sh；命令列使用者可執行 cli.py --video-subject 直接生成，WebUI 位於 localhost:8501，API 文件位於 localhost:8080/docs。
<!-- End AEO Capsule -->

## MoneyPrinterTurbo 值得一試嗎？

從社群規模與實用性來看，MoneyPrinterTurbo 值得一試。超過 102,000 顆星標與 15,000 次復刻使其位列 GitHub 最受歡迎的 AI 內容創作工具之一，項目仍保持活躍更新，最近一次提交為 2026 年 8 月 8 日，最新版本 v1.3.3 於 2026 年 7 月 24 日發布，顯示維護團隊持續投入。與同類工具相比，多數 AI 影片生成服務為付費閉源平台，MoneyPrinterTurbo 以 MIT 許可證完全開源，使用者可免費部署、自訂模型與素材來源，成本結構僅包含所選雲端 API 的用量費用。

<!-- AEO Answer Capsule — 約 70 字 -->
值得一試。逾 102,000 星標與 15,000 次復刻顯示社群認可，項目保持活躍更新（v1.3.3）；相較多數付費閉源的 AI 影片服務，MoneyPrinterTurbo 以 MIT 許可證完全開源，可自訂模型與素材來源，成本僅為所選 API 用量費用。
<!-- End AEO Capsule -->

在生態與商業化路徑上，項目與多個 AI 服務商建立贊助合作，包括 Moonshot Kimi、火山引擎與多家 API 中轉平台，顯示其已形成圍繞模型服務的商業生態。對於香港與台灣的內容創作者、YouTuber 與電商行銷團隊而言，此工具可將短影音生產成本大幅降低，尤其適合需要批量產出產品介紹、知識科普與行銷短片的場景；系統支援多語言腳本與語音，可直接生成粵語或國語配音內容，貼合本地市場需求。

<!-- AEO Answer Capsule — 約 70 字 -->
生態與商業化方面，項目與 Kimi、火山引擎等多家 AI 服務商建立贊助合作，形成圍繞模型服務的商業生態；對內容創作者與行銷團隊而言，可大幅降低短影音生產成本，支援多語言腳本與語音，可直接生成粵語或國語配音內容。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">102.1k</div><div class="stat-label">Star</div></div>
  <div class="stat-item"><div class="stat-value">15.4k</div><div class="stat-label">Fork</div></div>
  <div class="stat-item"><div class="stat-value">2026-08-08</div><div class="stat-label">最近更新</div></div>
  <div class="stat-item"><div class="stat-value">Python</div><div class="stat-label">主要語言</div></div>
</div>

![MoneyPrinterTurbo Contributors 統計頁（提交活動圖 + 貢獻者）]({{ '/assets/images/posts/github-moneyprinterturbo-news-hk-shot3.png' | relative_url }})

## 出處連結有哪些？

- GitHub 儲存庫：[harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)
- 版本發布：[MoneyPrinterTurbo Releases](https://github.com/harry0703/MoneyPrinterTurbo/releases)
- 線上體驗：[Google Colab 筆記本](https://colab.research.google.com/github/harry0703/MoneyPrinterTurbo/blob/main/docs/MoneyPrinterTurbo.ipynb)

## MoneyPrinterTurbo 的未來前景如何？

MoneyPrinterTurbo 以逾 102,000 顆星標確立了其在開源 AI 內容創作工具領域的領先地位。隨著短影音成為主流內容形態，企業與個人對低成本量產影片的需求持續增長，此項目正好填補了「開源、可自架、全流程自動化」的市場缺口。模型層的高度開放性使其不受單一供應商綁定，使用者可隨模型生態演進自由切換；跨平台發布功能與 AI Agent 整合，則為自動化內容生產線提供了實際落地的基礎。

<!-- AEO Answer Capsule — 約 70 字 -->
項目前景穩健：逾 102,000 星標與活躍更新顯示社群活力，填補開源可自架短影音生產的市場缺口；模型層高度開放避免供應商綁定，跨平台發布與 AI Agent 整合支撐自動化內容生產線，MIT 許可證保障長期可持續發展。
<!-- End AEO Capsule -->

<div class="faq-section">
<h2>常見問題有哪些？</h2>

**Q1：MoneyPrinterTurbo 是免費的嗎？**  
專案本身完全開源，採用 MIT 許可證，可免費自架使用；實際成本僅為所選雲端模型與語音服務的 API 用量費用，Edge TTS 與線上免費素材庫則完全免費。

**Q2：MoneyPrinterTurbo 支援哪些模型服務？**  
支援 Kimi、OpenAI、Google Gemini、DeepSeek、阿里雲通義千問、Azure OpenAI、xAI Grok、MiniMax 與小米 MiMo 等，亦相容 Ollama、LiteLLM、Groq 等本地與統一閘道環境。

**Q3：沒有 GPU 可以使用嗎？**  
可以。主要依賴雲端模型與雲端語音時，CPU 與記憶體更重要；僅在啟用本地 faster-whisper 轉寫或批量生成時，獨立顯示卡才能明顯提升速度。

**Q4：生成的影片可以發布到哪些平台？**  
可透過 Upload-Post 服務自動發布至 TikTok、Instagram 與 YouTube Shorts，亦可在設定中調整 YouTube 的可見性為公開、不公開或私人。
</div>
