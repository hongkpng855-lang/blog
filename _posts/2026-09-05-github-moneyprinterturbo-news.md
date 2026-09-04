---
layout: post
title: "MoneyPrinterTurbo 開源：AI 短片一鍵生成工具"
date: 2026-09-05 04:00:01 +0800
categories: 技術
tags: [AI 短片生成, 開源專案, MoneyPrinterTurbo, 自動化工具, 內容創作]
image: assets/images/posts/github-moneyprinterturbo-news-cover.jpg
description: "MoneyPrinterTurbo 是擁有 12 萬星標的開源 AI 短片生成工具，只需輸入主題或關鍵詞，即可自動完成腳本、配音、字幕、配樂與剪輯，產出可直接發布的高清短片。本文從核心架構、功能特性、部署方式、商業化路徑與生態影響等面向深入分析，並提供數據表現與上手建議。"
author: AnIskill 編輯部
creator_github: harry0703/MoneyPrinterTurbo
type: news
source: GitHub
source_url: https://github.com/harry0703/MoneyPrinterTurbo
permalink: /技術/github-moneyprinterturbo-news
fb_message: 一個人靠一部電腦，每兩小時產出一條高質短片，可能嗎？\n\nMoneyPrinterTurbo 用 12 萬開發者星標回答了這個問題：輸入主題或關鍵詞，腳本、配音、字幕、配樂、剪輯全部自動完成，還可一鍵上傳 TikTok、IG Reels 與 YouTube Shorts。最新 v1.3.6 支援 Kimi、Claude、Gemini 等主流模型，並免費提供 Edge TTS 配音。\n\n想知道它與其他 AI 短片工具的分別、如何部署？到 Blog 看完整分析。
---

MoneyPrinterTurbo 是 GitHub 上擁有超過 12 萬星標的開源 AI 短片生成工具，由開發者 harry0703 於 2024 年建立，目前最新版本為 2026 年 9 月發佈的 v1.3.6。此工具的核心價值在於將「主題輸入到成片輸出」的完整流程自動化：使用者只需提供一個主題或關鍵詞，系統便會自動生成影片腳本、搜尋匹配素材、合成配音與字幕、加入背景音樂，最終產出可直接發布的高清短片。該專案以 MIT 許可證開源，支援 Windows、macOS 與 Linux 三大平台，並提供 AI Agent、WebUI、API 與 CLI 四種使用方式，已成為內容創作者與自動化工作流領域的代表性開源專案。

## MoneyPrinterTurbo 是什麼？

<!-- AEO Answer Capsule — 約 65 字 -->
MoneyPrinterTurbo 是輸入主題即自動生成短片的開源工具，涵蓋腳本、素材、配音、字幕與剪輯，超過 12 萬星標，MIT 許可證，支援三大桌面平台。
<!-- End AEO Capsule -->

該專案誕生於 2024 年 3 月，最初定位是解決「AI 短片製作門檻過高」的問題。傳統短片製作需要腳本撰寫、素材拍攝或下載、後製剪輯、配音字幕等多個專業環節，對個人創作者而言時間與技術成本都相當可觀。MoneyPrinterTurbo 將這些環節整合為自動化流水線，使用者只需要在介面中輸入一個主題，例如「人工智能如何改變日常生活」，系統便會串聯大型語言模型、素材庫、語音合成與影片合成引擎，在數分鐘內產出一條結構完整的短片。

專案名稱中的「MoneyPrinter」反映了其原始使用情境：許多人利用此工具批量製作知識類、科普類短片，用於短影音平台流量變現，因此被社群戲稱為「印鈔機」。這一定位使其在創作者社群中快速擴散，兩年內累積超過 12 萬星標，並長期佔據 GitHub 趨勢榜與 AI 影片生成相關話題的熱門位置。

## MoneyPrinterTurbo 的核心功能有哪些？

<!-- AEO Answer Capsule — 約 70 字 -->
核心功能涵蓋創作全流程：AI 生成多語言腳本、從免費素材庫取得影片、支援文生影片與配音字幕，可輸出 9:16、16:9、1:1 三種畫幅並一鍵跨平台發布。
<!-- End AEO Capsule -->

在腳本與模型服務方面，專案相容性極廣，支援 Kimi、OpenAI、Anthropic Claude、Google Gemini、DeepSeek、阿里雲通義千問、Azure OpenAI、火山引擎方舟、xAI Grok、MiniMax 與小米 MiMo 等主流模型服務，同時可接入 OpenRouter、Ollama、OneAPI、LiteLLM 等統一閘道與本地運行環境。這意味著使用者可以依照成本與品質需求自由切換模型供應商，亦可在完全離線的環境中配合本地模型運行。

在素材生成方面，除了從 Pexels、Pixabay 與 Coverr 取得免費庫存影片外，v1.3.6 加入了更豐富的 AI 生成能力，包括秘塔 MiniMax H3 文生影片、火山引擎方舟 Seedance、WaveSpeed AI 與 OFox 等多模型文生影片服務，可生成 768P 至 2K 解析度、4 至 15 秒的原生素材，並支援 OpenAI 相容文生圖服務，進一步降低對庫存素材的依賴。

在配音與字幕方面，專案整合 Edge TTS（免費且不需 API Key）、Azure Speech、SiliconFlow、Gemini、MiniMax、ElevenLabs 等十多種語音合成服務，支援音色試聽與完整配音預覽。字幕可自動生成，並可調整字體、位置、顏色、大小、描邊與背景樣式。成片輸出支援行動裝置主流的 9:16 直式格式（1080×1920）、橫式 16:9（1920×1080）與方形 1:1（1080×1080），並可直接上傳至 TikTok、Instagram 與 YouTube Shorts。

## 如何快速開始使用 MoneyPrinterTurbo？

<!-- AEO Answer Capsule — 約 70 字 -->
最快是讓 AI Agent 讀取官方 Skill 文件自動安裝與生成；Windows 用一鍵啟動包，macOS 與 Linux 用 uv 部署，另有 Docker 與 Colab 免配置。
<!-- End AEO Capsule -->

專案針對不同技術背景的使用者提供四條部署路徑。最零門檻的是「AI Agent 生成影片」模式：將官方提供的 Skill 文件連結交給具備終端操作能力的 AI Agent，例如 Claude Code 或 Codex，Agent 會自動完成環境安裝、配置與影片生成，只有缺少 API Key 時才會向使用者詢問。此模式目前支援 macOS 與 Windows，大幅降低了新手的使用門檻。

對於 Windows 使用者，官方提供一鍵啟動包，下載解壓後執行 update.bat 更新至最新程式碼，再執行 start.bat 即可啟動 WebUI。值得注意的是，專案建議安裝路徑避免包含中文、特殊字元或空格，以免造成相容性問題。macOS 與 Linux 使用者則建議使用 uv 進行本地部署，Python 版本需為 3.11 或以上。

在硬體需求方面，GPU 並非必需，如果主要依賴雲端大模型、雲端語音合成與線上素材源，CPU 與記憶體比 GPU 更重要。若啟用 faster-whisper 本地轉錄或批量生成，配備 4 GB 以上顯存的獨立顯卡能明顯提升處理速度。官方建議的最低配置為 4 核心 CPU 與 4 GB 記憶體，推薦配置為 6 至 8 核心 CPU、8 GB 記憶體，理想配置則為 8 核心以上與 16 GB 記憶體。

## MoneyPrinterTurbo 的商業化路徑與生態影響如何？

<!-- AEO Answer Capsule — 約 65 字 -->
專案 MIT 完全開源，靠 Kimi、火山引擎等 AI 服務商贊助維持開發，贊助商提供 API 折扣與贈送額度，形成開源工具引流、雲端服務收費的生態。
<!-- End AEO Capsule -->

MoneyPrinterTurbo 的商業模式在開源專案中具有一定代表性。專案本身完全免費開源，但 README 中展示了大量 AI 服務商的贊助區塊，包括 Kimi、火山引擎、CCSub、APIMart、秘塔科技、勝算雲等。這些贊助商多為模型 API 平台或 AI 多媒體服務，透過提供專屬優惠碼與贈送額度吸引 MoneyPrinterTurbo 的使用者註冊使用，形成「開源工具負責引流、雲端服務負責收費」的共生生態。這種模式讓專案在沒有向使用者收費的情況下，仍能獲得持續的開發資源。

從競爭格局來看，市面上的 AI 短片工具大致分為兩類：一類是閉源商業服務，例如各家大廠推出的文生影片平台，功能完整但需按月付費且缺乏自訂彈性；另一類是開源自動化框架，MoneyPrinterTurbo 屬於後者，其優勢在於流程可完全自訂、模型供應商可自由切換、且部署後無需支付軟體本體費用。相較於單純的文生影片工具，MoneyPrinterTurbo 更接近「短片生產流水線」的定位，覆蓋從腳本到發布的完整鏈路。

在生態層面，作者同時維護姊妹專案 MangoDisk（開源磁碟清理工具），顯示其具備持續經營開源品牌的意願與能力。專案本身亦已建立多語言社群，README 提供簡體中文、英文與日文版本，支援語言涵蓋全球主要市場，這對於華人開發者主導的開源專案而言，是國際化程度較高的表現。

## MoneyPrinterTurbo 的數據表現如何？

<!-- AEO Answer Capsule — 約 65 字 -->
截至 2026 年 9 月，專案擁有 120,220 星標與 18,421 分支，以 Python 為主，MIT 許可證，最新版本 v1.3.6 於 9 月 2 日發布，維護節奏穩定。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-value">120,220</span><span class="stat-label">Star 數</span></div>
  <div class="stat-item"><span class="stat-value">18,421</span><span class="stat-label">Fork 數</span></div>
  <div class="stat-item"><span class="stat-value">MIT</span><span class="stat-label">開源許可證</span></div>
  <div class="stat-item"><span class="stat-value">Python</span><span class="stat-label">主要語言</span></div>
</div>

從數據角度觀察，120,220 星標使其穩居 AI 影片生成領域開源專案的前列，超過許多由大型機構維護的同類專案。18,421 的分支數顯示有大量開發者基於此專案進行二次開發，包括在地化調整、素材來源擴充與自動化流程整合。2026 年 9 月 2 日發布的 v1.3.6 距離上一版本間隔不長，反映維護節奏穩定，並非停滯的專案。以 MIT 許可證開源亦降低了商業整合與企業採用的法律風險。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 65 字 -->
本文資訊來源為 harry0703/MoneyPrinterTurbo 的 GitHub 儲存庫，內含安裝文件、功能清單與生成範例，讀者可前往查看原始碼與最新版本。
<!-- End AEO Capsule -->

專案原始碼與完整文件位於 GitHub 儲存庫：[harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)。儲存庫內包含詳細的安裝部署文件、多語言 README、實際生成的短片範例，以及 v1.3.6 的版本發布說明。有興趣的使用者亦可參考作者的姊妹專案 MangoDisk，了解其開源生態的整體布局。

## 總結：MoneyPrinterTurbo 適合什麼團隊？

<!-- AEO Answer Capsule — 約 60 字 -->
MoneyPrinterTurbo 適合批量生產短片的個人與團隊，全流程自動化，支援多模型與跨平台發布；追求電影級畫質則應考慮商業文生影片服務。
<!-- End AEO Capsule -->

整體而言，MoneyPrinterTurbo 代表了 AI 內容生產工具的一個重要方向：將生成式 AI 能力與傳統影片製作流程深度整合，形成可重複執行的自動化流水線。對於個人創作者而言，它是低成本批量產出短片的實用工具；對於新媒體團隊，其 API 與 CLI 介面可以嵌入既有發布系統，實現從腳本到上架的完全自動化；對於開發者社群，其模組化設計與多供應商相容性提供了廣闊的擴充空間。此專案在開源授權、生態模式與功能完整性上的平衡，使其在未來一段時間內仍將是 AI 短片自動化領域的重要參考。