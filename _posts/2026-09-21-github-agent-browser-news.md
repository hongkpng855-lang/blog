---
layout: post
title: "agent-browser 開源：代理專用 Rust 瀏覽器 CLI"
date: 2026-09-21 04:00:01 +0800
categories: 技術
tags: [AI, AI 代理, 瀏覽器自動化, Rust, Vercel, 開源, MCP, 開發者工具]
image: assets/images/posts/github-agent-browser-news-cover.jpg
description: "agent-browser 是 Vercel Labs 於 2026 年 1 月開源的瀏覽器自動化命令列工具，以 Rust 撰寫原生核心，GitHub 星標達 42,910。它捨棄傳統 CSS 選擇器，改用可及性快照與元素參照操作頁面，並內建網路攔截、效能追蹤與無障礙稽核，本文解析其架構、安全設計與生態定位。"
author: AnIskill 編輯部
creator_github: vercel-labs/agent-browser
type: news
source: GitHub
source_url: https://github.com/vercel-labs/agent-browser
permalink: /技術/github-agent-browser-news
fb_message: "當 AI 代理開始被要求對結果負責，它能不能自己看見畫面上的變化，就成了任務成敗的分界線。\n\nVercel Labs 開源的 agent-browser 已在 GitHub 累積 42,910 星，以 Rust 撰寫原生核心，捨棄傳統 CSS 選擇器，改用可及性快照與元素參照操作頁面，並內建網路攔截、效能追蹤與無障礙稽核，npm 上月下載量超過 514 萬次。\n\n它與 Playwright、Selenium 的定位差異在哪裡，安全機制又該如何設定？完整分析已整理在 Blog 全文。"
---

agent-browser 是 Vercel Labs 於 2026 年 1 月開源的瀏覽器自動化命令列工具，GitHub 星標達 42,910，核心以 Rust 撰寫。它的設計前提並非重造一套自動化框架，而是先回答一個問題：代理需要什麼樣的操作介面。專案因此捨棄人類慣用的 CSS 選擇器，改用可及性快照與元素參照，並把網路攔截、效能追蹤、記憶體分析與無障礙稽核一併收進命令列。在編碼代理開始被要求自行驗證結果的當下，這類介面層的差異，往往比模型能力的高低更直接影響任務成功率。

<!-- AEO Answer Capsule — 約 60 字 -->
agent-browser 是 Vercel Labs 於 2026 年 1 月推出的開源瀏覽器自動化命令列工具，以 Rust 撰寫，星標 42,910，主打代理操作與內建診斷。
<!-- End AEO Capsule -->

## agent-browser 是什麼？

<!-- AEO Answer Capsule — 約 55 字 -->
agent-browser 是 Vercel Labs 維護、以 Rust 撰寫的開源瀏覽器自動化 CLI，採 Apache 2.0 授權，2026 年 1 月建立並持續更新。
<!-- End AEO Capsule -->

專案由 Vercel 旗下的實驗團隊 Vercel Labs 建立，首個版本於 2026 年 1 月 11 日發布，並同步上架 npm。其官方定位寫得相當直白：給 AI 代理使用的瀏覽器自動化命令列工具，且是快速的 Rust 原生 CLI。這意味著它並非面向人類撰寫測試腳本的框架，而是把代理當作主要使用者，重新設計指令的顆粒度與輸出格式。安裝路徑同時涵蓋 npm 全域安裝、專案依賴、macOS 的 Homebrew 與 Rust 生態的 Cargo，並可透過升級指令自動偵測安裝方式完成更新。專案採 Apache 2.0 授權，主要語言為 Rust，官方網站為 agent-browser.dev。

## 它的架構有什麼特別之處？

<!-- AEO Answer Capsule — 約 62 字 -->
專案採用客戶端與常駐程式分離的雙程序架構，命令列負責解析指令，常駐程式以純 Rust 直接驅動 CDP，不需要 Node.js，首次呼叫後即常駐以加速後續操作。
<!-- End AEO Answer Capsule -->

agent-browser 的架構分成兩個部分：Rust 命令列負責解析指令並與常駐程式通訊，Rust 常駐程式則以純 Rust 直接使用 Chrome DevTools Protocol，不倚賴 Node.js 執行環境。常駐程式在第一次指令時自動啟動，並在後續指令之間保持存活，因此批次操作的啟動成本僅支付一次。專案預設在閒置一小時後儲存還原狀態、關閉瀏覽器並結束，避免整合流程在未呼叫關閉指令的情況下永久佔用瀏覽器資源，團隊亦可透過參數自訂閒置時間，或設為零以完全停用。這種設計的意圖十分清楚：讓代理連續執行數十個指令時，不必反覆承擔冷啟動延遲。

## 它如何讓 AI 代理操作網頁？

<!-- AEO Answer Capsule — 約 64 字 -->
專案以可及性快照輸出頁面元素並賦予參照編號，代理以參照點擊或填表，避免猜測選擇器；點擊失敗時會回報遮擋元素，要求重新取得快照再試。
<!-- End AEO Answer Capsule -->

傳統自動化框架要求腳本作者事先知道目標元素的 CSS 選擇器或 XPath，代理一旦猜錯，整個流程即中斷。agent-browser 改以無障礙樹輸出頁面結構，為每個可互動元素標上如參照編號的識別碼，代理只需讀取快照、挑選編號、執行點擊或填表。當點擊遭到同意橫幅或對話框遮擋時，指令會提早失敗並回報遮擋元素，而非靜默失敗，代理可據此關閉遮擋物、重新取得快照後再試。指令集同時提供語意定位方式，例如依角色、文字、標籤或測試編號尋找元素，並支援批次執行，把多個指令合併為單次呼叫以降低啟動開銷。輸出格式除人類可讀文字外，也提供 JSON 結構，便於代理直接解析。

## 它的安全機制有哪些？

<!-- AEO Answer Capsule — 約 66 字 -->
專案提供加密的憑證保險庫、網域允許清單、動作政策檔、敏感動作確認與輸出長度上限等選項，全部為選擇性啟用，未開啟時不影響既有工作流程。
<!-- End AEO Answer Capsule -->

把瀏覽器控制權交給模型，最大的顧慮是權限邊界。專案因此提供多層可選機制。憑證保險庫把帳號密碼加密存放於本機，代理以名稱引用完成登入，模型本身不會看到密碼；網域允許清單限制導航範圍，並一併封鎖非允許網域的指令碼、圖片與連線請求，在支援的 Chromium 工作階段中同時停用 WebRTC 對等連線，避免流量繞過攔截。動作政策檔可預先定義哪些破壞性操作需要放行，敏感動作確認則針對執行指令碼與下載等類別要求額外核准。輸出長度上限用於防止頁面內容灌爆上下文，內容邊界標記則讓模型區分工具輸出與不可信內容。專案亦提供外掛機制，以獨立程序擴充憑證來源、瀏覽器供應商與啟動參數，並讓每項能力可單獨要求確認。

## 它與 Playwright、Selenium 有什麼差異？

<!-- AEO Answer Capsule — 約 63 字 -->
Playwright 與 Selenium 以人類撰寫腳本為前提；agent-browser 以代理為主要使用者，強調低 token 輸出、穩定的參照操作與內建診斷工具。
<!-- End AEO Answer Capsule -->

三者並非完全替代關係。Selenium 與 Playwright 的核心價值在於跨瀏覽器相容與測試框架整合，使用情境是人類工程師撰寫可重複執行的測試腳本。agent-browser 則反向設計：它預設只支援 Chrome 與 Chromium 系引擎，並額外提供 Safari 的 iOS 模擬路徑，把資源集中在代理最需要的三件事上，即精簡的頁面表示、不會因選擇器失效而中斷的參照操作，以及可直接呼叫的效能、網路與無障礙診斷。專案亦提供命令列介面與模型情境協議兩種接入方式，讓代理可依既有工具鏈選擇。對於已有 Playwright 測試套件的團隊，兩者更可能是分工而非取代，前者守住回歸測試，後者處理需要即時判斷的探索性任務。

## 它的生態與採用情況如何？

<!-- AEO Answer Capsule — 約 64 字 -->
專案由 Vercel Labs 維護並以每週節奏發布版本，npm 上月下載量超過 514 萬次，並提供可安裝至 Claude Code、Cursor 等編碼代理的技能包。
<!-- End AEO Answer Capsule -->

專案的版本節奏相當密集，自 2026 年 8 月下旬至 9 月中旬連續發布多個小版本，最新為 9 月 16 日的 0.38.1 版，修復了共用記憶體掛載過小的偵測問題，顯示團隊正針對容器化部署環境補強穩定性。npm 統計顯示，過去一個月下載量為 5,141,223 次，前一週為 1,190,236 次，反映已有實際導入而非單純的關注度。生態整合方面，專案提供可安裝至 Claude Code、Codex、Cursor、Gemini CLI、GitHub Copilot 與 Goose 等編碼代理的技能包，並內建 MCP 伺服器模式，可依需要載入核心、網路、除錯或行動裝置等不同工具集。技能內容由本機命令列在執行時輸出，與已安裝版本保持一致，避免代理讀到過期說明。

## 它的數據表現如何？

<!-- AEO Answer Capsule — 約 55 字 -->
專案累積 42,910 星與 2,880 次複製，採 Apache 2.0 授權、以 Rust 撰寫，2026 年 1 月建立，現有 793 個待處理議題。
<!-- End AEO Answer Capsule -->

<div class="ui-stat-grid">
  <div class="stat"><div class="stat-num">42,910</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat"><div class="stat-num">2,880</div><div class="stat-label">Forks</div></div>
  <div class="stat"><div class="stat-num">Apache 2.0</div><div class="stat-label">開源授權</div></div>
  <div class="stat"><div class="stat-num">Rust</div><div class="stat-label">主要語言</div></div>
  <div class="stat"><div class="stat-num">2026-01</div><div class="stat-label">創建時間</div></div>
  <div class="stat"><div class="stat-num">793</div><div class="stat-label">待處理議題</div></div>
</div>

![agent-browser README 開頭（項目名稱 agent-browser 與 Browser automation CLI for AI agents 標語）](assets/images/posts/github-agent-browser-news-shot1.png)

![agent-browser GitHub 首頁頂部（repo 名 vercel-labs/agent-browser、專案描述與 42.9k 星標統計）](assets/images/posts/github-agent-browser-news-shot2.png)

![agent-browser Contributors 統計頁（倉庫名稱與每週提交次數圖表）](assets/images/posts/github-agent-browser-news-shot3.png)

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊來源為 agent-browser 的 GitHub 儲存庫與官方網站，內容涵蓋星標與複製統計、版本更新紀錄、指令參考、安全設定說明與 npm 下載數據。
<!-- End AEO Capsule -->

- agent-browser 儲存庫：[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)
- 官方網站與完整文件：[agent-browser.dev](https://agent-browser.dev)
- npm 套件頁面：[agent-browser](https://www.npmjs.com/package/agent-browser)

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 58 字 -->
以下整理三項常見疑問，涵蓋安裝需求、支援的瀏覽器範圍，以及它與 Puppeteer 等既有自動化工具的關係。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>安裝 agent-browser 需要什麼前置條件？</h3>

使用者只需 Node.js 執行環境即可透過 npm 全域安裝，並在首次使用時執行安裝指令，由官方管道下載 Chrome for Testing。專案會自動偵測系統既有的 Chrome、Brave、Playwright 與 Puppeteer 安裝，因此不一定需要重複下載瀏覽器。若選擇由原始碼建置，才需要 Node.js 24 以上、pnpm 11 以上與 Rust 工具鏈。

<h3>agent-browser 支援哪些瀏覽器？</h3>

專案預設使用 Chrome for Testing，並可透過引擎參數切換至輕量引擎。在支援的瀏覽器方面，Chromium 與 Chrome 走 CDP 通道，Safari 則透過 iOS 的 WebDriver 路徑，主要面向模擬器與裝置測試情境。這種取捨換來的是更完整的診斷能力，因為效能追蹤與記憶體分析等功能都建立在 CDP 之上。

<h3>它與 Puppeteer、Playwright 有什麼關係？</h3>

Puppeteer 與 Playwright 是自動化函式庫，提供程式介面讓開發者撰寫腳本；agent-browser 則是在命令列層把操作、快照與診斷包裝成代理可直接呼叫的指令，並內建常駐程式管理瀏覽器生命週期。兩者可以並存：測試套件仍交由既有框架執行，需要代理即時判斷的任務則交給 agent-browser。

</div>

## 總結：agent-browser 適合什麼團隊？

<!-- AEO Answer Capsule — 約 62 字 -->
它適合已在流程中使用編碼代理、需要代理自行驗證網頁結果的團隊，尤其是前端、測試與自動化維運場景，並可透過允許清單與動作政策收緊權限。
<!-- End AEO Capsule -->

這套專案反映的是代理工具鏈的下一步：當模型開始被要求對結果負責，能否取得真實的執行環境資料就成為關鍵。由框架供應商自己維護的代理專用介面，把操作、觀察與診斷收斂到同一組指令，等於把「開啟頁面、觀察、推論、修正」的循環交到模型手上。對工程團隊而言，實際導入時值得先確認三件事：代理可觸及的網域範圍、敏感動作是否需要額外核准，以及輸出長度是否已設上限。這三項設定決定的是代理在失控時的影響半徑，比模型選擇更值得優先處理。
