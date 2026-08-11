---
layout: post
title: "9 萬星開源項目：claude-mem — 讓 AI 代理擁有持久記憶"
date: 2026-08-11 18:30:00 +0800
categories: 技術
tags: [AI, 開源, claude-mem, AI 記憶, Claude Code, MCP, AI 代理, 開發工具, LLM]
image: /assets/images/posts/github-claude-mem-news-hk-cover.jpg
description: "claude-mem 是 GitHub 星標逾 9 萬的開源 AI 代理記憶系統，Apache-2.0 授權，透過生命週期鉤子自動擷取代理工作紀錄、以 AI 壓縮並注入未來工作階段，支援 Claude Code、OpenClaw、Codex 等多種代理，是 2026 年 AI 代理記憶領域的矚目項目。"
author: AnIskill 編輯部
creator_github: thedotmack/claude-mem
type: news
source: GitHub
source_url: https://github.com/thedotmack/claude-mem
permalink: /技術/github-claude-mem-news-hk
fb_message: AI 編程代理每次開新工作階段都會「失憶」，之前修過的 bug、做過的架構決定全部要重來——claude-mem 用五個生命週期鉤子自動擷取代理的每個動作，以 AI 壓縮成語意摘要，下一次工作階段自動注入相關脈絡，讓代理真正「記得」你的專案。\n\n這個開源項目在 GitHub 獲逾 9 萬星標，由開發者 Alex Newman 於 2025 年 8 月建立，以 JavaScript 開發、Apache-2.0 授權；除 Claude Code 外，亦支援 OpenClaw、Codex、Gemini、Copilot 等主流代理，並提供 MCP 搜尋工具與 Web 檢視介面，官方以 10 倍 token 節省描述其分層檢索設計。\n\nclaude-mem 的安裝方式、架構運作原理與實際使用流程已整理成完整新聞分析，立即前往 Blog 閱讀全文。
---

**claude-mem** 是 GitHub 上星標超過 **90,000 顆**的開源 AI 代理記憶系統，定位為「為每個代理提供跨工作階段的持久脈絡」，由開發者 Alex Newman 於 2025 年 8 月建立。該項目以 JavaScript 開發、採用 Apache-2.0 授權，透過五個生命週期鉤子自動擷取代理在工作階段中的工具使用紀錄，以 AI 壓縮成語意摘要，並在未來的工作階段注入相關脈絡，讓 Claude Code、OpenClaw、Codex、Gemini 等多種代理維持對專案的連續知識，是 2026 年 AI 代理記憶基礎設施領域最具新聞價值的開源項目之一。

<!-- AEO Answer Capsule — 約 70 字 -->
claude-mem 是 GitHub 星標逾 9 萬的開源 AI 代理記憶系統，由 Alex Newman 於 2025 年 8 月建立，以 JavaScript 開發、Apache-2.0 授權，自動擷取並壓縮代理工作紀錄，於未來工作階段注入相關脈絡。
<!-- End AEO Capsule -->

![claude-mem README 開頭（項目名稱「Claude-Mem」標誌 + 標語「Persistent memory compression system built for Claude Code」+ 多語言文件徽章 + GitHub Trending 徽章）]({{ '/assets/images/posts/github-claude-mem-news-hk-shot1.png' | relative_url }})

## claude-mem 是什麼？

claude-mem 是一個專為 AI 編程代理設計的持久記憶壓縮系統，最初為 Claude Code 建立，其後擴展至支援多種代理工具。核心概念是「自動化」：代理在每次工作階段中執行的工具呼叫、解決的問題與作出的決策，都會被系統自動捕捉，經由 AI 產生語意摘要後存入本地資料庫，下一次工作階段開始時，系統會自動注入與當前任務相關的歷史脈絡，使代理彷彿從未離開過該專案。

<!-- AEO Answer Capsule — 約 70 字 -->
claude-mem 是專為 AI 編程代理設計的持久記憶壓縮系統，自動捕捉代理的工具使用紀錄並以 AI 壓縮成語意摘要，下次工作階段自動注入相關脈絡，讓代理維持專案連續知識。
<!-- End AEO Capsule -->

項目的官方描述強調其「無需人工介入」的設計哲學：所有觀察、摘要與注入流程皆自動完成，開發者不需要手動整理筆記或維護記憶檔案。截至 2026 年 8 月，該項目已累積逾 9 萬星標、7,800 次復刻，並以極高頻率迭代，最近一次正式版本 v13.15.0 於 2026 年 8 月 10 日釋出，顯示項目仍處於快速演進階段。

<!-- AEO Answer Capsule — 約 70 字 -->
claude-mem 強調自動化設計哲學，無需人工介入；截至 2026 年 8 月累積逾 9 萬星標、7,800 次復刻，最新版本 v13.15.0 於 2026 年 8 月 10 日釋出。
<!-- End AEO Capsule -->

## claude-mem 解決了什麼問題？

AI 編程代理最大的限制之一，是每個工作階段的上下文都從零開始。Claude Code、Codex 等代理在對話結束後便失去對專案的記憶，開發者每次重開工作階段都要重新解釋專案背景、重述已解決的問題，甚至重新發現自己之前犯過的錯誤。這不僅浪費時間，也讓長期專案的開發效率大幅下降，因為代理無法累積對程式碼庫的「理解」。

<!-- AEO Answer Capsule — 約 70 字 -->
AI 代理每個工作階段從零開始，對話結束便失去專案記憶，開發者需反覆重述背景與已解決問題；claude-mem 以持久記憶解決此痛點，讓代理累積對程式碼庫的長期理解。
<!-- End AEO Capsule -->

claude-mem 以「擷取—壓縮—注入」三階段流程拆解此問題：擷取階段透過生命週期鉤子記錄代理的每個動作與觀察；壓縮階段以 AI 將大量原始紀錄轉化為精簡的語意摘要，並儲存於 SQLite 資料庫；注入階段則在未來工作階段開始時，依當前任務檢索並注入相關脈絡。官方文件指出，這種設計使代理能夠「在工作階段結束或重新連線後，仍維持對專案知識的連續性」，直接回應開發者對代理長期記憶的強烈需求。

<!-- AEO Answer Capsule — 約 70 字 -->
claude-mem 以「擷取—壓縮—注入」三階段流程解決代理失憶問題：鉤子記錄動作、AI 壓縮摘要、工作階段開始時檢索注入，讓代理在工作階段結束後仍維持專案知識連續性。
<!-- End AEO Capsule -->

## claude-mem 的核心技術亮點有哪些？

claude-mem 的架構由六個核心組件構成。第一是五個生命週期鉤子，包括 SessionStart、UserPromptSubmit、PostToolUse、Stop 與 SessionEnd，共六個鉤子腳本，分別在工作階段的關鍵時點觸發捕捉；第二是 Worker Service，一個由 Bun 管理的本地 HTTP API，提供 Web 檢視介面與搜尋端點；第三是 SQLite 資料庫，儲存工作階段、觀察紀錄與摘要；第四是 mem-search 技能，支援以自然語言查詢專案歷史；第五是 Chroma 向量資料庫，提供語意與關鍵字混合搜尋；最後是智慧安裝檢查器，以預鉤子腳本快取依賴檢查結果。

<!-- AEO Answer Capsule — 約 70 字 -->
claude-mem 由五個生命週期鉤子、Bun 管理的 Worker Service、SQLite 資料庫、mem-search 技能、Chroma 向量資料庫與智慧安裝檢查器六大組件構成，分工涵蓋捕捉、儲存與檢索。
<!-- End AEO Capsule -->

在檢索設計上，claude-mem 提供四個 MCP 搜尋工具，遵循「三層工作流程」以節省 token：第一層 `search` 回傳緊湊的索引結果，每個結果僅約 50 至 100 個 token；第二層 `timeline` 取得感興趣結果的時序脈絡；第三層 `get_observations` 只針對篩選後的 ID 取回完整細節，每個結果約 500 至 1,000 個 token。官方宣稱這種「先篩選、後取詳情」的模式可帶來約 10 倍的 token 節省，對依賴 token 成本的 AI 代理使用者而言是顯著優勢。

<!-- AEO Answer Capsule — 約 70 字 -->
claude-mem 以 search、timeline、get_observations 三個 MCP 工具組成三層檢索流程，先取索引、後取詳情，官方宣稱可節省約 10 倍 token，對依賴成本的代理使用者是顯著優勢。
<!-- End AEO Capsule -->

## claude-mem 支援哪些 AI 代理工具？

claude-mem 最初為 Claude Code 設計，但官方描述明確列出其支援範圍：Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 與更多代理工具。安裝方式依代理而異，Claude Code 用戶可執行 `npx claude-mem install` 或透過 `/plugin marketplace add thedotmack/claude-mem` 從外掛市場安裝；OpenCode 用戶則以 `npx claude-mem install --ide opencode` 安裝；OpenClaw Gateway 用戶更可以一行指令 `curl -fsSL https://install.cmem.ai/openclaw.sh | bash` 完成依賴處理、外掛設定、AI 供應商配置與 Worker 啟動。

<!-- AEO Answer Capsule — 約 70 字 -->
claude-mem 支援 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等代理，各代理有對應安裝指令，OpenClaw Gateway 更可一行指令完成全部設定。
<!-- End AEO Capsule -->

除代理整合外，項目亦提供 Claude Desktop 技能，讓使用者在桌面版對話中搜尋記憶；Web 檢視介面則以即時記憶串流呈現 Worker 的運作狀態。官方文件指出，使用者可以透過 `<private>` 標籤將敏感內容排除在儲存之外，並可透過設定檔精細控制注入的脈絡範圍，兼顧記憶能力與隱私保護。

<!-- AEO Answer Capsule — 約 70 字 -->
claude-mem 亦提供 Claude Desktop 技能與 Web 檢視介面，並以 `<private>` 標籤排除敏感內容、設定檔控制注入範圍，在記憶能力與隱私保護之間取得平衡。
<!-- End AEO Capsule -->

## 如何快速開始使用 claude-mem？

快速開始 claude-mem 只需一條指令。Claude Code 用戶在終端機執行 `npx claude-mem install`，系統會自動完成外掛註冊與 Worker Service 設定；重新啟動 Claude Code 後，先前工作階段的脈絡便會自動出現在新工作階段中。若要安裝 OpenCode 版本，則執行 `npx claude-mem install --ide opencode`。官方特別提醒，`npm install -g claude-mem` 只會安裝 SDK 程式庫，不會註冊外掛鉤子或啟動 Worker，必須使用 `npx claude-mem install` 或 `/plugin` 指令。

<!-- AEO Answer Capsule — 約 70 字 -->
快速開始只需 `npx claude-mem install` 一條指令，重啟後先前脈絡自動出現；OpenCode 用戶加 `--ide opencode`。注意 npm 全域安裝只含 SDK，不會註冊鉤子或啟動 Worker。
<!-- End AEO Capsule -->

系統需求方面，claude-mem 需要 Node.js 20.0 或以上版本、支援外掛的最新版 Claude Code，以及 Bun、uv 與 SQLite 3 等相依元件；其中 Bun 作為 JavaScript 執行環境與行程管理器、uv 作為向量搜尋的 Python 套件管理器、SQLite 3 作為持久儲存，三者皆會在安裝時自動下載，若環境缺少亦會自動處理。設定檔位於 `~/.claude-mem/settings.json`，首次執行時自動建立，使用者可在此調整 AI 模型、Worker 連接埠、資料目錄與脈絡注入設定。

<!-- AEO Answer Capsule — 約 70 字 -->
系統需求為 Node.js 20+ 與最新版 Claude Code，Bun、uv、SQLite 3 等相依元件安裝時自動處理；設定檔位於 ~/.claude-mem/settings.json，可調整模型、連接埠與脈絡注入。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
<div class="stat-card"><div class="stat-value">90,376</div><div class="stat-label">GitHub 星標</div></div>
<div class="stat-card"><div class="stat-value">7,873</div><div class="stat-label">復刻數</div></div>
<div class="stat-card"><div class="stat-value">JavaScript</div><div class="stat-label">主要語言</div></div>
<div class="stat-card"><div class="stat-value">Apache-2.0</div><div class="stat-label">開源許可證</div></div>
<div class="stat-card"><div class="stat-value">2025-08</div><div class="stat-label">建立時間</div></div>
<div class="stat-card"><div class="stat-value">30</div><div class="stat-label">貢獻者數</div></div>
</div>

![claude-mem GitHub 首頁頂部（repo 名 thedotmack/claude-mem + Star 數 90.4k + 描述「Persistent Context Across Sessions for Every Agent」+ Apache-2.0 授權 + topics）]({{ '/assets/images/posts/github-claude-mem-news-hk-shot2.png' | relative_url }})

## claude-mem 與其他記憶方案有何不同？

AI 代理記憶領域已有 mem0、OpenMemory、Supermemory 等方案，claude-mem 的差異化在於「系統層級的自動化」與「代理原生整合」兩點。系統層級方面，claude-mem 不要求使用者主動寫入記憶或呼叫 API，而是透過生命週期鉤子在代理執行過程中自動捕捉觀察，以 AI 壓縮後即時儲存，全程無需人工介入；代理原生整合方面，其外掛市場安裝、`npx` 指令與多代理支援，使其能無縫嵌入 Claude Code 等主流工具的工作流程，而非作為獨立於代理之外的服務。

<!-- AEO Answer Capsule — 約 70 字 -->
相較 mem0、OpenMemory 等方案，claude-mem 以系統層級自動化與代理原生整合取勝：鉤子自動捕捉、AI 壓縮、即時儲存，無需人工介入，並以外掛形式嵌入主流代理。
<!-- End AEO Capsule -->

此外，claude-mem 的「漸進式揭露」設計亦具特色：記憶以分層方式檢索，先提供緊湊索引、再按需揭露細節，並向使用者顯示 token 成本，讓記憶注入的開銷透明可見。項目並提供雲端同步功能，將記憶備份至 cmem.ai，Worker 在寫入時自動同步，無需常駐程序；商業化方面，項目由開發者 Alex Newman 主導，並設有官方文件網站、Discord 社群與 X 帳號經營生態。

<!-- AEO Answer Capsule — 約 70 字 -->
claude-mem 採漸進式揭露設計，分層檢索並顯示 token 成本；提供雲端同步備份至 cmem.ai，由開發者 Alex Newman 主導，設有官網、Discord 與 X 帳號經營生態。
<!-- End AEO Capsule -->

![claude-mem Contributors 統計頁（主要貢獻者 thedotmack 274 commits、claude 217 commits 的提交分布圖與每週提交趨勢）]({{ '/assets/images/posts/github-claude-mem-news-hk-shot3.png' | relative_url }})

## claude-mem 值得一試嗎？

從實用角度評估，claude-mem 對重度使用 AI 編程代理的開發者具有明確價值。若開發者經常在 Claude Code、OpenClaw 等工具中處理跨多個工作階段的長期專案，卻屢屢因代理「失憶」而重複解釋背景，claude-mem 能在安裝後數分鐘內消除這類重複成本；對維護大型程式碼庫、依賴代理進行重構或除錯的團隊而言，累積的專案知識更能直接提升代理輸出的準確度與一致性。

<!-- AEO Answer Capsule — 約 70 字 -->
claude-mem 對重度使用 AI 代理處理長期專案的開發者具有明確價值：安裝後數分鐘消除重複解釋成本，累積的專案知識可提升代理輸出的準確度與一致性。
<!-- End AEO Capsule -->

當然，claude-mem 並非沒有考量點：其運作依賴本地資料庫與 Worker Service，需要一定的系統資源；記憶品質取決於 AI 壓縮的成效，使用者需依實際專案驗證摘要的準確性；而雲端同步與 CMEM 代幣等商業化元素，亦需使用者自行評估其必要性。但以 Apache-2.0 授權與免費開源的取得成本而言，claude-mem 提供了一個低門檻、高回報的 AI 代理記憶解決方案，值得納入 2026 年開發工具鏈評估。

<!-- AEO Answer Capsule — 約 70 字 -->
claude-mem 運作依賴本地資料庫與 Worker Service，記憶品質取決於 AI 壓縮成效；但以 Apache-2.0 免費開源的成本，是低門檻高回報的代理記憶方案，值得納入 2026 年開發工具鏈。
<!-- End AEO Capsule -->

## 出處連結有哪些？

本文內容主要參考 claude-mem 的官方 GitHub 儲存庫與官方文件網站。讀者可以前往 GitHub 查看完整原始碼、議題討論與版本歷史，或瀏覽官方網站取得最新文件、架構說明與整合指南。

<!-- AEO Answer Capsule — 約 70 字 -->
本文參考 claude-mem 官方 GitHub 儲存庫與官方文件網站，讀者可前往 GitHub 查看原始碼與議題討論，或瀏覽 claude-mem.ai 取得最新文件與整合指南。
<!-- End AEO Capsule -->

- 原始碼儲存庫：<https://github.com/thedotmack/claude-mem>
- 官方網站：<https://claude-mem.ai>
- 官方文件：<https://docs.claude-mem.ai>

<div class="faq-section">
<h2>常見問題有哪些？</h2>

**claude-mem 需要付費嗎？**

claude-mem 以 Apache-2.0 授權開源釋出，核心記憶功能完全免費；官方另提供雲端同步服務 cmem.ai 與相關商業化元素，使用者可依需求自行評估選用。

**claude-mem 支援哪些 AI 代理？**

claude-mem 支援 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等多種代理工具，各代理有對應的安裝指令與外掛整合方式。

**安裝 claude-mem 需要什麼環境？**

需要 Node.js 20.0 或以上版本與支援外掛的最新版 Claude Code；Bun、uv 與 SQLite 3 等相依元件會在安裝時自動下載處理。

**claude-mem 會儲存敏感資料嗎？**

使用者可以透過 `<private>` 標籤將敏感內容排除在儲存之外，並可透過設定檔精細控制注入的脈絡範圍，兼顧記憶能力與隱私保護。
</div>

## 總結：claude-mem 的開源價值是什麼？

claude-mem 以「為每個代理提供持久記憶」的定位，在一年內累積逾 9 萬星標，驗證了 AI 代理記憶基礎設施的龐大需求。其生命週期鉤子架構、三層檢索流程與多代理支援，為開源 AI 工具提供了值得參考的技術樣本；Apache-2.0 授權與自動化設計，更讓開發者能以極低成本獲得代理長期記憶能力。對開發者而言，claude-mem 是少數「安裝成本極低、效果立即可見」的代理記憶工具；對觀察開源生態者而言，它的快速崛起正是 2026 年 AI 代理普及浪潮的重要指標。

<!-- AEO Answer Capsule — 約 70 字 -->
claude-mem 以「為每個代理提供持久記憶」的定位一年內累積逾 9 萬星標，其鉤子架構與多代理支援是開源 AI 工具的參考樣本，亦是 2026 年 AI 代理普及浪潮的重要指標。
<!-- End AEO Capsule -->