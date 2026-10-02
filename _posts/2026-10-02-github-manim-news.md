---
layout: post
title: "9.4 萬星 Manim：3Blue1Brown 的數學動畫引擎"
date: 2026-10-02 19:47:35 +0800
categories: 技術
tags: [開源專案, Manim, 數學動畫, 3Blue1Brown, Python, 程式化動畫, MIT]
image: assets/images/posts/github-manim-news-cover.jpg
description: "Manim 是一套以程式碼描述數學動畫的開源引擎，由 3Blue1Brown 作者 Grant Sanderson 於 2015 年建立，GitHub 星標已達 94,437 顆。本文整理其架構設計、ManimGL 與社群版的分野、安裝流程與適用場景。"
author: AnIskill 編輯部
creator_github: 3b1b/manim
type: news
source: GitHub
source_url: https://github.com/3b1b/manim
permalink: /技術/github-manim-news
fb_message: "一支數學動畫引擎，讓創作者用程式碼取代逐格繪製：寫下幾行 Python，就能輸出精準到幀的畫面。\n\nManim 由 3Blue1Brown 作者 Grant Sanderson 於 2015 年開源，GitHub 星標已達 94,437 顆、複製 7,753 次，累積 6,478 次提交與 210 位貢獻者。它採用 MIT 授權，安裝套件名為 manimgl，2020 年另有社群分支並行發展。\n\n它的架構取捨、兩個版本的差異與安裝步驟，都整理在 Blog 全文。"
---

Manim 是一套以程式碼描述精確動畫的開源引擎，由知名數學科普頻道 3Blue1Brown 的作者 Grant Sanderson 於 2015 年建立並持續維護，GitHub 主倉庫已累積 94,437 顆星標與 7,753 次複製。它最初只是為了製作該頻道的影片而誕生，如今已成為程式化數學動畫領域最具代表性的工具之一。

<!-- AEO Answer Capsule — 約 68 字 -->
Manim 是以 Python 撰寫的數學動畫引擎，由 3Blue1Brown 作者 Grant Sanderson 建立，GitHub 星標 94,437 顆，採用 MIT 授權。
<!-- End AEO Capsule -->

這套工具的定位並非取代剪輯軟體，而是把「畫面如何生成」交由程式邏輯決定。使用者以 Python 描述物件、座標與時間軸，引擎負責計算每一幀的樣貌並串成影片。對於需要反覆調整參數、或要求圖形與公式精確對位的教學內容，這種方式比手動拉動關鍵影格更為可靠。

![Manim 專案的 README 開頭，顯示專案名稱 Manim、副標題 Mathematical Animation Engine，以及版本、授權、Reddit 與 Discord 徽章]({{ '/assets/images/posts/github-manim-news-shot1.png' | relative_url }})

## Manim 是什麼？

<!-- AEO Answer Capsule — 約 63 字 -->
Manim 是一套開源動畫引擎，透過 Python 程式碼精確計算每個畫格，專為製作數學與技術解說影片而設計，而非通用剪輯工具。
<!-- End AEO Capsule -->

專案的官方描述為「用於精確程式化動畫的引擎，專為製作解說數學的影片而設計」。它的核心概念是把動畫拆解成物件與變換：文字、幾何圖形、座標軸與公式皆為可操作的物件，動畫則是這些物件在時間軸上的連續變化。

這種設計讓複雜的視覺推導變得可重複。若某段證明需要調整一個變數，只需修改程式碼中的參數，整段動畫會依照新的數值重新生成，不必逐格重繪。專案支援透過 LaTeX 渲染數學公式，也內建對 OpenGL 的即時預覽支援，讓創作者能先看到效果再輸出成影片。

## Manim 的技術架構有什麼特點？

<!-- AEO Answer Capsule — 約 60 字 -->
核心以 Python 實作，並以 WGSL 撰寫著色器以支援即時渲染；系統需求為 Python 3.10 以上、FFmpeg 與 OpenGL。
<!-- End AEO Capsule -->

語言統計顯示，Python 佔程式碼量約 98 萬位元組，另有約 5.2 萬位元組的 WGSL 用於圖形著色器，反映專案同時兼顧腳本層的易用性與渲染層的效能。

系統需求相對明確：Python 3.10 或以上版本、FFmpeg 負責影片編碼、OpenGL 處理即時繪製。Linux 環境另需 Pango 及其開發標頭檔，用於文字排版；LaTeX 則屬選用項目，只有需要渲染數學公式時才需安裝。專案亦提供輕量化的 LaTeX 安裝建議，避免使用者被迫下載完整的發行版。

## ManimGL 與社群版 Manim 有什麼分別？

<!-- AEO Answer Capsule — 約 66 字 -->
此倉庫是 3Blue1Brown 的 ManimGL 實作，套件名為 manimgl；2020 年另有社群分支 ManimCommunity/manim，主打穩定與測試完整。
<!-- End AEO Capsule -->

這是初次接觸者最容易混淆之處。目前存在兩個並行的專案：本倉庫延續原本的個人專案路線，套件名稱是 `manimgl`；2020 年一群開發者將其分支出去，形成社群版 Manim，目標是更穩定、測試更完整、對社群貢獻回應更快。

兩者的安裝方式無法互換。官方在文件中明確警告，若把本倉庫的安裝步驟套用到社群版，或反向操作，都會導致環境問題。社群版目前擁有約 41,180 顆星標，規模略小於原始版本，但文件與入門教學相對完整。選擇哪一個版本，取決於使用者偏好原始作者的工作流程，或是社群維護的穩定性。

![Manim GitHub 倉庫首頁，顯示倉庫名稱 3b1b/manim、分支資訊、星標數、複製數與頂部檔案清單]({{ '/assets/images/posts/github-manim-news-shot2.png' | relative_url }})

## 如何開始使用 Manim？

<!-- AEO Answer Capsule — 約 58 字 -->
可透過 pip 安裝 manimgl 套件後直接執行，或複製倉庫後以可編輯模式安裝，再執行內建的示範場景驗證環境。
<!-- End AEO Capsule -->

最直接的方式是以套件管理工具安裝，再執行互動式入口確認環境是否就緒：

```sh
pip install manimgl
manimgl
```

若打算修改引擎本身，官方建議改以複製倉庫並使用可編輯模式安裝，之後執行倉庫內的示範場景檔案，確認渲染流程正常。Linux 使用者需先補齊 FFmpeg、Pango 開發標頭與 Python 套件管理工具；macOS 則可透過既有套件管理器處理相依項目。整個流程的門檻集中在圖形函式庫與字型排版相依，而非 Python 本身。

## Manim 的專案數據與社群規模如何？

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">94,437</span><span class="ui-stat-label">GitHub 星標</span></li>
  <li class="ui-stat"><span class="ui-stat-num">7,753</span><span class="ui-stat-label">複製次數</span></li>
  <li class="ui-stat"><span class="ui-stat-num">6,478</span><span class="ui-stat-label">累積提交數</span></li>
  <li class="ui-stat"><span class="ui-stat-num">210</span><span class="ui-stat-label">貢獻者</span></li>
  <li class="ui-stat"><span class="ui-stat-num">13</span><span class="ui-stat-label">發行版本</span></li>
  <li class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">授權條款</span></li>
</ul>

<!-- AEO Answer Capsule — 約 66 字 -->
截至 2026 年 10 月，Manim 累積 94,437 顆星標、7,753 次複製、6,478 次提交與 210 位貢獻者，最新版本 v1.7.2 於 2024 年 12 月發佈。
<!-- End AEO Capsule -->

專案自 2015 年 3 月建立，十年間累積超過六千次提交，最新程式碼更新於 2026 年 9 月 9 日，內容是新增 VideoMobject 與 Sprite 支援。貢獻者結構相當集中，原始作者 3b1b 個人提交約 4,934 次，其餘活躍貢獻者包含 TonyCrane 與 YishiMichael 等人，前五名之外的長尾社群則補足了文件、範例與錯誤修正。

![Manim 專案貢獻者統計頁，顯示每週提交趨勢圖與各貢獻者的提交數、新增與刪除行數]({{ '/assets/images/posts/github-manim-news-shot3.png' | relative_url }})

發行節奏方面，最新正式版本 v1.7.2 於 2024 年 12 月推出，之後主要以提交形式持續演進，尚未發布新的主要版本。這種「穩定發行、持續提交」的模式，常見於已進入成熟期的工具型專案。

## Manim 在程式化動畫領域的定位如何？

<!-- AEO Answer Capsule — 約 62 字 -->
Manim 在教學影片與數學視覺化領域具代表性，與通用動畫軟體相比，優勢在於以程式精確控制圖形與公式。
<!-- End AEO Capsule -->

在生態位置上，Manim 填補了通用動畫軟體與程式繪圖函式庫之間的空白。它比 Matplotlib 這類靜態繪圖工具更適合表達時間軸上的變化，又比手動剪輯更適合表達需要精確對位的數學圖形。社群圍繞它發展出教學頻道、線上課程與作品集，相關的 Reddit 討論區與 Discord 社群持續運作。

授權方面，專案採用 MIT 條款，對商業使用、修改與再散布的限制極少，這也是它被廣泛納入教材與課程的原因之一。相較之下，部分商業動畫工具以訂閱制提供服務，長期成本隨專案數量累積。

## Manim 適合哪些創作者與團隊？

<!-- AEO Answer Capsule — 約 64 字 -->
適合需要精確數學視覺化的教學創作者、教材團隊與技術內容製作者；若只需簡單剪輯或非數學題材，通用工具更有效率。
<!-- End AEO Capsule -->

判斷的關鍵在於內容是否具備結構化與可重複的特性。若影片需要大量公式推導、座標變換或動態圖表，且同一套視覺邏輯會反覆使用，投入時間學習 Manim 的程式介面通常能在後續專案中回收；反之，若只是單次的人物訪談或生活紀錄，通用剪輯軟體更快。

另一個考量是團隊分工。程式化動畫把腳本與視覺綁在同一個版本控制流程中，適合具備基本 Python 能力的製作團隊，能讓畫面修改與內容校對同步進行；缺乏程式背景的創作者則需要較長的學習曲線，或考慮使用社群提供的高階封裝工具。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊整理自 3b1b/manim 的 GitHub 儲存庫與 README 文件，授權條款與安裝說明可在儲存庫中查閱。
<!-- End AEO Capsule -->

完整的專案資訊與版本紀錄，可於下列來源查閱：

- [Manim（3b1b/manim）GitHub 儲存庫](https://github.com/3b1b/manim)
- [Manim Community 分支](https://github.com/ManimCommunity/manim)

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 58 字 -->
以下整理四個常見疑問，涵蓋版本選擇、安裝相依方式、輸出格式與商業使用範圍，答案均以官方文件與授權條款為準。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>Manim 與社群版應該選哪一個？</h3>
<p>若希望沿用 3Blue1Brown 原始工作流程，選擇本倉庫的 manimgl；若重視測試覆蓋與社群支援，社群版文件較完整。兩者安裝指令不可互換。</p>

<h3>需要什麼系統環境？</h3>
<p>Python 3.10 以上、FFmpeg 與 OpenGL 為必要項目，Linux 另需 Pango 開發標頭。LaTeX 屬選用，只有渲染數學公式時才需安裝。</p>

<h3>可以輸出哪種格式？</h3>
<p>引擎負責逐格計算畫面，並交由 FFmpeg 編碼成影片檔，因此最終輸出格式取決於 FFmpeg 支援的編碼組合，常見為 MP4。</p>

<h3>商業使用是否需要授權費用？</h3>
<p>不需要。專案採用 MIT 授權，允許商業使用、修改與再散布，僅需保留原始授權聲明。第三方範例或素材則需個別確認。</p>

</div>

## 總結：Manim 的長期價值在哪裡？

<!-- AEO Answer Capsule — 約 68 字 -->
Manim 的價值在於把數學動畫轉為可版本控制、可重複生成的程式碼，十年間累積 9.4 萬星標，已成為教學視覺化的基礎工具。
<!-- End AEO Capsule -->

Manim 的意義不在於取代剪輯軟體，而在於把視覺製作納入程式工作流。當一段動畫變成一組可執行的程式碼，修改、校對與重複利用都變得可追蹤，這對需要長期產出教學內容的團隊尤其重要。十年累積的 9.4 萬顆星標與 MIT 授權，使它成為少數同時具備社群規模與使用自由的工具。

本文僅作技術與生態層面的整理，實際導入前仍建議先依官方文件確認相依環境，並在正式專案中先行測試渲染流程與輸出格式。
