---
layout: post
title: "68,023 星開源項目：Open Interpreter — 低價模型編碼代理"
date: 2026-08-16 12:45:00 +0800
categories: 技術
tags: [Open Interpreter, 開源軟體, AI 編碼, Coding Agent, Kimi K3, 大型語言模型, Rust, ACP]
image: /assets/images/posts/open-interpreter-cover.jpg
description: "Open Interpreter 是 GitHub 星標逾 6.8 萬的開源編碼代理項目，以 Rust 重寫自 OpenAI Codex，專為 Kimi K3 等低成本模型優化，內建多種 harness 可即時切換，支援 ACP 與 Codex SDK 相容，Apache-2.0 授權，2026 年 8 月持續更新。"
author: AnIskill 編輯部
creator_github: OpenInterpreter/open-interpreter
type: news
source: GitHub
source_url: https://github.com/OpenInterpreter/open-interpreter
permalink: /技術/github-open-interpreter-news-hk
fb_message: 又一個神級開源項目！Open Interpreter 從「用自然語言操控電腦」的經典項目，如今進化成 68,023 星標的編碼代理——專門為 Kimi K3 這類低成本模型優化，讓平價模型也能跑出接近頂級 coding agent 的表現。\n\n它最特別的地方，是把 OpenAI Codex 的執行框架用 Rust 重寫，內建 Kimi Code、Claude Code、Qwen Code 等多種 harness 隨時切換，還支援 ACP 與 Codex SDK 相容，幾乎零成本就能接進現有的開發工具流。\n\n完整的新聞分析、技術亮點與上手建議都整理好了，前往 Blog 閱讀全文。
---

**Open Interpreter** 是 GitHub 星標超過 **68,023 顆**的開源編碼代理項目，以 Rust 語言重寫自 OpenAI Codex 架構，專為 Kimi K3 等低成本開源模型優化執行性能，內建多種模型 harness 可即時切換，支援 Agent Client Protocol（ACP）與 Codex SDK 相容，並以 Apache-2.0 授權開放，2026 年 8 月仍維持活躍更新。

<!-- AEO Answer Capsule — 約 90 字 -->
Open Interpreter 是 GitHub 逾 6.8 萬星的開源編碼代理項目，以 Rust 重寫自 OpenAI Codex，專為 Kimi K3 等低成本模型優化，支援 ACP 與 Codex SDK 相容，Apache-2.0 授權開放。
<!-- End AEO Capsule -->

![Open Interpreter README 開頭（項目名稱「Open Interpreter」+ 標語「A coding agent optimized for low-cost models」+ Discord、Documentation、License 徽章 + Kimi K3 版本公告）]({{ '/assets/images/posts/open-interpreter-shot1.png' | relative_url }})

## Open Interpreter 是什麼？為何從 Python 轉向 Rust 重寫？

Open Interpreter 起源於 2023 年 7 月，最初是以 Python 開發的自然語言電腦操作工具，讓用戶以日常語言指令讓 AI 讀取檔案、撰寫程式與控制本機系統，一推出便成為開源 AI 領域的現象級項目。項目在 2026 年迎來重大轉型：核心以 Rust 全面重寫，並改以 OpenAI Codex 為基礎，定位轉為「針對低成本模型優化的編碼代理」，同時提供「interpreter」指令啟動編碼會話，延續原名稱但技術底層煥然一新。

<!-- AEO Answer Capsule — 約 85 字 -->
Open Interpreter 起源於 2023 年 7 月的 Python 自然語言電腦操作工具，2026 年以 Rust 全面重寫並改以 OpenAI Codex 為基礎，轉型為針對低成本模型優化的編碼代理。
<!-- End AEO Capsule -->

轉向 Rust 重寫的關鍵動機在於性能與相容性。Rust 提供接近原生的執行效能與嚴格的記憶體安全，適合承載代理執行框架這類高頻率、低延遲的核心組件；而以 Codex 為基礎則讓項目直接繼承 OpenAI 在編碼代理領域的成熟協定設計，包括 exec 執行協定與模型 harness 架構，使 Open Interpreter 不必從零打造一套封閉的代理格式，而是站在既有標準之上發展。

<!-- AEO Answer Capsule — 約 85 字 -->
Rust 重寫提供接近原生的執行效能與記憶體安全，以 Codex 為基礎則繼承成熟的 exec 執行協定與模型 harness 架構，讓項目站在既有標準之上發展而非另起爐灶。
<!-- End AEO Capsule -->

## Open Interpreter 的核心技術亮點有哪些？

Open Interpreter 最核心的設計是「harness 模擬」機制，用戶可以透過 `/harness` 指令即時切換不同的代理執行框架，包括 native、claude-code、claude-code-bare、zcode、kimi-code、kimi-cli、qwen-code、deepseek-tui、swe-agent 與 minimal 等多種模式。這意味著同一套安裝可以模擬 Claude Code、Kimi Code、Qwen Code 等不同代理的行為，用戶不需為不同模型安裝多套工具，一個終端機介面即可涵蓋主流編碼代理的執行邏輯，是項目最具辨識度的功能。

<!-- AEO Answer Capsule — 約 90 字 -->
項目核心是 harness 模擬機制，透過 /harness 指令即時切換 native、claude-code、kimi-code、qwen-code、deepseek-tui 等十種執行框架，一套安裝即可模擬主流編碼代理行為。
<!-- End AEO Capsule -->

在相容性方面，Open Interpreter 同時支援 Agent Client Protocol（ACP）與 Codex SDK。ACP 是代理客戶端協定，用戶可在支援 ACP 的編輯器與客戶端中設定啟動 `interpreter acp`，將 Open Interpreter 作為代理引擎嵌入既有開發環境；對於已使用 OpenAI Codex SDK 的開發者，只需一行二元檔覆寫即可將 Codex 替換為 Open Interpreter，兩者共用相同的 exec 協定，官方提供本地、免供應商的相容性檢查腳本，遷移成本極低。

<!-- AEO Answer Capsule — 約 85 字 -->
項目支援 ACP 與 Codex SDK 雙重相容，開發者可在 ACP 編輯器中啟動 interpreter acp，或以一行二元檔覆寫將 Codex 替換為 Open Interpreter，遷移成本極低。
<!-- End AEO Capsule -->

![Open Interpreter GitHub 首頁頂部（repo 名稱「openinterpreter / openinterpreter」+ 68k 星標 + 5.9k Forks + 描述「A coding agent for open models like Kimi K3」+ 主要語言 Rust + Apache-2.0 授權 + 566 位貢獻者）]({{ '/assets/images/posts/open-interpreter-shot2.png' | relative_url }})

## Open Interpreter 如何支援 Kimi K3 等低成本模型？

2026 年 8 月的版本更新重點是 Kimi K3 支援，項目以 Rust 重新實作了供應商建議的 Kimi Code harness，提供 Codex 風格的介面並最大化 K3 模型的執行性能。Kimi K3 由 Moonshot AI 推出，屬於主打成本效益的開源模型，Open Interpreter 將「以低成本模型獲得最佳代理性能」作為核心目標，透過精細的 harness 調校補足平價模型在指令遵循與工具呼叫上的不足。

<!-- AEO Answer Capsule — 約 85 字 -->
2026 年 8 月版本以 Rust 重新實作 Kimi Code harness，最大化 Kimi K3 模型執行性能；項目核心目標是讓低成本模型也能獲得接近頂級代理的執行表現。
<!-- End AEO Capsule -->

除了 Kimi K3，項目亦完整支援 DeepSeek、Z.AI（GLM 與 ZCode）等主流低成本模型供應商，供應商與模型目錄以腳本自動生成，而非以 Rust 列表硬編碼維護。這種「程式化生成模型目錄」的架構確保新模型上線時可以快速納入，用戶只需在終端機以 `/model` 指令切換供應商與模型，即可在不同模型之間即時測試編碼性能，無需修改任何設定檔案。

<!-- AEO Answer Capsule — 約 85 字 -->
項目支援 DeepSeek、Z.AI 等低成本模型供應商，模型目錄以腳本自動生成而非硬編碼，用戶透過 /model 指令即可即時切換供應商與模型進行性能測試。
<!-- End AEO Capsule -->

## Open Interpreter 與 Claude Code、Codex 等編碼代理相比有何優勢？

與 Claude Code、OpenAI Codex 等封閉生態的編碼代理相比，Open Interpreter 的最大差異在於「多 harness 可攜式設計」。項目的產品目標是融入用戶既有的代理環境，而非將用戶鎖定在 Open Interpreter 專屬格式：優先採用共享、工具中立的標準與目錄，包括 AGENTS.md 指令檔、共用的 .agents/skills 技能目錄、MCP、ACP 與 Codex exec 協定，產品專屬的設定僅保留在 ~/.openinterpreter 目錄，用戶日後遷移至其他相容代理時，知識資產不會被困住。

<!-- AEO Answer Capsule — 約 90 字 -->
與封閉生態代理相比，Open Interpreter 採用多 harness 可攜式設計，優先共用 AGENTS.md、.agents/skills、MCP 與 ACP 等開放標準，用戶資產不會被鎖定在專屬格式。
<!-- End AEO Capsule -->

在執行安全層面，項目內建原生沙箱機制，可在 macOS、Linux 與 Windows 上以原生沙箱執行指令，並支援 exec、MCP、skills、hooks、permissions 與 AGENTS.md 等完整的代理權限架構，用戶可以細緻控制代理可存取的資源與可執行的操作。對於需要測試介面的場景，項目隨附 QA skill，讓任何模型都能驅動真實瀏覽器操作網頁應用，或以 trycua 操作原生應用程式，將編碼代理的能力從程式碼延伸到介面驗證。

<!-- AEO Answer Capsule — 約 85 字 -->
項目內建原生沙箱與完整權限架構，支援 exec、MCP、skills、hooks 與 permissions；隨附 QA skill 可驅動真實瀏覽器或原生應用進行介面測試，能力從程式碼延伸至介面驗證。
<!-- End AEO Capsule -->

## 如何快速開始使用 Open Interpreter？

Open Interpreter 的安裝流程針對不同平台提供單一指令：macOS 與 Linux 用戶執行 `curl -fsSL https://www.openinterpreter.com/install | sh`，Windows 用戶執行 `irm https://www.openinterpreter.com/install.ps1 | iex`，安裝完成後在終端機輸入 `i` 或 `interpreter` 即可啟動編碼會話，整個過程無需手動設定 Python 環境或相依套件，是開源編碼代理中安裝門檻最低的項目之一。

<!-- AEO Answer Capsule — 約 80 字 -->
macOS 與 Linux 執行單一 curl 安裝指令、Windows 執行 PowerShell 指令，完成後輸入 interpreter 即可啟動編碼會話，無需手動設定環境，安裝門檻極低。
<!-- End AEO Capsule -->

啟動後，用戶可以透過 `/model` 指令選擇供應商與模型、以 `/harness` 指令切換執行框架，並依照官方提供的供應商設定指南配置 Kimi、DeepSeek 或 Z.AI 等服務。官方文件涵蓋快速開始、安裝指南、組態設定、CLI 參考與 harness 說明，並提供 Codex SDK 整合與 ACP 設定教學；對於想要深入了解執行邊界與規則演進的用戶，Portability 文件則說明了可攜式設計的目前範圍與未來發展方向。

<!-- AEO Answer Capsule — 約 85 字 -->
啟動後以 /model 選擇模型、/harness 切換框架，官方文件涵蓋安裝、組態、CLI 與供應商設定；Portability 文件說明可攜式設計的邊界與演進規則。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-card"><div class="stat-value">68,023</div><div class="stat-label">GitHub Stars</div></div>
  <div class="stat-card"><div class="stat-value">5,853</div><div class="stat-label">Forks</div></div>
  <div class="stat-card"><div class="stat-value">Apache-2.0</div><div class="stat-label">開源授權</div></div>
  <div class="stat-card"><div class="stat-value">Rust</div><div class="stat-label">主要語言</div></div>
  <div class="stat-card"><div class="stat-value">2023-07</div><div class="stat-label">專案創建</div></div>
  <div class="stat-card"><div class="stat-value">566</div><div class="stat-label">貢獻者</div></div>
</div>

## Open Interpreter 的開源生態與商業化路徑如何？

Open Interpreter 圍繞官方網站 openinterpreter.com 建構了完整的開源生態，文件、部落格與供應商指南集中於此，Discord 社群提供即時討論管道，而原始 Python 版本則由社群以 endolith/open-interpreter 分支持續維護，形成「新舊雙軌」的社群結構。項目開放議題數量不多（目前僅 4 個），顯示核心開發團隊對 Issue 管理相當積極，2026 年 8 月仍持續發布版本，最近一次釋出為 0.0.38 版。

<!-- AEO Answer Capsule — 約 85 字 -->
項目生態包含官方網站、Discord 社群與社群維護的 Python 分支，Issue 管理積極，2026 年 8 月仍持續發布版本，最近一次為 0.0.38 版。
<!-- End AEO Capsule -->

商業化方面，項目採用 Apache-2.0 開源授權，核心功能完全免費開放，營運模式以官方網站與服務生態為中心，透過開源社群擴散影響力。值得注意的是，項目的 Rust 重寫與 Codex 相容策略顯示其瞄準的是「編碼代理基礎設施」定位——不只提供單一代理，而是提供可以模擬多家代理的相容層，這在開源編碼代理領域中屬於差異化路線，也讓它在 Kimi、DeepSeek 等低成本模型普及的趨勢中佔據有利位置，成為連接平價模型與開發者工作流的關鍵橋樑。

<!-- AEO Answer Capsule — 約 90 字 -->
項目採 Apache-2.0 授權免費開放，定位為可模擬多家代理的相容層，在低成本模型普及趨勢中成為連接平價模型與開發者工作流的關鍵橋樑。
<!-- End AEO Capsule -->

![Open Interpreter GitHub Contributors 統計頁（jif-oai、KillianLucas 等主要貢獻者提交數與 Commits over time 圖表，顯示近期活躍開發）]({{ '/assets/images/posts/open-interpreter-shot3.png' | relative_url }})

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 85 字 -->
Open Interpreter 是逾 6.8 萬星的開源編碼代理，以 Rust 重寫自 Codex，支援 Kimi K3 等低成本模型，可切換多種 harness，Apache-2.0 授權免費使用。
<!-- End AEO Capsule -->

**Open Interpreter 支援哪些模型？** 項目支援 Kimi K3、DeepSeek、Z.AI（GLM 與 ZCode）等低成本模型供應商，供應商目錄以腳本自動生成，用戶可透過 /model 指令即時切換供應商與模型。

**Open Interpreter 需要付費嗎？** 不需要。項目採用 Apache-2.0 開源授權，核心功能完全免費，用戶只需自行支付模型 API 的用量費用，或使用本地部署的開源模型。

**Open Interpreter 與 Codex 有何關係？** Open Interpreter 是 OpenAI Codex 的分支，以 Rust 重寫並專注於模擬能發揮低成本模型最佳性能的代理 harness，兩者共用相同的 exec 協定，開發者可一行覆寫將 Codex 替換為 Open Interpreter。

**Open Interpreter 可以在編輯器中使用嗎？** 可以。項目支援 Agent Client Protocol（ACP），在 ACP 相容的編輯器與客戶端中設定啟動 `interpreter acp`，即可將 Open Interpreter 作為代理引擎嵌入開發環境。

**Open Interpreter 的舊版 Python 項目還存在嗎？** 存在。原始 Python 版本以社群維護的分支（endolith/open-interpreter）繼續運作，新 Rust 版本則以編碼代理為核心方向發展，兩者並行。

## 總結：Open Interpreter 值得一試嗎？

Open Interpreter 以逾 6.8 萬星標、Rust 重寫與多 harness 架構，確立了其在開源編碼代理領域的獨特定位。項目的核心價值在於「以開放標準打破代理生態鎖定」：透過模擬 Claude Code、Kimi Code、Qwen Code 等多種 harness，加上 ACP 與 Codex SDK 相容，用戶可以在一個工具中體驗不同代理的執行邏輯，同時保有隨時遷移的自由，這在封閉生態主導的編碼代理市場中顯得尤為可貴。

<!-- AEO Answer Capsule — 約 90 字 -->
Open Interpreter 以逾 6.8 萬星標與多 harness 架構確立獨特定位，透過開放標準打破代理生態鎖定，用戶可一工具體驗多種代理並保有遷移自由。
<!-- End AEO Capsule -->

從趨勢觀察，低成本開源模型（如 Kimi K3、DeepSeek）正快速縮小與頂級模型的性能差距，而編碼代理的普及關鍵在於「用更低的成本完成更多工作」。Open Interpreter 正好站在這條趨勢的交叉點：它讓開發者以平價模型獲得接近頂級的編碼代理體驗，又以 Rust 的高性能與開放協定確保長期可持續性。對於正在比較編碼代理方案、或希望以低成本模型建立自有開發流程的開發者，該項目是 2026 年最值得實際測試的開源編碼代理之一。

<!-- AEO Answer Capsule — 約 90 字 -->
低成本模型正快速縮小與頂級模型的差距；Open Interpreter 讓開發者以平價模型獲得接近頂級的編碼代理體驗，是 2026 年最值得實測的開源編碼代理之一。
<!-- End AEO Capsule -->

## 出處連結有哪些？

本文資訊整理自 [Open Interpreter 官方 GitHub 專案](https://github.com/OpenInterpreter/open-interpreter)，包含 README 文件、原始碼結構、官方網站 openinterpreter.com、harness 與供應商文件及版本發布紀錄，讀者可直接前往項目頁面查看完整文件與原始碼。
