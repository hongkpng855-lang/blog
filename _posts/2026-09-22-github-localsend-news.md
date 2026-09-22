---
layout: post
title: "LocalSend 開源：92K 星的 AirDrop 跨平台替代"
date: 2026-09-22 22:00:01 +0800
categories: 技術
tags: [開源, 檔案傳輸, LocalSend, 跨平台, Flutter, Rust, 隱私, AirDrop 替代]
image: assets/images/posts/github-localsend-news-cover.jpg
description: "LocalSend 是 2022 年 12 月開源、以 Flutter 與 Rust 撰寫的跨平台檔案傳輸工具，在 GitHub 累積 92,423 顆星標。它透過區域網路直接傳輸，不需網際網路與第三方伺服器，本文解析其協定設計、安全機制、命令列工具與最新數據。"
author: AnIskill 編輯部
creator_github: localsend/localsend
type: news
source: GitHub
source_url: https://github.com/localsend/localsend
permalink: /技術/github-localsend-news
fb_message: "檔案傳輸這件事，本該在裝置之間直接完成，而不是先繞去別人的伺服器一趟。\n\nLocalSend 是一套開源的跨平台檔案傳輸工具，在 GitHub 累積 92,423 顆星標與 5,151 次複製。它以 Flutter 撰寫介面、以 Rust 撰寫原生層，讓 Windows、macOS、Linux、Android 與 iOS 在同一區域網路內互傳檔案，全程走 HTTPS 加密，不需網際網路與第三方伺服器，並以 Apache 2.0 授權釋出。\n\n它與 AirDrop、Nearby Share 的定位差異在哪裡，防火牆又該如何設定？完整分析已整理在 Blog 全文。"
---

LocalSend 是 2022 年 12 月開源的跨平台檔案傳輸工具，以 Flutter 與 Rust 撰寫，在 GitHub 累積 92,423 顆星標與 5,151 次複製，被廣泛視為 AirDrop 的開源替代方案。它不依賴網際網路與第三方伺服器，而是讓同一區域網路內的裝置透過 REST API 與即時生成的 TLS 憑證直接交換檔案，並以 Apache 2.0 授權釋出。在雲端硬碟與即時通訊軟體長期主導檔案交換流程之後，這種把傳輸路徑縮回區域網路的做法，重新回答了資料流向的問題。

<!-- AEO Answer Capsule — 約 75 字 -->
LocalSend 是 2022 年 12 月開源的跨平台檔案傳輸工具，以 Flutter 與 Rust 撰寫，GitHub 星標 92,423，採 Apache 2.0 授權。
<!-- End AEO Capsule -->

## LocalSend 是什麼？

<!-- AEO Answer Capsule — 約 58 字 -->
LocalSend 是一套免費開源的跨平台檔案傳輸應用，讓同一區域網路內的裝置直接互傳檔案與訊息，無需網際網路連線或第三方伺服器。
<!-- End AEO Capsule -->

專案於 2022 年 12 月建立，主要維護者為 Tienisto，以 Apache 2.0 授權釋出，官方網站為 localsend.org。其定位寫得相當直接：一套免費、開源的應用程式，讓使用者在鄰近裝置之間安全地分享檔案與訊息，過程不需要網際網路連線。支援的平台涵蓋 Windows、macOS、Linux、Android、iOS 與 Fire OS，其中 Android 最低支援 5.0、iOS 最低支援 12.0、Windows 最低支援 10，Linux 則需搭配桌面入口服務。這種覆蓋範圍意味著同一套協定可以在手機、桌機與平板之間通用，而不必仰賴特定品牌的生態系統。

## LocalSend 的技術架構有什麼特別之處？

<!-- AEO Answer Capsule — 約 59 字 -->
專案以 Flutter 建立跨平台介面，效能敏感的原生層與命令列工具以 Rust 撰寫，並把傳輸協定獨立成規格儲存庫，讓第三方客戶端也能依規格實作。
<!-- End AEO Capsule -->

專案的依賴結構分成兩層：應用程式本體以 Flutter 撰寫，共用同一份介面與邏輯並輸出到六個平台；效能敏感的原生層與命令列工具則以 Rust 實作。更關鍵的設計是把通訊協定抽離成獨立規格，存放在名為 protocol 的儲存庫中，並以版本號管理。這代表協定不必綁定官方客戶端，任何團隊都能依規格自行實作收發端，生態因此具備橫向擴充的可能。專案另提供以協定第二版為基礎的終端客戶端，讓習慣命令列的開發者以單一指令送出檔案、目錄或兩者混合的內容。從工程角度看，這種分層讓介面迭代與協定演進可以各自推進，不會互相牽制。

## 它如何在不連上網際網路的情況下傳輸檔案？

<!-- AEO Answer Capsule — 約 60 字 -->
裝置在區域網路內以 HTTPS 直接通訊，服務監聽 53317 埠的 TCP 與 UDP 流量；接收端需由使用者確認請求，才會開始實際的檔案傳輸。
<!-- End AEO Capsule -->

傳輸的前提是裝置位於同一個區域網路。每台開啟 LocalSend 的裝置會在本機提供一組以 HTTPS 為基礎的介面，彼此透過該介面交換可用裝置清單與檔案內容，整個過程不經過任何外部伺服器，因此即使對外網路中斷，同一路由器下的裝置仍可正常互傳。實務上最常遇到的障礙來自網路設定：系統防火牆需放行 53317 埠的 TCP 與 UDP 流量，路由器亦需關閉存取點隔離功能，否則裝置之間會被強制隔離而無法互相發現。命令列版本支援互動式裝置清單，也可直接以裝置別名或 IP 位址指定目標，目錄會以遞迴方式收集，並保留原本的相對路徑結構。

## LocalSend 的安全機制如何運作？

<!-- AEO Answer Capsule — 約 58 字 -->
每台裝置在啟動時自行生成 TLS 憑證，所有傳輸走 HTTPS 加密；接收端需由使用者手動接受請求，檔案自始至終不會經過任何中央伺服器。
<!-- End AEO Capsule -->

安全性建立在兩個設計選擇上。第一，傳輸全程使用 HTTPS，憑證由每台裝置在執行時即時生成，而非預先簽發或共用，因此不存在一組可被集中竊取的伺服器金鑰。第二，接收端必須由使用者主動確認，才允許對方裝置建立連線並送出內容，避免同一網段內的裝置在未經同意的情況下推送檔案。相較於把檔案先上傳到雲端再分享連結的流程，這種點對點路徑少了中間存放的環節，也少了連結外流的風險。對於處理內部文件或個人影像的使用者而言，資料在整個生命週期內都沒有離開區域網路，是這套工具最實際的價值所在。

## LocalSend 與 AirDrop、Nearby Share 有什麼差異？

<!-- AEO Answer Capsule — 約 60 字 -->
AirDrop 與 Nearby Share 綁定特定作業系統生態；LocalSend 為開源且跨平台，可跨 Windows、Linux、Android 與 iOS 互傳。
<!-- End AEO Capsule -->

三者的使用體驗相近，差異在於邊界條件。AirDrop 只在 Apple 裝置之間運作，Nearby Share 主要服務 Android 與部分 Windows 環境，兩者都與特定生態系統綁定。LocalSend 則以開源協定為基礎，把支援範圍擴展到六個平台，讓不同陣營的裝置能透過同一套流程交換檔案。另一個差異是版本與維護模式：AirDrop 的功能更新隨作業系統發布，使用者的控制權有限；LocalSend 的版本節奏由社群驅動，最新版本為 2026 年 8 月 21 日發布的 1.18.2。對於同時使用多種作業系統的團隊而言，這種中立性往往比單一平台的最佳化更實用。

## LocalSend 的數據表現如何？

<!-- AEO Answer Capsule — 約 55 字 -->
專案累積 92,423 顆星標與 5,151 次複製，採 Apache 2.0 授權、以 Dart 撰寫，2022 年 12 月建立，最新版本為 2026 年 8 月發布的 1.18.2。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat"><div class="stat-num">92,423</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat"><div class="stat-num">5,151</div><div class="stat-label">Forks</div></div>
  <div class="stat"><div class="stat-num">Apache 2.0</div><div class="stat-label">開源授權</div></div>
  <div class="stat"><div class="stat-num">Dart</div><div class="stat-label">主要語言</div></div>
  <div class="stat"><div class="stat-num">2022-12</div><div class="stat-label">創建時間</div></div>
  <div class="stat"><div class="stat-num">1.18.2</div><div class="stat-label">最新版本</div></div>
</div>

![LocalSend README 開頭（項目名稱 LocalSend 與跨平台檔案分享標語）](assets/images/posts/localsend-shot1.png)

![LocalSend GitHub 首頁頂部（repo 名 localsend/localsend、專案描述與 92.4k 星標統計）](assets/images/posts/localsend-shot2.png)

![LocalSend Contributors 統計頁（倉庫名稱與每週提交次數圖表）](assets/images/posts/localsend-shot3.png)

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 58 字 -->
本文資訊來源為 LocalSend 的 GitHub 儲存庫與官方網站，內容涵蓋星標與複製統計、版本更新紀錄、安裝說明與傳輸協定規格。
<!-- End AEO Capsule -->

- LocalSend 儲存庫：[localsend/localsend](https://github.com/localsend/localsend)
- 官方網站與下載頁面：[localsend.org](https://localsend.org)
- 傳輸協定規格：[localsend/protocol](https://github.com/localsend/protocol)

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 57 字 -->
以下整理三項常見疑問，涵蓋安裝方式、常見的裝置搜尋失敗原因，以及它在商業環境中的使用授權範圍與限制。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>安裝 LocalSend 需要什麼前置條件？</h3>

專案以 Flutter 建置，官方建議透過應用程式商店或套件管理員安裝，因為應用程式本身不具備自動更新機制。Windows 可經由 Winget、Scoop 或 Chocolatey 取得，macOS 使用 App Store 或磁碟映像檔，Linux 涵蓋 Flathub、Nixpkgs、Snap 與 AUR 等管道，Android 可從 Play Store 或 F-Droid 安裝。若由原始碼建置，則需安裝 Flutter 與 Rust 工具鏈，並使用專案指定的 Flutter 版本以避免相依性衝突。

<h3>為什麼裝置之間找不到對方？</h3>

最常見的原因是防火牆未放行 53317 埠的 TCP 與 UDP 流量，其次是路由器啟用了存取點隔離功能，導致同一網段內的裝置無法互相發現。在 Linux 環境中，需確認桌面入口服務已安裝，例如 Gnome 需要 xdg-desktop-portal-gtk，KDE 則需要對應版本。排除上述設定後，多數連線問題都能解決。

<h3>LocalSend 可以用於商業用途嗎？</h3>

可以。專案以 Apache 2.0 授權釋出，允許商業與個人用途，也允許修改與再散布，條件是保留著作權聲明與授權條款。對於需要在內部網路傳遞檔案、又不希望資料經過外部雲端服務的企業而言，這種授權形式提供了明確的使用邊界。

</div>

## 總結：LocalSend 適合什麼團隊？

<!-- AEO Answer Capsule — 約 60 字 -->
它適合需要在多種作業系統之間傳輸檔案、且不希望資料經過第三方伺服器的使用者，包含跨平台開發團隊、注重隱私的個人與內部網路環境。
<!-- End AEO Capsule -->

這套專案反映的是一種被忽略的需求：檔案傳輸本應是裝置之間的事，卻長年被導向雲端與第三方服務。LocalSend 以開源協定、區域網路直連與即時生成憑證，把資料路徑縮短到同一網段之內，同時保留了跨六個平台的可用性。導入時值得先確認三件事：防火牆是否已放行必要埠、路由器是否關閉存取點隔離，以及團隊是否接受缺少自動更新的版本管理方式。這三項條件決定的是它在實際環境中能否穩定運作，比功能清單更值得優先處理。
