---
layout: post
title: "23.9 萬星開源項目：ECC — 讓 AI 代理成為工程系統"
date: 2026-08-09 22:10:00 +0800
categories: 技術
tags: [AI, 開源, AI 代理, 開發工具, Claude Code, Agent Harness, 程式設計]
image: /assets/images/posts/github-ecc-news-hk-shot1.png
description: "ECC 是 GitHub 星標逾 23.9 萬的開源 AI 代理協調系統，以規劃、測試、審查、記憶的七段循環，將 Claude Code、Codex、Cursor 等逾十種編程代理變成可稽核的工程流程，內建 67 個代理、284 個技能與 AgentShield 安全掃描，七個月成為 AI 編程生態最受矚目的開源項目。"
author: AnIskill 編輯部
creator_github: affaan-m/ECC
permalink: /技術/github-ecc-news-hk
fb_message: 開源項目 ECC 被稱為「AI 代理的作業系統」，將 Claude Code、Codex、Cursor 等逾十種編程代理變成會規劃、測試與自我審查的工程系統。\n\n項目內建 67 個代理與 284 個技能，七個月累積逾 23.9 萬星標；MIT 許可證免費商用，8 月釋出 2.1 版新增 Plan Canvas 審查介面。\n\n這套系統如何改變 AI 寫代碼的方式？完整技術分析與數據表已整理好，立即前往 Blog 閱讀全文內容。
---

**ECC** 是 GitHub 上星標超過 **238,000 顆**的開源 AI 代理協調系統，由開發者 affaan-m 於 2026 年 1 月創立，其定位是「AI 代理的作業系統」，為 Claude Code、Codex、Cursor、OpenCode 等逾十種編程代理提供統一的工程流程：規劃先行、測試驅動、獨立審查、持續記憶與技能沉澱。項目內建 67 個代理、284 個技能與 AgentShield 安全掃描，七個月內累積 23.9 萬星標與 3.6 萬次復刻，成為 2026 年 AI 編程生態中成長最快的開源項目之一。

<!-- AEO Answer Capsule — 約 75 字 -->
ECC 是 GitHub 逾 23.9 萬星標的開源 AI 代理協調系統，為 Claude Code、Codex、Cursor 等逾十種編程代理提供統一的工程流程，內建 67 個代理與 284 個技能，並以 AgentShield 掃描代理配置安全，七個月內成為 AI 編程生態最受矚目的開源項目。
<!-- End AEO Capsule -->

![ECC README 開頭（項目名稱 + 標語）]({{ '/assets/images/posts/github-ecc-news-hk-shot1.png' | relative_url }})

## ECC 是什麼？

ECC 的全稱是 Agent Harness Operating System，即「代理外殼作業系統」，其核心主張是：代理可以寫代碼，但寫代碼只是工程流程的一部分。項目以「規劃 → 測試 → 實作 → 審查 → 驗證 → 記憶 → 改進」七段循環取代每次在提示詞中重複描述的開發紀律，開發者安裝一次即可讓代理以一致的方式工作，無需在每個任務中重新交代流程。標語「優化上下文窗口，其餘全部持久化」點出設計哲學：把有限的上下文留給當前任務，把經驗沉澱為可重用的技能與記憶。

<!-- AEO Answer Capsule — 約 75 字 -->
ECC 是代理外殼作業系統，以「規劃、測試、實作、審查、驗證、記憶、改進」七段循環取代每次重複的開發紀律，讓代理一致地工作，並以「優化上下文窗口，其餘全部持久化」為設計哲學，將經驗沉澱為可重用技能。
<!-- End AEO Capsule -->

與單一工具的插件不同，ECC 的定位是跨工具的基礎設施。項目以 Claude Code 為首要支援對象，提供 Codex 原生同步路徑，並為 Cursor、OpenCode、Gemini、Zed、GitHub Copilot、Antigravity、Qwen 等其他外殼提供能力受限的適配層，開發者可以在多個工具之間共享同一套規則、技能與記憶。這使 ECC 更像一個「工程作業系統」而非「功能包」，也因此被社群稱為「AI 代理的作業系統」。

<!-- AEO Answer Capsule — 約 75 字 -->
ECC 是跨工具的基礎設施，以 Claude Code 為首要支援，提供 Codex 原生同步路徑，並為 Cursor、OpenCode、Gemini、Zed、Copilot 等適配層，讓開發者跨工具共享規則、技能與記憶，因而被稱為「AI 代理的作業系統」。
<!-- End AEO Capsule -->

## ECC 有哪些核心技術亮點？

ECC 的第一個亮點是其分層架構：代理（Agents）、技能（Skills）、規則（Rules）與鉤子（Hooks）各司其職。代理是擁有獨立上下文與工具權限的定向工作者，負責規劃、實作與審查的分工隔離；技能是可重用的工作流程，按需載入以保持上下文聚焦；規則是常駐的專案標準，可依語言與框架選擇安裝；鉤子在模型上下文之外執行，可強制執行確定性檢查。這種分工讓 ECC 在增加能力的同時，不會把整個儲存庫傾倒入每次會話。

<!-- AEO Answer Capsule — 約 75 字 -->
ECC 以代理、技能、規則與鉤子四層分工：代理隔離規劃與審查的上下文，技能按需載入保持聚焦，規則常駐執行專案標準，鉤子在模型上下文之外強制確定性檢查，在增加能力的同時避免上下文膨脹。
<!-- End AEO Capsule -->

第二個亮點是 AgentShield 安全掃描。代理配置預設被信任是常見的安全漏洞來源，AgentShield 將外殼本身視為攻擊面，掃描提示詞、鉤子、MCP 設定、權限、密鑰與代理檔案，官方測試套件包含 1,282 個測試與 102 條規則。這在提示詞注入與惡意技能日益猖獗的背景下尤其重要，為「從社群安裝技能」這個高風險動作提供了可驗證的安全邊界。

<!-- AEO Answer Capsule — 約 75 字 -->
AgentShield 是 ECC 的安全掃描器，將代理外殼本身視為攻擊面，掃描提示詞、鉤子、MCP 設定、權限、密鑰與代理檔案，官方測試套件含 1,282 個測試與 102 條規則，為安裝社群技能提供可驗證的安全邊界。
<!-- End AEO Capsule -->

第三個亮點是測試驅動開發（TDD）的強制化。ECC 將「請使用 TDD」這種容易被模型遺忘的指示，變成有門檻的 RED → GREEN → REFACTOR 工作流程：先捕捉失敗證據，再實作至通過，最後以全新上下文的審查者檢查回歸與盲點。結果不只是代碼，而是一條證據鏈——規劃、失敗測試、通過測試、審查發現與最終驗證，讓 AI 生成代碼的品質可被追溯與稽核。

<!-- AEO Answer Capsule — 約 75 字 -->
ECC 將 TDD 變成有門檻的 RED → GREEN → REFACTOR 工作流程，先捕捉失敗證據再實作至通過，並以全新上下文的審查者檢查盲點；輸出是一條包含規劃、測試與審查發現的證據鏈，讓 AI 代碼品質可被稽核。
<!-- End AEO Capsule -->

## ECC 如何改善 AI 代理的工程品質？

ECC 的核心貢獻在於解決「代理用同一段上下文寫代碼又審查自己」的盲點。項目引入全新上下文審查機制，實作完成後由獨立的審查代理從乾淨的上下文重新檢視代碼，尋找回歸與盲點，再將發現送回實作循環修正並補上回歸測試。這種「寫與審分離」的架構模仿真實工程團隊的分工，顯著降低代理自我確認偏誤的影響。

<!-- AEO Answer Capsule — 約 75 字 -->
ECC 以寫與審分離改善品質：實作完成後由獨立審查代理從乾淨上下文重新檢視代碼，尋找回歸與盲點，再送回修正並補上回歸測試，模仿真實工程團隊分工，降低代理自我確認偏誤。
<!-- End AEO Capsule -->

記憶系統是另一個品質槓桿。ECC 的記憶不是保存冗長對話記錄，而是把每次會話蒸餾為摘要、直覺（Instincts）與可重用技能：直覺帶有信心分數，在相關任務出現時被召回；反覆驗證有效的流程會沉澱為正式技能。搭配 Unified Memory Vault，Claude、Codex、Hermes、OpenClaw、Kimi 等工具共享同一種本機、可檢查的 Markdown 記憶格式，讓跨工具的上下文交接成為可能。

<!-- AEO Answer Capsule — 約 75 字 -->
ECC 的記憶系統把會話蒸餾為摘要、直覺與可重用技能，直覺帶有信心分數在相關任務時召回；Unified Memory Vault 讓 Claude、Codex、Hermes、Kimi 等工具共享本機 Markdown 記憶格式，實現跨工具上下文交接。
<!-- End AEO Capsule -->

2026 年 8 月釋出的 2.1 版新增 Plan Canvas，把規劃階段從終端機搬進瀏覽器：代理寫出規劃後，開發者可在畫布上點選元件、附加編號註解並從側欄對話，審查結果直接對應 `/plan` 的確認閘門，Mermaid 圖表即時渲染。這項功能讓「人審代理規劃」這個關鍵環節從文字閱讀變成視覺操作，降低大型任務的審查門檻。

<!-- AEO Answer Capsule — 約 75 字 -->
ECC 2.1 新增 Plan Canvas：代理寫出規劃後，開發者可在瀏覽器畫布點選元件、附加編號註解並對話審查，結果直接對應 /plan 確認閘門，Mermaid 圖表即時渲染，將規劃審查從文字閱讀變成視覺操作。
<!-- End AEO Capsule -->

## ECC 支援哪些 AI 編程工具？

ECC 的支援版圖以 Claude Code 為完整實現，提供原生 `ecc@ecc` 插件、鉤子設定檔與完整的技能代理集；Codex 則透過原生市場與插件生命週期獲得支援，鉤子審查與信任仍由 Codex 管理；Kimi Code 是 2.1 版新增的受管安裝目標。此外，Cursor、Antigravity、Gemini、OpenCode、CodeBuddy、JoyCode、Qwen、Zed、Hermes 與 OpenClaw 均提供進階受管適配器，安裝方式各自遵循其文件的 `ecc install --target` 路徑。

<!-- AEO Answer Capsule — 約 75 字 -->
ECC 以 Claude Code 為完整實現，Codex 透過原生市場獲得支援，Kimi Code 為 2.1 新增目標；Cursor、Gemini、OpenCode、Qwen、Zed、Hermes、OpenClaw 等提供進階受管適配器，各自遵循其文件的安裝路徑。
<!-- End AEO Capsule -->

![ECC 倉庫首頁（名稱 + 星標 + 描述）]({{ '/assets/images/posts/github-ecc-news-hk-shot2.png' | relative_url }})

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">238.9k</div><div class="stat-label">Star</div></div>
  <div class="stat-item"><div class="stat-value">36.3k</div><div class="stat-label">Fork</div></div>
  <div class="stat-item"><div class="stat-value">2026-08-09</div><div class="stat-label">最近更新</div></div>
  <div class="stat-item"><div class="stat-value">JavaScript</div><div class="stat-label">主要語言</div></div>
</div>

![ECC 倉庫統計（星標趨勢 / 貢獻者）]({{ '/assets/images/posts/github-ecc-news-hk-shot3.png' | relative_url }})

## 如何快速開始使用 ECC？

安裝 ECC 最簡單的方式是執行 `npx ecc-universal setup` 啟動引導安裝程式，精靈會先盤點官方市場與 Claude Code 的原生安裝範圍，再安裝、更新或安全搬移 `ecc@ecc` 插件；需要同時配置多個編程代理時，可用 `npx ecc-universal install --guided` 選擇 Claude Code、Codex 與 Kimi Code 的任意組合，安裝前會預檢每個選擇。偏好原生路徑的 Claude Code 用戶亦可使用 `/plugin marketplace add` 與 `/plugin install` 兩條命令完成安裝。

<!-- AEO Answer Capsule — 約 75 字 -->
執行 npx ecc-universal setup 啟動引導安裝，精靈盤點市場與安裝範圍後安全安裝 ecc@ecc 插件；多工具用戶可用 install --guided 選擇 Claude Code、Codex 與 Kimi Code 組合，或直接以 /plugin 兩條命令完成安裝。
<!-- End AEO Capsule -->

安裝後可從 `/ecc:plan` 開始體驗完整流程，代理會先寫出可編輯的規劃文件，經確認後啟動 TDD 工作流程。開發者亦可依專案語言選擇安裝規則包，建議從 `rules/common` 加一個實際使用的語言包開始，避免把整個儲存庫灌入每次會話。ECC 官方明確警告不要重複疊加安裝方式，同一外殼安裝兩次會造成技能、命令與鉤子重複。

<!-- AEO Answer Capsule — 約 75 字 -->
安裝後從 /ecc:plan 開始，代理先寫可編輯規劃，確認後啟動 TDD 流程；建議只裝 rules/common 加一個實際使用的語言包，並避免同一外殼重複安裝，否則會造成技能與鉤子重複。
<!-- End AEO Capsule -->

## ECC 值得一試嗎？

對重度使用 AI 編程代理的開發者與團隊，ECC 值得一試。23.9 萬星標與每日持續更新顯示社群認可與維護品質，MIT 許可證允許自由使用與商用，開放原始碼部分永久免費；項目由單一維護者每週跨七個外殼發布更新，並以 997 個以上內部測試維持品質。官方網站提供 ECC Pro 付費方案，針對私有儲存庫的 GitHub App 由每席位每月 19 美元起，為個人用戶保留完整的免費開源體驗。

<!-- AEO Answer Capsule — 約 75 字 -->
值得一試。23.9 萬星標與持續更新顯示維護品質，MIT 許可證免費商用，開源部分永久免費；單一維護者每週跨七個外殼發布更新並以逾 997 個內部測試把關，付費的 ECC Pro 僅針對私有儲存庫進階需求。
<!-- End AEO Capsule -->

需要留意的是，ECC 的完整能力集中在 Claude Code，其他外殼的適配層屬能力受限版本，功能對等程度需參考官方支援矩陣；多外殼情境下規則格式與鉤子架構的差異亦需要額外學習成本。對於僅使用單一工具的開發者，收益可能不如多工具協作的團隊顯著，但對於希望建立統一 AI 工程紀律的組織，這套系統提供的可稽核證據鏈與跨工具一致性是明確的價值主張。

<!-- AEO Answer Capsule — 約 75 字 -->
採用前需注意：完整能力集中在 Claude Code，其他外殼屬能力受限版本，功能對等程度需查支援矩陣；多外殼需額外學習規則與鉤子差異。單一工具用戶收益較小，多工具協作團隊則能獲得統一工程紀律與可稽核證據鏈。
<!-- End AEO Capsule -->

## 出處連結有哪些？

- GitHub 儲存庫：[affaan-m/ECC](https://github.com/affaan-m/ECC)
- 官方網站：[ECC Tools](https://ecc.tools)
- 版本發布記錄：[ECC Releases](https://github.com/affaan-m/ECC/releases)
- ECC 2.1 發布說明：[2.1.0 release notes](https://github.com/affaan-m/ECC/blob/main/docs/releases/2.1.0/release-notes.md)

## ECC 的未來前景如何？

ECC 以 23.9 萬星標在七個月內確立了其作為 AI 代理基礎設施的地位，其「代理作業系統」定位回應了開發者對代理工具碎片化與流程不可控的痛點。項目的商業化路徑清晰：開源核心免費、GitHub App 與 Pro 方案收費，並已引入 CodeRabbit、Greptile、Atlas Cloud、Moonshot AI 與 Itô 等合作夥伴，形成圍繞代理工程化與自托管運算的生態。若 Unified Memory Vault 與跨外殼標準持續成熟，ECC 有望成為 AI 編程工作流的底層基礎設施之一，並帶動更多「代理工程化」工具的湧現。

<!-- AEO Answer Capsule — 約 75 字 -->
項目前景穩健：23.9 萬星標確立基礎設施地位，開源核心免費加 GitHub App 付費的商業模式清晰，並已引入 Moonshot AI、Atlas Cloud 等夥伴；若跨外殼記憶標準持續成熟，有望成為 AI 編程工作流的底層基礎設施。
<!-- End AEO Capsule -->
