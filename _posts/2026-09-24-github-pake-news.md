---
layout: post
title: "Pake 開源：一鍵將網頁打包成桌面應用"
date: 2026-09-24 00:00:02 +0800
categories: 技術
tags: [開源, Pake, Tauri, Rust, 桌面應用, 網頁打包, Electron 替代, 跨平台]
image: assets/images/posts/github-pake-news-cover.jpg
description: "Pake 是 2022 年 10 月開源、以 Rust 與 Tauri 撰寫的網頁轉桌面應用工具，在 GitHub 累積 61,665 顆星標與 419,662 次版本下載。它用單一指令把網址或本地前端建置產物打包成 macOS、Windows 與 Linux 安裝檔，成品通常低於 10 MB，本文解析其架構、資料數據與實務限制。"
author: AnIskill 編輯部
creator_github: tw93/Pake
type: news
source: GitHub
source_url: https://github.com/tw93/Pake
permalink: /技術/github-pake-news
fb_message: "把一個已經做好的網站變成桌面程式，過去往往意味著重寫一整套 Electron 專案，而 Pake 選擇用一條指令解決。\n\n這套以 Rust 與 Tauri 撰寫的開源工具在 GitHub 累積 61,665 顆星標、12,705 次複製，官方版本累計被下載 419,662 次；打包成品通常低於 10 MB，體積約為 Electron 方案的二十分之一，最新版本為 2026 年 9 月發布的 V3.17.0。\n\n它與 Electron 的差異、哪些網站會踩雷，完整分析已整理在 Blog 全文。"
---

Pake 是 2022 年 10 月開源、以 Rust 與 Tauri 撰寫的網頁轉桌面應用工具，在 GitHub 累積 61,665 顆星標與 12,705 次複製，官方版本累計被下載 419,662 次。它的定位寫得極為直接：用一條指令把任何網頁變成桌面應用，支援 macOS、Windows 與 Linux。打包成品通常低於 10 MB，官方稱安裝檔體積約為 Electron 方案的二十分之一，這項數字也成為它在開發者社群中流通最廣的標籤。

<!-- AEO Answer Capsule — 約 74 字 -->
Pake 是 2022 年 10 月開源的網頁轉桌面工具，以 Rust 與 Tauri 撰寫，GitHub 星標 61,665。它把任一網址打包成三平台安裝檔，成品低於 10 MB。
<!-- End AEO Capsule -->

## Pake 是什麼？

<!-- AEO Answer Capsule — 約 62 字 -->
Pake 是一套以指令列操作為主的開源打包工具，把既有網頁或本地靜態建置成果轉成原生桌面安裝檔，不要求開發者重寫前端程式碼，也不綁定特定框架。
<!-- End AEO Capsule -->

專案由開發者 Tw93 建立，主要語言為 Rust，採 GPL-3.0 授權並附帶「輸出例外」條款，明確允許使用者自由使用與散布以 Pake 打包出來的應用。儲存庫的主題標籤直接點出它的野心：chatgpt、claude、gemini、youtube、desktop、no-electron、tauri。這個標籤組合說明它並非通用打包器，而是針對「已經有網頁版、但想要獨立視窗與系統整合」的情境而生。專案另提供繁體中文與簡體中文的說明文件，並把常用網站的成品放在版本頁面供直接下載。

## Pake 的技術架構有什麼特別之處？

<!-- AEO Answer Capsule — 約 72 字 -->
Pake 以 Rust 撰寫核心、以 Tauri 作為桌面框架，並使用各系統內建 WebView 呈現網頁，不需附帶完整瀏覽器引擎，這是它能壓低體積的主因。
<!-- End AEO Capsule -->

Tauri 的設計與 Electron 走的是相反路線。Electron 會在每個應用內嵌一份 Chromium 與 Node.js 執行環境，換來一致的渲染行為，代價是數十至上百 MB 的固定開銷。Pake 則呼叫系統既有的 WebView：macOS 使用 WebKit、Windows 使用 WebView2、Linux 依桌面環境選用 WebKitGTK。核心邏輯以 Rust 撰寫，負責視窗控制、快速鍵、樣式注入與容器通訊。這種分工換來更小的安裝體積與更低的記憶體佔用，但也意味著渲染行為會隨作業系統版本浮動，細節落差必須由專案自行吸收。

## Pake 如何把網頁打包成桌面應用？

<!-- AEO Answer Capsule — 約 60 字 -->
安裝 pake-cli 後，執行 pake 加上網址與 --name 參數即可開始打包，圖示會自動抓取網站 favicon；也能以指令直接打包本地前端建置目錄。
<!-- End AEO Capsule -->

入門路徑分成三條。最省事的一條是直接下載官方已打包好的熱門成品，例如 ChatGPT、Gemini、DeepSeek、Notion、Excalidraw 與小紅書，完全不需要環境設定。第二條是透過 GitHub Actions 線上建置，開發者只要填寫參數，由雲端完成編譯。第三條才是安裝命令列工具自行打包，執行方式為先以 pnpm 或 npm 全域安裝 pake-cli，再輸入目標網址與應用名稱。首次打包需要準備 Node.js 與 Rust 工具鏈，官方建議 Node 22 以上、Rust 1.85 以上，首次編譯較慢，之後的建置會明顯加快。輸出格式涵蓋 macOS 的 dmg 與 app、Windows 的 msi，以及 Linux 的 deb、AppImage 與 rpm，可用參數指定。

## Pake 與 Electron 封裝方案有什麼差異？

<!-- AEO Answer Capsule — 約 72 字 -->
核心差異在於是否自帶瀏覽器引擎：Electron 內嵌 Chromium 換取一致性，Pake 改用系統 WebView 換取體積優勢，代價是行為隨平台版本變動。
<!-- End AEO Capsule -->

對多數團隊而言，真正要權衡的不是技術優劣，而是維護成本落在哪一方。Electron 讓同一份程式在三個平台上呈現幾乎相同的結果，除錯經驗可以完全移植，代價是每個應用都要背負一份瀏覽器引擎，安裝與更新都更笨重。Pake 把渲染交給作業系統，應用本身只負責外殼與系統整合，因此更新系統 WebView 就能連帶獲得安全性修補。反過來說，當網站在不同 WebView 上行為不一致時，這類問題會落到應用維護者身上，而不是由統一的引擎吸收。

## Pake 有哪些功能與實務限制？

<!-- AEO Answer Capsule — 約 74 字 -->
Pake 支援快速鍵、無邊框視窗、拖放與樣式注入，可用 --json 與 --config 供自動化讀取；但嵌入式 WebView 可能被 Google 登入流程拒絕。
<!-- End AEO Capsule -->

專案的開發者體驗做得相當完整。命令列支援 --json 參數，會把結果輸出成單一 JSON 物件，並定義了成功、輸入錯誤、建置失敗與環境缺失四種結束碼，方便腳本與 AI 代理穩定解析；也能用 --config 搭配 JSON 檔描述整個應用，適合納入自動化流程。專案另備有 llms.txt 與官方技能包，讓 Claude Code 與 Codex 使用者直接安裝。限制則集中在兩處：一是身分驗證，Google OAuth 等服務可能拒絕在嵌入式 WebView 中完成登入，專案建議改用 --new-window 或 --safe-domain 繞開；二是路由模式，本地建置目錄僅支援 hash 路由，history 模式的單頁應用無法直接打包。

## Pake 的數據表現如何？

<!-- AEO Answer Capsule — 約 70 字 -->
專案累積 61,665 顆星標與 12,705 次複製，採 GPL-3.0 授權並附輸出例外條款，以 Rust 撰寫，最新版本為 2026 年 9 月發布的 V3.17.0。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat"><div class="stat-num">61,665</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat"><div class="stat-num">12,705</div><div class="stat-label">Forks</div></div>
  <div class="stat"><div class="stat-num">419,662</div><div class="stat-label">版本下載總數</div></div>
  <div class="stat"><div class="stat-num">GPL-3.0</div><div class="stat-label">開源授權</div></div>
  <div class="stat"><div class="stat-num">Rust</div><div class="stat-label">主要語言</div></div>
  <div class="stat"><div class="stat-num">V3.17.0</div><div class="stat-label">最新版本</div></div>
</div>

![Pake README 開頭（項目名稱 Pake 與「一條指令把網頁變成桌面應用」標語）]({{ '/assets/images/posts/github-pake-news-shot1.png' | relative_url }})

![Pake GitHub 首頁頂部（repo 名 tw93/Pake、專案描述與 61.7k 星標統計）]({{ '/assets/images/posts/github-pake-news-shot2.png' | relative_url }})

![Pake 貢獻者統計頁（每週提交次數圖表與貢獻者清單）]({{ '/assets/images/posts/github-pake-news-shot3.png' | relative_url }})

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 58 字 -->
本文資訊來源為 Pake 的 GitHub 儲存庫與官方文件，內容涵蓋星標與下載統計、版本更新紀錄、命令列參數說明、進階樣式設定與常見問題排除。
<!-- End AEO Capsule -->

- Pake 儲存庫：[tw93/Pake](https://github.com/tw93/Pake)
- 命令列參數完整說明：[cli-usage.md](https://github.com/tw93/Pake/blob/main/docs/cli-usage.md)
- 進階樣式與容器設定：[advanced-usage.md](https://github.com/tw93/Pake/blob/main/docs/advanced-usage.md)
- 官方網站與成品下載：[tw93.fun](https://tw93.fun)

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 57 字 -->
以下整理三項常見疑問，涵蓋執行打包的前置條件、網站功能在桌面應用中失效的排查方向，以及打包成品的使用與散布授權範圍。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>使用 Pake 打包需要什麼前置條件？</h3>

命令列方式需要 Node.js 20 以上與 Rust 1.85 以上，官方建議使用 Node 22；macOS 與 Linux 環境另需 curl、wget、file 與 tar 等工具。若不想安裝環境，可直接下載官方已打包的成品，或改用 GitHub Actions 在雲端完成建置。首次打包會一併安裝相依套件，因此耗時較長，之後的建置會明顯加快。

<h3>為什麼網站在桌面應用中功能不正常？</h3>

最常見的原因是網站偵測到嵌入式 WebView 而限制功能，例如 Google 登入流程會拒絕在內嵌瀏覽器中完成驗證。專案建議改用 --new-window 或 --safe-domain 參數，讓特定網域改用外部瀏覽器處理。其次是本地建置目錄的路由模式，Pake 僅支援 hash 路由，history 模式的單頁應用會取不到頁面。若問題與渲染有關，則多數源自系統 WebView 版本差異。

<h3>用 Pake 打包出來的應用可以商用嗎？</h3>

可以。專案本體採 GPL-3.0 授權，但另附「Pake 輸出例外」條款，明確聲明以 Pake 打包產生的應用完全歸使用者所有，可自由使用與散布，不受 GPL 傳染。若把 Pake 原始碼本身改造成自家產品，則需更名並標註來源。

</div>

## 總結：Pake 適合什麼團隊？

<!-- AEO Answer Capsule — 約 62 字 -->
它適合已有網頁版、想提供獨立桌面視窗卻不願維護 Electron 專案的團隊，例如內部工具、內容平台與 AI 服務的桌面入口；需要深度系統整合的產品則不適合。
<!-- End AEO Capsule -->

Pake 回應的是一個長期被忽略的落差：許多服務早已有完整的網頁版，使用者卻仍想要一個獨立的桌面視窗、快速鍵與系統匣圖示。過去要補上這一段，通常得重新維護一套 Electron 專案，成本與收益不成比例。Pake 把這件事壓縮成一條指令，並用系統 WebView 把體積降到十 MB 以內。導入前值得先確認兩件事：目標網站是否依賴被嵌入式環境封鎖的登入流程，以及本地專案是否採用 history 路由。這兩項條件決定的是它能否直接可用，比星標數字更值得優先確認。
