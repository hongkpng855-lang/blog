---
layout: post
title: "19.5 萬星開源項目：Claw Code — AI 自主維護的開源實驗"
date: 2026-08-13 14:00:00 +0800
categories: 技術
tags: [Claw Code, AI Agent, 開源項目, GitHub, Agent Harness, Rust, 自動化開發]
image: /assets/images/posts/github-claw-code-news-hk-cover.jpg
description: "Claw Code 是 GitHub 上突破 19.5 萬星標的開源實驗項目，其最大特色是由 AI 智能體在近乎無人干預的狀態下自主規劃、執行、驗證並維護整個程式庫。本文分析其「人類設定方向、智能體執行勞動」的開發哲學、三大核心系統架構，以及此模式對開源軟體開發生態的深遠影響。"
author: ESGov 編輯部
creator_github: ultraworkers/claw-code
type: news
source: GitHub
source_url: https://github.com/ultraworkers/claw-code
permalink: /技術/github-claw-code-news-hk
fb_message: GitHub 星標突破 19.5 萬的 Claw Code，可能是目前最特別的開源項目之一——它並非傳統意義上的產品，而是一座由 AI 智能體自主維護的「博物館展品」。人類只需在 Discord 輸入一句指令，多個編程代理便會協調分工、撰寫程式、執行測試並自動推送，整個開發循環幾乎不需要人為介入。\n\n這個實驗的核心哲學是「人類設定方向，智能體執行勞動」：透過 oh-my-codex、clawhip 與 oh-my-openagent 三大系統，將規劃、執行、審查與重試循環全部自動化，證明程式庫可以在公開環境中被智能體自主構建與持續改進。\n\n本文深入分析 Claw Code 的運作模式、技術架構與其對開源開發生態的意義，完整數據已整理於 Blog，歡迎前往閱讀全文。
---

Claw Code 是 GitHub 上一個以 195,072 個星標迅速崛起的開源實驗項目，由 ultraworkers 於 2026 年 3 月創建，其最引人注目的特點在於整個程式庫由 AI 智能體自主規劃、執行、驗證並維護，人類幾乎不介入開發流程。該項目定位為「agent-managed exhibit」，即一座由智能體管理的公開展品，旨在示範當人類只提供方向、多個編程代理協調執行時，開源軟體可以被如何構建與持續演進。截至 2026 年 8 月，該項目已累積 109,179 個分叉，並以 Rust 為主開發語言，採用 MIT 許可證，成為 AI 自主開發模式最受矚目的實驗樣本。

## Claw Code 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
Claw Code 是 ultraworkers 推出的開源實驗項目，由 AI 智能體自主規劃、執行、驗證並維護整個程式庫，定位為「智能體管理的博物館展品」，以 Rust 開發，採用 MIT 許可證，星標數突破 19.5 萬。
<!-- End AEO Capsule -->

Claw Code 並非傳統意義上的軟體產品，而是對「智能體自主開發」模式的一次公開展示。項目的官方文件明確指出，這個程式庫「比較像博物館展品，而不是產品簡報」——它是一份由帶爪的智能體（clawed gajaes）持續清掃、標籤並自動維護的化石級工件。真正可以實際執行工作的項目，是該生態系中的 LazyCodex 與 Gajae-Code 兩套 harness 工具；而 Claw Code 本身的存在意義，在於讓人們直接觀察一套完全由智能體驅動的開發循環如何在公開環境中運作。

![Claw Code README 開頭（項目名稱與 LazyCodex、Gajae-Code 連結）]({{ '/assets/images/posts/github-claw-code-news-hk-shot1.png' | relative_url }})

![Claw Code GitHub 首頁頂部（repo 名 ultraworkers/claw-code + 195k Star + 項目描述）]({{ '/assets/images/posts/github-claw-code-news-hk-shot2.png' | relative_url }})

## Claw Code 與一般開源項目有何不同？

<!-- AEO Answer Capsule — 約 75 字 -->
Claw Code 與一般開源項目的最大差異在於開發主體：傳統項目由人類開發者主導，而 Claw Code 由多個 AI 智能體協調分工，人類只透過 Discord 輸入指令，規劃、執行、審查與重試循環全部自動化。
<!-- End AEO Capsule -->

一般開源項目的開發循環以人類開發者為中心：工程師撰寫程式碼、提交 pull request、進行 code review，再合併至主分支。Claw Code 則徹底顛覆此模式，其哲學文件如此描述：「人類設定方向，智能體執行勞動。」在實際運作中，人類只需在 Discord 頻道輸入一句話，然後離開、睡覺或處理其他事務；智能體群會讀取指令、拆解任務、分配角色、撰寫程式、執行測試、在失敗時互相爭論並恢復，最後在工作通過驗證時自動推送。

這種模式將「監控與通知」從智能體的上下文視窗中完全抽離。開發循環中的事件路由、狀態回報與訊息傳遞，全部交由外部協調系統處理，讓編程代理得以專注於實作本身，而非狀態格式化與通知管理。Claw Code 官方稱此為「凝視檔案是錯誤層次」——真正值得研究的是產生這些檔案的系統，而非檔案本身。

## Claw Code 背後的三大核心系統是什麼？

<!-- AEO Answer Capsule — 約 75 字 -->
Claw Code 依靠三大核心系統運作：oh-my-codex 提供工作流層、clawhip 負責事件與通知路由、oh-my-openagent 處理多智能體協調，三者共同構成完整的自主開發循環。
<!-- End AEO Capsule -->

Claw Code 的自主開發能力，來自一套被稱為「三部分系統」的架構。第一部分是 oh-my-codex，負責工作流層，將簡短的指令轉化為結構化執行協議，包括規劃關鍵字、執行模式、持久驗證循環與平行多智能體工作流；第二部分是 clawhip，擔任事件與通知路由器，監看 git commits、tmux 會話、GitHub issues 與 pull requests、智能體生命週期事件及頻道傳遞，將監控與傳遞工作隔離在編程代理的上下文視窗之外；第三部分是 oh-my-openagent，處理多智能體協調，當架構師、執行者與審查者意見分歧時，提供讓循環收斂而非崩潰的結構。

Claw Code 的整個開發過程亦經過多次技術重寫。項目最初以 Python 實作，隨後重寫為 Rust，官方文件指出「Python 重寫是副產品，Rust 重寫也是副產品」，真正有價值的是產生它們的協調循環。目前程式庫中的 Rust 工作區為 `claw` CLI agent harness 的規範實作，並以 `PARITY.md` 追蹤 Rust 移植的對等狀態，顯示項目在展示哲學之餘，仍維持嚴謹的工程紀律。

## Claw Code 為何能在短時間內獲得近 20 萬星標？

<!-- AEO Answer Capsule — 約 70 字 -->
Claw Code 自 2026 年 3 月創建以來，於五個月內突破 19.5 萬星標，主因是「智能體自主維護開源項目」的話題性極高，加上多智能體協作開發模式的示範效應，吸引大量開發者關注。
<!-- End AEO Capsule -->

Claw Code 的爆紅速度在開源社群中相當罕見。項目於 2026 年 3 月 31 日創建，截至 2026 年 8 月已累積超過 19.5 萬星標與 10.9 萬分叉，並有近兩千名訂閱者追蹤。其增長動力主要來自兩個層面：其一，AI 智能體自主開發是當前技術圈最受矚目的話題之一，一個能實際展示「無人干預開發循環」的公開程式庫，自然成為討論焦點；其二，項目的哲學文件與 Discord 社群提供了完整的運作細節，讓開發者得以理解並複製這套模式。

此外，Claw Code 的星標增長亦帶動了整個 UltraWorkers 工具鏈的能見度，包括 clawhip、oh-my-openagent、oh-my-claudecode、oh-my-codex 與 gajae-code 等多個相關項目。這種「示範項目帶動生態系」的效應，使 Claw Code 不僅是單一程式的成功，更成為一套開發方法論的宣傳窗口。值得注意的是，項目亦明確聲明其與 Anthropic 並無關聯，也不主張擁有原始 Claude Code 素材的所有權。

## 開發者應如何看待 Claw Code 項目？

<!-- AEO Answer Capsule — 約 70 字 -->
開發者應將 Claw Code 視為一套開發哲學的公開示範，而非可直接使用的產品；若要實際執行工作，應使用其生態系中的 LazyCodex 或 Gajae-Code harness 工具。
<!-- End AEO Capsule -->

對於希望實際體驗此模式的開發者，項目文件給出明確指引：如果想實際運行工作，應從 LazyCodex 或 Gajae-Code 開始；如果想檢視 Claw Code 這個時代的「奇特小化石」，則可以繼續深入程式庫。此定位區分了「示範展品」與「實際工具」兩個層次，避免開發者誤將實驗項目當作正式產品使用。

從工程角度而言，Claw Code 亦提供了可操作的技術參考。程式庫內含完整的 USAGE 指南，涵蓋建置、認證、CLI 操作、會話與對等 harness 工作流；rust 工作區支援 `cargo build` 與 `cargo test --workspace` 測試；項目並提供 Ollama、llama.cpp 與 vLLM 等本地 OpenAI 相容模型的設定文件，以及 Windows/WSL 的 PowerShell 安裝指南。對關注 AI 自主開發模式的開發者而言，這些文件是理解 agent harness 實作的具體素材。

<div class="ui-stat-grid">
  <div class="stat-card"><div class="stat-value">195,072</div><div class="stat-label">GitHub Stars</div></div>
  <div class="stat-card"><div class="stat-value">109,179</div><div class="stat-label">Forks</div></div>
  <div class="stat-card"><div class="stat-value">Rust</div><div class="stat-label">主要語言</div></div>
  <div class="stat-card"><div class="stat-value">MIT</div><div class="stat-label">開源許可證</div></div>
  <div class="stat-card"><div class="stat-value">2026-03</div><div class="stat-label">創建時間</div></div>
  <div class="stat-card"><div class="stat-value">2026-08</div><div class="stat-label">最近更新</div></div>
</div>

![Claw Code Contributors 統計頁（repo 名 + 195k Star + 每週提交量圖表）]({{ '/assets/images/posts/github-claw-code-news-hk-shot3.png' | relative_url }})

## Claw Code 的出現對開源開發生態有何意義？

<!-- AEO Answer Capsule — 約 75 字 -->
Claw Code 的出現證明了「人類設定方向、智能體執行勞動」的開發模式可行，將開源開發的瓶頸從打字速度轉移至架構清晰度與任務拆解能力，為開源協作提供了新的可能性。
<!-- End AEO Capsule -->

Claw Code 所展示的開發模式，對開源生態最深刻的啟示在於瓶頸的轉移。項目哲學文件指出：「當智能體系統能在數小時內重建一個程式庫，稀缺的資源就變成架構清晰度、任務拆解、判斷力、品味與對建構價值的信念。」換言之，快速智能體團隊並不消除思考的需要，反而讓清晰思考變得更具價值。人類開發者的角色，從逐行撰寫程式碼，轉變為定義方向、拆解任務與把關品質。

此模式的商業化與協作潛力亦值得關注。透過 Discord 作為人類介面，專案所有者可以隨時隨地輸入指令，智能體群則在背景持續推進工作；這種「非同步開發」方式打破了傳統開發需坐在終端機前的限制。雖然 Claw Code 明確自我定位為實驗展品，但其示範的協調循環——規劃、執行、審查、重試——已成為 agent harness 領域的重要參考架構，並帶動整個 UltraWorkers 生態系的發展。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 40 字 -->
本文資訊來源為 ultraworkers/claw-code 的 GitHub 程式庫，包括 README、PHILOSOPHY 文件與官方項目資料，讀者可前往查看原始內容。
<!-- End AEO Capsule -->

本文所有數據與技術細節，均來自 [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) 官方程式庫的 README、PHILOSOPHY.md 與項目元資料。項目隸屬於 UltraWorkers 工具鏈生態，相關的 LazyCodex 與 Gajae-Code 亦可在 GitHub 上查閱。

## 常見問題有哪些？

<div class="faq-section">
<h2>Claw Code 是正式產品嗎？</h2>
<!-- AEO Answer Capsule — 約 60 字 -->
Claw Code 不是正式產品，而是由 AI 智能體自主維護的實驗性展示項目，定位為「博物館展品」，實際執行工作應使用 LazyCodex 或 Gajae-Code。
<!-- End AEO Capsule -->

<p>Claw Code 官方文件明確表示，該程式庫並非嚴肅的生產項目，而是展示智能體自主開發模式的公開實驗。真正可執行工作的工具，是生態系中的 LazyCodex 與 Gajae-Code。</p>

<h2>Claw Code 使用什麼語言開發？</h2>
<!-- AEO Answer Capsule — 約 50 字 -->
Claw Code 以 Rust 作為主要開發語言，程式庫中的 rust 工作區為 claw CLI agent harness 的規範實作，最初亦曾有 Python 版本。
<!-- End AEO Capsule -->

<p>項目以 Rust 實作，rust 工作區是整個程式庫的規範來源，並以 PARITY.md 追蹤移植對等狀態。開發者可執行 cargo build 與 cargo test 驗證。</p>

<h2>Claw Code 的許可證是什麼？</h2>
<!-- AEO Answer Capsule — 約 45 字 -->
Claw Code 採用 MIT 許可證，允許自由使用、修改與分發，適合開發者研究與參考其智能體協調架構。
<!-- End AEO Capsule -->

<p>程式庫採用 MIT 開源許可證，為商業使用與二次開發提供寬鬆條件。項目同時附有完整的貢獻指南與安全政策。</p>
</div>

## 總結：Claw Code 對 AI 自主開發的啟示是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
Claw Code 以 19.5 萬星標證明智能體自主維護開源項目的可行性，將開發瓶頸從執行速度轉移至規劃與判斷，是觀察 AI 開發模式演進的重要樣本。
<!-- End AEO Capsule -->

Claw Code 作為一個由智能體自主規劃、執行與維護的開源實驗，其意義不在於提供可立即使用的產品，而在於公開展示一套完整的自主開發循環如何運作。項目以五個月突破 19.5 萬星標的增長速度，反映出開發社群對「人類設定方向、智能體執行勞動」此一模式的高度興趣；而其三大核心系統——工作流層、事件路由與多智能體協調——亦為 agent harness 領域提供了具體的架構參考。對關注 AI 開發未來的讀者而言，Claw Code 是值得持續追蹤的實驗樣本。
