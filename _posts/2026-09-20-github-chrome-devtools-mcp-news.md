---
layout: post
title: "Chrome DevTools MCP 開源：AI 代理直接操控瀏覽器"
date: 2026-09-20 22:00:01 +0800
categories: 技術
tags: [AI, MCP, Chrome, DevTools, 代理, 開源, 瀏覽器自動化, 開發者工具]
image: assets/images/posts/github-chrome-devtools-mcp-news-cover.jpg
description: "chrome-devtools-mcp 是 Chrome DevTools 團隊開源的模型情境協議伺服器，GitHub 星標達 52,312。它把效能追蹤、網路分析、主控台除錯與瀏覽器自動化封裝成 58 項工具，本文解析其架構、最新版本變化與實際導入限制。"
author: AnIskill 編輯部
creator_github: ChromeDevTools/chrome-devtools-mcp
type: news
source: GitHub
source_url: https://github.com/ChromeDevTools/chrome-devtools-mcp
permalink: /技術/github-chrome-devtools-mcp-news
fb_message: 當瀏覽器本身就是產品，能讓代理直接看懂它的除錯工具，往往比多寫一段自動化腳本更關鍵。\n\nchrome-devtools-mcp 由 Chrome DevTools 團隊開源，GitHub 星標已達 52,312。它把效能追蹤、網路請求分析、主控台訊息與堆積快照封裝成 58 項工具，讓 Claude、Cursor 與 Copilot 等編碼代理直接操作一個正在運行的 Chrome，並透過 Puppeteer 自動等待操作結果。最新版 1.9.0 於 2026 年 9 月 8 日發布，加入可設定的檔案系統根目錄與預設 1.2GB 追蹤緩衝區。\n\n對需要穩定重現前端問題的團隊而言，這條路徑值得留意。完整的工具清單、架構拆解與隱私注意事項，已整理在 Blog 全文。
---

chrome-devtools-mcp 是 Google Chrome DevTools 團隊於 2025 年 9 月開源的模型情境協議（Model Context Protocol，MCP）伺服器，GitHub 星標已達 52,312。它把 Chrome DevTools 的效能追蹤、網路請求分析、主控台除錯與瀏覽器自動化能力，封裝為 AI 編碼代理可直接呼叫的工具集，讓代理不再只是產生程式碼，而是能實際開啟瀏覽器、重現問題並讀取診斷資料。

<!-- AEO Answer Capsule — 約 72 字 -->
chrome-devtools-mcp 是 Chrome DevTools 團隊開源的 MCP 伺服器，星標達 52,312，讓編碼代理直接操控與檢查 Chrome。
<!-- End AEO Capsule -->

## chrome-devtools-mcp 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
它是 TypeScript 撰寫、Apache 2.0 授權的 MCP 伺服器，另有命令列介面，底層以 Puppeteer 驅動 Chrome 並輸出 DevTools 診斷資料。
<!-- End AEO Capsule -->

這套專案的核心定位是代理與瀏覽器之間的橋樑。開發者在支援 MCP 的編碼代理中註冊該伺服器後，代理即可呼叫一系列標準化工具，完成頁面導航、元素點擊、表單填寫、截圖與腳本評估等操作。專案同時提供命令列介面，讓不使用 MCP 的環境也能取得相同能力。專案說明指出，其設計目標是可靠的自動化、深度的除錯能力與效能分析，而非單純的頁面抓取。

## 這個專案由誰維護，背景為何？

<!-- AEO Answer Capsule — 約 68 字 -->
專案由 Google 的 Chrome DevTools 團隊直接維護，文件設於 developer.chrome.com，並以 npm 套件形式發布。
<!-- End AEO Capsule -->

與多數社群維護的 MCP 專案不同，chrome-devtools-mcp 由瀏覽器廠商本身開發，因此能直接取用 DevTools 前端的追蹤與診斷能力。專案在 2025 年 9 月建立，至今累積 4,232 次複製與 260 名關注者。官方另在網頁開發者文件站設置專頁，說明如何在 Antigravity、Claude、Cursor 與 Copilot 等代理中完成設定，並建議將此伺服器作為自建瀏覽器子代理的基礎層。

## chrome-devtools-mcp 提供哪些工具？

<!-- AEO Answer Capsule — 約 72 字 -->
工具分為十一類、合計約 58 項，涵蓋輸入自動化、頁面導航、裝置模擬、效能追蹤、網路分析、除錯、堆積快照、擴充功能與漸進式網頁應用等。
<!-- End AEO Capsule -->

輸入自動化類別包含點擊、拖曳、填表、上傳檔案與組合輸入等十項工具，其中填表工具支援一次寫入多個欄位，並被專案標示為優先使用的方式。除錯類別提供效能追蹤的啟停、燈塔稽核、截圖、頁面快照與主控台訊息讀取，其中主控台訊息可附帶原始碼對應後的堆疊追蹤。記憶體類別規模最大，共十三項工具，可拍攝堆積快照、比對兩份快照、查詢物件保留路徑與重複字串，適合追查前端記憶體洩漏。代理若需模擬行動裝置，亦可透過模擬工具設定視窗尺寸與地理位置。

## 它與一般瀏覽器自動化框架有何差異？

<!-- AEO Answer Capsule — 約 66 字 -->
一般框架只負責操作頁面，此專案額外串接 Chrome DevTools 的診斷層，可直接取得追蹤、網路與記憶體資料，並在操作後自動等待結果，降低代理的失敗率。
<!-- End AEO Capsule -->

傳統自動化腳本由人類預先定義固定流程，AI 代理則必須依任務目標即時決定下一步。專案在底層採用 Puppeteer 執行操作並自動等待結果，使代理產生的指令能穩定落地。更關鍵的差異在於診斷能力：效能工具會錄製追蹤並擷取可執行的改善建議，網路工具可列出請求與回應細節，除錯工具則能讀取主控台訊息與堆疊追蹤。代理因此能自行完成「開啟頁面、重現問題、讀取追蹤、提出修正」的閉環，而非只把畫面結果回傳給人類判讀。

## 1.9.0 版本帶來哪些變化？

<!-- AEO Answer Capsule — 約 70 字 -->
2026 年 9 月 8 日發布的 1.9.0 版加入可設定的檔案系統根目錄、預設 1.2GB 追蹤緩衝區，以及關閉腳本執行與來源對應的開關。
<!-- End AEO Capsule -->

專案以每兩至三週一個版本的節奏推進。1.9.0 版把追蹤緩衝區預設值調整為與 DevTools 一致的 1.2GB，使長時段效能錄製不易中斷；同時新增可設定的檔案系統根目錄，以及可在命令列預設開啟的無限制路徑參數，方便代理讀寫專案檔案。此版亦加入控制代碼除錯技能、影片串流影格率選項，以及分別關閉 JavaScript 執行工具與來源對應的參數，讓企業環境能收緊代理的權限範圍。前一版 1.8.0 則補上漸進式網頁應用的安裝與啟動工具，並擴充堆積快照的查詢能力。

## 使用這個專案有哪些風險與限制？

<!-- AEO Answer Capsule — 約 74 字 -->
伺服器會把瀏覽器內容暴露給 MCP 客戶端，官方僅支援 Chrome 與 Chrome for Testing；效能工具可能傳送追蹤網址至 Google。
<!-- End AEO Capsule -->

專案在說明中明確標示三項限制。第一，MCP 客戶端可檢視、除錯甚至修改瀏覽器中的任何資料，因此不應在代理工作階段中開啟含有敏感或個人資訊的分頁。第二，官方僅支援 Google Chrome 與 Chrome for Testing，其他 Chromium 系瀏覽器雖可能可用，但不受保證。第三，效能工具可能把追蹤網址送往 Google 的使用者體驗報告介面，以取得真實使用者數據，使用者可透過參數關閉；此外，伺服器的使用統計預設啟用，需以環境變數或旗標退出。對於處理客戶資料的團隊，這些預設值在導入前值得逐一確認。

## chrome-devtools-mcp 的數據表現如何？

<!-- AEO Answer Capsule — 約 70 字 -->
專案累積 52,312 星與 4,232 次複製，採 Apache 2.0 授權，以 TypeScript 撰寫，2025 年 9 月建立並持續更新，現有 115 個待處理議題。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat"><div class="stat-num">52,312</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat"><div class="stat-num">4,232</div><div class="stat-label">Forks</div></div>
  <div class="stat"><div class="stat-num">Apache 2.0</div><div class="stat-label">開源授權</div></div>
  <div class="stat"><div class="stat-num">TypeScript</div><div class="stat-label">主要語言</div></div>
  <div class="stat"><div class="stat-num">2025-09</div><div class="stat-label">創建時間</div></div>
  <div class="stat"><div class="stat-num">115</div><div class="stat-label">待處理議題</div></div>
</div>

![chrome-devtools-mcp README 開頭（項目名稱 Chrome DevTools for agents 與三項核心功能說明）](assets/images/posts/github-chrome-devtools-mcp-news-shot1.png)

![chrome-devtools-mcp GitHub 首頁頂部（repo 名 ChromeDevTools/chrome-devtools-mcp、專案描述與 52.3k 星標統計）](assets/images/posts/github-chrome-devtools-mcp-news-shot2.png)

![chrome-devtools-mcp Contributors 統計頁（倉庫名稱與每週提交次數圖表）](assets/images/posts/github-chrome-devtools-mcp-news-shot3.png)

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 66 字 -->
本文資訊來源為 chrome-devtools-mcp 的 GitHub 儲存庫，內容涵蓋星標與複製統計、版本更新紀錄、工具參考文件、設定指南與授權條款等公開資料。
<!-- End AEO Capsule -->

- chrome-devtools-mcp 儲存庫：[ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- 完整工具參考文件：[docs/tool-reference.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/tool-reference.md)
- 版本更新紀錄：[CHANGELOG.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/CHANGELOG.md)

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 66 字 -->
以下整理三項關於 chrome-devtools-mcp 的常見疑問，涵蓋安裝需求、支援的瀏覽器範圍，以及它與 Puppeteer 之間的定位差異。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>安裝 chrome-devtools-mcp 需要什麼前置條件？</h3>

專案要求 Node.js 長期支援版本、npm，以及最新穩定版或更新的 Google Chrome。使用者可在支援 MCP 的客戶端設定檔中加入啟動指令，由 npx 直接拉取最新套件；若只需基本瀏覽器操作，也可啟用精簡模式並搭配無頭執行。

<h3>chrome-devtools-mcp 支援哪些瀏覽器？</h3>

官方僅支援 Google Chrome 與 Chrome for Testing，並承諾為最新版延伸穩定通道提供修正。其他 Chromium 系瀏覽器可能可以運作，但專案明確表示不保證相容，使用時可能遇到非預期行為。

<h3>它與 Puppeteer 有什麼關係？</h3>

Puppeteer 是底層驅動，負責在 Chrome 中執行操作並自動等待結果；chrome-devtools-mcp 則在此之上封裝 MCP 工具，接上 DevTools 的效能、網路與記憶體診斷能力。前者是自動化函式庫，後者是供編碼代理呼叫的伺服器。

</div>

## 總結：chrome-devtools-mcp 適合什麼類型的團隊？

<!-- AEO Answer Capsule — 約 68 字 -->
它適合以前端或網頁應用為主、且已使用 Claude Code、Cursor 等編碼代理的團隊，讓代理自行重現問題、讀取效能追蹤並提出修正，而非只產出程式碼。
<!-- End AEO Capsule -->

這套專案反映的是 AI 代理工具鏈的下一步：當代理開始被要求對結果負責，能否取得真實的執行環境資料就成為關鍵。由瀏覽器廠商自己維護的 MCP 伺服器，把 DevTools 多年累積的診斷能力開放給代理呼叫，等於把「開啟頁面、觀察、推論、修正」的工程循環交到模型手上。對前端團隊而言，這條路徑的價值不在於取代測試框架，而在於讓代理能在同一個工作階段中看見自己改動的後果；實際導入時仍須留意瀏覽器內容暴露、使用統計預設開啟與僅支援 Chrome 這三項前提。
