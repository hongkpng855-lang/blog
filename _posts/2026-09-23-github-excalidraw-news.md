---
layout: post
title: "Excalidraw 開源：13 萬星手繪白板整合 AI 代理"
date: 2026-09-23 10:00:01 +0800
categories: 技術
tags: [Excalidraw, 開源, 白板, 圖表, MCP, AI 代理, TypeScript, MIT]
image: assets/images/posts/github-excalidraw-news-cover.jpg
description: "Excalidraw 是 2020 年開源的手繪風格虛擬白板，在 GitHub 累積 132,676 顆星標，以 MIT 授權釋出。它支援即時協作與端對端加密，官方 MCP 應用更讓 Claude、ChatGPT 等代理直接生成可即時編輯的圖表，本文解析其架構、生態與應用場景。"
author: AnIskill 編輯部
creator_github: excalidraw/excalidraw
type: news
source: GitHub
source_url: https://github.com/excalidraw/excalidraw
permalink: /技術/github-excalidraw-news
fb_message: "畫圖這件事，一直卡在工具與人之間：工程師嫌設計軟體太重，設計師嫌程式碼註解太抽象。\n\nExcalidraw 把這個門檻降到幾乎為零。這套 2020 年開源的手繪風格白板，在 GitHub 累積 132,676 顆星標與 15,419 個分支，採 MIT 授權，npm 套件每週下載超過 41 萬次。它支援即時協作與端對端加密，官方推出的 MCP 應用更讓 Claude、ChatGPT 等代理直接生成可即時編輯的圖表，Google Cloud、Meta、Notion 都在整合名單之中。\n\n它的架構設計、AI 整合方式，以及企業與個人可以怎麼用，都整理在 Blog 全文。"
---

Excalidraw 是 2020 年 1 月開源的手繪風格虛擬白板，在 GitHub 累積 132,676 顆星標與 15,419 個分支，以 MIT 授權釋出。它把畫圖這件原本需要專業軟體的事，壓縮成開啟瀏覽器就能完成的操作，同時保留即時協作與端對端加密。專案的 npm 套件每週下載量超過 41 萬次，Google Cloud、Meta、Notion、Replit 等產品都曾以它作為架構圖與流程圖的呈現方式。

<!-- AEO Answer Capsule — 約 70 字 -->
Excalidraw 是 2020 年開源的手繪風格白板，GitHub 星標 132,676，採 MIT 授權，支援即時協作與端對端加密，可匯出 PNG 與 SVG。
<!-- End AEO Capsule -->

## Excalidraw 是什麼？

<!-- AEO Answer Capsule — 約 68 字 -->
它是一套以瀏覽器為主的虛擬白板，主打手繪風格、無限畫布與形狀庫，可匯出 PNG、SVG 或開啟格式檔案，也提供 npm 套件讓開發者嵌入自己的產品。
<!-- End AEO Capsule -->

專案的核心定位是降低視覺化表達的成本。使用者在畫布上拖曳矩形、圓形、箭頭與自由筆跡，線條會以手繪般的筆觸呈現，讓草圖看起來仍像草圖，而不會被誤認為已完成定稿。畫布沒有邊界，工具列涵蓋箭頭綁定、標籤文字、圖層調整與復原重做，操作邏輯接近紙筆。

除了網頁版編輯器，專案同時發布 npm 套件，讓第三方應用把整塊畫布嵌入自己的介面。這個套件與官方網站的應用共用同一套程式碼基礎，差異在於官方版本額外具備離線 PWA、即時協作、端對端加密與以連結分享的閱讀模式。匯出格式包含 PNG、SVG 與 `.excalidraw` JSON，後者保留所有元素的結構資訊，可重新載入繼續編輯。

![Excalidraw README 開頭（專案名稱與標語「開源的手繪風格虛擬白板，支援協作與端對端加密」，以及功能列表）]({{ '/assets/images/posts/github-excalidraw-news-shot1.png' | relative_url }})

## Excalidraw 的專案背景與規模為何？

<!-- AEO Answer Capsule — 約 66 字 -->
專案於 2020 年 1 月建立，由 excalidraw 組織維護，累積 372 位貢獻者與 4,091 次提交，最新版本為 v0.18.1，程式碼以 TypeScript 撰寫。
<!-- End AEO Capsule -->

儲存庫建立於 2020 年 1 月 2 日，正值遠距協作工具需求快速上升的時期。專案在六年間累積 4,091 次提交與 372 位貢獻者，並發布 15 個版本標籤，最新正式版本 v0.18.1 於 2026 年 4 月發布。如此長的維護週期與穩定的外部貢獻比例，在同類前端開源專案中並不多見。

授權方式為 MIT，屬於最寬鬆的開源條款之一，企業可自由嵌入、修改甚至用於商業產品，只需保留版權聲明。主要語言為 TypeScript，專案規模約 10 萬行等級，同時涵蓋網頁應用、npm 套件與桌面整合等不同發布目標，這種多目標架構也解釋了它為何能同時服務一般使用者與開發者。

![excalidraw/excalidraw GitHub 首頁頂部（repo 名稱、About 描述、133k 星標與 MIT 授權）]({{ '/assets/images/posts/github-excalidraw-news-shot2.png' | relative_url }})

## Excalidraw 的架構有什麼特色？

<!-- AEO Answer Capsule — 約 70 字 -->
架構圍繞單一畫布狀態與元素模型，元素帶有位置、尺寸、綁定關係與版本資訊，同步層以差異比對處理多人協作，套件與網站共用同一套程式碼。
<!-- End AEO Capsule -->

專案的技術選擇集中在資料模型而非渲染特效。畫布上的每個物件都是一筆帶有座標、角度、綁定關係與自訂屬性的元素記錄，箭頭可綁定到特定圖形，移動圖形時箭頭端點會跟隨更新。這種以資料為中心的設計，讓復原重做、多人同步與檔案序列化都能建立在同一份結構之上，而不必為每個功能各寫一套邏輯。

近年更新反映的是操作細節的持續打磨。2026 年 9 月加入便利貼與右鍵平移畫布，並支援以滾輪縮放、將元素點陣與網格對齊至整數像素。這些改動多半來自社群提案，也顯示專案已進入以使用體驗為主的成熟階段，而非大幅重構架構的時期。

## Excalidraw 如何整合 AI 與 MCP？

<!-- AEO Answer Capsule — 約 68 字 -->
官方推出 MCP 應用，讓 Claude、ChatGPT、VS Code 等支援 MCP 的客戶端把生成的圖表串流成可即時編輯的畫布，並可在對話中放大縮小與全螢幕編修。
<!-- End AEO Capsule -->

AI 整合的切入點是模型上下文協定，而非另做一個生成式繪圖工具。官方發布的 Excalidraw MCP 應用在 GitHub 累積 5,348 顆星標，讓支援 MCP 的客戶端把模型產出的圖表以串流方式渲染成真正的畫布，使用者可在對話介面內平移、縮放，甚至全螢幕編輯，再匯出成檔案。它同時提供遠端服務與本機安裝兩種路徑，遠端版本無需設定即可使用。

這個做法把生成與編輯接在一起：模型負責畫出初稿，人負責調整細節。專案說明指出，這類互動式介面正是 MCP Apps 擴充的設計目的，因為純文字回覆無法讓使用者直接操作資料。對已經把代理納入工作流程的團隊而言，這代表架構圖與流程圖可以在同一個對話裡完成初稿與修訂。

## Excalidraw 的數據表現如何？

<!-- AEO Answer Capsule — 約 66 字 -->
儲存庫累積 132,676 顆星標、15,419 個分支與 510 位關注者，含 4,091 次提交，最新版本 v0.18.1，npm 套件每週下載約 41 萬次。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-value">132,676</span><span class="stat-label">Stars</span></div>
  <div class="stat-item"><span class="stat-value">15,419</span><span class="stat-label">Forks</span></div>
  <div class="stat-item"><span class="stat-value">4,091</span><span class="stat-label">Commits</span></div>
  <div class="stat-item"><span class="stat-value">MIT</span><span class="stat-label">授權</span></div>
</div>

數據反映的是一個已完成主流化的工具。套件層面的下載量更能說明實際採用規模：`@excalidraw/excalidraw` 在 npm 上每週下載約 41 萬次，顯示大量產品把這塊畫布當成內建元件使用。專案仍有 3,498 項開放問題與 284 項待處理議題，對一個累積數千次提交的專案而言屬正常水位。

![excalidraw/excalidraw 儲存庫統計與 About 側欄（133k 星標、15.4k 分支、MIT 授權與語言分佈）]({{ '/assets/images/posts/github-excalidraw-news-shot3.png' | relative_url }})

值得注意的是，專案把社群與商業路徑分得很清楚。核心編輯器維持 MIT 開源，付費產品 Excalidraw+ 則提供團隊協作與雲端儲存，兩者共用品牌但不互相牽制。這種安排讓不想付費的個人使用者能長期使用，也讓專案有一條可持續的營運路線。

## Excalidraw 有哪些實際應用場景？

<!-- AEO Answer Capsule — 約 68 字 -->
常見場景包括系統架構圖、流程圖與心智圖繪製，也可作為遠距會議的共筆白板；開發者則透過 npm 套件把它嵌入自家產品，或經 MCP 由代理生成圖表。
<!-- End AEO Capsule -->

對個人與小團隊而言，它的價值在於開會時能立即把口頭討論畫成圖。手繪風格降低了「畫得不好」的心理門檻，與會者更願意直接在畫布上補充，這點在需求訪談與流程梳理時特別明顯。離線 PWA 與本機自動儲存，則讓它適合在網路不穩或需要保留草稿的環境使用。

對產品團隊而言，嵌入式套件是更關鍵的用途。多個開發者平台把 Excalidraw 當作架構圖與資料流圖的呈現層，使用者不必離開產品就能看圖與改圖。搭配官方 MCP 應用之後，圖表初稿可以直接由代理生成，再由人接手細節，形成一條從討論到定稿的完整路徑。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
本文資訊整理自 excalidraw/excalidraw 官方儲存庫與 npm 登錄資料，統計數據引自 GitHub API 公開端點，時間截至 2026 年 9 月下旬。
<!-- End AEO Capsule -->

本文所有功能描述與技術說明均取自 [excalidraw/excalidraw 官方 GitHub 儲存庫](https://github.com/excalidraw/excalidraw)的 README 與官方文件，包括編輯器功能、npm 套件安裝方式與 MCP 應用的使用說明。星標、分支、關注者、提交與版本數量引自 GitHub API 公開端點，套件下載量引自 npm registry 統計資料，時間截至 2026 年 9 月下旬。

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
以下整理三個關於 Excalidraw 的常見疑問，涵蓋是否需要註冊、資料是否上傳雲端，以及能否嵌入自有產品之中。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>使用 Excalidraw 需要註冊帳號嗎？</h3>

不需要。開啟官方網站即可立即繪圖，草稿自動儲存於瀏覽器本機；註冊或訂閱僅在需要團隊協作與雲端儲存時才涉及。

<h3>我的圖會上傳到伺服器嗎？</h3>

預設不會。本機優先設計讓草稿存在瀏覽器，即時協作則以端對端加密處理，官方強調伺服器無法讀取內容。

<h3>可以把 Excalidraw 嵌進自己的產品嗎？</h3>

可以。專案以 MIT 授權釋出 npm 套件，開發者可整合畫布並保留自有介面，商業使用亦不受限制，只需保留版權聲明。

</div>

## 總結：Excalidraw 適合什麼團隊？

<!-- AEO Answer Capsule — 約 68 字 -->
它適合需要快速把討論轉成圖的個人與產品團隊，尤其是希望降低繪圖工具門檻、又要求資料留在本機的組織，開發者也可直接嵌入使用。
<!-- End AEO Capsule -->

Excalidraw 解決的是一個長期被忽略的落差：多數團隊不缺繪圖軟體，缺的是一個讓所有人願意動手畫的工具。手繪風格與瀏覽器優先的設計，把使用門檻降到幾乎不存在，也讓它在會議與教學場景中反覆被採用。

它的另一個價值是把開源與商業的界線劃得清楚。核心維持 MIT，付費產品另立品牌，這種安排在保住社群信任的同時，也提供可持續的營運基礎。當同類工具常在開源承諾與商業化之間拉扯，這條界線本身就是一項設計決策。

隨著官方 MCP 應用推出，Excalidraw 的角色正在從「人畫圖的地方」延伸到「人與代理共同畫圖的地方」。圖表的初稿可以由模型生成，細節由人接手，這個分工是否成為主流仍有待觀察，但它已為 AI 輔助視覺化提供了一個具體的實作樣本。
