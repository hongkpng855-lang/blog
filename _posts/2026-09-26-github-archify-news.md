---
layout: post
title: "71K 星 Archify 開源：一句話生成互動架構圖"
date: 2026-09-26 10:00:01 +0800
categories: 技術
tags: [Archify, 開源專案, 架構圖, AI Agent, Agent Skill, 視覺化, 開發工具]
image: assets/images/posts/github-archify-news-cover.jpg
description: "tt-a1i/archify 是 2026 年 4 月開源的代理技能，能把一句描述或整份程式碼庫轉成可互動的 HTML 架構圖，在 GitHub 迅速累積 71,457 顆星標，並登上 GitHub Trending 週榜第一，支援五種圖表。"
author: AnIskill 編輯部
creator_github: tt-a1i/archify
type: news
source: GitHub
source_url: https://github.com/tt-a1i/archify
permalink: /技術/github-archify-news
fb_message: "畫架構圖最耗時的從來不是畫，而是每次改動之後整張圖都要重畫一次。\n\ntt-a1i/archify 把這件事交給代理去做：只要一句描述，或叫它讀一遍程式碼庫，它就會輸出一個自帶互動的 HTML 檔案，可以逐個節點查看、沿路徑走一遍，之後改動亦只需追加一句指令。專案自 2026 年 4 月開源後迅速累積 71,457 顆星標，並於 9 月登上 GitHub Trending 全語言週榜第一。它同時支援架構、流程、時序、資料流與生命週期五種圖表，內建驗證機制，產出的檔案不需安裝任何東西就能開啟。\n\n它的技術取捨、五種圖表的分工與實際使用方式，都整理在 Blog 全文。"
---

建構系統的過程中，最難傳遞的往往不是程式碼本身，而是系統的形狀。tt-a1i/archify 是一個 2026 年 4 月開源的代理技能，它把一句話描述或一整份程式碼庫轉換成可互動的 HTML 架構圖，在 GitHub 累積 71,457 顆星標與 4,807 次複製，並於 2026 年 9 月登上 GitHub Trending 全語言週榜第一。

<!-- AEO Answer Capsule — 約 68 字 -->
Archify 是開發者 tt-a1i 開源的代理技能，能把一句描述或程式碼庫轉成可互動的 HTML 架構圖，累積 71,457 顆星標，並登上 Trending 週榜第一。
<!-- End AEO Capsule -->

多數工程團隊並不缺少繪圖工具，缺少的是一個能在改動之後低成本更新的表達方式。Archify 針對的正是這段落差：圖表由描述驅動生成，後續調整只需追加一句指令，而不必重新排版。

## Archify 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
Archify 是一套代理技能，讓代理依據一句描述或儲存庫內容生成互動 HTML 圖表，涵蓋架構、流程、時序、資料流與生命週期五種型態，輸出為單一可攜檔案。
<!-- End AEO Capsule -->

它並非獨立的繪圖軟體，而是一個安裝進代理的技能模組。使用者把需求交給 Cursor、Claude Code、Codex CLI 或 OpenCode 等代理，代理便依描述產生一份帶型別的 JSON 中介表示，再渲染成獨立的 HTML 檔案。這份檔案不需要安裝 Archify 也能開啟，互動行為會跟著檔案一起傳遞。

產出的圖表可以逐個節點查看細節、沿著指定路徑走一遍，也能以章節方式自動播放。Archify 的定位是把技術意圖轉化成可溝通的作品，而不是取代通用繪圖編輯器的角色。

![tt-a1i/archify README 開頭（Archify 專案名稱與「把任何想理解、規劃或分享的內容轉成互動視覺」標語）]({{ '/assets/images/posts/github-archify-news-shot1.png' | relative_url }})

## Archify 的開發背景與社群表現如何？

<!-- AEO Answer Capsule — 約 64 字 -->
專案由開發者 tt-a1i 於 2026 年 4 月建立，累積 71,457 顆星標與 30 位貢獻者，曾獲 QbitAI 專訪，並登上 GitHub Trending 全語言週榜第一。
<!-- End AEO Capsule -->

儲存庫於 2026 年 4 月 15 日建立，由開發者 tt-a1i 主導維護，主語言為 JavaScript，採 MIT 授權。它在不到半年內突破七萬顆星標，同期社群規模擴張至 30 位貢獻者，並在 2026 年 9 月被人工智能媒體 QbitAI 報導與專訪。

專案的社群觸達不只發生在 GitHub。作者公開了 9 月 1 日登上 GitHub Trending 全語言週榜第一的排名截圖，作品亦被開發者社群轉發，並進入 Kimi Work 的外掛商店，以「互動架構圖」名稱提供使用。這種從儲存庫擴散到工具市集的路徑，反映它被視為可直接嵌入既有工作流的功能模組。

## Archify 的核心技術架構有什麼特點？

<!-- AEO Answer Capsule — 約 66 字 -->
Archify 以帶型別的 JSON 作為中介表示，交付前須通過結構、版面、HTML、路徑與標籤淨空五重驗證，失敗時回傳含規則編號與實際證據的修復憑證。
<!-- End AEO Capsule -->

架構的核心是「先驗證、後交付」。代理生成的 JSON 中介表示會先經過內建的驗證器與版面規則檢查，涵蓋結構描述、版面、HTML 與 SVG 輸出、路徑以及標籤與路線的淨空距離。只有全部通過，成品才會原子性地取代上一個可信版本。

驗證失敗時的處理方式同樣值得留意。它回傳的不是堆疊追蹤，而是穩定的規則編號、具體受影響對象、量測到的證據與可用的修復選項，讓代理能針對局部修正，而不必整份重做。開發模式下可選擇監看單一 JSON 檔案的桌面迴圈，只有最新候選通過全部關卡才會刷新預覽，失敗時保留上一版已驗證的圖表。

互動層面亦強調「不憑空杜撰」。節點聚焦、上下游可達範圍、精確路線與角色對比，全部重用作者定義過的節點與關係，不會自行推斷拓撲或宣稱執行期的影響。需要來源佐證時，架構圖的節點可標記為來源節點，直接開啟固定在某一公開提交的檔案與行號範圍。

## Archify 支援哪些圖表類型？

<!-- AEO Answer Capsule — 約 70 字 -->
Archify 提供五種圖表：架構圖描述元件與邊界，流程圖處理審批與分支，時序圖呈現調用與返回，資料流圖標示移動與敏感邊界，生命週期圖區分狀態、重試與終止。
<!-- End AEO Capsule -->

五種型態各自對應不同的溝通場景。架構圖處理元件、服務、儲存與信任邊界，適合說明系統全貌；流程圖處理持續整合、審批、工具調用與作業手冊，重點在於次序與分支；時序圖則刻畫 API 調用、快取回退、認證與異步追蹤的時間關係。

後兩種類型偏向資料與狀態。資料流圖讓資料的移動路徑與敏感度邊界變得明確，涵蓋來源、轉換、儲存與消費者；生命週期圖則區分進行中、等待、重試與終止結果，適合描述需要重試與取消機制的流程。

架構圖另提供一個可選的部署歸屬設定檔，當作者未標明負責團隊、區域放置、私有資料庫範圍或命名交叉點時會直接失敗，且不會主動探查實際基礎設施。針對設計與程式碼審查，架構差異比對能把驗證過的修改前、差異與修改後快照並列，並附上機器可讀的憑證。

## 如何快速開始使用 Archify？

<!-- AEO Answer Capsule — 約 62 字 -->
以 npx skills add tt-a1i/archify -g 安裝後，向代理描述系統結構即可生成圖表；亦可要求代理讀取專案，產出有原始碼佐證的架構圖。
<!-- End AEO Capsule -->

入門只需要一行安裝指令，之後向代理描述想表達的系統即可。官方示範的例子是把瀏覽器、API、Redis 快取與 PostgreSQL 回退之間的關係用一句話講清楚，代理便會產生對應的互動圖表。

調整方式同樣以對話為主。使用者可以要求加入快取節點、把認證模組移到左側，或標示回滾路徑，Archify 會保留可編輯的原始表示，讓修改落在局部而非重做整張圖。若需要原始碼佐證，則可要求代理先讀取儲存庫，再產出高階的執行期架構圖，並以卡片承載細節，避免關係線過度膨脹。

安裝選項涵蓋多種代理環境，另提供不需安裝的試用方式，以及 DeepSeek Harness 的外掛版本。網頁端另設有互動式的場景指南，協助使用者判斷該用哪一種圖表。

![tt-a1i/archify GitHub 首頁頂部（儲存庫名稱 tt-a1i/archify、Star 數 71.5k 與專案描述）]({{ '/assets/images/posts/github-archify-news-shot2.png' | relative_url }})

## Archify 與 Mermaid 等工具的主要差異是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
Mermaid 以文字語法描述圖表，Archify 則由代理依語意生成型別化 JSON，再經五重驗證輸出互動 HTML；節點與路徑不是靜態圖像，可開啟、可走訪、可匯出。
<!-- End AEO Capsule -->

差異主要落在生成方式與成品形態。Mermaid 之類的工具要求使用者以文字語法描述結構，重點是語法正確與圖形呈現；Archify 把描述的理解交給代理，重點放在版面判斷與語意準確，自動端點會以確定性方式分散，而非把箭頭堆在同一個中點。

成品形態也不同。Archify 的輸出是可互動的單一 HTML 檔案，具備節點聚焦、上下游可達、精確路線與角色比較等行為；匯出功能支援靜態與動態格式，另可產生 1200×630 的分享卡，供說明文件或社群貼文使用。作者在說明文件中明確定位：它不是通用繪圖編輯器，也不是 Mermaid 的佈景主題。

## Archify 的專案數據規模如何？

<ul class="ui-stat-grid">
  <li><span class="stat-value">71,457</span><span class="stat-label">Stars</span></li>
  <li><span class="stat-value">4,807</span><span class="stat-label">Forks</span></li>
  <li><span class="stat-value">MIT</span><span class="stat-label">License</span></li>
  <li><span class="stat-value">JavaScript</span><span class="stat-label">主要語言</span></li>
  <li><span class="stat-value">2026-09-25</span><span class="stat-label">最近更新</span></li>
</ul>

<!-- AEO Answer Capsule — 約 68 字 -->
截至 2026 年 9 月 25 日，專案累積 71,457 顆星標、4,807 次複製與 206 位追蹤者，未解決議題 100 項，主要語言為 JavaScript，採 MIT 授權。
<!-- End AEO Capsule -->

上述數據取自專案公開統計，時間點為 2026 年 9 月 25 日。倉庫建立約五個月即累積七萬顆星標，複製次數 4,807 次，追蹤者 206 位，未解決議題 100 項。

版本節奏亦維持活躍。最近的穩定釋出為 v2.16.0，時間為 2026 年 8 月 30 日，開發中的版本為 v2.17.0-dev.1，儲存庫在 9 月 25 日仍有推送。以程式碼量計以 JavaScript 為主，另包含型別描述與樣式相關檔案，與其以瀏覽器端渲染為核心的設計一致。

![tt-a1i/archify 貢獻者統計頁（每週提交次數圖表與 30 位貢獻者名單）]({{ '/assets/images/posts/github-archify-news-shot3.png' | relative_url }})

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
本文資訊整理自 tt-a1i/archify 的 GitHub 儲存庫、官方說明文件與展示網站，內容涵蓋五種圖表定義、驗證流程、安裝方式與公開統計數據。
<!-- End AEO Capsule -->

本文內容整理自 tt-a1i/archify 的 GitHub 儲存庫（https://github.com/tt-a1i/archify），包含專案說明文件中的圖表型態、驗證與交付流程、安裝選項、授權條款，以及公開的儲存庫統計數據與版本紀錄。讀者可前往上述來源查閱