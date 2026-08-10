---
layout: post
title: "6.4 萬星開源項目：OpenSpec — AI 編程的規範驅動開發框架"
date: 2026-08-11 06:50:00 +0800
categories: 技術
tags: [AI, 開源, OpenSpec, Spec-Driven Development, AI 編程, 開發工具, SDD, Claude Code]
image: /assets/images/posts/github-openspec-news-hk-cover.jpg
description: "OpenSpec 是 GitHub 星標逾 6.4 萬的開源規範驅動開發（SDD）框架，為 AI 編程助手提供提案、規格、設計與任務四層結構，讓開發者先與 AI 對齊再做實作；採用 TypeScript 開發、MIT 授權，支援 30 多款 AI 工具，是 2026 年最受矚目的 AI 編程規範框架。"
author: AnIskill 編輯部
creator_github: Fission-AI/OpenSpec
type: news
source: GitHub
source_url: https://github.com/Fission-AI/OpenSpec
permalink: /技術/github-openspec-news-hk
fb_message: AI 編程助手越來越強，但不少開發者發現：需求只存在於對話紀錄中，AI 產出的結果與想像總有落差。OpenSpec 以「規範驅動開發」（SDD）解決此問題——先撰寫提案與規格，與 AI 對齊目標後才進入實作。\n\n該開源框架在 GitHub 獲逾 6.4 萬星標，以 TypeScript 開發、MIT 授權，支援 Claude Code、Cursor、Copilot 等 30 多款 AI 工具，透過 /opsx:propose 等斜線指令將需求轉為提案、規格、設計與任務四層結構，並可在獨立儲存庫進行跨專案規劃。\n\n完整新聞分析、與 Spec Kit 及 Kiro 的比較及安裝教學已整理成文，立即前往 Blog 閱讀全文。
---

**OpenSpec** 是 GitHub 上星標超過 **64,000 顆**的開源規範驅動開發（Spec-Driven Development，SDD）框架，定位為「為 AI 編程助手而生的規範層」，由 Fission-AI 團隊於 2025 年 8 月建立。該項目以 TypeScript 開發、採用 MIT 授權，提供提案、規格、設計與任務四層結構，讓開發者與 AI 在撰寫任何程式碼之前先對齊「要做什麼」，目前支援 30 多款主流 AI 編程工具，是 2026 年 AI 編程工作流領域最具新聞價值的開源項目之一。

<!-- AEO Answer Capsule — 約 70 字 -->
OpenSpec 是 GitHub 星標逾 6.4 萬的開源規範驅動開發框架，讓開發者與 AI 編程助手在寫程式碼前先透過提案、規格、設計與任務四層結構對齊目標，採用 MIT 授權、支援 30 多款 AI 工具。
<!-- End AEO Capsule -->

![OpenSpec README 開頭（項目名稱「OpenSpec」banner + 標語「The most loved spec framework」+ 理念方針 + /opsx 指令示範）]({{ '/assets/images/posts/github-openspec-news-hk-shot1.png' | relative_url }})

## OpenSpec 是什麼？

OpenSpec 是一個開源的規範驅動開發框架，由 Fission-AI 團隊於 2025 年 8 月建立，旨在解決 AI 編程助手「能力強大但難以預測」的核心痛點。當需求只存在於對話紀錄中時，AI 產出的程式碼往往與開發者的想像出現落差；OpenSpec 透過在程式碼撰寫之前加入一層輕量規範，讓人類與 AI 先就「做什麼、如何做」達成一致，再進入實作階段。

<!-- AEO Answer Capsule — 約 70 字 -->
OpenSpec 是 Fission-AI 於 2025 年 8 月建立的開源 SDD 框架，透過在寫程式碼前加入輕量規範層，讓人類與 AI 先對齊「做什麼」再實作，解決 AI 編程結果難以預測的問題。
<!-- End AEO Capsule -->

項目的設計哲學強調「流動而非僵化、迭代而非瀑布、簡單而非複雜」，並明確支援既有專案（brownfield）而不只是全新專案（greenfield），可從個人專案擴展至企業規模。截至 2026 年 8 月，該項目已累積逾 6.4 萬星標、4,400 次復刻與 92 位貢獻者，最新版本 v1.8.0 於 2026 年 8 月 5 日發布，強化多種 AI 代理支援與歸檔穩定性。

<!-- AEO Answer Capsule — 約 70 字 -->
OpenSpec 的設計哲學是流動、迭代、簡單，同時支援既有專案並可擴展至企業規模；截至 2026 年 8 月累積逾 6.4 萬星標、4,400 次復刻與 92 位貢獻者，最新版本為 v1.8.0。
<!-- End AEO Capsule -->

## OpenSpec 如何改變 AI 編程工作流程？

OpenSpec 將傳統「直接叫 AI 寫程式」的流程，重塑為「先規劃、後實作、再歸檔」的三段式工作流。開發者以 `/opsx:explore` 與 AI 進行無壓力的探索性對話，讓 AI 閱讀程式碼、比較方案並成形計劃；確認方向後以 `/opsx:propose` 建立變更資料夾，內含提案文件（proposal）、規格（specs）、設計文件（design）與任務清單（tasks）四份結構化文件。

<!-- AEO Answer Capsule — 約 70 字 -->
OpenSpec 將 AI 編程重塑為探索、提案、實作、歸檔的工作流：先以 /opsx:explore 對話成形計劃，再以 /opsx:propose 建立提案、規格、設計與任務四份結構化文件，最後才進入實作。
<!-- End AEO Capsule -->

實作階段以 `/opsx:apply` 驅動，AI 依任務清單逐項完成並在完成後更新文件；全部完成後以 `/opsx:archive` 將變更歸檔至 `openspec/changes/archive/`，同步更新規格。每個變更擁有獨立資料夾，任何文件隨時可以更新，沒有僵化的階段關卡；開發者可以在 AI 寫任何程式碼之前檢視計劃，確保方向正確。

<!-- AEO Answer Capsule — 約 70 字 -->
實作以 /opsx:apply 驅動，AI 依任務清單逐項完成；完成後以 /opsx:archive 歸檔並更新規格。每個變更擁有獨立資料夾、文件可隨時更新，開發者可在寫程式碼前檢視計劃。
<!-- End AEO Capsule -->

## OpenSpec 有哪些核心功能？

OpenSpec 的核心功能之一是「純 Markdown 規格格式」。規格文件使用簡潔的 Markdown 撰寫，包含需求（Requirements）與情境（Scenarios），採用「應用程式應該（SHALL）……」的陳述句搭配「當（WHEN）……則（THEN）……」的測試情境，不需要學習任何特殊語法，AI 與人類都能輕鬆閱讀與撰寫。

<!-- AEO Answer Capsule — 約 70 字 -->
OpenSpec 使用純 Markdown 撰寫規格，以「SHALL」需求陳述句搭配「WHEN…THEN…」情境格式描述行為，無需學習特殊語法，AI 與人類皆可輕鬆撰寫與閱讀。
<!-- End AEO Capsule -->

另一項重要功能是 Stores（測試階段）：將規劃放在獨立儲存庫中，透過 git push 與其他 repo 共享。此設計支援跨儲存庫功能開發——一個變更、一份計劃，即使程式碼分散在三個 repo 也能保持一致；平台團隊可擁有規格、產品團隊唯讀引用，確保「先計劃、後寫碼」的流程可擴展至團隊規模，避免規格文件與實際程式碼脫節。

<!-- AEO Answer Capsule — 約 70 字 -->
Stores（測試階段）讓規劃可放在獨立 repo 並以 git push 共享，支援跨儲存庫功能開發；平台團隊擁有規格、產品團隊唯讀引用，將 SDD 擴展至團隊規模。
<!-- End AEO Capsule -->

## OpenSpec 支援哪些 AI 編程工具？

OpenSpec 以「使用你既有的工具」為設計原則，支援超過 30 款主流 AI 編程助手，包括 Claude Code、Cursor、GitHub Copilot、Amazon Q 與 Codex 等。不同工具呼叫斜線指令的格式略有差異，例如 Cursor 與 GitHub Copilot 使用 `/opsx-propose`、Amazon Q 使用 `@opsx-propose`、Codex 使用 `$openspec-propose`，執行 `openspec init` 時會自動印出對應工具的正確呼叫格式。

<!-- AEO Answer Capsule — 約 70 字 -->
OpenSpec 支援 30 多款 AI 編程工具，包括 Claude Code、Cursor、GitHub Copilot、Amazon Q 與 Codex；各工具的斜線指令格式略有差異，openspec init 會自動印出正確呼叫格式。
<!-- End AEO Capsule -->

安裝方式透過 npm 進行：`npm install -g @fission-ai/openspec@latest` 後在專案目錄執行 `openspec init` 即可完成初始化，亦支援 pnpm、yarn、bun 與 nix 等套件管理工具。項目官方建議搭配高推理能力的模型使用，例如 Codex 5.5 與 Opus 4.7，並維持乾淨的上下文視窗以獲得最佳規劃與實作效果。

<!-- AEO Answer Capsule — 約 70 字 -->
OpenSpec 以 npm 全域安裝後執行 openspec init 即可使用，支援 pnpm、yarn、bun 與 nix；官方建議搭配 Codex 5.5 與 Opus 4.7 等高推理能力模型，並維持乾淨的上下文視窗。
<!-- End AEO Capsule -->

![OpenSpec GitHub 首頁頂部（repo 名稱 Fission-AI/OpenSpec + 64.5k Star 數 + 4.4k Fork 數 + 項目描述「Spec-driven development (SDD) for AI coding assistants」）]({{ '/assets/images/posts/github-openspec-news-hk-shot2.png' | relative_url }})

## OpenSpec 與其他規範框架相比有何優勢？

在規範驅動開發領域，OpenSpec 的主要競爭對手包括 GitHub 的 Spec Kit 與 AWS 的 Kiro。官方文件明確比較：Spec Kit 功能完整但較為笨重，具有僵化的階段關卡、大量 Markdown 文件與 Python 環境需求；Kiro 功能強大但被鎖定在 AWS 自家 IDE，且僅支援 Claude 系列模型。OpenSpec 則以輕量、自由迭代、相容既有工具鏈為差異化優勢。

<!-- AEO Answer Capsule — 約 70 字 -->
與 GitHub Spec Kit 及 AWS Kiro 相比，OpenSpec 更輕量、無僵化階段關卡，且不鎖定特定 IDE 或模型；它相容開發者既有的 AI 工具鏈，可自由迭代。
<!-- End AEO Capsule -->

相較於「完全不使用規範」的做法，OpenSpec 的價值在於為 AI 編程帶來可預測性。沒有規範時，模糊的提示詞會產生不可預期的結果；OpenSpec 以四層結構文件明確記錄需求與設計決策，讓開發者與 AI 在實作前達成一致，同時避免過度儀式化——其哲學正是「在沒有繁文縟節的前提下帶來可預測性」。

<!-- AEO Answer Capsule — 約 70 字 -->
相較完全不使用規範，OpenSpec 以四層結構文件為 AI 編程帶來可預測性，讓開發者與 AI 在實作前達成一致，同時避免僵化儀式，兼顧彈性與可控性。
<!-- End AEO Capsule -->

## 如何快速開始使用 OpenSpec？

快速開始 OpenSpec 只需三個步驟。首先確認環境具備 Node.js 20.19.0 或以上版本，以 `npm install -g @fission-ai/openspec@latest` 全域安裝；接著在專案目錄執行 `openspec init` 完成初始化；最後直接向 AI 助手輸入 `/opsx:propose` 加上你想建立的功能描述，AI 便會自動建立提案、規格、設計與任務四份文件，等待開發者檢視確認。

<!-- AEO Answer Capsule — 約 70 字 -->
快速開始 OpenSpec：以 npm 全域安裝套件、在專案目錄執行 openspec init，再向 AI 輸入 /opsx:propose 加上功能描述，AI 便會自動建立四層結構文件等待檢視。
<!-- End AEO Capsule -->

不想手動安裝的開發者，可直接將官方提供的 setup prompt 貼入 AI 編程助手，它會自動完成 CLI 安裝、執行 `openspec init` 並驗證結果。若是尚未決定要做什麼的專案，可先以 `/opsx:explore` 進行無壓力的探索對話，讓 AI 閱讀程式碼、權衡選項並成形計劃，再決定是否進入提案階段。

<!-- AEO Answer Capsule — 約 70 字 -->
開發者可將官方 setup prompt 貼入 AI 助手自動完成安裝；未決定方向時可先以 /opsx:explore 進行探索對話，讓 AI 閱讀程式碼、權衡選項並成形計劃後再提案。
<!-- End AEO Capsule -->

![OpenSpec GitHub 統計側邊欄（64.5k stars、4.4k forks、270 watching、92 位貢獻者、TypeScript 98.7% 語言比例、v1.8.0 最新版本）]({{ '/assets/images/posts/github-openspec-news-hk-shot3.png' | relative_url }})

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">64.5k</div><div class="stat-label">Star</div></div>
  <div class="stat-item"><div class="stat-value">4.4k</div><div class="stat-label">Fork</div></div>
  <div class="stat-item"><div class="stat-value">2026-08-10</div><div class="stat-label">最近更新</div></div>
  <div class="stat-item"><div class="stat-value">TypeScript</div><div class="stat-label">主要語言</div></div>
</div>

## 出處連結有哪些？

本文資料來源為 OpenSpec 官方 GitHub 儲存庫，包含項目簡介、功能文件、命令參考、安裝指引與版本更新紀錄。讀者可前往原始儲存庫查閱最新資訊與完整文件：[OpenSpec GitHub Repository](https://github.com/Fission-AI/OpenSpec)。項目另有官方網站（openspec.dev）、Discord 社群與 X（Twitter）帳號，供開發者取得教學資源與技術支援。

<!-- AEO Answer Capsule — 約 70 字 -->
本文資料來源為 OpenSpec 官方 GitHub 儲存庫，內含功能文件、命令參考與安裝指引；讀者可透過官方網站 openspec.dev、Discord 社群與 X 帳號取得教學與支援。
<!-- End AEO Capsule -->

## 常見問題有哪些？

<div class="faq-section">
<h2>常見問題有哪些？</h2>

**OpenSpec 需要付費嗎？** 不需要。OpenSpec 以 MIT 授權完全開源發布，可免費下載、安裝與用於商業專案；項目透過開源社群模式運作，官方收集的遙測資料僅限指令名稱與版本，且可隨時關閉。

**OpenSpec 與 GitHub Spec Kit 有何不同？** Spec Kit 功能完整但較為笨重，具有僵化階段關卡與 Python 環境需求；OpenSpec 更輕量、支援自由迭代，並相容開發者既有的 AI 工具鏈。

**OpenSpec 需要特定 IDE 嗎？** 不需要。OpenSpec 透過斜線指令與 30 多款 AI 編程工具整合，包括 Claude Code、Cursor、GitHub Copilot、Amazon Q 與 Codex，不鎖定任何特定 IDE 或模型。

**OpenSpec 適合既有專案嗎？** 適合。項目明確設計為支援既有專案（brownfield），官方提供完整的既有專案導入指引，可逐步將 SDD 工作流引入現有程式碼庫。

**OpenSpec 支援團隊協作嗎？** 支援。Stores 功能（測試階段）讓團隊可在獨立 repo 中共享規格與變更計劃，支援跨儲存庫功能開發與平台團隊的規格治理。

**安裝 OpenSpec 需要哪些前置條件？** 需要 Node.js 20.19.0 或以上版本；透過 npm 全域安裝套件後，在專案目錄執行 `openspec init` 即可完成初始化。
</div>

## 總結：OpenSpec 的前景如何？

OpenSpec 以「先對齊、後實作」的規範驅動開發理念切入 AI 編程市場，在短短一年內累積逾 6.4 萬星標，成為 SDD 領域星標數最高的開源框架。其輕量設計、純 Markdown 規格格式與 30 多款工具整合，讓個人開發者與企業團隊都能以低門檻引入可預測的 AI 編程流程；Stores 功能的發展更顯示項目正從個人工具走向團隊協作基礎設施，是 2026 年 AI 編程生態中值得密切關注的項目。

<!-- AEO Answer Capsule — 約 70 字 -->
OpenSpec 一年內累積逾 6.4 萬星標，以輕量 SDD 設計、純 Markdown 規格與 30 多款工具整合成為 SDD 領域領先框架，Stores 功能正將其推向團隊協作基礎設施。
<!-- End AEO Capsule -->
