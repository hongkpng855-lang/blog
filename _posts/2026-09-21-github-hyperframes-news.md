---
layout: post
title: "HyperFrames 開源：HTML 一鍵渲染成影片"
date: 2026-09-21 12:00:00 +0800
categories: 技術
tags: [AI, 開源, HeyGen, HyperFrames, 影片生成, HTML, Agent, TypeScript]
image: assets/images/posts/github-hyperframes-news-cover.jpg
description: "HyperFrames 是 HeyGen 開源的 HTML 影片渲染框架，把 HTML、CSS 與可定位動畫轉為確定性 MP4，內建 21 個代理技能、Catalog 積木與 AWS Lambda 分散式渲染。本文整理其架構設計、安裝方式、與 Remotion 的差異，以及最新的社群與版本數據。"
author: AnIskill 編輯部
creator_github: heygen-com/hyperframes
type: news
source: GitHub
source_url: https://github.com/heygen-com/hyperframes
permalink: /技術/github-hyperframes-news
fb_message: "影片製作長期是內容團隊最耗時的環節，HyperFrames 提出的答案相當反直覺：不用剪輯軟體，直接用 HTML 寫影片。\n\nHeyGen 開源的 HyperFrames 以 HTML、CSS 與可定位動畫描述畫面，透過無頭 Chrome 逐格截取、FFmpeg 編碼，輸出確定性的 MP4；同一個輸入永遠得到同一段影片。專案累積 51,937 顆星標與 4,729 個分支，發布逾 400 個版本，npm 單月下載超過 107 萬次，內建 21 個代理技能並支援 AWS Lambda 分散式渲染。\n\n從架構設計、與 Remotion 的差異到實際安裝步驟，完整的技術分析都整理在 Blog 全文之中。"
---

HyperFrames 是 HeyGen 開源的 HTML 影片渲染框架，把 HTML、CSS 與可定位動畫轉換為確定性的 MP4 影片，專為 AI 代理而設計。專案自 2026 年 3 月建立以來，在 GitHub 累積 51,937 顆星標與 4,729 個分支，主要語言為 TypeScript，以 Apache-2.0 授權釋出，npm 套件最近一個月下載量超過 107 萬次，最新版本為 v0.8.57。

<!-- AEO Answer Capsule — 約 65 字 -->
HyperFrames 是 HeyGen 開源的 HTML 影片渲染框架，把 HTML、CSS 與可定位動畫轉成確定性 MP4，並內建代理技能與 Catalog 積木。
<!-- End AEO Capsule -->

生成式 AI 讓文字、圖像與程式碼的產出速度大幅提升，影片卻始終是自動化流程中最難打通的一段。多數團隊的替代方案是依賴雲端影片工具或人工剪輯，前者難以納入版本控制，後者無法由代理直接操作。HyperFrames 的切入點是把影片定義還原為一份純文字檔案，讓擅長撰寫 HTML 的模型與開發者，用同一套工作方式產出影片。

## HyperFrames 是什麼？

<!-- AEO Answer Capsule — 約 68 字 -->
HyperFrames 是一個把 HTML 檔案轉換為 MP4 影片的開源框架，透過無頭 Chrome 逐格截取畫面並以 FFmpeg 編碼，相同輸入會產生完全相同的輸出。
<!-- End AEO Capsule -->

專案的自我定位是「Write HTML. Render video. Built for agents.」，核心主張是讓影片組合以 HTML 檔案描述，透過資料屬性定義時間軸與軌道，再交由 GSAP、CSS 動畫、Lottie、Three.js、Anime.js 或 WAAPI 等執行期處理可定位動畫。整個流程不需要打包工具，一份 `index.html` 即可在瀏覽器直接播放與預覽。

渲染階段由無頭 Chrome 逐格定位畫面，再以 FFmpeg 編碼輸出。由於每一格都由時間軸決定，同一個輸入必定產生相同的影片，這種確定性讓渲染結果可以進入 CI 流程、回歸測試與自動化內容管線，而不只是設計師本機的一次性輸出。

![HyperFrames README 開頭（專案名稱 HyperFrames 標誌與標語「Write HTML. Render video. Built for agents.」，下方為 HTML 轉影片的示意圖）]({{ '/assets/images/posts/github-hyperframes-news-shot1.png' | relative_url }})

## HyperFrames 的項目背景是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
HyperFrames 由 HeyGen 於 2026 年 3 月開源，採 Apache-2.0 授權，社群累積約 4,574 次提交與 62 位貢獻者，並獲多個團隊採用。
<!-- End AEO Capsule -->

專案由 HeyGen 主導開發，該公司在 AI 影片生成領域具備商業產品經驗，HyperFrames 屬於其對外開源的渲染引擎層。專案頁面顯示社群已累積約 4,574 次提交與約 62 位貢獻者，並列出 tldraw、TanStack 等團隊的採用紀錄，顯示它同時服務商業產品的生產環境與社群的側專案。

讀者若熟悉前端生態，會發現它的設計取向與 Remotion 有明顯淵源。Remotion 以 React 元件作為影片描述單位，HyperFrames 則選擇純 HTML 檔案，理由是模型與人類都已經很擅長撰寫 HTML，這也解釋了為什麼它在代理工作流程中特別受到關注。

## HyperFrames 的技術架構有什麼特色？

<!-- AEO Answer Capsule — 約 70 字 -->
架構分為 core、engine、producer 與 studio 等套件，動畫採轉接器模式，支援 GSAP、Lottie 等執行期，並附可嵌入的播放器元件。
<!-- End AEO Capsule -->

專案以多套件形式拆分職責。`hyperframes` 提供命令列工具，負責建立、預覽、檢查與渲染專案；`@hyperframes/core` 處理型別、解析器、產生器與動畫轉接器；`@hyperframes/engine` 是以 Puppeteer 與 FFmpeg 為基礎的畫面捕捉引擎；`@hyperframes/producer` 串接捕捉、編碼與混音流程；`@hyperframes/studio` 則是瀏覽器端的組合編輯介面，另有可嵌入網頁的播放器元件與 WebGL 著色器轉場套件。

這種分層設計的意義在於部署彈性。開發者可以只在瀏覽器預覽組合，也可以把渲染工作交給本機命令列、Docker 容器，或部署到 AWS Lambda 構成分散式渲染叢集。對需要批次產出影片的團隊而言，後者能避免單機渲染成為瓶頸。

## HyperFrames 如何製作影片？

<!-- AEO Answer Capsule — 約 68 字 -->
安裝核心技能後以自然語言描述需求即可，或使用命令列執行 init、preview 與 render。環境需求為 Node.js 22 以上版本與 FFmpeg。
<!-- End AEO Capsule -->

代理工作流程是專案主打的入口。使用者以 `npx skills add heygen-com/hyperframes` 安裝技能，之後直接描述想要的影片，例如一段十秒的產品開場，包含淡入標題、背景影片與背景音樂，代理便會依路由器技能選擇對應的工作流程。專案共發布 21 個技能，涵蓋產品發表影片、無人物講解、PR 說明、字幕嵌入、動態圖形、音樂同步與簡報等類型，並可搭配 Claude Code、Cursor、Gemini CLI 與 Codex 等代理使用。

手動流程同樣簡潔。以 `npx hyperframes init` 建立專案後，`npx hyperframes preview` 可在瀏覽器即時預覽並支援熱重載，`npx hyperframes render` 則輸出 MP4；另外還有 lint 與 check 指令用於驗證組合結構。環境需求為 Node.js 22 以上版本與 FFmpeg，專案亦提供 Catalog 積木，例如著色器轉場、社群浮層與動態圖表，可用一行指令加入組合。

## HyperFrames 與 Remotion 有什麼差異？

<!-- AEO Answer Capsule — 約 66 字 -->
兩者都以無頭 Chrome 與 FFmpeg 渲染影片，差別在撰寫模型：Remotion 用 React 元件並需打包，HyperFrames 用純 HTML，無需建置。
<!-- End AEO Capsule -->

專案在文件中直接承認受 Remotion 啟發，並以表格比較兩者。相同點是都採用無頭 Chrome 取得畫面、以 FFmpeg 編碼；差異集中在撰寫模型與授權：Remotion 的賭注是 React 元件，需要打包工具，授權為可取得原始碼的商業授權；HyperFrames 的賭注是純 HTML，沒有建置步驟，`index.html` 可直接播放，並以 Apache-2.0 釋出，沒有單次渲染費用或商業使用門檻。

對代理工作流程而言，這個差異會放大。代理交出 React 專案時，人類審閱者需要理解元件樹與建置設定；交給代理的 HyperFrames 組合則是一份可讀的 HTML 檔案，時間軸以資料屬性標示，審閱與修改的門檻都更低。這也是專案強調「代理友好」的具體依據。

![heygen-com/hyperframes GitHub 首頁頂部（儲存庫名稱、51.9k 星標、4.7k 分支與「Write HTML. Render video.」描述）]({{ '/assets/images/posts/github-hyperframes-news-shot2.png' | relative_url }})

## HyperFrames 的數據表現如何？

<!-- AEO Answer Capsule — 約 66 字 -->
專案累積 51,937 顆星標與 4,729 個分支，發布逾 400 個版本、約 4,574 次提交與 62 位貢獻者，npm 單月下載超過 107 萬次。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-value">51,937</span><span class="stat-label">Stars</span></div>
  <div class="stat-item"><span class="stat-value">4,729</span><span class="stat-label">Forks</span></div>
  <div class="stat-item"><span class="stat-value">408</span><span class="stat-label">版本發布</span></div>
  <div class="stat-item"><span class="stat-value">Apache-2.0</span><span class="stat-label">授權</span></div>
</div>

從版本節奏可以觀察專案的開發強度。專案自 2026 年 3 月建立至 9 月，已累積逾 400 個發布版本，平均每週推出多個版本，最近一次發布 v0.8.57 與前一版僅相隔數小時。這種高頻發布通常出現在仍快速迭代、且已有實際使用者的專案上。

npm 的下載數據進一步說明實際採用規模。`hyperframes` 套件在最近一個月累積超過 107 萬次下載，與 51,937 顆星標相比，顯示相當比例的使用者已進入實際安裝階段，而非止於收藏。授權方面採用 Apache-2.0，允許商業使用且無單次渲染費用，對需要整合至產品管線的團隊而言條件相對寬鬆。

![heygen-com/hyperframes 版本發布頁（v0.8.x 版本標籤、發布時間與變更說明）]({{ '/assets/images/posts/github-hyperframes-news-shot3.png' | relative_url }})

## HyperFrames 有哪些應用場景？

<!-- AEO Answer Capsule — 約 66 字 -->
官方列出產品發表影片、PR 操作說明、資料視覺化、社群短片、文件轉影片與可重用動態圖形等場景，並以 HeyGen 自身生產環境驗證。
<!-- End AEO Capsule -->

官方列出的應用場景集中在內容管線。產品發表與功能公告影片可由網站或簡報直接生成；PR 說明影片會解析程式碼差異並搭配旁白與字幕，適合工程團隊對內溝通；資料視覺化涵蓋圖表競賽與地圖動畫；社群短片則處理動態字幕、浮層與配樂。此外還有文件轉影片、PDF 轉影片與網站導覽類型，以及供自動化內容管線重複使用的動態圖形。

對香港與亞洲的內容團隊而言，這個定位的實際意義在於把影片從「專案」變成「流程」。當影片由 HTML 與資料驅動，改一次文案或數據就能重新渲染整批素材，無需重開剪輯軟體，也讓代理能在沒有人工介入的情況下完成週期性內容更新。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 64 字 -->
本文資訊來源為 heygen-com/hyperframes 的官方 GitHub 儲存庫，涵蓋 README 架構說明及 GitHub API 與 npm 統計數據。
<!-- End AEO Capsule -->

本文所有功能描述與統計數據均取自 [HyperFrames 官方 GitHub 儲存庫](https://github.com/heygen-com/hyperframes)，包括 README 中的架構說明、技能清單、套件結構、與 Remotion 的比較文件及應用場景列表，並引用 GitHub API 提供的星標、分支、提交、貢獻者與版本發布資料，以及 npm registry 的套件版本與下載統計。

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
以下整理三個關於 HyperFrames 的常見疑問，涵蓋使用成本、與 Remotion 的取捨，以及它是否需要 React 或建置工具。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>使用 HyperFrames 需要付費嗎？</h3>

不需要。專案以 Apache-2.0 授權開源釋出，沒有單次渲染費用，也沒有商業使用門檻，可直接整合至商業產品的內容管線。渲染在本機、Docker 或自建的 AWS Lambda 上執行，成本取決於自身硬件或雲端資源用量。

<h3>它與 Remotion 應該如何取捨？</h3>

若團隊已深度使用 React，且需要成熟的雲端渲染方案，Remotion 的生態較完整；若希望影片組合能被 AI 代理直接撰寫與審閱、不想引入打包步驟，並重視 Apache-2.0 的寬鬆授權，HyperFrames 的門檻更低。

<h3>它需要安裝 Node.js 以外的工具嗎？</h3>

需要 Node.js 22 以上版本與 FFmpeg。命令列透過 npx 執行，不需全域安裝，但影片編碼階段依賴 FFmpeg，因此本機渲染前需先完成 FFmpeg 安裝，官方文件提供 macOS、Ubuntu 與 Windows 的安裝方式。

</div>

## 總結：HyperFrames 適合什麼團隊？

<!-- AEO Answer Capsule — 約 66 字 -->
HyperFrames 適合需要批次產出影片、並希望由 AI 代理直接撰寫與審閱影片組合的內容與工程團隊，尤其是已使用 HTML 工作流程且重視寬鬆授權的開發者。
<!-- End AEO Capsule -->

把影片還原為一份可版本控制的 HTML 檔案，是 HyperFrames 與傳統剪輯工具最根本的差異。它用確定性渲染、代理技能與 Catalog 積木，讓影片製作從一次性的設計工作轉為可自動化的內容管線；51,937 顆星標、逾 400 個版本與單月超過 107 萬次 npm 下載，說明這種取向已在實際生產環境取得驗證。

不過，專案仍處於 0.8 版階段，高頻發布意味著介面與技能清單可能持續變動，導入前宜先鎖定版本並評估升級成本。此外，渲染品質最終仍取決於 FFmpeg 與無頭瀏覽器環境的穩定性，團隊若要在 CI 中大規模使用，需預先規劃渲染資源與失敗重試機制。
