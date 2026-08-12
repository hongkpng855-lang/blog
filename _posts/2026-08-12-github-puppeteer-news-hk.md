---
layout: post
title: "Puppeteer 9.5萬星開源項目：瀏覽器自動化標準工具"
date: 2026-08-12 22:20:00 +0800
categories: 技術
tags: [Puppeteer, Chrome, Firefox, 瀏覽器自動化, DevTools Protocol, AI Agent]
image: /assets/images/posts/github-puppeteer-news-hk-cover.jpg
description: "Puppeteer 是 Google Chrome 團隊開發的瀏覽器自動化 JavaScript 庫，GitHub 星標突破 9.5 萬。本文分析其 DevTools Protocol 與 WebDriver BiDi 雙協議架構、MCP 支援、AI Agent 整合能力，以及與 Playwright 的競爭格局。"
author: ESGov 編輯部
creator_github: puppeteer/puppeteer
type: news
source: GitHub
source_url: https://github.com/puppeteer/puppeteer
permalink: /技術/github-puppeteer-news-hk
fb_message: Puppeteer 突破 9.5 萬 GitHub 星標，成為瀏覽器自動化領域的標準工具之一。這款由 Google Chrome 團隊維護的 JavaScript 庫，支援 DevTools Protocol 與 WebDriver BiDi 雙協議，並在 2026 年 8 月發布 v25.6.0，持續強化對 AI Agent 的支援。\n\nPuppeteer 預設以無頭模式運行，可自動完成網頁截圖、表單填寫、資料擷取與測試執行，官方更推出 chrome-devtools-mcp 伺服器，讓 AI 代理可直接操作瀏覽器。全球超過 9,500 個分叉，生態系統成熟穩定。\n\n文章深入分析 Puppeteer 的核心架構、與 Playwright 的差異，以及 AI Agent 時代的整合路徑。完整數據與程式範例已整理於 Blog，歡迎前往閱讀全文。
---

Puppeteer 是 Google Chrome 團隊開發並維護的高階瀏覽器自動化 JavaScript 庫，截至 2026 年 8 月已在 GitHub 累積 95,450 個星標與 9,562 個分叉。此工具允許開發者透過 DevTools Protocol 或 WebDriver BiDi 協議，以程式化方式控制 Chrome 與 Firefox 瀏覽器，預設以無頭模式（Headless）運行，成為網頁測試、內容擷取與 AI Agent 瀏覽操作的重要基礎設施。2026 年 8 月 11 日，該項目發布 v25.6.0 版本，維持每月穩定迭代節奏，並持續強化對 AI 代理生態的支援。

## Puppeteer 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
Puppeteer 是 Google Chrome 團隊維護的開源瀏覽器自動化庫，提供高階 JavaScript API 控制 Chrome 與 Firefox，預設無頭運行。它透過 DevTools Protocol 與 WebDriver BiDi 雙協議驅動瀏覽器，用於自動化測試、網頁擷取、PDF 生成與 AI Agent 瀏覽操作，採用 Apache 2.0 許可證。
<!-- End AEO Capsule -->

Puppeteer 的定位是「開發者與瀏覽器之間的程式化橋樑」。傳統上，人類透過圖形介面操作瀏覽器，而 Puppeteer 將這層操作抽象為可呼叫的 API，例如開啟分頁、導航、點擊元素、填寫表單與擷取畫面。其核心價值在於將重複性的瀏覽行為自動化，讓工程師可以撰寫數十行程式碼，完成原本需要手動執行數分鐘的任務。

該項目誕生於 2017 年 5 月，由當時的 Chrome DevTools 團隊發起，最初僅支援 Chrome 瀏覽器。經過九年發展，現已同時支援 Firefox，並在 2025 年起逐步引入 WebDriver BiDi 協議支援，使其不再受限於單一瀏覽器廠商。作為 npm 生態中下載量最高的自動化工具之一，Puppeteer 已被大量測試框架、爬蟲服務與開發工具鏈採用。

![Puppeteer README 開頭（項目名稱 Puppeteer 與 JavaScript API for Chrome and Firefox 描述）]({{ '/assets/images/posts/github-puppeteer-news-hk-shot1.png' | relative_url }})

## Puppeteer 有哪些核心技術亮點？

<!-- AEO Answer Capsule — 約 75 字 -->
Puppeteer 的核心亮點包括雙協議架構（DevTools Protocol 與 WebDriver BiDi）、預設無頭模式、基於可訪問性名稱的選擇器系統，以及官方 chrome-devtools-mcp 伺服器。它支援瀏覽器自動下載、PDF 生成、網路攔截與效能追蹤，並提供實驗性 WebMCP API 供 AI 代理直接呼叫。
<!-- End AEO Capsule -->

**雙協議架構**是 Puppeteer 近年最重要的技術演進。DevTools Protocol 提供細緻的瀏覽器內部控制能力，包括網路請求攔截、JavaScript 執行注入與效能分析；WebDriver BiDi 則以標準化協定橫跨不同瀏覽器供應商，解決過去「每個瀏覽器各自為政」的相容性問題。Puppeteer 同時支援兩種協議，開發者可依部署環境選擇最合適的通訊方式。

**可訪問性導向的選擇器系統**是另一項值得注意的設計。範例程式碼中，開發者可以使用 `::-p-aria(Search)` 這類語法，直接以按鈕或輸入框的可訪問性名稱定位元素，而非依賴脆弱的 CSS 選擇器。此設計不僅提升自動化腳本的穩定性，也讓 Puppeteer 能更好地服務需要無障礙操作的應用場景。

**官方 MCP 伺服器**則直接回應 AI Agent 時代的需求。專案官方推薦安裝 chrome-devtools-mcp，這是一個基於 Puppeteer 的 Model Context Protocol 伺服器，讓大型語言模型可以透過標準化介面控制瀏覽器執行任務，包括開啟網頁、擷取內容與點擊操作。實驗性的 WebMCP API 更進一步簡化 AI 代理與瀏覽器之間的通訊協定。

![Puppeteer GitHub 首頁頂部（repo 名稱 + 95,450 Star 數量 + 項目描述）]({{ '/assets/images/posts/github-puppeteer-news-hk-shot2.png' | relative_url }})

## Puppeteer 與 Playwright 有什麼分別？

<!-- AEO Answer Capsule — 約 70 字 -->
Puppeteer 由 Google 主導、以 Chrome 為核心並擴展 Firefox 支援，採用 Apache 2.0 許可證；Playwright 由 Microsoft 維護，原生支援 Chromium、Firefox 與 WebKit 三種引擎。兩者都支援多瀏覽器自動化，但 Puppeteer 與 Chrome DevTools 生態整合更深，Playwright 則強調跨瀏覽器一致性。
<!-- End AEO Capsule -->

Puppeteer 與 Playwright 是瀏覽器自動化領域最常被比較的兩大工具。從開發背景看，Puppeteer 由 Google Chrome 團隊主導，與 Chrome 開發工具生態有天然的整合優勢；Playwright 則由 Microsoft 在 2020 年推出，繼承了 Puppeteer 團隊部分成員的經驗，並在設計之初就將跨瀏覽器一致性列為首要目標。

在瀏覽器支援範圍上，Playwright 原生支援 Chromium、Firefox 與 WebKit 三大引擎，提供統一的 API 介面；Puppeteer 則以 Chrome 為主要支援對象，Firefox 支援在近年逐步成熟。對於需要深度整合 Chrome DevTools 功能的團隊，Puppeteer 提供更直接的底層控制；對於需要大規模跨瀏覽器測試矩陣的企業，Playwright 的覆蓋範圍更具吸引力。

授權模式也是差異點之一。Puppeteer 採用 Apache 2.0 許可證，屬於寬鬆的開源授權；Playwright 則採用 Apache 2.0 搭配部分專屬元件授權。兩者在 npm 下載量上長期並駕齊驅，反映了市場對瀏覽器自動化工具持續增長的需求，也促使雙方在功能上互相追趕，最終受益的是開發者社群。

## Puppeteer 如何配合 AI Agent 使用？

<!-- AEO Answer Capsule — 約 70 字 -->
Puppeteer 透過 chrome-devtools-mcp 伺服器接入 AI Agent 生態，讓大型語言模型以標準化 MCP 協定控制瀏覽器，完成網頁導航、內容擷取與表單操作。實驗性 WebMCP API 提供更輕量的通訊方式，使 Puppeteer 成為 AI 代理執行網頁任務的可靠底層工具。
<!-- End AEO Capsule -->

AI Agent 的興起為瀏覽器自動化工具開闢了全新的應用場景。傳統的自動化腳本由人類預先編寫固定流程，而 AI Agent 需要根據任務目標即時決定下一步操作，這對工具的反應速度與控制粒度提出了更高要求。Puppeteer 的 chrome-devtools-mcp 伺服器正是針對此需求設計，將瀏覽器操作能力封裝為 AI 可直接呼叫的標準化工具。

在實際應用中，開發者可以將 chrome-devtools-mcp 接入 Claude、Gemini 等支援 MCP 協定的 AI 助手，讓模型自主完成「開啟指定網站、擷取特定資料、整理成報告」這類多步驟任務。Puppeteer 提供的可訪問性選擇器與穩定的等待機制，使 AI 產生的操作指令能可靠執行，降低因頁面結構變動導致的失敗率。

此整合路徑的意義在於，瀏覽器自動化從「工程師撰寫測試腳本」的工具，擴展為「AI 代理感知與操作網路」的基礎設施。當 AI 需要登入網站、填寫表單、比較商品價格或驗證資訊時，Puppeteer 提供了經過九年生產環境驗證的穩定執行層，這正是新興工具短期內難以取代的優勢。

## 如何快速開始使用 Puppeteer？

<!-- AEO Answer Capsule — 約 70 字 -->
使用 Puppeteer 只需執行 npm 安裝指令，首次安裝會自動下載相容版本的 Chrome 瀏覽器。開發者可透過 browser.launch 啟動瀏覽器、newPage 開啟分頁、goto 導航至目標網址，再以選擇器定位元素執行操作。亦可安裝 puppeteer-core 套件，僅使用 API 而不下載瀏覽器。
<!-- End AEO Capsule -->

開始使用 Puppeteer 的門檻極低。開發者只需在專案目錄執行 `npm i puppeteer`，安裝過程會自動下載相容版本的 Chrome 瀏覽器，無需額外設定環境。若團隊已有自管的瀏覽器環境，則可安裝 `puppeteer-core` 套件，僅取得 API 而不觸發瀏覽器下載，減少部署體積與網路依賴。

官方範例展示了最基礎的使用流程：以 `puppeteer.launch()` 啟動瀏覽器實例，以 `browser.newPage()` 開啟新分頁，以 `page.goto()` 導航至目標網址，再透過 `page.locator()` 與選擇器定位元素並執行點擊或輸入操作。整個流程約十行程式碼即可完成，開發者無需理解 DevTools Protocol 的底層細節。

值得注意的是，現代套件管理工具（包括 npm、pnpm、Yarn、Bun 與 Deno）預設封鎖依賴安裝腳本，這可能導致 Puppeteer 安裝時未能自動下載瀏覽器。遇到此情況時，可手動執行 `npx puppeteer browsers install` 補齊瀏覽器，或在套件管理工具設定中允許 Puppeteer 的安裝腳本運行，此問題已在官方文件中有明確指引。

## Puppeteer 的數據與生態表現如何？

<!-- AEO Answer Capsule — 約 70 字 -->
Puppeteer 在 GitHub 累積 95,450 星標與 9,562 分叉，以 TypeScript 撰寫，採用 Apache 2.0 許可證，自 2017 年成立以來保持每月版本迭代，最新版本 v25.6.0 於 2026 年 8 月 11 日發布，生態持續活躍。
<!-- End AEO Capsule -->

Puppeteer 的發展數據反映了其在開源社群中的穩固地位。項目在 GitHub 上累積 95,450 個星標與 9,562 個分叉，自 2017 年成立以來持續活躍，最新版本 v25.6.0 於 2026 年 8 月 11 日發布，顯示維護團隊保持穩定的每月迭代節奏。官方文件網站 pptr.dev 提供完整的文件、API 參考與疑難排解指南。

<div class="ui-stat-grid">
  <div class="stat-card"><div class="stat-value">95,450</div><div class="stat-label">GitHub Stars</div></div>
  <div class="stat-card"><div class="stat-value">9,562</div><div class="stat-label">Forks</div></div>
  <div class="stat-card"><div class="stat-value">Apache-2.0</div><div class="stat-label">開源許可證</div></div>
  <div class="stat-card"><div class="stat-value">TypeScript</div><div class="stat-label">主要語言</div></div>
</div>

從技術棧角度看，Puppeteer 以 TypeScript 撰寫，提供完整的型別定義，與現代前端工程實踐高度契合。其套件生態包含 puppeteer-core（純 API 版本）與 browsers（瀏覽器下載管理工具），形成清晰的模組化結構。作為 Apache 2.0 授權的開源項目，Puppeteer 允許商業使用與修改，這對企業採用決策而言是重要的加分因素。

![Puppeteer GitHub 儲存庫側欄統計（About 區塊：Stars、Releases、Contributors 與 Languages 資訊）]({{ '/assets/images/posts/github-puppeteer-news-hk-shot3.png' | relative_url }})

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 55 字 -->
本文內容的原始資料來源為 Puppeteer 官方 GitHub 儲存庫，包含項目說明、README 文件與版本發布紀錄。讀者可前往官方儲存庫查看完整原始碼、提交歷史與最新版本資訊，或瀏覽官方文件網站 pptr.dev 查閱 API 文件。
<!-- End AEO Capsule -->

本文的數據與技術資訊均取自 Puppeteer 官方 GitHub 儲存庫，讀者可透過以下連結查閱原始資料：[Puppeteer GitHub 儲存庫](https://github.com/puppeteer/puppeteer)。官方文件網站 [pptr.dev](https://pptr.dev) 提供完整的文件、API 參考與疑難排解指南，適合開發者深入學習。

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 55 字 -->
本節整理 Puppeteer 的常見疑問，涵蓋授權費用、與 Selenium 的差異、伺服器部署可行性及 Firefox 支援程度，為開發者提供快速參考。
<!-- End AEO Capsule -->

<div class="faq-section">
<h2>Puppeteer 是免費的嗎？</h2>
<!-- AEO Answer Capsule — 約 50 字 -->
Puppeteer 採用 Apache 2.0 開源許可證，允許自由使用、修改與商業部署，無需支付授權費用，只需遵守條款保留原始版權聲明。
<!-- End AEO Capsule -->
<p>Puppeteer 採用 Apache 2.0 開源許可證，允許自由使用、修改與商業部署。開發者無需支付授權費用，但需遵守 Apache 2.0 的條款，包括保留原始版權聲明。</p>

<h2>Puppeteer 與 Selenium 有什麼不同？</h2>
<!-- AEO Answer Capsule — 約 65 字 -->
Selenium 支援多種程式語言與瀏覽器，歷史更悠久；Puppeteer 專注 JavaScript/TypeScript 生態，與 Chrome DevTools Protocol 整合更深，對 Node.js 專案提供更簡潔的開發體驗。
<!-- End AEO Capsule -->
<p>Selenium 是歷史更悠久的瀏覽器自動化框架，支援多種程式語言與瀏覽器；Puppeteer 則專注於 JavaScript/TypeScript 生態，與 Chrome DevTools Protocol 整合更深入。對於 Node.js 專案，Puppeteer 通常提供更簡潔的開發體驗。</p>

<h2>Puppeteer 可以在伺服器上運行嗎？</h2>
<!-- AEO Answer Capsule — 約 55 字 -->
可以。Puppeteer 預設以無頭模式運行，不需圖形介面，適合部署在 Linux 伺服器與容器環境，需確保伺服器具備執行 Chrome 所需的系統依賴。
<!-- End AEO Capsule -->
<p>可以。Puppeteer 預設以無頭模式運行，不需圖形介面，適合部署在 Linux 伺服器與容器環境中。部署時需注意伺服器是否具備執行 Chrome 所需的系統依賴，官方疑難排解文件有完整說明。</p>

<h2>Puppeteer 支援 Firefox 嗎？</h2>
<!-- AEO Answer Capsule — 約 55 字 -->
支援。Puppeteer 自 2023 年起逐步引入 Firefox 支援，可透過 WebDriver BiDi 協議控制 Firefox，Chrome 仍是主要支援與優化對象。
<!-- End AEO Capsule -->
<p>支援。Puppeteer 自 2023 年起逐步引入 Firefox 支援，現可透過 WebDriver BiDi 協議控制 Firefox 瀏覽器。Chrome 仍是主要支援與優化對象，Firefox 支援適用於需要跨瀏覽器驗證的測試場景。</p>
</div>

## 總結：Puppeteer 值得一試嗎？

<!-- AEO Answer Capsule — 約 75 字 -->
Puppeteer 是經過九年生產驗證的瀏覽器自動化標準工具，9.5 萬星標與每月穩定版本迭代證明其生態活力。對於需要網頁自動化、測試或 AI Agent 瀏覽操作的開發者，Puppeteer 提供成熟的 API、雙協議架構與官方 MCP 支援，值得納入技術選型考量。
<!-- End AEO Capsule -->

綜合來看，Puppeteer 的價值在於其「成熟度」與「生態位置」。作為瀏覽器自動化領域的先行者，它經歷了九年的大規模生產環境考驗，累積了完整的文件、社群支援與企業採用案例。雙協議架構使其在 Chrome 生態的深度整合與標準化跨瀏覽器支援之間取得平衡，而 MCP 伺服器的推出則確保它在 AI Agent 時代繼續保持相關性。

對於開發者而言，Puppeteer 的低學習門檻使其成為瀏覽器自動化入門的理想選擇；對於企業而言，Apache 2.0 授權與 Google 團隊的持續維護提供了穩定的長期依賴保障。隨著 AI Agent 逐漸成為網路應用的重要組成部分，Puppeteer 這類經過驗證的瀏覽器控制層，其戰略價值有望進一步提升。
