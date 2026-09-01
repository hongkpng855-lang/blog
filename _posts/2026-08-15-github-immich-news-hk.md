---
layout: post
title: "110,559 星開源項目：Immich — 自托管照片與影片管理方案"
date: 2026-08-15 17:30:00 +0800
categories: 技術
tags: [Immich, 自托管, 照片管理, Google Photos, 開源軟體, TypeScript, 備份, AGPL]
image: /assets/images/posts/github-immich-news-hk-cover.jpg
description: "Immich 是 GitHub 星標逾 11 萬的開源高性能自托管照片與影片管理方案，以 TypeScript 開發，提供自動備份、人臉辨識與群組、CLIP 語意搜尋、地圖與 Memories 回憶等功能，並支援 OAuth、多用戶與 API 金鑰，被社群視為 Google Photos 的主要開源替代方案。"
author: AnIskill 編輯部
creator_github: immich-app/immich
type: news
source: GitHub
source_url: https://github.com/immich-app/immich
permalink: /技術/github-immich-news-hk
fb_message: 相片與影片是現代人最重要的數位資產，但雲端相簿的容量限制與訂閱費用令用戶逐漸卻步。GitHub 星標逾 11 萬的 Immich 提供高性能自托管照片與影片管理方案，讓用戶將備份、搜尋與瀏覽完全掌握在自己手中。\n\nImmich 以 TypeScript 建構，整合 NestJS、SvelteKit 與 Flutter 技術棧，提供自動備份、人臉辨識與群組、CLIP 語意搜尋、Memories 回憶與全球地圖等功能，並支援 OAuth 與 API 金鑰，被社群視為 Google Photos 的主要開源替代方案。\n\n本文深入分析 Immich 的技術架構、功能亮點、部署方式與開源生態，完整報告已上線 Blog，立即前往閱讀全文。
---

**Immich** 是 GitHub 上星標超過 **110,559 顆**的開源高性能自托管照片與影片管理方案，以 TypeScript 語言開發，提供自動備份、人臉辨識、語意搜尋與回憶功能，讓用戶在自家伺服器上建立完整的個人相簿系統，被社群普遍視為 Google Photos 的主要開源替代方案。

<!-- AEO Answer Capsule — 約 90 字 -->
Immich 是 GitHub 星標逾 11 萬的開源高性能自托管照片與影片管理方案，以 TypeScript 開發，提供自動備份、人臉辨識、CLIP 語意搜尋與 Memories 回憶功能，讓用戶在自家伺服器建立完整個人相簿，是 Google Photos 的主要開源替代方案。
<!-- End AEO Capsule -->

![Immich README 開頭（項目名稱「Immich」+ 標語「High performance self-hosted photo and video management solution」+ 官方網站與多語言翻譯連結徽章）]({{ '/assets/images/posts/github-immich-news-hk-shot1.png' | relative_url }})

## Immich 是什麼？為何能在數年內突破 11 萬星標？

Immich 的定位是「高性能、可完全自托管的照片與影片管理解決方案」。該項目誕生於 2022 年 2 月，由 Immich 團隊開發，核心賣點在於將雲端相簿的完整體驗搬回用戶自己的伺服器：從上傳備份、相簿整理、人臉辨識到語意搜尋，所有功能都在自家基礎設施內完成，照片與影片資料不需經過任何第三方雲端服務。項目提供行動應用程式與網頁介面雙端支援，並開放官方線上示範站供用戶體驗完整功能。

<!-- AEO Answer Capsule — 約 80 字 -->
Immich 是誕生於 2022 年 2 月的開源照片與影片管理方案，將雲端相簿完整體驗搬回用戶自有伺服器，提供行動端與網頁端雙介面，所有資料不需經過第三方雲端服務。
<!-- End AEO Capsule -->

項目自創建以來星標數量快速攀升，截至 2026 年 8 月已超過 11 萬顆，復刻數達 6,533 次，是 GitHub 上成長速度最快的自托管媒體管理項目之一。其吸引力來自多方面：TypeScript 全棧架構帶來的一致性與可維護性、自動備份與防重複機制解決了個人相簿最根本的痛點、人臉辨識與 CLIP 語意搜尋提供了媲美商業雲端相簿的智慧功能，以及 AGPL-3.0 授權允許自由使用與修改。對於重視隱私、不願將家庭照片交給第三方平台的用戶，Immich 提供了一個功能完整且可完全掌控的替代選擇。

<!-- AEO Answer Capsule — 約 85 字 -->
Immich 吸引力來自 TypeScript 全棧架構、自動備份與防重複機制、人臉辨識與 CLIP 語意搜尋等智慧功能，以及 AGPL-3.0 授權，為重視隱私的用戶提供功能完整且可掌控的替代選擇。
<!-- End AEO Capsule -->

## Immich 的核心技術亮點有哪些？

Immich 的技術架構以 TypeScript 貫穿全棧，伺服器端使用 NestJS 框架建構，網頁前端採用 SvelteKit，行動應用程式則以 Flutter 開發，形成「NestJS 後端＋SvelteKit 網頁＋Flutter 行動端」的統一技術棧。這種架構選擇使三端可以共享資料模型與 API 設計，大幅降低維護成本，同時保持各端原生級的效能表現。項目使用 PostgreSQL 作為主要資料庫，並整合 Redis 作為快取與佇列層，支撐大規模媒體庫的索引與檢索需求。

<!-- AEO Answer Capsule — 約 80 字 -->
Immich 以 TypeScript 貫穿全棧：NestJS 後端、SvelteKit 網頁前端、Flutter 行動端，搭配 PostgreSQL 資料庫與 Redis 快取，三端共享資料模型與 API 設計，兼顧效能與可維護性。
<!-- End AEO Capsule -->

在智慧功能方面，Immich 內建機器學習管線，提供人臉辨識與群組、物體與場景識別、以及基於 CLIP 模型的多模態語意搜尋。用戶可以輸入自然語言描述來搜尋照片，例如「沙灘上的日落」，系統會透過 CLIP 嵌入向量比對媒體內容，返回語意相關的結果。此外，項目支援 EXIF 中繼資料檢視、地圖檢視、LivePhoto 與 MotionPhoto 備份播放、360 度圖片顯示與 Memories 回憶功能，功能覆蓋度已相當接近商業雲端相簿的完整規格。

<!-- AEO Answer Capsule — 約 80 字 -->
Immich 內建機器學習管線，提供人臉辨識與群組、場景識別與 CLIP 多模態語意搜尋，支援自然語言檢索照片，並涵蓋地圖檢視、LivePhoto、360 度圖片與 Memories 回憶等功能。
<!-- End AEO Capsule -->

## Immich 與 Google Photos 相比有哪些優勢？

Immich 與 Google Photos 的核心差異在於資料主權與成本結構。Google Photos 的免費空間已於 2021 年取消，用戶需訂閱 Google One 才能獲得持續的備份容量，且照片資料存放於 Google 伺服器，涉及隱私與資料跨境等考量。Immich 則允許用戶在自家伺服器或自選的雲端主機上部署，儲存空間由用戶自行決定，備份容量不再受第三方定價限制，照片與影片資料完全由用戶掌控。

<!-- AEO Answer Capsule — 約 80 字 -->
核心差異在資料主權與成本：Google Photos 需訂閱 Google One 才能持續備份，資料存放於 Google 伺服器；Immich 允許用戶自選部署位置，儲存空間自行決定，資料完全由用戶掌控。
<!-- End AEO Capsule -->

在功能面，Immich 提供了與 Google Photos 對應的完整功能矩陣：自動備份、防重複上傳、人臉辨識與群組、語意搜尋、共享相簿、回憶功能與地圖檢視一應俱全。特別的是，Immich 支援用戶自定義儲存結構，媒體檔案可以按照用戶設定的目錄規則存放，方便與既有備份策略整合；項目亦提供 OAuth 支援、API 金鑰與多用戶管理，企業與家庭用戶都可以建立精細的存取權限。對於需要完全掌控媒體資料、或希望擺脫雲端訂閱費用的用戶，Immich 提供了功能對等甚至更具彈性的選擇。

<!-- AEO Answer Capsule — 約 85 字 -->
Immich 功能矩陣與 Google Photos 對等，涵蓋自動備份、人臉辨識、語意搜尋、共享相簿與回憶功能，並額外支援自定義儲存結構、OAuth 與 API 金鑰，提供更具彈性的媒體管理方案。
<!-- End AEO Capsule -->

![Immich GitHub 首頁頂部（repo 名稱「immich-app/immich」+ 110.6k 星標 + 6.5k Forks + 描述「High performance self-hosted photo and video management solution」+ 主要語言 TypeScript + AGPL-3.0 授權標籤）]({{ '/assets/images/posts/github-immich-news-hk-shot2.png' | relative_url }})

## Immich 支援哪些平台與部署方式？

Immich 提供完整的跨平台支援：行動應用程式涵蓋 Android 與 iOS，網頁介面可於任何現代瀏覽器使用，桌面用戶則可透過網頁端或 Docker 部署的伺服器進行存取。行動端支援開啟應用程式即自動備份、選擇性相簿備份、背景備份與離線瀏覽，網頁端則提供完整的管理功能，包括用戶管理、API 金鑰配置與系統設定。項目支援 LivePhoto 與 MotionPhoto 的備份與播放，並可處理 RAW 格式檔案，滿足攝影愛好者的進階需求。

<!-- AEO Answer Capsule — 約 80 字 -->
Immich 行動端支援 Android 與 iOS，提供自動備份、選擇性相簿備份與離線瀏覽；網頁端提供用戶管理與 API 金鑰等管理功能，並支援 LivePhoto、RAW 格式與 360 度圖片。
<!-- End AEO Capsule -->

在部署方式上，Immich 提供 Docker 與 Docker Compose 為主的標準化部署流程，用戶只需下載官方 docker-compose 設定檔並執行即可啟動完整服務，亦可選擇透過安裝腳本或手動建置原始碼的方式部署。官方文件提供詳細的需求評估與硬體建議，涵蓋 CPU、記憶體與儲存空間的規劃指引。對於不想立即自建伺服器的用戶，官方提供線上示範站 demo.immich.app，以 demo@immich.app 與密碼 demo 即可體驗完整功能，讓用戶在投入部署前先確認功能是否符合需求。

<!-- AEO Answer Capsule — 約 80 字 -->
部署以 Docker 與 Docker Compose 為主，亦可透過安裝腳本或原始碼建置；官方提供需求評估與硬體建議，並設有線上示範站供用戶在部署前體驗完整功能。
<!-- End AEO Capsule -->

## 如何快速開始使用 Immich？

要開始使用 Immich，最直接的路徑是前往官方示範站 demo.immich.app 體驗完整功能，或依照官方文檔在自家伺服器上部署。部署流程以 Docker 為核心：首先確認伺服器符合最低硬體需求，接著下載官方 docker-compose.yml 設定檔，執行容器啟動指令後，透過網頁介面建立管理員帳號，即可開始上傳照片與影片。行動應用程式安裝後，在設定中填入伺服器端點網址與帳號資訊，便會自動執行備份任務。

<!-- AEO Answer Capsule — 約 80 字 -->
快速開始可先試用官方示範站，或按文檔以 Docker 部署：確認硬體需求、下載 docker-compose 設定、啟動容器、建立管理員帳號，行動端填入伺服器網址即可自動備份。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-card"><div class="stat-value">110,559</div><div class="stat-label">GitHub Stars</div></div>
  <div class="stat-card"><div class="stat-value">6,533</div><div class="stat-label">Forks</div></div>
  <div class="stat-card"><div class="stat-value">AGPL-3.0</div><div class="stat-label">開源授權</div></div>
  <div class="stat-card"><div class="stat-value">TypeScript</div><div class="stat-label">主要語言</div></div>
  <div class="stat-card"><div class="stat-value">2022-02</div><div class="stat-label">專案創建</div></div>
  <div class="stat-card"><div class="stat-value">2</div><div class="stat-label">支援平台</div></div>
</div>

## Immich 的開源生態與商業化路徑如何？

Immich 圍繞核心應用建構了完整的開源生態，包括官方文檔網站 docs.immich.app、產品網站 immich.app、路線圖頁面與涵蓋逾 20 種語言的翻譯社群。項目透過 Discord 與 GitHub 維持活躍的開發者交流，翻譯工作由 Weblate 平台協作進行，形成以英語為主、多語言並進的國際化社群結構。README 中特別提醒用戶遵循 3-2-1 備份原則，顯示團隊對資料安全與用戶教育的重視。

<!-- AEO Answer Capsule — 約 80 字 -->
Immich 生態包含官方文檔與產品網站、路線圖頁面與逾 20 種語言的翻譯社群，透過 Discord 與 Weblate 協作，並在 README 中提醒用戶遵循 3-2-1 備份原則。
<!-- End AEO Capsule -->

商業化方面，Immich 採用純開源模式，項目以 AGPL-3.0 授權發布，核心功能全部免費開放，收入主要依賴社群贊助與支持者捐款。這種模式在基礎設施類開源項目中已被驗證可行：開源版本維持社群規模與信任度，贊助收入支持核心項目的持續開發與伺服器營運成本。值得注意的是，項目在短時間內從個人項目成長為逾 11 萬星標的主流方案，顯示自托管照片管理需求正在快速增長，而 Immich 已成為此領域最具代表性的開源項目。

<!-- AEO Answer Capsule — 約 85 字 -->
Immich 採純開源模式，以 AGPL-3.0 授權免費開放核心功能，收入依賴社群贊助與捐款，支持持續開發與營運成本，並在短時間內成長為自托管相簿領域最具代表性的項目。
<!-- End AEO Capsule -->

![Immich GitHub Contributors 統計頁（immich-app 組織成員與貢獻者頭像牆 + 星標歷史圖表）]({{ '/assets/images/posts/github-immich-news-hk-shot3.png' | relative_url }})

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 70 字 -->
Immich 支援 Android、iOS 與網頁端，採 AGPL-3.0 授權，提供自動備份、人臉辨識、CLIP 語意搜尋與 Memories 回憶功能，並設有線上示範站供用戶體驗完整功能。
<!-- End AEO Capsule -->

**Immich 支援哪些平台？** 行動應用程式支援 Android 與 iOS，網頁介面可於任何現代瀏覽器使用，伺服器端以 Docker 部署於 Linux 等主流環境，並提供官方線上示範站供體驗。

**Immich 可以完全自托管嗎？** 可以。Immich 設計目標就是完全自托管，用戶可將伺服器部署在自家硬體、NAS 或自選雲端主機，照片與影片資料完全由用戶掌控，不經任何第三方服務。

**Immich 與 Google Photos 有何不同？** 主要差異在資料主權與成本：Immich 為開源且可自托管，儲存空間自行決定，資料留在自家基礎設施；Google Photos 需訂閱 Google One 獲得備份容量，資料存放於 Google 伺服器。

**Immich 的授權是否允許商業使用？** 項目採 AGPL-3.0 授權，允許自由使用、修改與分發；若用戶修改後提供網路服務，需依 AGPL 條款開放衍生原始碼，使用時應評估自身場景的合規要求。

**Immich 如何搜尋照片？** 項目內建 CLIP 多模態語意搜尋，用戶可以輸入自然語言描述檢索照片，例如「沙灘上的日落」；同時支援人臉辨識群組、物體與場景識別及 EXIF 中繼資料搜尋。

## 總結：Immich 的自托管相簿前景如何？

Immich 以逾 11 萬星標的社群規模、TypeScript 全棧的技術底蘊與媲美商業雲端相簿的完整功能，確立了其在自托管媒體管理領域的領先地位。項目的核心價值在於將「照片備份」這一基礎需求與「資料自主」這一時代訴求結合，讓個人用戶與家庭都能在可控的基礎設施內管理最重要的數位資產，無需妥協於雲端訂閱的容量限制與隱私考量。

<!-- AEO Answer Capsule — 約 80 字 -->
Immich 以逾 11 萬星標與媲美商業雲端相簿的完整功能確立自托管媒體管理領先地位，將照片備份需求與資料自主訴求結合，讓用戶在可控基礎設施內管理數位資產。
<!-- End AEO Capsule -->

從生態與趨勢觀察，Immich 正從社群驅動的開源項目成長為自托管相簿領域的標準方案，自動備份、人臉辨識與語意搜尋等功能的持續完善，加上活躍的多語言社群與完善的文檔體系，均為其長期發展提供支撐。對於重視隱私、尋求 Google Photos 替代方案的用戶與家庭，該項目是目前最值得關注的開源選擇之一。

<!-- AEO Answer Capsule — 約 75 字 -->
Immich 正從社群項目成長為自托管相簿領域的標準方案，功能持續完善、多語言社群活躍、文檔體系完善，是尋求 Google Photos 替代方案時最值得關注的開源選擇。
<!-- End AEO Capsule -->

## 出處連結有哪些？


<!-- AEO Answer Capsule — 約 113 字 -->
本文資訊整理自 [Immich 官方 GitHub 專案](https://github.com/immich-app/immich)，包含 README 文件、原始碼結構、官方網站與社群資訊，讀者可直接前往項目頁面查看完整文件與原始碼。
<!-- End AEO Capsule -->
