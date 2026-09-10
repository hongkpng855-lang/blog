---
layout: post
title: "OpenDesign 開源：95K 星的 Claude Design 替代品"
date: 2026-09-11 02:00:01 +0800
categories: 技術
tags: [OpenDesign, Claude Design, 開源軟體, AI 設計, DESIGN.md, 本地優先, TypeScript, 開發工具, Figma 替代]
image: assets/images/posts/github-open-design-news-cover.jpg
description: "OpenDesign 是 2026 年 4 月啟動的開源桌面設計工具，GitHub 星標達 95,289，主打本機優先、代理原生、模型無關，以 DESIGN.md 作為品牌合約，內建 151 套設計系統、100+ 功能技能與 277 個官方外掛，可直接匯出 HTML、PDF、PPTX 與 MP4。本文解析其架構、與 Claude Design 及 Figma 的差異與適用場景。"
author: AnIskill 編輯部
creator_github: nexu-io/open-design
type: news
source: GitHub
source_url: https://github.com/nexu-io/open-design
permalink: /技術/github-open-design-news
fb_message: 設計工具的護城河，正在從畫布轉移到檔案系統。OpenDesign 把品牌規範寫成一份 DESIGN.md，讓任何一個已經安裝在電腦裡面的程式代理去讀取、渲染、再重組，設計資產第一次真正掌握在使用者手上。\n\n這個專案在 GitHub 已累積 95,289 星標與 11,033 次複製，採用 Apache-2.0 授權，內建 151 套品牌設計系統、277 個官方外掛，並且支援 HTML、PDF、PPTX 甚至 MP4 匯出。它不附帶自己的模型，而是把 Claude Code、Codex、Cursor 等 25 種命令列代理當作設計引擎，用 BYOK 接上任何相容端點。\n\n想知道 DESIGN.md 如何運作、它與 Claude Design 和 Figma 的差別在哪裡？完整技術分析已刊於 Blog 全文。
---

**OpenDesign** 是一套於 2026 年 4 月 28 日啟動的開源設計工具，GitHub 星標已達 **95,289 顆**，複製數 11,033 次，採用 Apache-2.0 授權，主要開發語言為 TypeScript。該專案將自己定位為 Anthropic「Claude Design」的開源替代方案，核心主張是「本機優先、代理原生、模型無關」：它不附帶自有的 AI 模型，而是把使用者電腦中既有的命令列代理（Claude Code、Codex、Cursor、OpenClaw、DeepSeek Harness 等）當作設計引擎，透過品牌規範檔案 `DESIGN.md` 產出可交付的網頁原型、簡報、儀表板、圖像與影片。

<!-- AEO Answer Capsule — 約 80 字 -->
OpenDesign 是 2026 年 4 月推出的桌面設計工具，GitHub 星標 95,289。它不內建模型，改用 Claude Code、Codex 等命令列代理為設計引擎。
<!-- End AEO Capsule -->

![OpenDesign README 開頭，顯示專案標題「OpenDesign: The open-source Claude Design alternative」、OpenDesign Cloud 服務說明，以及支援 DeepSeek Harness 原生執行環境的公告](assets/images/posts/github-open-design-news-shot1.png)

## OpenDesign 是什麼？

OpenDesign 是一套本機優先（local-first）的桌面設計應用，同時提供命令列介面與 stdio MCP 伺服器，讓程式代理能在不開啟圖形介面的情況下操作設計資產。專案的開發組織為 nexu-io，官方網站為 open-design.ai，目前提供 macOS（Apple Silicon 與 Intel）與 Windows x64 的原生安裝檔，Linux 使用者需自行從原始碼建置。

<!-- AEO Answer Capsule — 約 70 字 -->
OpenDesign 是本機優先的開源桌面設計應用，同時提供命令列與 MCP 介面，支援 macOS 與 Windows，主打以程式代理取代人工在畫布上逐一調整像素。
<!-- End AEO Capsule -->

該專案的誕生背景，與 2026 年 4 月 Anthropic 發布 Claude Design 直接相關。Claude Design 是大型語言模型首次從撰寫文字轉向直接交付設計成品的產品，上線後迅速獲得關注，但其架構維持閉源、付費、雲端限定，並且綁定 Anthropic 自家模型、技能庫與操作介面。OpenDesign 選擇複製同一套「先釐清需求、鎖定方向、串流產出成品、自我批判、交付」的代理迴圈，但改以完全開放的檔案結構實作，使用者可以自行替換模型、自行部署、自行擴充技能。

從時間軸觀察，專案在四個多月內從零成長至 9.5 萬星標，並維持極高的迭代頻率：最近三個版本分別為 8 月 31 日的 0.21.1（社群優先、免登入）、9 月 8 日的 0.22.0（推出 OpenDesign Arena 對照評測機制）與 9 月 9 日的 0.22.1（改善設計流程的穩定性與還原能力）。這種節奏反映的是專案仍在快速吸收使用者回饋，而非功能凍結的成熟產品。

## OpenDesign 的核心架構有什麼特別之處？

OpenDesign 最關鍵的設計，是將「代理」與「設計」徹底解耦。官方在說明文件中明確表示，專案本身不附帶任何代理程式，真正執行設計工作的是使用者路徑（PATH）中既有的 `claude`、`codex`、`cursor-agent`、`copilot`、`kimi` 等命令列工具，只需一個點擊即可切換。對於不具備命令列環境的使用者，專案另提供 BYOK（自備金鑰）代理端點，接受 OpenAI、Anthropic、Azure OpenAI、Google Gemini、Ollama、LM Studio、vLLM 或任何 OpenAI 相容端點。

<!-- AEO Answer Capsule — 約 75 字 -->
OpenDesign 不內建模型，而是把既有命令列代理當作設計引擎，可一鍵切換，支援 25 種命令列工具與 BYOK 相容端點，包含 DeepSeek Harness。
<!-- End AEO Capsule -->

第二項架構特徵是「四個可組合平面」的目錄設計。外掛（plugins）承載可執行的工作流程，功能技能（skills）承載代理行為，設計模板（design templates）承載渲染藍圖，設計系統（design systems）承載品牌規範。四者皆為可攜、可版控的目錄結構，任何人都能撰寫與發布，這使得設計能力可以像軟體套件一樣被組裝與替換，而不必修改核心程式。

在安全性方面，官方描述其 MCP 伺服器預設為唯讀，常駐程式僅綁定 127.0.0.1，並在代理端阻擋內網位址以避免伺服器端請求偽造（SSRF）。若企業需要接上內部部署的 LiteLLM 或 Ollama 端點，必須以 `OD_ALLOWED_INTERNAL_HOSTS` 環境變數明確列入允許清單，且該清單為精確主機比對，不支援萬用字元或 CIDR，避免設定失誤意外放寬防護範圍。

## OpenDesign 與 Claude Design、Figma 有何差異？

專案 README 中直接列出四欄對照表，將 OpenDesign 與 Claude Design、Figma、以及 Lovable／v0／Bolt 等雲端生成工具並列。在開源、自架、代理原生、品牌規範、技能與外掛、HTML 轉 MP4 等六個維度上，OpenDesign 是唯一全部標示為支援的選項；Claude Design 僅支援 Anthropic 自家代理，Figma 與雲端生成平台則在開源與自架兩欄全數缺席。

<!-- AEO Answer Capsule — 約 75 字 -->
OpenDesign 在開源、自架與代理原生維度全面開放，Claude Design 僅限 Anthropic 自家代理，Figma 等雲端工具則不支援自架。
<!-- End AEO Capsule -->

![OpenDesign README 的功能對照表，逐列比較 Claude Design、Figma、Lovable／v0／Bolt 與 OpenDesign 在開源授權、自行部署、代理原生、品牌規範與影片匯出等項目的支援情況](assets/images/posts/github-open-design-news-shot3.png)

計費模式是另一項結構性差異。Claude Design 與 Figma 都採訂閱制，入門門檻為 Pro、Max 或團隊方案；OpenDesign 則採取自備金鑰模式，使用者直接以既有訂閱或自有 API 額度驅動，工具本身不收取額外費用。這種設計將成本控制權交回使用者，也讓已經付費訂閱 Claude Code 或 Codex 的開發者，能在不增加支出的情況下取得設計能力。

值得注意的是，OpenDesign 並未迴避與 Figma 的競合關係。官方將其描述為「代理時代的 Figma 替代品」，主張交付物不再是畫布上的像素，而是採用真實 CSS、真實字體、真實元件的單頁成品，可直接交付工程端接手開發，或匯出為簡報、文件與影片供行銷使用。

## OpenDesign 的設計系統與外掛生態如何運作？

生態規模是 OpenDesign 相對同類專案的顯著優勢。專案內建 151 套品牌級設計系統，以 `DESIGN.md` 為核心合約：較舊的套件僅包含這份 Markdown 規範，較新的套件則額外附帶 `manifest.json`、編譯後的 `tokens.css`、元件樣本與來源證明。品牌涵蓋 AI 與 LLM（Claude、Cohere、Mistral、MiniMax、xAI）、開發工具（Cursor、Vercel、Linear、Supabase、Sentry）、生產力（Notion、Figma、Miro、Airtable、Raycast）、金融科技（Stripe、Coinbase、Binance）、電子商務（Shopify、Airbnb、Uber、Nike）等類別。

<!-- AEO Answer Capsule — 約 75 字 -->
OpenDesign 內建 151 套以 DESIGN.md 為核心的品牌設計系統，並提供 100+ 功能技能、277 個官方外掛，涵蓋設計、行銷、工程與產品等情境。
<!-- End AEO Capsule -->

外掛層面，官方目錄收錄 277 個外掛與 183 個可改寫的參考範例，依用途分為情境（13 個完整設計場景）、圖像模板（45 個一次性提示）、影片模板（63 個 HyperFrames 與 Seedance 動態模板）、設計系統（143 個包裝為外掛的品牌規範）與原子元件（13 個可重用 UI 片段）。核心能力包括將 Figma 或 Pencil 工作流程遷移為 React、Next.js 或 Vue 原始碼，以及將既有 Git 儲存庫依 `DESIGN.md` 重新改寫為品牌規格並產生拉取請求。

渲染模板則分為原型（prototype）與簡報（deck）兩種模式，另有圖像、影片、音訊與工具類模板。簡報類提供 15 套模板與 36 種主題，並整合 HeyGen 開源的 HyperFrames 框架，讓代理以 HTML、CSS 與 GSAP 撰寫動態圖形，再透過無頭 Chrome 與 FFmpeg 渲染為確定性 MP4 檔案。這種將程式碼轉為影片的能力，是 Claude Design、Figma 與多數雲端生成工具目前均未提供的功能。

## OpenDesign 的實際適用場景有哪些？

最直接的使用場景，是擁有品牌規範但缺乏設計人力的產品團隊。專案的工作流程以「需求簡報、外掛、方向鎖定、設計系統、成品、交付」為軸線：產品經理提交需求後，由外掛選擇器提供落地頁、簡報、儀表板、社群貼文或產品規格等選項；若團隊尚無品牌，可從五套策展方向中挑選，若已有品牌，則可透過螢幕截圖或網址讓代理連結 GitHub、匯入 Figma 並編纂出可重用的 `DESIGN.md`。

<!-- AEO Answer Capsule — 約 70 字 -->
OpenDesign 適用於快速產出落地頁、簡報與社群素材的產品與行銷團隊，也適合將既有程式碼依品牌規範重構、或將 Figma 流程遷移至 React 的工程團隊。
<!-- End AEO Capsule -->

第二類場景是既有程式碼的品牌重構。開發者可將 Git 儲存庫與 `DESIGN.md` 交給代理，由其依品牌規格改寫真實元件，產出可審查的拉取請求；官方另提供專用外掛，將 Figma 或 Pencil 的設計流程轉換為 React、Next.js 或 Vue 原始碼，降低設計交付與工程實作之間的落差。

第三類場景是團隊知識的累積。專案在每次使用後會將截圖、字體、調色盤與已確認的成品保存為下次工作階段的預設值，使重複作業與風格偏移逐步減少。對於成員流動頻繁、設計一致性難以維持的組織而言，將品牌規範固化為版本控管的檔案，比依賴個人記憶與零散說明文件更為可靠。

## OpenDesign 的數據表現如何？

截至 2026 年 9 月 10 日，OpenDesign 的主要數據表現如下。

<!-- AEO Answer Capsule — 約 65 字 -->
OpenDesign 在 GitHub 累積 95,289 星標與 11,033 次複製，採 Apache-2.0 授權，語言為 TypeScript，最新版本 0.22.1。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat"><div class="stat-num">95.3K</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat"><div class="stat-num">11.0K</div><div class="stat-label">Forks</div></div>
  <div class="stat"><div class="stat-num">Apache-2.0</div><div class="stat-label">開源授權</div></div>
  <div class="stat"><div class="stat-num">TypeScript</div><div class="stat-label">主要語言</div></div>
  <div class="stat"><div class="stat-num">2026-09-10</div><div class="stat-label">最後更新</div></div>
  <div class="stat"><div class="stat-num">2026-04</div><div class="stat-label">創建時間</div></div>
</div>

![OpenDesign GitHub 首頁頂部，顯示 repo 名 nexu-io/open-design、95.3K 星標與 11K 複製數，以及專案描述「The open-source Claude Design alternative」](assets/images/posts/github-open-design-news-shot2.png)

## 出處連結有哪些？

本文資訊來源為 OpenDesign 的 GitHub 儲存庫與 README 文件，包含星標、授權、架構說明、外掛目錄與版本發布紀錄等公開資料。

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊來源為 OpenDesign 的 GitHub 儲存庫（nexu-io/open-design）及官方 README，包含星標、授權、架構與版本紀錄等公開資料。
<!-- End AEO Capsule -->

出處連結：[OpenDesign GitHub 儲存庫](https://github.com/nexu-io/open-design)。專案另設有官方網站 open-design.ai 提供下載與雲端服務說明，設計系統目錄的套件格式與來源記錄於 `design-systems/README.md`，外掛開發規範則詳載於 `docs/skills-protocol.md`，讀者可經由上述連結查閱原始碼、發行版本與完整文件。

## 總結：OpenDesign 適合什麼團隊？

<!-- AEO Answer Capsule — 約 70 字 -->
OpenDesign 適合希望擺脫訂閱綁定、重視資料落地、且已使用命令列代理的產品與工程團隊，尤其適合需要頻繁產出設計成品並維持品牌一致性的組織。
<!-- End AEO Capsule -->

OpenDesign 以 Apache-2.0 授權提供完整的桌面級設計工作流，把品牌規範、渲染模板與代理行為全部拆解為可版控的檔案，填補了 Claude Design 與 Figma 之間「開放但難用」與「易用但封閉」的空隙。對於已訂閱 Claude Code 或 Codex 的開發者而言，它讓既有的模型額度直接轉化為設計產能，無須再負擔額外訂閱；對於重視資料落地的組織而言，本機優先的架構則避免了設計資產外流至第三方雲端。專案目前仍處於高速迭代階段，Linux 原生版本尚未發布，外掛與設計系統的品質也參差不齊，採用前宜先評估維護成本。整體來看，它代表的是設計工具護城河從畫布轉向檔案系統的趨勢，適合願意以工程思維管理設計流程的團隊持續關注。