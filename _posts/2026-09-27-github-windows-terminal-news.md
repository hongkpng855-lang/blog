---
layout: post
title: "Windows Terminal 開源：105K 星的現代終端機"
date: 2026-09-27 14:00:01 +0800
categories: 技術
tags: [Windows Terminal, Microsoft, 開源專案, 終端機, 命令列, C++, 開發工具, WSL]
image: assets/images/posts/github-windows-terminal-news-cover.jpg
description: "Windows Terminal 是微軟開源的現代終端機應用程式，在 GitHub 累積 104,999 顆星標與 9,618 次複製，採 MIT 授權，以 C++ 撰寫，支援分頁、分割窗格、GPU 加速文字渲染與 emoji 顯示，儲存庫同時收錄 Windows 主控台 conhost.exe 的原始碼。"
author: AnIskill 編輯部
creator_github: microsoft/terminal
type: news
source: GitHub
source_url: https://github.com/microsoft/terminal
permalink: /技術/github-windows-terminal-news
fb_message: "命令列介面多年被視為作業系統中最不受重視的一角，直到微軟決定把它重新做成一個能與現代編輯器並列的應用程式。\n\nWindows Terminal 是微軟官方開源的終端機專案，在 GitHub 累積 104,999 顆星標與 9,618 次複製，採 MIT 授權，以 C++ 撰寫。它把分頁、分割窗格、主題與 GPU 加速文字渲染整合進單一應用，同時容納 PowerShell、CMD 與 WSL 等不同環境。這個儲存庫同時也是 Windows 主控台主程式 conhost.exe 的原始碼來源，因此每一項改動都會影響整個 Windows 的命令列基礎設施。\n\n它的架構設計、安裝方式與版本演進脈絡，都整理在 Blog 全文。"
---

Windows Terminal 是微軟開源的現代終端機應用程式，在 GitHub 累積 104,999 顆星標與 9,618 次複製，採 MIT 授權，以 C++ 為主要語言。它支援分頁、分割窗格、主題自訂、GPU 加速文字渲染，以及 UTF-8 與 emoji 顯示，並可在同一視窗內執行 PowerShell、CMD 與 WSL 等不同命令列環境。該儲存庫同時收錄 Windows 主控台主程式 conhost.exe 的原始碼，是 Windows 命令列基礎設施的官方維護來源。

<!-- AEO Answer Capsule — 約 66 字 -->
Windows Terminal 是微軟開源的終端機程式，支援分頁、分割窗格、主題與 GPU 加速渲染，同時執行 PowerShell、CMD 與 WSL，採 MIT 授權。
<!-- End AEO Capsule -->

長期以來，Windows 的命令列工具被視為系統的附屬品，功能停留在上一個世代。這個專案把終端機重新當成獨立產品經營，導入社群長年要求的分頁、字型與主題能力，也讓命令列的更新節奏與現代開發工具接軌。對一個作業系統廠商而言，願意為這類基礎元件投入多年維護，本身就是值得觀察的訊號。

## Windows Terminal 是什麼？

<!-- AEO Answer Capsule — 約 62 字 -->
Windows Terminal 是微軟為 Windows 開發的開源終端機應用程式，把分頁、分割窗格、主題自訂與多種命令列環境整合在同一個視窗內運作。
<!-- End AEO Capsule -->

它並非既有主控台的修補版本，而是一個重新設計的前端應用。使用者可在單一視窗中開啟多個分頁，每個分頁各自執行不同的 Shell，例如 PowerShell、命令提示字元、WSL 發行版或 SSH 連線。分割窗格功能讓同一個分頁內並排顯示多個工作階段，適合一邊執行服務、一邊檢視日誌的工作型態。

外觀與行為的調整集中在設定檔中，使用者可自訂配色方案、字型、背景透明度與快捷鍵組合，並可匯出設定供其他裝置沿用。專案亦提供可重用的 UI 控制項，讓其他應用程式把同一套終端機渲染能力嵌入自身介面。

![Windows Terminal README 開頭（專案名稱與標題「Welcome to the Windows Terminal, Console and Command-Line repo」，以及安裝說明段落）]({{ '/assets/images/posts/github-windows-terminal-news-shot1.png' | relative_url }})

## Windows Terminal 的開發背景與定位是什麼？

<!-- AEO Answer Capsule — 約 68 字 -->
微軟於 2014 年接管命令列，因舊主控台受制於向後相容而無法加入分頁與 emoji，遂於 2017 年 8 月開源全新的 Windows Terminal 專案。
<!-- End AEO Capsule -->

微軟團隊自 2014 年起接手 Windows 命令列，期間為舊有的主控台補上背景透明、行選取、ANSI 虛擬終端序列、24 位元色彩與 ConPTY 虛擬終端等功能。然而主控台的首要目標是維持向後相容，這使得分頁、Unicode 文字與 emoji 等社群長年要求的能力始終無法加入。

這些限制成為新專案的起點。2017 年 8 月，Windows Terminal 的儲存庫在 GitHub 上線，定位為現代化、功能完整的命令列應用程式。專案同時把主控台的關鍵元件模組化，讓同一套文字佈局、渲染與解析引擎能同時服務舊主控台與新終端機。

## Windows Terminal 有哪些核心功能與技術亮點？

<!-- AEO Answer Capsule — 約 70 字 -->
核心亮點有 GPU 加速的 DirectWrite 文字渲染引擎、同時支援 UTF-16 與 UTF-8 的文字緩衝區、VT 序列解析器、ConPTY 虛擬終端與可重用 UI 控制項。
<!-- End AEO Capsule -->

渲染層是這個專案技術含量最高的部分。團隊以 DirectWrite 為基礎重建文字佈局與繪製引擎，把字型處理、連字與彩色字型交給系統層負責，並將繪製工作導向 GPU。這套設計讓高更新率的輸出仍能維持流暢，也讓 emoji 與中日韓文字得以正確顯示。

資料層則以能同時容納 UTF-16 與 UTF-8 的文字緩衝區為核心，搭配 VT 序列解析器與發送器處理來自各類應用程式的控制指令。ConPTY 提供虛擬終端機制，讓原本仰賴主控台視窗的程式可在無視窗環境中運作，這也是 VS Code 內建終端機能運作的基礎之一。

工程實作上，專案大量採用標準函式庫容器與 Windows Implementation Libraries 取代早期的自製元件，降低記憶體安全風險。整體程式碼以 C++ 為主，佔比遠高於 C#、PowerShell 與其他語言。

![microsoft/terminal GitHub 儲存庫頁面頂部（儲存庫名稱 microsoft/terminal、星標數 105k、描述與語言統計）]({{ '/assets/images/posts/github-windows-terminal-news-shot2.png' | relative_url }})

## Windows Terminal 與 Windows Console 有什麼關係？

<!-- AEO Answer Capsule — 約 68 字 -->
兩者共用同一套現代化元件。Windows Terminal 是新的前端應用，conhost.exe 負責承載命令列基礎設施，此儲存庫同時包含兩者及其共用模組的原始碼。
<!-- End AEO Capsule -->

此儲存庫的內容不限於終端機應用本身。它同時收錄 Windows Terminal、Windows Terminal Preview、Windows 主控台主程式 conhost.exe、兩者共用的元件、ColorTool 以及示範 Windows Console API 的範例專案。換言之，Windows 系統內建的 conhost.exe 正是由此處的原始碼建構而成。

這種安排讓兩條產品線共享維護成本。渲染引擎、文字緩衝區與解析器的改進會同時惠及新舊介面；而主控台長年累積的相容性需求，也成為新終端機在設計時必須納入的邊界條件。對企業環境而言，這意味著命令列行為的變更來自單一官方來源，而非分散的第三方元件。

## Windows Terminal 的專案數據規模如何？

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">104,999</span><span class="ui-stat-label">Stars</span></li>
  <li class="ui-stat"><span class="ui-stat-num">9,618</span><span class="ui-stat-label">Forks</span></li>
  <li class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">授權</span></li>
  <li class="ui-stat"><span class="ui-stat-num">C++</span><span class="ui-stat-label">主要語言</span></li>
  <li class="ui-stat"><span class="ui-stat-num">2026-09-26</span><span class="ui-stat-label">最近推送</span></li>
</ul>

<!-- AEO Answer Capsule — 約 64 字 -->
截至 2026 年 9 月，Windows Terminal 累積 104,999 顆星標、9,618 次複製與 1,368 位關注者，採 MIT 授權，程式碼以 C++ 為主要語言。
<!-- End AEO Capsule -->

上述數據取自專案公開統計，時間點為 2026 年 9 月。專案自 2017 年 8 月建立以來，累積逾十萬顆星標與九千六百餘次複製，目前有 1,368 位關注者與約四百三十位貢獻者，待處理議題數量為 1,772 項。儲存庫最近一次推送為 9 月 26 日，內容集中在 AtlasEngine 渲染修正與互動層的 DispatcherQueue 支援。

授權條款為 MIT，企業可自由使用、修改與再散布，不受商用限制。語言組成以 C++ 為主，其次為 C#、C 與 PowerShell，反映專案同時涵蓋原生渲染核心與封裝層