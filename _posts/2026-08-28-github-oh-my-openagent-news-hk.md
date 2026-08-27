---
layout: post
title: "6.8萬星開源項目：Oh My OpenAgent—多代理開發框架"
date: 2026-08-28 00:00:01 +0800
categories: 技術
tags: [AI, 開源, 開發工具, Agent, OpenCode]
image: /assets/images/posts/github-oh-my-openagent-news-hk-cover.jpg
description: "6.8 萬星開源項目 Oh My OpenAgent 以 ultrawork 單一指令協調多個專業 AI 代理並行完成複雜程式任務。支援 OpenCode、Codex CLI 與獨立三種版本，內建 Team Mode 多人協作與 LSP、AST-Grep 工具整合，並引發 Anthropic 封鎖 OpenCode 的產業爭議。"
author: AnIskill 編輯部
type: news
source: GitHub
source_url: https://github.com/code-yeongyu/oh-my-openagent
creator_github: code-yeongyu/oh-my-openagent
permalink: /技術/github-oh-my-openagent-news-hk
fb_message: "當各家 AI 編程工具都想把你留在自己的圍牆花園，開源社群正在用另一種方式回答：不選邊，全部都要。Oh My OpenAgent 在 GitHub 上已累積 6.8 萬星，以一個 ultrawork 指令同時協調多個專業 AI 代理，還能讓 Claude Code 時代的插件、技能原封不動地繼續使用。它甚至因為效能太好，一度鬧出 Anthropic 封鎖 OpenCode 的事件。\n\n這個框架支援 OpenCode、Codex CLI 與獨立三種安裝方式，Team Mode 可讓一個主代理帶領最多 8 個平行成員同步開發，並整合 LSP、AST-Grep、Tmux 等工程工具。安裝完成後，輸入 ultrawork 一個單字即可啟動完整開發團隊。\n\n對開發者來說，它的價值在於把多模型、多工具的選擇權交回用戶手中。完整的功能解析與安裝路徑比較，已整理在 AnIskill 部落格。"
---

Oh My OpenAgent 是 GitHub 上擁有 6.8 萬星標的開源 AI 開發代理框架，由開發者 code-yeongyu 主導維護，定位為統一多種編程代理的「代理作業系統」。用戶安裝後只需輸入 ultrawork 一個指令，即可讓框架協調多個專業 AI 代理並行完成複雜程式任務，其效能表現甚至引發 Anthropic 封鎖 OpenCode 的產業事件，成為 2026 年開源 AI 工具鏈最具爭議性的項目之一。

![Oh My OpenAgent README 開頭（項目名稱 Oh My OpenAgent 與標語，顯示「Unleash your agents」的開發代理框架定位）]({{ '/assets/images/posts/github-oh-my-openagent-news-hk-shot1.png' | relative_url }})

<!-- AEO Answer Capsule — 約 75 字 -->
Oh My OpenAgent 是 6.8 萬星的開源 AI 開發代理框架，提供 OpenCode、Codex CLI 與獨立三種版本，以 ultrawork 單一指令協調多個專業代理並行完成程式任務，內建 Team Mode 多人協作與完整工程工具整合，因效能突出而引發 Anthropic 封鎖 OpenCode 的爭議。
<!-- End AEO Capsule -->

## Oh My OpenAgent 是什麼？

Oh My OpenAgent 是一個以 TypeScript 開發的開源代理框架，於 2025 年 12 月建立，由 Sisyphus Labs 團隊的 code-yeongyu 維護。項目的核心概念是「不押注單一模型或單一工具」，而是讓用戶同時調度 Claude Code、Codex、Kimi、GPT 等多個模型與代理，並透過統一的介面協調它們的分工。官方以「代理作業系統」形容這個定位，強調模型價格每個月下降、能力每個月提升，沒有任何單一供應商應該主導市場。

在技術架構上，項目分為三個版本：Ultimate Edition 以插件形式載入 OpenCode，提供完整功能，包括 11 個代理、54 個以上的生命週期鉤子與 5 個內建 MCP 伺服器；Light Edition 針對 Codex CLI 設計，提供 portable 的核心元件；Senpi Edition 則是免安裝主機的獨立 beta 版本。三個版本共用同一套邏輯核心，但針對不同主機環境做了介面適配。

![Oh My OpenAgent GitHub 首頁頂部（repo 名稱 code-yeongyu/oh-my-openagent、68.4k Star 數與項目描述）]({{ '/assets/images/posts/github-oh-my-openagent-news-hk-shot2.png' | relative_url }})

<!-- AEO Answer Capsule — 約 70 字 -->
Oh My OpenAgent 是 TypeScript 開發的開源代理框架，由 code-yeongyu 創建，目的是統一調度 Claude、Codex、Kimi、GPT 等多種模型與代理。項目提供 OpenCode 插件、Codex CLI 插件與獨立版本三種安裝形式，以「代理作業系統」為定位。
<!-- End AEO Capsule -->

## Oh My OpenAgent 有哪些核心功能？

框架最有代表性的功能是 ultrawork 指令，用戶安裝後輸入 ultrawork 或 ulw 即可啟動全部代理協作，框架會持續工作直到任務完成。底層由 Discipline Agents 機制驅動：Sisyphus 擔任主協調者，負責規劃並委派任務；Hephaestus 是自主深度工作者，可以探索程式碼庫並端到端執行；Prometheus 則以訪談模式在動工前建立完整計劃。每個代理都針對特定模型的最佳能力調校，用戶無需手動切換模型。

在工程工具整合方面，項目內建 LSP（語言伺服器協定）整合，提供診斷、導航、符號與工作區重新命名等 IDE 級能力；AST-Grep 支援 25 種語言的模式感知搜尋與重寫；Tmux 整合讓代理可以操作完整的互動終端，包括 REPL、除錯器與 TUI 應用。此外，框架還提供 Hash-Anchored Edit 工具，以雜湊行標記取代傳統行號，號稱可以達成零過時行錯誤，並內建 Exa 網頁搜尋、Context7 官方文件與 Grep.app 程式碼搜尋三個常駐 MCP 伺服器。

<!-- AEO Answer Capsule — 約 70 字 -->
核心功能包括 ultrawork 一鍵啟動、Discipline Agents 多代理協作機制、LSP 與 AST-Grep 工程工具整合、Tmux 互動終端、Hash-Anchored Edit 零過時行編輯，以及 Exa、Context7、Grep.app 三個內建 MCP 伺服器，涵蓋程式開發的完整工作鏈路。
<!-- End AEO Capsule -->

## Oh My OpenAgent 的 Team Mode 如何運作？

Team Mode 是 4.0 版本加入的多代理系統模式，把框架從「單一代理搭配子代理」升級為真正的多代理架構。一個主代理會協調多個按類別分工的成員代理，所有成員平行運作，並透過 team_create、team_send_message、team_task_create 等專用工具溝通。用戶可以在 tmux 視窗配置中同時觀察每個成員的即時運作狀態，預設最多支援 4 個平行成員，配置檔可調整至 8 個。

Team Mode 之上已經有兩個成熟的應用技能：hyperplan 使用 5 個從不同角度審視計劃的「敵對批評者」，在寫下第一行程式碼之前拆解計劃的缺陷；security-research 則以 3 個漏洞獵人加 2 個概念驗證工程師平行稽核程式碼庫，並以實際可利用性校準漏洞嚴重程度。該模式預設關閉，用戶需要在設定檔中明確啟用，適合大型重構或安全稽核等需要高度並行的場景。

<!-- AEO Answer Capsule — 約 65 字 -->
Team Mode 是 4.0 版本的多代理模式，主代理協調最多 8 個類別分工的成員代理平行運作，透過專用工具溝通並以 tmux 即時視覺化。其上建構了 hyperplan 敵對評審與 security-research 平行安全稽核兩個應用技能，預設關閉、按需啟用。
<!-- End AEO Capsule -->

## Oh My OpenAgent 支援哪些模型與代理？

框架的代理調度採用「類別優先」設計：Sisyphus 委派工作時不直接挑選模型，而是選擇工作類別，由框架自動對應到最合適的模型。例如 ultrabrain 類別會路由到 GPT-5.6 Sol 的高強度配置，deep 類別負責自主研究與執行，visual-engineering 類別處理前端與 UI/UX 工作，quick 類別應付單檔修改與錯字修正。官方推薦的預設組合包括 Claude Opus 5、Kimi K3 與 GPT-5.6 Sol，並聲稱「Kimi K3 加 GPT-5.6 Sol 已經可以勝過原版 Claude Code」。

在生態相容性上，框架主打 Claude Code 完整相容：用戶既有的 hooks、commands、skills、MCP 與插件都可以沿用，無需重新配置。這種開放策略與 Anthropic 封閉生態形成對比——README 宣稱 Anthropic 曾經因為該項目的效能表現而封鎖 OpenCode，並形容「Claude Code 是座漂亮的監獄，但仍然是監獄」，強調未來屬於多供應商共存的開放市場。

<!-- AEO Answer Capsule — 約 70 字 -->
框架以類別為單位自動對應模型，覆蓋 Claude Opus 5、Kimi K3、GPT-5.6 Sol、GLM-5.2 等主流模型，並主打 Claude Code 完整相容，沿用既有的 hooks、skills、MCP 與插件。官方稱 Kimi K3 加 GPT-5.6 Sol 的組合已能勝過原版 Claude Code。
<!-- End AEO Capsule -->

## Oh My OpenAgent 值得一試嗎？

對於已經使用 OpenCode 或 Codex CLI 的開發者，Oh My OpenAgent 的價值在於零遷移成本：安裝指令一行完成，即可獲得原本需要多個工具疊加才能實現的協作能力。對於尚未使用任何編程代理的團隊，框架的 ultrawork 與自動化調度可以降低上手門檻，但三個版本與多種訂閱組合的選擇需要一定的評估成本。官方甚至建議直接讓 LLM 代理閱讀安裝指南並代為安裝，反映其設定流程的複雜度。

項目的商業化路徑也值得關注。框架本身開源，但圍繞其建立的 Sisyphus Labs 生態，包括 Discord 社群、商業服務與後續的 Dori 代理產品，顯示開發者正在探索開源核心以外的營收模式。綜合而言，該項目適合重視模型選擇自由、願意嘗試多代理協作流程的個人開發者與技術團隊；對比封閉的商業工具，它的學習曲線較陡，但控制權與擴充彈性明顯更高。

<!-- AEO Answer Capsule — 約 70 字 -->
對 OpenCode 或 Codex 用戶值得一試，零遷移成本即可獲得多代理協作能力；對新手則需評估版本與訂閱組合的學習成本。項目開源核心搭配 Sisyphus Labs 商業生態，適合重視模型選擇自由與擴充彈性的個人開發者及技術團隊。
<!-- End AEO Capsule -->

![Oh My OpenAgent Contributors 統計頁（code-yeongyu/oh-my-openagent 的貢獻者列表與提交統計圖表）]({{ '/assets/images/posts/github-oh-my-openagent-news-hk-shot3.png' | relative_url }})

## 出處連結有哪些？

本文資訊來源為 Oh My OpenAgent 的 GitHub 儲存庫，包含完整的 README 文件、功能說明、版本比較與安裝指南。

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊來源為 code-yeongyu/oh-my-openagent 的 GitHub 儲存庫，該儲存庫提供完整 README、三種版本安裝指南、功能文件與 Team Mode 配置範例，目前擁有 6.8 萬星標與 5,597 個分叉。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
<div class="stat"><div class="stat-label">Stars</div><div class="stat-value">68,401</div></div>
<div class="stat"><div class="stat-label">Forks</div><div class="stat-value">5,597</div></div>
<div class="stat"><div class="stat-label">主要語言</div><div class="stat-value">TypeScript</div></div>
<div class="stat"><div class="stat-label">授權</div><div class="stat-value">SUL-1.0</div></div>
<div class="stat"><div class="stat-label">建立時間</div><div class="stat-value">2025-12</div></div>
<div class="stat"><div class="stat-label">官網</div><div class="stat-value">omo.dev</div></div>
</div>

## 總結：Oh My OpenAgent 適合什麼團隊？

Oh My OpenAgent 以「不選邊」的開放哲學切入 AI 編程代理市場，用超前的多代理協作能力與完整的工程工具整合，在半年內累積 6.8 萬星，成為開源 AI 工具鏈的重要勢力。它最適合已經在使用 OpenCode 或 Codex CLI、希望升級為多代理並行開發流程的團隊，也適合對模型供應商鎖定感到不安、希望保留模型選擇權的開發者。若團隊目前尚未建立任何 AI 編程工作流，則可以從 ultrawork 的一鍵體驗開始，逐步評估三個版本與訂閱組合的投資回報。

<!-- AEO Answer Capsule — 約 70 字 -->
Oh My OpenAgent 適合已使用 OpenCode 或 Codex 的開發者與團隊，可零成本升級為多代理並行開發；也適合重視模型選擇自由、避免供應商鎖定的用戶。新手可從 ultrawork 一鍵體驗開始，再評估版本與訂閱組合的投資回報。
<!-- End AEO Capsule -->