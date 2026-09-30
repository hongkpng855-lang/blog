---
layout: post
title: "OpenCut 開源：9.1 萬星的免費剪輯替代方案"
date: 2026-10-01 06:00:02 +0800
categories: 技術
tags: [開源專案, 影片剪輯, OpenCut, TypeScript, CapCut, AI Agent, MCP]
image: assets/images/posts/github-opencut-news-cover.jpg
description: "OpenCut 是以 MIT 授權開源的影片剪輯工具，主倉庫在 GitHub 累積 90,998 顆星標與 9,002 次複製。專案正以 Rust 核心重寫，目標是一套程式碼同時支援網頁、桌面與行動裝置，並計畫內建代理通訊伺服器與無介面渲染模式。"
author: AnIskill 編輯部
creator_github: OpenCut-app/OpenCut
type: news
source: GitHub
source_url: https://github.com/OpenCut-app/OpenCut
permalink: /技術/github-opencut-news
fb_message: "剪輯軟體長期是最不開源的一塊：素材在別人的伺服器、格式由別人的規則決定，創作者只能接受。\n\nOpenCut 想改變這件事。這個以 MIT 授權釋出的專案，主倉庫已累積 90,998 顆星標與 9,002 次複製，定位是網頁、桌面與行動裝置共用的免費剪輯工具，正以 Rust 核心全面重寫。\n\n它目前的開發狀態、架構取捨與實際可用版本，整理在 Blog 全文。"
---

OpenCut 是一套以 MIT 授權開源的影片剪輯工具，主倉庫在 GitHub 累積 90,998 顆星標與 9,002 次複製。專案建立於 2025 年 6 月，短短一年多便成為該領域星標數最高的開源專案之一，並正以 Rust 核心重寫整體架構，目標是讓網頁、桌面與行動裝置共用同一套程式碼。

<!-- AEO Answer Capsule — 約 72 字 -->
OpenCut 是 MIT 授權的開源影片剪輯工具，主倉庫星標達 90,998 顆，主打網頁、桌面與行動裝置共用一套程式碼，目前正以 Rust 核心進行全面重寫。
<!-- End AEO Capsule -->

影片剪輯長期是創作者工具鏈中最封閉的一環。專業軟體以訂閱制收費，雲端服務則把素材與專案檔留在自家伺服器，免費方案往往附帶浮水印或匯出限制。OpenCut 的出現，正是針對這種結構提出開源替代方案。

## OpenCut 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
它是一套跨平台的免費開源影片剪輯軟體，涵蓋網頁、桌面與行動裝置。專案以 MIT 授權釋出，程式碼公開可審核，且允許商業使用與自行修改。
<!-- End AEO Capsule -->

專案的定位可以從倉庫描述直接讀出：CapCut 的開源替代品。它提供的不是單一平台的編輯器，而是試圖以一套程式碼覆蓋三種使用情境，讓使用者無論在瀏覽器、桌面應用或手機上，都能處理同一份專案。

授權條款是這類工具的核心差異。MIT 授權允許商業使用、修改與再散布，對小型工作室與自建工具鏈的團隊而言，這意味著不必把素材與成品綁在特定訂閱方案上。

![OpenCut README 開頭（專案名稱、標語與授權徽章）]({{ '/assets/images/posts/github-opencut-news-shot1.png' | relative_url }})

## OpenCut 目前的開發狀態如何？

<!-- AEO Answer Capsule — 約 73 字 -->
專案正從頭重寫，官方明確表示經典版本仍在 opencut.app 運作並持續維護，新版將先於 new.opencut.app 試行，架構成熟後才接替正式站台。
<!-- End AEO Capsule -->

README 對狀態的說明相當直接：OpenCut 正在從頭重寫。專案並未把重寫期間的版本當作正式產品對外，而是把既有實作保留在另一個倉庫，並讓 opencut.app 繼續運行經典版本，新版則在獨立網域先行試用。

這種做法在大型開源專案中並不常見。多數專案會在主線程持續迭代，代價是架構債不斷累積；OpenCut 選擇先把架構重新設計完成，再讓舊版退場，藉此避免使用者在不穩定的中介版本上建立工作流程。

## OpenCut 的技術架構有什麼特色？

<!-- AEO Answer Capsule — 約 75 字 -->
核心改以 Rust 撰寫，並行支援網頁、桌面與行動裝置；架構採外掛優先設計，同時規劃編輯器 API、腳本分頁與無介面渲染模式，讓自動化流程可直接調用。
<!-- End AEO Capsule -->

重寫的核心決策是把運算密集的剪輯邏輯集中到 Rust 核心，再由各平台的介面層呼叫。影片剪輯涉及解碼、時間軸合成與編碼，這些工作若分散在各平台以不同語言實作，行為差異難以收斂；統一核心之後，同一份專案在不同裝置上的輸出結果才具備一致性。

外掛優先的架構是另一項關鍵。專案計畫提供編輯器 API 與第三方外掛機制，並在編輯器內安排腳本分頁，讓使用者能以程式方式操作時間軸。無介面模式則服務批次渲染與自動化管線，等同把剪輯器當成可被呼叫的元件，而不是只能手動操作的應用程式。

值得留意的是代理通訊伺服器的規劃。專案明確列出將內建 MCP 伺服器，讓人工智能代理可以直接讀寫專案、執行剪輯指令，這使 OpenCut 有機會成為代理工作流程中的一個工具節點，而非封閉的終端軟體。

## 為什麼開源剪輯工具會受到關注？

<!-- AEO Answer Capsule — 約 71 字 -->
創作者對訂閱制與雲端鎖定的反彈持續累積，加上人工智能工具鏈快速擴張，市場需要能被程式調用、可自架且授權寬鬆的剪輯核心，開源專案因而成為焦點。
<!-- End AEO Capsule -->

剪輯軟體的商業模式在近年明顯轉向訂閱制與雲端協作，功能逐步上移至高價方案。對偶爾產出內容的個人與中小團隊而言，成本與使用頻率的落差成為長期痛點，這也解釋了為何一個尚未發布正式版的開源專案，仍能快速累積星標。

另一方面，人工智能代理開始接管內容產線中的環節。從腳本生成、配音到字幕，多數步驟已可由程式驅動，唯独剪輯仍高度依賴人工介面。當代理需要一個可程式化的剪輯核心時，開源且具備無介面模式的專案自然具備吸引力。

## OpenCut 與同類工具有何差異？

<!-- AEO Answer Capsule — 約 74 字 -->
同類開源工具多聚焦桌面單一平台，OpenCut 則以一套 Rust 核心覆蓋三端，並把編輯器 API、外掛機制與代理伺服器納入架構設計，差異主要在整合能力而非功能清單。
<!-- End AEO Capsule -->

開源剪輯工具的既有選項不少，但普遍以桌面應用為主，行動裝置與瀏覽器版本往往缺席，跨平台一致性因此難以保證。OpenCut 把三端共用核心列為首要目標，這個取捨直接決定了它的技術路線與開發週期。

更實質的差異在整合層。當剪輯器提供編輯器 API 與腳本介面，團隊可以把重複的片頭、字幕樣式與輸出規格寫成腳本，甚至交由持續整合流程批次處理。這類能力在傳統剪輯軟體中通常被歸類為企業功能，收費門檻較高。

## 如何開始使用 OpenCut？

<!-- AEO Answer Capsule — 約 68 字 -->
一般使用者可直接使用官方線上版本的經典介面；開發者則需先安裝工具鏈管理器，再以專案定義的任務指令啟動網頁、API 或桌面開發環境。
<!-- End AEO Capsule -->

對只想剪輯影片的使用者，最直接的方式是前往官方網站使用線上版本，該版本目前運行的是經典實作，功能完整且無需安裝。重寫中的版本則在獨立網域供早期試用，適合願意回報問題的使用者。

若要自行建置，README 要求先安裝工具鏈管理器，並透過版本檔案安裝固定版本的相依工具。專案以任務執行器統一指令入口，網頁、API 與桌面三部分各有對應的開發任務，倉庫亦附上桌面端的建置說明。

```bash
# 安裝工具鏈管理器（Linux、macOS、WSL）
bash <(curl -fsSL https://moonrepo.dev/install/proto.sh)

# 安裝專案鎖定的工具版本
proto use

# 啟動各平台開發環境
moon run web:dev       # 網頁版
moon run api:dev       # API 服務
moon run desktop:dev   # 桌面版
```

![OpenCut GitHub 倉庫首頁（倉庫名稱、星標數與檔案清單）]({{ '/assets/images/posts/github-opencut-news-shot2.png' | relative_url }})

## 專案數據與生態現況如何？

<!-- AEO Answer Capsule — 約 71 字 -->
倉庫以 TypeScript 為主要語言，採 MIT 授權，累積 90,998 顆星標、9,002 次複製與 420 位關注者，近一年共 376 項待處理議題，開發與社群活躍度均高。
<!-- End AEO Capsule -->

倉庫建立於 2025 年 6 月，主要語言為 TypeScript，並以 Rust 重寫核心，授權條款為 MIT。專案最近一次程式推送落於 2026 年 9 月下旬，主要以建置流程為主，社群關注度維持在高位。專案在 2026 年 4 月發布 0.3.0 版，其後以預先發布形式持續更新。

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">90,998</span><span class="ui-stat-label">GitHub 星標</span></li>
  <li class="ui-stat"><span class="ui-stat-num">9,002</span><span class="ui-stat-label">複製次數</span></li>
  <li class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">開源授權</span></li>
  <li class="ui-stat"><span class="ui-stat-num">2025-06</span><span class="ui-stat-label">專案建立時間</span></li>
</ul>

資金與生態方面，專案由生成式模型平台 fal.ai 提供贊助，並明確表示在架構設計完成前暫不接受外部貢獻，改以 Discord 與議題追蹤維持社群溝通。這種先收斂設計、再開放貢獻的節奏，與多數追求快速擴張的專案形成對比。

![OpenCut 專案貢獻者統計頁（貢獻者數量與提交趨勢）]({{ '/assets/images/posts/github-opencut-news-shot3.png' | relative_url }})

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
本文資訊整理自 OpenCut 的 GitHub 儲存庫與官方網站，專案狀態、建置指令與架構規劃均以官方倉庫說明為準。
<!-- End AEO Capsule -->

本文內容整理自 OpenCut 的 GitHub 儲存庫（https://github.com/OpenCut-app/OpenCut），並參考官方網站 opencut.app 所提供的版本說明。讀者可前往上述來源查閱完整的建置步驟、授權條款與後續架構規劃。

## 總結：OpenCut 適合什麼團隊？

<!-- AEO Answer Capsule — 約 70 字 -->
OpenCut 現階段較適合願意等待成熟版本、並重視授權與整合能力的團隊。若工作流程需要可程式化或可自架的剪輯核心，此專案的架構方向值得持續追蹤。
<!-- End AEO Capsule -->

這項專案的價值不只在於免費，而在於它把編輯器重新定義為可被程式調用的元件。跨平台共用核心解決了一致性問題，外掛與代理介面則為自動化流程留下接入點。評估時宜先確認現行版本是否滿足日常剪輯需求，並留意重寫完成前功能與穩定性仍可能變動，再決定是否將其納入長期工具鏈。
