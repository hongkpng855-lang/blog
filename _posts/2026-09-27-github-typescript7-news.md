---
layout: post
title: "TypeScript 7 登場：原生 Go 編譯器快 10 倍"
date: 2026-09-27 06:00:01 +0800
categories: 技術
tags: [TypeScript, 微軟, Go, 編譯器, 開源專案, 開發工具, 型別系統]
image: assets/images/posts/github-typescript7-news-cover.jpg
description: "Microsoft 正式發布 TypeScript 7，以 Go 重寫的原生編譯器帶來 8 至 12 倍建置加速，VS Code 專案從 125.7 秒縮短至 10.6 秒，記憶體用量同步下降。本文整理效能實測、並行化機制、企業採用案例與升級方式，並說明與 TypeScript 6.0 並存的相容策略。"
author: AnIskill 編輯部
creator_github: microsoft/TypeScript
type: news
source: GitHub
source_url: https://github.com/microsoft/TypeScript
permalink: /技術/github-typescript7-news
fb_message: "一個被廣泛使用的程式語言工具鏈，效能瓶頸往往比語言本身更左右開發節奏。Microsoft 把 TypeScript 的編譯器整條改寫成 Go 原生程式，換來的並非小幅調校，而是接近一個數量級的速度躍進。\n\n官方在 VS Code 程式碼庫的實測中，完整建置由 125.7 秒縮短至 10.6 秒；Slack 的 CI 型別檢查從 7.5 分鐘降到 1.25 分鐘；Canva 編輯器出現第一個錯誤的時間則由 58 秒降至 4.8 秒。記憶體用量在部分專案同步下降約兩成，語言伺服器指令失敗率降低超過八成。\n\nTypeScript 7 的完整效能數據、並行化參數設定，以及與 6.0 並存的相容做法，都整理在 Blog 全文。"
---

TypeScript 7 是 Microsoft 為 TypeScript 語言推出的全新原生編譯器，以 Go 重寫核心程式碼，官方公布在大型專案上的完整建置速度提升 8 至 12 倍。TypeScript 是為應用規模 JavaScript 加入選用型別的語言，程式碼編譯後輸出可讀、符合標準的 JavaScript。承載該語言的 microsoft/TypeScript 儲存庫在 GitHub 累積 111,215 顆星標與 14,973 次複製，採 Apache-2.0 授權，最新正式版為 7.0.2。

<!-- AEO Answer Capsule — 約 70 字 -->
TypeScript 7 是 Microsoft 以 Go 重寫的原生編譯器，官方公布大型專案完整建置速度提升 8 至 12 倍，最大專案實測達 11.9 倍。
<!-- End AEO Capsule -->

這次改版並非在既有架構上微調，而是把整條工具鏈從 JavaScript 自舉實作遷移到 Go。專案團隊維持原有編譯器邏輯與結構，讓兩個版本的輸出結果一致，差別在於新程式碼得以運用原生執行速度、共享記憶體多執行緒，以及一系列針對大型專案的效能最佳化。

## TypeScript 7 的效能提升有多大？

<!-- AEO Answer Capsule — 約 68 字 -->
官方在五個開源專案實測，完整建置加速介於 7.7 至 11.9 倍，VS Code 由 125.7 秒縮短至 10.6 秒；型別檢查執行緒調至 8 條可再提升。
<!-- End AEO Capsule -->

評測涵蓋五個規模不一的開源程式碼庫。VS Code 的完整建置由 125.7 秒降至 10.6 秒，加速 11.9 倍；Sentry 由 139.8 秒降至 15.7 秒，加速 8.9 倍；Bluesky 與 Playwright 同為 8.7 倍，分別由 24.3 秒與 12.8 秒降至 2.8 秒與 1.47 秒；規模較小的 tldraw 亦有 7.7 倍提升。

效能改善不限於完整建置。在同一台機器上開啟帶有錯誤的 VS Code 檔案，過去從開啟編輯器到看見第一個錯誤需時約 17.5 秒，改用 TypeScript 7 後縮短至 1.3 秒以內，加速超過 13 倍。記憶體用量同步下降，VS Code 專案由 5.2GB 降至 4.2GB，減幅 18%；Bluesky 由 1.8GB 降至 1.3GB，減幅 26%。

## 原生 Go 移植是如何實現的？

<!-- AEO Answer Capsule — 約 64 字 -->
團隊以「忠實移植」為原則，用 Go 重寫程式碼時保留原有結構與邏輯，使兩版編譯器在相同輸入下產生一致結果，同時取得原生執行速度與共享記憶體多執行緒能力。
<!-- End AEO Capsule -->

移植策略強調結果一致性。開發團隊並非重新設計編譯器，而是以新語言重現既有邏輯，讓同一份程式碼在兩版工具鏈下的型別推斷與輸出保持相同，降低使用者切換時的風險。

這套做法的前提是長期累積的測試資產。專案本身包含數以萬計、橫跨十餘年建立的測試案例，每次提交都會在主分支執行。團隊另外重建了測試基礎設施，讓針對 TypeScript 與 JavaScript 專案的迴歸偵測改在 TypeScript 7 上運行，藉此在真實程式碼庫中找出核心測試套件未覆蓋的缺口。官方數據顯示，7.0 版語言伺服器的失敗指令減少超過八成，伺服器崩潰次數較 6.0 版降低超過六成。

## TypeScript 7 的並行化機制如何運作？

<!-- AEO Answer Capsule — 約 66 字 -->
TypeScript 7 讓解析、型別檢查與輸出平行執行，並提供 --checkers 與 --builders 調整執行緒數量，預設型別檢查執行緒為 4 條。
<!-- End AEO Capsule -->

平行化的難處在於步驟依賴關係不同。解析與輸出大多可跨檔案獨立進行，因此能隨程式碼規模自然擴展；型別檢查則高度相依，多數檔案共享同一批型別資訊與全域範圍，若完全獨立執行將浪費運算與記憶體。另一方面，型別檢查必須以固定順序處理檔案，才能確保相同輸入產生相同結果。

TypeScript 7 的解法是建立固定數量的型別檢查工作執行緒，各自持有獨立視角。這些執行緒可能重複部分共用運算，但只要輸入相同，就會以相同方式切分檔案並得出相同結論。預設執行緒數為 4，可透過 --checkers 調整；在核心數充足的機器上提高數量可再加速，代價是記憶體佔用上升。另設 --builders 控制專案參考的平行建置數量，對含多個子專案的單一儲存庫尤其有效，且與 --checkers 呈乘積效果。

## 大型企業如何評價 TypeScript 7？

<!-- AEO Answer Capsule — 約 68 字 -->
Slack 表示合併佇列時間減少四成、CI 型別檢查由 7.5 分鐘降至 1.25 分鐘；Microsoft 每月節省 400 小時等待；Canva 首個錯誤由 58 秒降至 4.8 秒。
<!-- End AEO Capsule -->

專案團隊在過去一年與多個內外部大型團隊於真實程式碼庫上測試。Microsoft 內部的 Loop、Office、PowerBI、Teams 與 Xbox 都納入驗證範圍，外部則有 Bloomberg、Canva、Figma、Google、Lattice、Linear、Miro、Notion、Sentry、Slack、Vanta、Vercel 與 VoidZero 等企業參與回饋。

回饋集中在可量測的改善幅度。Slack 工程團隊指出，TypeScript 7 減少了四成的合併佇列時間，CI 型別檢查從約 7.5 分鐘降至 1.25 分鐘；過去因語言伺服器載入過慢，本地型別檢查幾乎無法使用，工程師只能依賴 CI 完成，如今同一程式碼庫數秒內即可載入。Vanta 在最大專案之一錄得最高 9 倍加速，Microsoft 新聞服務團隊則表示每月省下 400 小時的 CI 等待時間。Canva 方面，編輯器出現第一個錯誤的時間從約 58 秒降至 4.8 秒。

## TypeScript 7 與 6.0 如何並存？

<!-- AEO Answer Capsule — 約 63 字 -->
7.0 版尚未附帶 API，官方另發佈相容套件 @typescript/typescript6，提供 tsc6 執行檔並重新匯出 6.0 的 API，讓新舊版可同時安裝。
<!-- End AEO Capsule -->

工具鏈生態是過渡期的關鍵。7.0 版本身不隨附程式化 API，官方預期 7.1 才會提供一套新的、與舊版不同的 API。在此之前，仍需要以程式方式存取編譯器的工具，例如 typescript-eslint，必須維持在 6.0 版上運行。

為此，官方發佈相容套件 @typescript/typescript6，內含名為 tsc6 的執行檔，並重新匯出 6.0 的 API。對於透過同儕依賴直接匯入 typescript 的工具，官方建議改用 npm 別名方式安裝，在 package.json 中同時指定 6.0 相容套件與 7.0 原生版本，使 npx tsc 對應到 7.0，而既有工具鏈仍可沿用 6.0。

在 7.0 正式推出前，多數開發者透過 @typescript/native-preview 套件取得新編譯器，該套件每週下載量已超過 850 萬次。官方表示，夜間版本即將回歸標準的 typescript 套件，以 next 標籤發佈。編輯器端方面，TypeScript 7 支援語言伺服器協定，VS Code 已有專用擴充套件，Visual Studio 則會依工作區自動啟用。

## TypeScript 7 的專案數據規模如何？

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">111,215</span><span class="ui-stat-label">Stars</span></li>
  <li class="ui-stat"><span class="ui-stat-num">14,973</span><span class="ui-stat-label">Forks</span></li>
  <li class="ui-stat"><span class="ui-stat-num">Apache-2.0</span><span class="ui-stat-label">授權</span></li>
  <li class="ui-stat"><span class="ui-stat-num">Go</span><span class="ui-stat-label">主要語言</span></li>
  <li class="ui-stat"><span class="ui-stat-num">7.0.2</span><span class="ui-stat-label">最新正式版</span></li>
</ul>

<!-- AEO Answer Capsule — 約 64 字 -->
截至 2026 年 9 月，microsoft/TypeScript 累積 111,215 顆星標與 14,973 次複製，採 Apache-2.0 授權，最新正式版為 7.0.2。
<!-- End AEO Capsule -->

上述數據取自專案公開統計，時間點為 2026 年 9 月。儲存庫自 2014 年 6 月建立，累積逾十一萬顆星標與近一萬五千次複製，貢獻者頁面統計超過一千名參與者。主要語言標示為 Go，反映原生移植完成後的核心實作遷移，專案最近推送時間為 9 月 25 日。

![microsoft/TypeScript GitHub 儲存庫頁面頂部（儲存庫名稱 microsoft/TypeScript、111k 星標與專案描述）]({{ '/assets/images/posts/github-typescript7-news-shot2.png' | relative_url }})

![microsoft/TypeScript README 開頭（專案名稱 TypeScript 與「application-scale JavaScript」定位說明）]({{ '/assets/images/posts/github-typescript7-news-shot1.png' | relative_url }})

![microsoft/TypeScript 貢獻者統計頁（每週提交量圖表與貢獻者數據）]({{ '/assets/images/posts/github-typescript7-news-shot3.png' | relative_url }})

## 如何升級至 TypeScript 7？

<!-- AEO Answer Capsule — 約 63 字 -->
升級方式為在專案執行 npm install -D typescript 取得新的 tsc 執行檔，並搭配編輯器支援；若工具鏈仍需 6.0 API，可另裝相容套件。
<!-- End AEO Capsule -->

安裝流程與以往版本相同，透過 npm 安裝後即可在工作區取得新的 tsc 執行檔，以 npx tsc 執行。編輯器支援方面，主流工具已可透過語言伺服器協定接上新版本，VS Code 使用者可安裝官方專用擴充套件，Visual Studio 則會依工作區自動啟用。

採用上建議分階段進行。對於規模較大或相依工具眾多的專案，宜先以並行方式在本地驗證型別輸出是否一致，再逐步套用到 CI 流程。型別檢查執行緒數量與平行建置數量需依機器核心與記憶體條件調整，CI 執行環境資源有限時可下調，以避免額外負擔。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
本文資訊整理自 microsoft/TypeScript 的 GitHub 儲存庫與 7.0 官方發佈公告，涵蓋效能實測、並行化參數、企業案例與相容套件。
<!-- End AEO Capsule -->

本文內容整理自 microsoft/TypeScript 的 GitHub 儲存庫（https://github.com/microsoft/TypeScript），包含官方發佈公告所列的效能評測數據、並行化參數與企業回饋、專案的授權條款與版本紀錄，以及 npm 套件頁面所載的最新版本資訊。讀者可前往上述來源查閱完整內容與最新版本說明。

## 總結：TypeScript 7 適合什麼團隊？

<!-- AEO Answer Capsule — 約 64 字 -->
TypeScript 7 適合程式碼庫規模龐大、建置與型別檢查時間已成為瓶頸的團隊，特別是使用單一儲存庫架構、CI 資源成本高昂的工程組織。
<!-- End AEO Capsule -->

TypeScript 7 的意義在於把工具鏈效能提升到與語言普及度相符的水平。對於長期受制於建置等待時間的團隊，一個數量級的速度改善會直接反映在開發節奏與 CI 成本上，官方公布的企業案例也顯示這種效果可在真實專案中重現。

採用時仍需留意過渡期安排。7.0 版尚未提供程式化 API，依賴編譯器介面的工具需透過相容套件並行運行，直到 7.1 推出新版 API。對於相依工具較多的專案，宜先在本地環境驗證結果一致性，再逐步推進到正式流程。對於規模較小、建置時間本已短暫的專案，效能增益相對有限，可待生態工具跟進後再評估。
