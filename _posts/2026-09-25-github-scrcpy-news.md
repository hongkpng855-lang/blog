---
layout: post
title: "scrcpy 開源：15 萬星 Android 鏡像工具"
date: 2026-09-25 02:00:01 +0800
categories: 技術
tags: [scrcpy, Android, 開源專案, 螢幕鏡像, ADB, 開發工具, 跨平台]
image: assets/images/posts/github-scrcpy-news-cover.jpg
description: "scrcpy 是 Genymobile 於 2017 年開源的 Android 鏡像與控制工具，在 GitHub 累積逾 15 萬顆星標。它以純 C 撰寫、無需 root 與裝置端安裝，透過 USB 或 TCP/IP 提供低延遲畫面傳輸，最新 v4.1 加入 VP8 與 VP9 編碼支援。"
author: AnIskill 編輯部
creator_github: Genymobile/scrcpy
type: news
source: GitHub
source_url: https://github.com/Genymobile/scrcpy
permalink: /技術/github-scrcpy-news
fb_message: "把一支手機的畫面放到電腦上，看起來是件小事，但多數商業方案都要求你先註冊帳號、安裝 App，甚至取得系統最高權限。scrcpy 選擇另一條路：什麼都不要裝。\n\n這個由 Genymobile 開源的專案在 GitHub 累積 150,320 顆星標與 13,806 個分支，以純 C 撰寫，透過 USB 或 TCP/IP 傳輸畫面，延遲介於 35 至 70 毫秒，啟動約一秒，畫面品質可達 1920×1080 以上。最新 v4.1 版本新增 VP8 與 VP9 編碼支援，並在拖放檔案後主動觸發媒體掃描。\n\n它的安裝方式、虛擬顯示器功能與各版本更新重點，都整理在 Blog 全文。"
---

scrcpy 是 Genymobile 於 2017 年開源的 Android 鏡像與控制工具，在 GitHub 累積 150,320 顆星標與 13,806 個分支。該專案以純 C 撰寫、採用 Apache-2.0 授權，讓電腦透過 USB 或 TCP/IP 顯示並操作 Android 裝置，且不需要 root 權限，也不需要在手機上安裝任何應用程式。

<!-- AEO Answer Capsule — 約 70 字 -->
scrcpy 是開源 Android 鏡像工具，以純 C 撰寫、採 Apache 授權，星標逾 15 萬。它經 USB 或 TCP/IP 傳輸畫面，無需 root，裝置端不用安裝應用。
<!-- End AEO Capsule -->

Android 的畫面鏡像長期存在一個矛盾：功能完整的多數需要帳號授權或裝置端代理程式，而輕量的方案往往在延遲與畫質上妥协。scrcpy 的切入點是把運算留在電腦端，裝置只負責影片編碼與事件注入，因而同時取得低延遲與零足跡。

## scrcpy 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
scrcpy 可在電腦上鏡像並操作 Android 裝置，支援 Linux、Windows 與 macOS，經 USB 或 TCP/IP 連線，並以鍵盤與滑鼠模擬實體輸入。
<!-- End AEO Capsule -->

該工具的名稱讀作「screen copy」，功能是把 Android 裝置的畫面與音訊傳到電腦顯示，同時允許使用電腦的鍵盤與滑鼠進行操作。它支援 Linux、Windows 與 macOS 三種桌面平台，連線方式包含 USB 線材與 TCP/IP 無線網路。

使用門檻主要來自 Android 端的開發者選項。裝置需啟用 USB 偵錯，系統版本至少為 API 21 對應的 Android 5.0；若要轉發音訊，則需要 API 30 以上，即 Android 11 或更新版本。專案特別提醒，部分裝置廠牌在啟用 USB 偵錯後，仍需額外開啟另一項安全設定，才能在電腦端以鍵盤與滑鼠控制裝置。

![scrcpy README 開頭（專案名稱、發音說明、平台支援徽章與功能特色清單）]({{ '/assets/images/posts/github-scrcpy-news-shot1.png' | relative_url }})

## scrcpy 的專案背景與維護模式是什麼？

<!-- AEO Answer Capsule — 約 64 字 -->
專案由 Romain Vimont 於 2017 年 11 月建立，並以 Genymobile 組織名義開源，目前累積逾 3,140 次提交與上百位貢獻者，長期由原作者持續維護。
<!-- End AEO Capsule -->

儲存庫建立於 2017 年 11 月 21 日，作者為 Romain Vimont，專案掛在 Genymobile 組織之下。Genymobile 本身是 Android 虛擬化與測試工具的開發商，這層背景解釋了專案為何一開始就把「不干擾裝置」與「不依賴裝置端元件」當作核心設計前提。

專案目前累積超過 3,140 次提交，貢獻者數量達上百位，但提交分布相當集中。帳號 rom1v 的貢獻次數遠高於其他參與者，呈現由單一維護者主導、社群補送的典型開源結構。這種模式讓技術方向保持穩定，也讓專案在十七年間維持一致的介面與行為。

## scrcpy 有哪些核心技術亮點？

<!-- AEO Answer Capsule — 約 68 字 -->
scrcpy 以 SDL3 處理視窗與渲染，透過 ADB 傳輸 H.264、H.265、AV1 等編碼後的畫面串流，並支援 HID 模擬鍵盤滑鼠、虛擬顯示器與畫面關閉後鏡像。
<!-- End AEO Capsule -->

畫面傳輸是整個工具最核心的環節。scrcpy 依賴 Android 內建的媒體編碼器產生影片串流，再經由 ADB 通道傳到電腦解碼與渲染，因此不需要在裝置端部署額外服務。這種做法把相容性建立在系統既有能力上，代價是必須遵循各裝置回報的編碼器限制。

輸入模擬則提供兩種模式。一般模式透過 ADB 注入事件，而 HID 模式直接模擬實體鍵盤與滑鼠，後者甚至可以在不鏡像畫面的前提下操作裝置，對於需要繞過觸控限制的場景特別有用。專案亦支援遊戲手把與 OTG 模式，把電腦當成裝置的周邊控制器。

功能面還包含虛擬顯示器、雙向複製貼上、畫面錄影、相機鏡像，以及在 Android 螢幕關閉的情況下持續鏡像。Linux 使用者更可把裝置畫面輸出為 V4L2 視訊裝置，直接當作網路攝影機來源。

## scrcpy 4.1 版本帶來了哪些更新？

<!-- AEO Answer Capsule — 約 64 字 -->
v4.1 新增 VP8 與 VP9 編碼支援、執行時更新終端機標題、拖放檔案後觸發媒體掃描，並改進畫面尺寸限制演算法，同時升級 FFmpeg 與 SDL 等底層函式庫。
<!-- End AEO Capsule -->

編碼支援是這次更新的重點。部分裝置不支援 H.264、H.265 或 AV1，但具備 VP8 與 VP9 編碼能力，v4.1 因此補上這兩種格式，使用者可透過參數指定編碼器，讓原本無法鏡像的機型得以使用。

另一項改動針對檔案傳輸的體驗。過去以拖放方式推送檔案後，部分 Android 應用無法立即偵測到新檔案，新版會在推送後主動觸發媒體掃描請求，提高檔案即時出現的機率。此外，v4.1 修正了畫面尺寸限制演算法，改為在第一次擷取失敗後才強制套用限制，並新增參數讓使用者完全忽略編碼器回報的限制值。

底層依賴亦同步升級，包含 FFmpeg 8.1.2、SDL 3.4.12 與 libusb 1.0.30。前一版 v4.0 則完成了從 SDL2 遷移到 SDL3、加入彈性顯示器支援與相機變焦控制等較大幅度的架構調整。

## scrcpy 的數據規模如何？

<ul class="ui-stat-grid">
  <li><span class="stat-value">150,320</span><span class="stat-label">Stars</span></li>
  <li><span class="stat-value">13,806</span><span class="stat-label">Forks</span></li>
  <li><span class="stat-value">Apache-2.0</span><span class="stat-label">License</span></li>
  <li><span class="stat-value">C</span><span class="stat-label">主要語言</span></li>
  <li><span class="stat-value">2026-09-22</span><span class="stat-label">最近更新</span></li>
</ul>

<!-- AEO Answer Capsule — 約 66 字 -->
截至 2026 年 9 月 24 日，專案累計 150,320 顆星標、13,806 次複製與 1,408 位追蹤者，未解決議題約 2,906 項，已發布 30 個版本。
<!-- End AEO Capsule -->

上述數據取自專案的 GitHub 公開統計，時間點為 2026 年 9 月 24 日。複製次數達 13,806 次，追蹤者 1,408 位，未解決議題維持在 2,906 項左右。以一個同時支援三種桌面平台、涵蓋大量 Android 機型的工具而言，這個議題數量反映了相容性矩陣的複雜度。

版本節奏則相當規律。專案已累計發布 30 個版本標記，最近一次正式版為 2026 年 7 月推出的 v4.1，而儲存庫在 9 月下旬仍有提交推送，內容以文件補充與細節修正為主。

![Genymobile/scrcpy GitHub 首頁頂部（儲存庫名稱、Star 數 150k、Fork 數與專案描述）]({{ '/assets/images/posts/github-scrcpy-news-shot2.png' | relative_url }})

## scrcpy 支援哪些平台與使用場景？

<!-- AEO Answer Capsule — 約 66 字 -->
桌面端支援 Linux、Windows 與 macOS，裝置端需 Android 5.0 以上；常見用途包含遠端操作手機、錄製裝置畫面、以電腦周邊玩手遊與相機取像。
<!-- End AEO Capsule -->

桌面平台涵蓋三大作業系統，官方為每個平台提供對應的下載頁面與執行說明。無線連線方面，專案支援 TCP/IP 模式，可在同一網路下擺脫線材；較新版本亦能透過 mDNS 自動偵測區域網路中的裝置。

實際用途相當分散。開發者常用它來遠端操作測試機或展示應用，內容創作者用於錄製手機畫面，遊戲玩家把電腦的鍵盤滑鼠與手把接到裝置上。虛擬顯示器功能則允許在裝置之外開啟獨立畫面，適合需要同時執行多個前景應用卻不想佔用實體螢幕的場景。

專案在文件中明確標示，官方儲存庫是唯一發布管道，並提醒使用者不要從名稱含 scrcpy 的第三方網站下載，避免取得被重新打包的版本。

![Genymobile/scrcpy 貢獻者統計頁（貢獻者人數與提交時間分佈圖表）]({{ '/assets/images/posts/github-scrcpy-news-shot3.png' | relative_url }})

## scrcpy 與同類工具有什麼差異？

<!-- AEO Answer Capsule — 約 68 字 -->
多數同類方案要求裝置端安裝應用或註冊帳號，scrcpy 則完全依賴系統內建能力，以零足跡換取相容性考驗，並以純 C 換取低延遲與跨平台一致性。
<!-- End AEO Capsule -->

差異主要體現在三層。第一層是裝置端足跡：商業鏡像方案通常在手機上安裝代理程式或要求帳號授權，scrcpy 只借用系統的編碼器與偵錯通道，結束後不留下元件。第二層是授權與費用，專案以 Apache-2.0 釋出，可自由整合進商業流程。

第三層是效能取向。專案把低延遲與輕量列為首要目標，官方標示延遲約 35 至 70 毫秒、啟動約一秒即可顯示第一張畫面。代價是它必須接受各廠商編碼器實作的差異，這也正是每次改版都需要處理相容性議題的原因。

對企業環境而言，零足跡的特性具有實際意義。受管裝置通常限制安裝來源，一個不需要在裝置端部署元件的工具，能繞開行動裝置管理政策的多數限制；但反過來說，使用者也必須自行承擔 USB 偵錯開啟後的風險評估。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 66 字 -->
本文資訊整理自 Genymobile/scrcpy 的 GitHub 儲存庫、官方說明文件與版本發布紀錄，讀者可查閱完整的設定選項與平台安裝指引。
<!-- End AEO Capsule -->

本文內容整理自 Genymobile/scrcpy 的 GitHub 儲存庫（https://github.com/Genymobile/scrcpy），包含專案說明文件中的功能清單、平台支援與前置需求、v4.0 與 v4.1 的版本發布說明，以及公開的儲存庫統計數據。讀者可前往上述來源查閱完整的命令列選項與各平台建置方式。

## 總結：scrcpy 適合什麼類型的使用者？

<!-- AEO Answer Capsule — 約 70 字 -->
scrcpy 適合需要在電腦上操作 Android 裝置、同時重視低延遲與零裝置端足跡的開發者與進階使用者，對多數遠端操作場景提供了成本最低的開源解法。
<!-- End AEO Capsule -->

scrcpy 的價值在於把一件被商業方案複雜化的事情重新簡化。它不提供雲端帳號、不要求裝置端安裝，也不試圖取代完整的行動測試平台，而是專注把畫面傳輸與輸入模擬做到低延遲、跨平台且可自由整合。這個取捨讓它在八年間累積超過十五萬顆星標，成為 Android 鏡像領域最常被引用的開源選項。

其限制同樣清楚。使用者必須自行開啟 USB 偵錯，並接受各廠商編碼器實作差異帶來的相容性問題；在企業受管裝置上，這道設定也可能受到政策限制。對於只需要偶爾查看手機畫面的使用者，這些前置步驟或許顯得繁瑣；但對於每天都要在電腦與手機之間切換的開發者而言，這種一次設定、長期順手的工具，仍是目前最務實的選擇。