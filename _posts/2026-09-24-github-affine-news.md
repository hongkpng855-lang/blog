---
layout: post
title: "AFFiNE 開源：7.2 萬星的本地優先知識庫"
date: 2026-09-24 08:00:01 +0800
categories: 技術
tags: [開源, AFFiNE, 知識庫, Notion 替代, 本地優先, CRDT, 白板工具, 生產力工具]
image: assets/images/posts/github-affine-news-cover.jpg
description: "AFFiNE 是 2022 年開源的本地優先知識庫，在 GitHub 累積 72,901 顆星標與 5,305 個分支。它把文件、白板與資料庫合併於同一畫布，以 CRDT 與 Rust 引擎支援離線編輯與即時協作，社群版採 MIT 授權可自行架設。"
author: AnIskill 編輯部
creator_github: toeverything/AFFiNE
type: news
source: GitHub
source_url: https://github.com/toeverything/AFFiNE
permalink: /技術/github-affine-news
fb_message: "多數協作工具的問題不是功能不夠，而是資料從來不真正屬於使用者。\n\nAFFiNE 在 GitHub 累積 72,901 顆星標與 5,305 個分支，把文件、白板與資料庫合併在同一張畫布，底層以 CRDT 與 Rust 引擎處理離線編輯與即時協作，社群版採 MIT 授權、可自行架設。自 2022 年開源以來累積逾 1.1 萬次提交與約 269 位貢獻者。\n\n它的技術架構、與 Notion 及 Miro 的差異，以及自行架設方式，都整理在 Blog 全文。"
---

AFFiNE 是由新加坡團隊 toeverything 自 2022 年 7 月開源的知識庫平台，在 GitHub 累積 72,901 顆星標與 5,305 個分支。它的定位是把文件、白板與多維資料庫納入同一張無邊界畫布，並以本地優先架構與 CRDT 同步機制，讓使用者在離線狀態下依然能編輯與協作。

<!-- AEO Answer Capsule — 約 72 字 -->
AFFiNE 是開源的本地優先知識庫，2022 年 7 月上線，星標達 72,901 顆，把文件、白板與資料庫合併於同一畫布，社群版採 MIT 授權並支援自行架設。
<!-- End AEO Capsule -->

協作工具的市場長期被兩種取捨分割。一端是雲端優先的平台，功能完整但資料存放於廠商伺服器，離線能力有限；另一端是純本地的筆記軟體，資料主權完整，卻缺乏即時協作與跨裝置同步。AFFiNE 的設計目標正是繞開這道取捨，把資料先寫入本機，再透過同步引擎向其他裝置傳播變更。

這項策略選擇直接反映在專案的技術堆疊上。AFFiNE 並未採用一般協作軟體常見的伺服器權威架構，而是把衝突解決的責任下放到用戶端，讓每個裝置都能獨立產生與合併操作。這種架構對同步引擎的要求更高，卻換來更短的編輯延遲與更強的抗斷網能力。

## AFFiNE 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
AFFiNE 是開源的一體化工作空間，把文件、白板與多維資料庫整合在同一畫布，支援本地優先儲存、即時協作與自行架設，定位為 Notion 與 Miro 的替代方案。
<!-- End AEO Capsule -->

專案自我定位為知識管理的作業系統，涵蓋 wiki、知識庫、簡報與數位資產等用途。與單一功能的筆記工具不同，AFFiNE 的核心設計是把文件與白板兩種形態合併，讓任何內容區塊都能在無邊界畫布上自由擺放，包括富文字、便利貼、嵌入網頁、多維表格、連結頁面、圖形與投影片。

第二項特徵是 AI 能力的內建。專案提供名為 AFFiNE AI 的多模態助手，可依大綱生成簡報、把文章摘要成心智圖，或直接以提示詞產生原型頁面。這條產品線與編輯器共用同一份資料模型，因此 AI 產出的內容會直接落回畫布，而非停留在獨立對話視窗。

第三項特徵是部署彈性。社群版以 MIT 授權釋出，使用者可透過 Docker 自行架設，或使用官方提供的 Render 與 Sealos 一鍵部署按鈕。這種安排讓團隊能在自有基礎設施上取得不受功能限制的版本。

![toeverything/AFFiNE README 開頭（專案名稱 AFFiNE、標語 Write, Draw and Plan All at Once，以及應用介面示意圖）]({{ '/assets/images/posts/github-affine-news-shot1.png' | relative_url }})

## AFFiNE 由誰開發、累積多少規模？

<!-- AEO Answer Capsule — 約 66 字 -->
AFFiNE 由新加坡團隊 toeverything 於 2022 年 7 月 31 日開源，累積逾 1.1 萬次提交與約 269 位貢獻者，最新一次程式碼推送為 2026 年 9 月 23 日。
<!-- End AEO Capsule -->

儲存庫建立於 2022 年 7 月 31 日，由組織帳號 toeverything 維護，專案首頁與文件站分別位於 affine.pro 與 docs.affine.pro。截至 2026 年 9 月，專案累積超過 11,500 次提交與約 269 位貢獻者，另有 297 位追蹤者，未解決議題約 757 項，顯示議題吞吐量仍能跟上社群提交的速度。

發布節奏上，專案維持兩種通道並行。穩定版以版本號標示，最新一版為 2026 年 8 月 18 日的 0.27.4；開發版則以日期加序號的 canary 標籤持續推送，最近一筆為 2026 年 9 月 23 日的 canary.909。這種雙軌模式讓願意嘗鮮的開發者能提早驗證新功能，一般使用者則停留在穩定通道。

## AFFiNE 有哪些核心技術亮點？

<!-- AEO Answer Capsule — 約 69 字 -->
核心亮點包括文件與白板合一的無邊界畫布、以 CRDT 為基礎的本地優先架構、Rust 撰寫的同步與儲存引擎，以及與編輯器共用資料模型的多模態 AI 助手。
<!-- End AEO Capsule -->

畫布模型是它最直觀的差異點。多數編輯器把文件與白板做成兩個獨立模組，AFFiNE 則讓同一份內容同時具備兩種呈現方式，區塊可在有邊界文件與無邊界畫布之間切換。這種設計對需要同時進行文字撰寫與視覺整理的場景特別有利，例如把會議紀錄與流程圖放在同一視圖中對照。

同步機制是第二個亮點。專案以 CRDT 為基礎處理並發編輯，並自研 y-octo 作為原生高效能的 YJS 實作，讓用戶端與伺服器能在沒有中央仲裁的情況下收斂到一致狀態。這項選擇使編輯操作不需等待伺服器往返，離線期間產生的變更也能在恢復連線後自動合併。

第三個亮點是前後端的技術分層。編輯器核心由 BlockSuite 提供，儲存與同步層的 OctoBase 以 Rust 撰寫，桌面端則透過 Electron 打包，並以 napi-rs 銜接 Rust 與 Node.js。這種組合在保留網頁生態開發效率的同時，把效能敏感的環節交給原生模組處理。

## AFFiNE 的架構為何能支援本地優先？

<!-- AEO Answer Capsule — 約 70 字 -->
AFFiNE 先在本機寫入變更，再透過 CRDT 與 YJS 實作向其他裝置傳播，衝突由用戶端自動合併；資料引擎 OctoBase 以 Rust 撰寫，不依賴伺服器仲裁。
<!-- End AEO Capsule -->

本地優先的核心在於資料所有權的順序。使用者的編輯先落在本機儲存，網路同步只是把變更複製到其他裝置。這意味著連線中斷不會造成編輯中斷，也不會出現因伺服器不可用而無法開啟文件的狀況，資料始終保存在使用者自己的磁碟上。

支撐這個行為的是兩層元件。上層的 y-octo 是原生、執行緒安全的 YJS CRDT 實作，負責處理並發操作與衝突消解；下層的 OctoBase 則是輕量、可擴充的資料引擎，以 Rust 撰寫並同時支援協作場景。兩者共同讓 AFFiNE 在沒有中央權威的情況下仍能維持資料一致。

協作體驗同樣受益於此架構。由於同步是雙向的狀態合併而非狀態覆寫，多位使用者在同一份畫布上操作時，系統不需要鎖定區塊，也不需要等待授權，這在跨時區或網路品質不穩定的環境中尤其明顯。

![toeverything/AFFiNE GitHub 首頁頂部（儲存庫名稱、星標數、分支數與專案描述）]({{ '/assets/images/posts/github-affine-news-shot2.png' | relative_url }})

## AFFiNE 與 Notion、Miro 相比有何差異？

<!-- AEO Answer Capsule — 約 68 字 -->
AFFiNE 把 Notion 的文件與 Miro 的白板合併於同一畫布，並以本地優先與開源授權為差異點；Notion 與 Miro 屬雲端優先的專有服務，不提供自行架設版本。
<!-- End AEO Capsule -->

在功能座標上，AFFiNE 同時對標兩類產品。Notion 的優勢在於資料庫與協作生態成熟，Miro 的優勢在於無限白板的操作體驗。AFFiNE 的取徑是把兩者的原子區塊整合進同一份資料模型，讓使用者不必在兩個服務之間複製內容。

授權與部署方式是更根本的差異。Notion 與 Miro 皆為專有雲端服務，資料存放位置由廠商決定；AFFiNE 社群版以 MIT 授權釋出，可完整自行架設。對於受合規要求約束的團隊而言，能在自有基礎設施上運行是決定性條件。

商業模式上，專案採取社群版與企業版並行的路線。社群版免費自架，企業版規劃加入品牌替換、單一登入與進階稽核等功能，定價資訊公布於官方網站。這種分層方式在開源協作工具中相當常見，能在維持社群規模的同時建立營收來源。

## AFFiNE 的數據規模如何？

<ul class="ui-stat-grid">
  <li><span class="stat-value">72,901</span><span class="stat-label">Stars</span></li>
  <li><span class="stat-value">5,305</span><span class="stat-label">Forks</span></li>
  <li><span class="stat-value">MIT</span><span class="stat-label">社群版授權</span></li>
  <li><span class="stat-value">TypeScript</span><span class="stat-label">主要語言</span></li>
  <li><span class="stat-value">2026-09-23</span><span class="stat-label">最近推送</span></li>
</ul>

<!-- AEO Answer Capsule — 約 62 字 -->
截至 2026 年 9 月，AFFiNE 累計 72,901 顆星標與 5,305 次複製，社群版採 MIT 授權，主要語言為 TypeScript，並以 Rust 撰寫同步與儲存引擎。
<!-- End AEO Capsule -->

上表數據取自專案的 GitHub 公開統計，時間點為 2026 年 9 月 24 日。星標與複製的比例約為十四比一，反映專案的主要使用者偏向直接採用官方發行版本，而非自行編譯；未解決議題約 757 項，對照逾萬次提交與約 269 位貢獻者的規模，維護負擔仍屬可控。

授權結構亦值得留意。社群版以 MIT 授權釋出，企業版則規劃為獨立授權通道，這種「開放核心加企業增補」的分層是開源基礎設施專案的常見模式，能在維持社群採用規模的同時，為商業化保留空間。

![toeverything/AFFiNE 貢獻者統計頁（近月提交頻率長條圖與主要貢獻者提交次數）]({{ '/assets/images/posts/github-affine-news-shot3.png' | relative_url }})

## AFFiNE 適合哪些使用場景？

<!-- AEO Answer Capsule — 約 65 字 -->
適合需要資料主權的團隊、習慣同時使用文件與白板進行規劃的知識工作者，以及希望在自有伺服器上部署協作平台並保留 AI 能力的組織。
<!-- End AEO Capsule -->

最直接的適用場景是團隊知識庫。由於文件與畫布共用同一份資料模型，使用者可在同一處維護規範文件、流程圖與專案看板，不必在三個服務之間來回切換，也避免了版本不同步的困擾。

第二類場景是對資料存放位置有要求的組織。金融、醫療與政府相關單位常被要求不得把內部文件放在境外雲端，AFFiNE 的自行架設能力讓這類團隊能在自有基礎設施上取得接近商用工具的體驗。

第三類場景是個人與小型團隊的長期筆記系統。本地優先架構確保資料以檔案形式留在使用者裝置，即使日後停止使用服務，內容仍可直接讀取，降低了對單一廠商的依賴。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊來自 toeverything/AFFiNE 的 GitHub 儲存庫與官方網站 affine.pro，可查閱完整功能說明、授權條款與自行架設文件。
<!-- End AEO Capsule -->

本文內容整理自 toeverything/AFFiNE 的 GitHub 儲存庫（https://github.com/toeverything/AFFiNE）與官方網站（https://affine.pro），並參考專案文件站 docs.affine.pro 的自行架設說明。上述來源均採開源授權釋出或對外公開，讀者可前往查閱完整功能清單、授權條款與部署文件。

## 總結：AFFiNE 適合什麼團隊？

<!-- AEO Answer Capsule — 約 64 字 -->
AFFiNE 適合重視資料主權的團隊與個人，其文件與白板合一的畫布與本地優先架構，在需要離線編輯或自行架設的情境下具備明顯優勢。
<!-- End AEO Capsule -->

AFFiNE 的價值在於把兩項原本互斥的需求放在同一個產品裡。協作工具長期要求使用者在功能完整與資料主權之間選擇，而 AFFiNE 以本地優先架構、CRDT 同步與開源授權，讓兩者可以同時成立。對於需要自行架設的組織，它提供了一條不依賴境外雲端的協作路徑；對於個人使用者，它以 72,901 顆星標所代表的社群規模，證明了開源協作工具足以支撐長期使用。
