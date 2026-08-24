---
layout: post
title: "6萬星開源項目：Ghostty — Zig 寫的 GPU 加速原生終端模擬器"
date: 2026-08-25 06:00:00 +0800
categories: 技術
tags: [Ghostty, 終端模擬器, Zig, 開源, GPU, 開發工具]
image: assets/images/posts/github-ghostty-news-cover.jpg
description: "Ghostty 是 Mitchell Hashimoto 創建、以 Zig 語言開發的 GPU 加速終端模擬器，GitHub 獲 60,105 顆星標。文章分析其多執行緒架構、Metal/OpenGL 渲染與 libghostty 嵌入式函式庫，並與 Alacritty、iTerm2 等競品比較性能，探討開源終端生態的未來方向。"
author: AnIskill 編輯部
creator_github: ghostty-org/ghostty
type: news
source: GitHub
source_url: https://github.com/ghostty-org/ghostty
permalink: /技術/github-ghostty-news
fb_message: 終端模擬器一直被認為是「夠用就好」的開發工具，但 Ghostty 的出現打破了這個印象。它以 Zig 語言從零打造，把速度、功能與原生介面三者同時做到極致，上線一年已累積逾 6 萬顆星標。\n\nGhostty 採用多執行緒架構與 Metal/OpenGL GPU 渲染，性能與 Alacritty 同級，卻支援 Kitty 圖形協定、分頁分割、設定 GUI 等豐富功能；macOS 版以 SwiftUI 原生打造，Linux 版深度整合 systemd。\n\n開發者 Mitchell Hashimoto 更將核心拆成 libghostty 函式庫，讓任何應用都能嵌入高效終端。想了解 Ghostty 的架構細節與競品比較，完整分析已上線部落格。
---

Ghostty 是 HashiCorp 共同創辦人 Mitchell Hashimoto 發起、以 Zig 語言編寫的跨平台終端模擬器，GitHub 上獲 60,105 顆星標，主打「快速、功能豐富、原生」三項特質並存。此項目自 2024 年底發布 1.0 以來迅速成為開發工具圈的焦點，其多執行緒架構與 GPU 加速渲染被認為重新定義了終端模擬器的性能天花板，同時透過 libghostty 函式庫將終端能力開放給所有應用程式。

![Ghostty README 開頭（項目名稱與標語，顯示 Ghostty 是快速、原生、功能豐富的終端模擬器）]({{ '/assets/images/posts/github-ghostty-news-shot1.png' | relative_url }})

## Ghostty 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
Ghostty 是 Mitchell Hashimoto 開發的開源終端模擬器，以 Zig 語言編寫，GitHub 獲 60,105 顆星標。它同時提供 macOS 與 Linux 原生應用，以及可嵌入第三方專案的 libghostty C/Zig 函式庫，核心賣點是速度、功能與原生體驗三者兼得。
<!-- End AEO Capsule -->

Ghostty 的定位非常明確：傳統終端模擬器往往迫使使用者在「速度、功能、原生介面」三選一，例如 Alacritty 以極致性能見長但功能精簡，iTerm2 功能豐富卻在 macOS 上以 CPU 軟體渲染見稱。Ghostty 的設計目標是同時提供三者，並以 Zig 語言從底層打造，避開 C 語言在記憶體安全與建構複雜度上的包袱。

此項目由 Mitchell Hashimoto 於 2022 年 3 月創建，他此前創立 HashiCorp 並開發 Vagrant、Terraform 等基礎設施工具，在開發者社群具高度聲望。Ghostty 於 2024 年 12 月發布 1.0 穩定版，截至 2026 年 8 月已迭代至 v1.3.1，官方宣稱每日有數百萬使用者與機器運行。

## Ghostty 有哪些核心技術亮點？

<!-- AEO Answer Capsule — 約 75 字 -->
Ghostty 的核心亮點包括：以 Zig 編寫的單一共享核心、每終端獨立的多執行緒架構（讀取、寫入、渲染三執行緒分離）、Linux 使用 OpenGL 與 macOS 使用 Metal 的 GPU 渲染，以及對 Kitty 圖形協定、同步渲染、明暗模式通知等現代控制序列的完整支援。
<!-- End AEO Capsule -->

在終端模擬標準上，Ghostty 團隊完成了全面的 xterm 行為審計，建立一致性測試案例，並支援比多數終端模擬器更現代的控制序列，包括 Kitty 圖形協定、Kitty 影像協定、剪貼簿序列、同步渲染與明暗模式通知。團隊在 README 中表示，Ghostty 是「最符合標準且功能最豐富的終端模擬器之一」，其行為定義優先順序為標準規範、xterm 行為、其他主流終端，確保相容性有跡可循。

性能方面，Ghostty 的架構採用每終端獨立的讀取、寫入與渲染三條執行緒，讀取執行緒內建高度最佳化的終端解析器，利用 CPU 專屬 SIMD 指令加速，渲染則在 Linux 使用 OpenGL、macOS 使用 Metal。官方基準顯示，Ghostty 與 Alacritty 的差距僅在數個百分點內，但兩者都比 Terminal.app 與 iTerm2 快約一百倍，同時 Ghostty 的功能豐富度與原生體驗遠勝 Alacritty。

## Ghostty 的跨平台架構如何做到原生體驗？

<!-- AEO Answer Capsule — 約 70 字 -->
Ghostty 不走「最低共同標準」路線：macOS 版是真正的 SwiftUI 應用，配備選單列、設定 GUI、AppleScript 與捷徑支援，並用 Metal 渲染與 CoreText 字體；Linux 版以 GTK 建構，深度整合 systemd，支援單一實例、永遠開啟與 cgroup 隔離。
<!-- End AEO Capsule -->

此項目刻意拒絕「一次編寫、隨處運行」的妥協，而是以 Zig 撰寫龐大的共享核心，再於各平台補上原生介面。macOS 版是真正的 SwiftUI 應用程式，具備完整的視窗管理、選單列、設定圖形介面，並以 Metal 渲染器搭配 CoreText 字體發現機制，同時支援 AppleScript 與 Apple 捷徑（AppIntents）等系統整合。Linux 版則以 GTK 建構，深度整合 systemd，提供 always-on、單一實例新視窗與 cgroup 隔離等能力。

團隊的目標是讓每個平台的使用者都覺得 Ghostty「為自己的平台而生」，甚至以為它只支援該平台。這種平台優先策略與許多跨平台工具「最低共同標準」的做法形成鮮明對比，也是 Ghostty 在開發者口碑上快速累積的關鍵因素。

## libghostty 函式庫如何擴展終端生態？

<!-- AEO Answer Capsule — 約 70 字 -->
libghostty 是 Ghostty 拆出的跨平台 C/Zig 函式庫，讓第三方應用程式可以嵌入高效終端模擬能力，零依賴、適用於 macOS、Linux、Windows 與 WebAssembly。目前已拆出 libghostty-vt 子函式庫，專注終端序列解析與狀態維護，並有 Ghostling 等完整參考專案。
<!-- End AEO Capsule -->

除獨立終端模擬器外，Ghostty 同時以 libghostty 形式提供嵌入式能力。此函式庫以 C 相容介面開放，任何專案都可以將高效終端嵌入自己的應用程式，而不需要從頭開發終端模擬邏輯。團隊將 libghostty 逐步拆解為更小單元，首先釋出的是專注於終端序列解析與狀態維護的 libghostty-vt，該子函式庫已可用於 Zig 與 C，並相容 macOS、Linux、Windows 與 WebAssembly。

由於終端解析邏輯已在 Ghostty GUI 中長期驗證，libghostty-vt 的功能穩定性極高，API 簽名仍在演進。官方提供 example 目錄展示 C 與 Zig 的整合範例，並有 Ghostling 專案作為完整實作參考，社群亦整理出 awesome-libghostty 資源清單。此舉將終端模擬從「獨立應用」提升為「可組合的基礎元件」，為開發工具與 IDE 整合開啟新路徑。

## Ghostty 與其他終端模擬器相比表現如何？

<!-- AEO Answer Capsule — 約 75 字 -->
基準測試顯示，Ghostty 與 Alacritty 同屬頂級性能梯隊，差距僅數個百分點，但都比 Terminal.app 與 iTerm2 快約一百倍。Ghostty 的功能豐富度與原生體驗明顯勝過 Alacritty，而相較 iTerm2 則以 GPU 渲染與多執行緒架構取得性能優勢。
<!-- End AEO Capsule -->

終端模擬器市場長期由 Alacritty、iTerm2、Kitty、WezTerm 等項目主導。Ghostty 的切入點是同時滿足性能與功能：Alacritty 以 Rust 編寫、GPU 加速聞名，但功能相對精簡；iTerm2 是 macOS 功能最全面的選擇，卻以 CPU 渲染為主；Kitty 以 GPU 渲染與圖形協定見長，但設定採用單一設定檔且跨平台體驗較不原生。Ghostty 以 Zig 語言重寫核心，在性能上與 Alacritty 並駕齊驅，同時提供分割視窗、分頁、設定 GUI 與圖形協定支援，填補了「又快又完整」的市場空缺。

從生態角度看，Ghostty 的出現也帶動了終端標準的進步。團隊完成 xterm 行為全面審計並建立一致性測試，同時積極支援 Kitty 圖形協定等現代序列，這些投入讓終端生態的相容性基準更清晰。官方路線圖顯示，專案已完成標準相容、性能、視窗功能、原生體驗與 libghostty 等五個階段，唯一未完成的是 Ghostty 專屬控制序列，團隊基於避免生態碎片化的考量暫緩推進。

<div class="ui-stat-grid">
  <div class="ui-stat"><span class="stat-label">Star 數</span><span class="stat-value">60,105</span></div>
  <div class="ui-stat"><span class="stat-label">Fork 數</span><span class="stat-value">3,328</span></div>
  <div class="ui-stat"><span class="stat-label">主要語言</span><span class="stat-value">Zig</span></div>
  <div class="ui-stat"><span class="stat-label">授權</span><span class="stat-value">MIT</span></div>
  <div class="ui-stat"><span class="stat-label">創建日期</span><span class="stat-value">2022-03-29</span></div>
  <div class="ui-stat"><span class="stat-label">最新版本</span><span class="stat-value">v1.3.1</span></div>
</div>

![Ghostty GitHub 首頁頂部（repo 名稱、Star 數與描述，顯示 60,105 顆星與快速原生終端模擬器定位）]({{ '/assets/images/posts/github-ghostty-news-shot2.png' | relative_url }})

## Ghostty 的市場與生態影響如何？

<!-- AEO Answer Capsule — 約 70 字 -->
Ghostty 以 60,105 顆星標成為終端模擬器領域星標數最高的開源項目之一，其背後是 HashiCorp 創辦人 Mitchell Hashimoto 的個人影響力與 Zig 語言的技術話題性。libghostty 的開放讓終端能力成為可嵌入元件，預期將帶動 IDE、編輯器與自動化工具整合終端的新一波應用。
<!-- End AEO Capsule -->

Ghostty 的新聞價值不只來自技術，也來自其開發者背景。Mitchell Hashimoto 在基礎設施領域的聲望，使此項目從發布前就備受關注，2024 年底 1.0 發布更成為開發者社群熱議話題。以 Zig 語言撰寫大型 GUI 應用本身即是話題，因為 Zig 仍屬相對年輕的系統程式語言，Ghostty 成為 Zig 生態最具代表性的成功案例之一，也間接推動了社群對 Zig 的採用意願。

商業化路徑方面，Ghostty 以 MIT 授權完全開源，官方未採用捐贈或付費模式，主要透過社群貢獻與 Hashimoto 個人資源維持開發。其影響力更多體現在生態標準與開發者習慣上：多執行緒終端架構、GPU 渲染、嵌入式終端函式庫等概念，正在被更多新興工具吸收，未來整合 Ghostty 核心的應用生態值得持續觀察。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 50 字 -->
本文資訊來源為 Ghostty 官方 GitHub 儲存庫 ghostty-org/ghostty，所有星標數、復刻數、版本與技術細節均擷取自該儲存庫公開資料，未採用第三方轉載來源。
<!-- End AEO Capsule -->

本文資訊來源為 Ghostty 官方 GitHub 儲存庫：[ghostty-org/ghostty](https://github.com/ghostty-org/ghostty)。所有星標數、復刻數、版本資訊與架構描述均擷取自該儲存庫的 README、標籤與提交記錄等公開資料。

## 總結：Ghostty 適合什麼團隊？

<!-- AEO Answer Capsule — 約 70 字 -->
Ghostty 適合追求性能與功能兼得的開發者、Zig 語言學習者，以及需要嵌入式終端能力的工具開發團隊。它以 60,105 顆星標與 v1.3.1 穩定版本證明成熟度，對 macOS 與 Linux 使用者而言是目前終端模擬器的最佳選擇之一。
<!-- End AEO Capsule -->

綜合而言，Ghostty 以 Zig 語言、多執行緒架構與 GPU 渲染重新定義了終端模擬器的性能基準，並以原生介面策略確保每個平台的使用體驗。對追求極致性能的開發者，Ghostty 提供與 Alacritty 同級的速度與更完整的功能；對工具開發者，libghostty 提供可嵌入的終端基礎元件；對 Zig 生態關注者，此項目是語言能力的絕佳示範。

終端模擬器作為開發者每日必用的基礎工具，其演進速度長期緩慢，Ghostty 的出現打破了這種停滯。隨著 libghostty 逐步成熟與生態整合案例增加，此項目的影響力可望從「高效終端」延伸至「終端能力的標準化基礎設施」，後續發展值得持續追蹤。