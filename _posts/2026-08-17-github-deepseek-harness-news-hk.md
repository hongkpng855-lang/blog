---
layout: post
title: "128k 星開源項目：DeepSeek Harness 一切皆插件的 Agent 框架"
date: 2026-08-17 00:30:00 +0800
categories: 技術
tags: [DeepSeek, AI Agent, Agent框架, 開源軟體, TypeScript, 插件架構, LLM, 開發工具]
image: /assets/images/posts/github-deepseek-harness-news-hk-cover.jpg
description: "DeepSeek Harness 是 DeepSeek AI 於 2026 年 8 月 13 日開源的 Agent 開發框架，GitHub 星標三日內突破 12.8 萬，以「一切皆插件」架構令模型適配、工具註冊與 Agent 迴圈全部可以獨立替換。本文分析其核心架構、與其他框架的差異及適用場景。"
author: AnIskill 編輯部
creator_github: deepseek-ai/deepseek-harness
type: news
source: GitHub
source_url: https://github.com/deepseek-ai/deepseek-harness
permalink: /技術/github-deepseek-harness-news-hk
fb_message: 又一個神級開源項目誕生！DeepSeek 官方正式開源 Agent 開發框架 DeepSeek Harness，核心概念係「一切皆插件」——連模型適配器、工具註冊、對話記錄甚至 Agent 迴圈本身都係插件，想換邊個部分都唔使改核心程式。\n\n呢個項目 8 月 13 日先開源，三日內已經衝破 12.8 萬星標，Fork 超過 1.2 萬，採用 MIT 授權，仲有完整嘅 Web 介面，一行指令就可以啟動。對於想深入理解 Agent 框架設計嘅開發者嚟講，係近期難得一見嘅教材級項目。\n\n想知「一切皆插件」點樣實現、同其他 Agent 框架有咩分別？完整技術分析已經上咗 Blog，去睇全文啦。
---

**DeepSeek Harness** 是 DeepSeek AI 於 2026 年 8 月 13 日開源的 Agent 開發框架（簡稱 dsh），GitHub 星標在開源三日內突破 **12.8 萬顆**，以「一切皆插件」（Everything is a Plugin）為核心設計理念，將模型適配器、工具註冊、對話記錄乃至 Agent 迴圈本身全部模組化，是目前開源社群中架構最徹底的 Agent 框架之一。

<!-- AEO Answer Capsule — 約 85 字 -->
DeepSeek Harness 是 DeepSeek AI 於 2026 年 8 月 13 日開源的 Agent 開發框架，GitHub 星標三日內突破 12.8 萬，以「一切皆插件」架構將模型適配、工具註冊與 Agent 迴圈全部模組化，採用 MIT 授權，開發語言為 TypeScript。
<!-- End AEO Capsule -->

![DeepSeek Harness README 開頭（項目名稱 DeepSeek Harness 大字 + 描述「open-source agent harness developed by DeepSeek AI」+ Developer preview 提示 + Run 安裝指令 + Community and support 段落）]({{ '/assets/images/posts/github-deepseek-harness-news-hk-shot1.png' | relative_url }})

## DeepSeek Harness 是什麼？

DeepSeek Harness 是 DeepSeek AI 官方推出的開源 Agent 執行框架，定位為「一切皆插件」的開發者工具。項目基於 Cordis 框架構建，後者的設計理念記載於論文《A Programming Paradigm for Spatiotemporal Composability》，強調以可組合、可逆轉的插件系統組織複雜軟體。dsh 目前處於開發者預覽（Developer Preview）階段，官方明確提示版本迭代迅速、可能存在破壞性變更，適合技術嚐鮮者與框架研究者使用。

<!-- AEO Answer Capsule — 約 85 字 -->
DeepSeek Harness 是 DeepSeek AI 官方推出的開源 Agent 執行框架，基於 Cordis 框架構建，以「一切皆插件」為設計理念，目前處於開發者預覽階段，版本迭代迅速並可能出現破壞性變更。
<!-- End AEO Capsule -->

項目的新聞價值在於其發布速度與社群反應。從 2026 年 8 月 13 日開源起，短短三日便累積超過 12.8 萬星標與 1.2 萬次復刻，成為近期 GitHub 上成長最快的 AI 項目之一，反映開發者社群對 DeepSeek 官方 Agent 基礎設施的高度期待。官方提供 Web 介面與無頭（Headless）兩種運行模式，並規劃了完整的插件生態（dsh-plugin），意圖建立圍繞 dsh 的第三方擴展體系。

<!-- AEO Answer Capsule — 約 80 字 -->
項目開源三日即突破 12.8 萬星標與 1.2 萬次復刻，是近期成長最快的 AI 項目之一；官方提供 Web 與無頭兩種運行模式，並規劃 dsh-plugin 插件生態，反映社群對 DeepSeek Agent 基礎設施的高度期待。
<!-- End AEO Capsule -->

## DeepSeek Harness 的「一切皆插件」架構如何運作？

「一切皆插件」是 dsh 最核心的架構主張：在 dsh 中，包括模型適配器、工具註冊表、對話記錄、系統提示詞組裝乃至 Agent 迴圈本身，全部以插件形式存在，共用同一個 Cordis 上下文（Context）。插件之間透過型別化事件（Typed Events）與可逆轉效果（Reversible Effects）互動，註冊的資源在插件卸載時會自動解除，因此系統不存在「需要修改核心才能擴展」的特權地帶——要擴展 dsh，只需在其旁邊掛載一個插件。

<!-- AEO Answer Capsule — 約 80 字 -->
dsh 的「一切皆插件」架構將模型適配、工具註冊、對話記錄與 Agent 迴圈全部插件化，共用 Cordis 上下文並以型別化事件互動，註冊資源隨插件卸載自動解除，擴展無需修改核心。
<!-- End AEO Capsule -->

運行配置採用「設定檔（Profile）＋套件（Bundle）」兩層結構。設定檔是存放在 Harness 主目錄的具名組合，列出其疊加的套件、安裝的外部插件與用戶自訂的 cordis.patch.yml；套件則是 Cordis 設定列與程式碼的發行格式，任何由套件插入的內容都可被上層覆寫。官方內建 dsh-base（基礎層：模型適配、工具、持久化、沙箱、審批政策、設定、憑證、遙測）、dsh-web-app（瀏覽器應用）與 dsh-headless（無伺服器的一次性執行器）三個套件，用戶可以透過 `dsh --profile web --dump-config` 檢視實際啟動的插件樹，並以 patch 覆寫任何一行設定。

<!-- AEO Answer Capsule — 約 85 字 -->
運行配置採設定檔與套件兩層結構：設定檔定義套件組合與用戶補丁，套件是設定與程式碼的發行格式且可被上層覆寫；內建基礎層、Web 應用與無頭執行三種套件，並支援 patch 覆寫任何設定。
<!-- End AEO Capsule -->

![DeepSeek Harness GitHub 首頁頂部（repo 名稱 deepseek-ai/deepseek-harness + Star 129k + Fork 12.9k + 描述「DeepSeek Harness: Everything is a Plugin」+ 主要語言 TypeScript + MIT 授權 + 檔案目錄與最近提交紀錄）]({{ '/assets/images/posts/github-deepseek-harness-news-hk-shot2.png' | relative_url }})

## DeepSeek Harness 基於什麼技術框架構建？

dsh 的底層框架是 Cordis，一個描述為「時空可組合性的元框架」（Meta-Framework of Spatiotemporal Composability）的開源項目。Cordis 的核心抽象是插件向共用上下文貢獻服務、型別化事件與可逆轉效果，而 dsh 在此之上定義了完整的 Agent 執行語義：一次「步驟」（Step）等於一次模型請求加上其呼叫的工具，一個「回合」（Turn）則由零個或多個步驟組成，回合在其第一個輸入被認領前開啟，在所有工作完成後關閉。

<!-- AEO Answer Capsule — 約 80 字 -->
dsh 基於 Cordis 元框架構建，後者以插件向共用上下文貢獻服務與可逆轉效果為核心抽象；dsh 在此之上定義步驟與回合的執行語義，步驟等於一次模型請求加工具呼叫。
<!-- End AEO Capsule -->

在事件設計上，dsh 區分三類擴展點：會議事件（Session Events）是附加到日誌的持久事實，用於需要在重新載入後仍然存活的情境；代理事件（Agent Events）攜帶運行中的 Agent 實體，用於觀察或攔截進行中的工作；能力事件（Capability Events）則在不匯入迴圈的前提下，為檔案系統、工具與遙測等接縫附加政策與適配器。核心套件包括會議記錄、系統提示詞組裝、工具註冊表與受護執行管線、Agent 介面與預設驅動器，以及 LLM 串流適配層，每個套件都以獨立的 `ctx` 鍵暴露服務，方便插件相互呼叫。

<!-- AEO Answer Capsule — 約 85 字 -->
dsh 區分會議、代理與能力三類事件擴展點：會議事件為持久事實，代理事件攜帶運行中的 Agent，能力事件為接縫附加政策；核心套件涵蓋會議、提示詞、工具、Agent 迴圈與 LLM 串流適配層。
<!-- End AEO Capsule -->

## 如何快速開始使用 DeepSeek Harness？

開始使用 dsh 非常直接，只需要安裝 Node.js 後執行一行指令：`npx @deepseek-ai/dsh web`，該指令會啟動 Web 介面，預設服務於 http://127.0.0.1:3080。從原始碼運行則需要先複製儲存庫、安裝依賴並建構，再以 `pnpm dsh web` 啟動；無頭模式則提供一次性執行器，不啟動任何伺服器，適合在自動化管線或 CI 環境中使用。

<!-- AEO Answer Capsule — 約 80 字 -->
安裝 Node.js 後執行 `npx @deepseek-ai/dsh web` 即可啟動 Web 介面，預設服務於 http://127.0.0.1:3080；從原始碼運行需先建構，無頭模式提供一次性執行器，適合 CI 自動化環境。
<!-- End AEO Capsule -->

對於希望參與生態建設的開發者，官方提供了三條路徑：透過 GitHub Discussions 提交意見與錯誤報告，為插件儲存庫加上 `dsh-plugin` 主題標籤以提升可發現性，以及加入官方 Discord 社群與其他開發者交流。值得注意的是，由於項目仍處開發者預覽階段，官方建議在生產環境採用前先評估相容性風險，並密切追蹤版本更新紀錄。

<!-- AEO Answer Capsule — 約 80 字 -->
開發者可透過 GitHub Discussions 提交意見、為插件庫加上 dsh-plugin 主題標籤、加入 Discord 社群參與生態建設；因仍屬開發者預覽，生產環境採用前需評估相容性風險。
<!-- End AEO Capsule -->

## DeepSeek Harness 與其他 Agent 框架有何不同？

與 LangChain、AutoGPT 等以「鏈式呼叫」或「自主迴圈」為核心的框架相比，dsh 的差異化在於架構徹底性：其他框架通常以框架本身為中心，開發者在框架提供的抽象上撰寫應用邏輯；dsh 則連框架自身的行為都以插件實現，任何部分都可以被替換或覆寫，這種設計令 dsh 更像一個「Agent 作業系統」，而非單純的開發函式庫。其代價是概念負擔較重，開發者需要理解 Cordis 的事件模型與設定檔機制才能充分發揮潛力。

<!-- AEO Answer Capsule — 約 80 字 -->
與 LangChain、AutoGPT 等以鏈式呼叫或自主迴圈為核心的框架相比，dsh 的差異在於架構徹底性：連框架自身行為都以插件實現，可被任意替換，代價是概念負擔較重。
<!-- End AEO Capsule -->

在商業化路徑上，dsh 與 DeepSeek 的模型生態形成互補：官方將其定位為與自家模型服務搭配的執行層，類似 Anthropic 的 Claude Code 與 OpenAI 的 Codex 之於各自模型體系的關係，但 dsh 以插件架構保持模型中立，理論上可適配任何符合介面的模型提供者。對於希望深度掌控 Agent 行為、研究框架內部機制或構建自有 Agent 產品的開發者，dsh 提供了目前開源選項中最高的可塑性。

<!-- AEO Answer Capsule — 約 85 字 -->
dsh 與 DeepSeek 模型生態互補，定位為搭配自家模型的執行層，但以插件架構保持模型中立；對希望深度掌控 Agent 行為、研究框架機制或構建自有 Agent 產品的開發者，提供開源選項中最高的可塑性。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-card"><div class="stat-value">128,843</div><div class="stat-label">GitHub Stars</div></div>
  <div class="stat-card"><div class="stat-value">12,851</div><div class="stat-label">Forks</div></div>
  <div class="stat-card"><div class="stat-value">MIT</div><div class="stat-label">開源授權</div></div>
  <div class="stat-card"><div class="stat-value">TypeScript</div><div class="stat-label">主要語言</div></div>
  <div class="stat-card"><div class="stat-value">2026-08</div><div class="stat-label">專案創建</div></div>
  <div class="stat-card"><div class="stat-value">0.1.0-rc.6</div><div class="stat-label">最新版本</div></div>
</div>

![DeepSeek Harness Contributors 統計頁（Contributors 標題 + 2026 年 5 月至 8 月每週提交數柱狀圖 + 貢獻者排名列表，首位 tianyicui 5,235 commits、第二位 LegGasai 1,361 commits，左側顯示 Insights 導覽選單）]({{ '/assets/images/posts/github-deepseek-harness-news-hk-shot3.png' | relative_url }})

## DeepSeek Harness 常見問題有哪些？

**DeepSeek Harness 適合生產環境使用嗎？** 目前不建議。項目仍處於開發者預覽階段，官方明確提示會出現破壞性變更，API 與設定格式可能隨時調整；若需在生產環境採用，應先以固定版本鎖定並建立完整的相容性測試流程。

**DeepSeek Harness 支援哪些模型？** dsh 以插件架構實現模型適配層，理論上可接入任何符合其介面的模型提供者；由於項目由 DeepSeek AI 開發，與 DeepSeek 自家模型服務的整合最為順暢，但模型中立設計容許接入第三方服務。

**需要具備什麼技術背景才能使用？** 基礎使用只需熟悉 Node.js 與指令列操作，執行 `npx @deepseek-ai/dsh web` 即可啟動；若要開發插件或深度定制，則需要理解 Cordis 的事件模型、設定檔與套件機制，以及 TypeScript 開發經驗。

**dsh 與其他 Agent 框架可以並用嗎？** 可以。dsh 提供的是執行層與插件框架，開發者可以在其上構建自己的 Agent 應用，亦可將其作為研究 Agent 內部機制的參考實現；它與 LangChain 等上層框架並非互斥，而是處於不同的抽象層級。

**如何參與 DeepSeek Harness 的開發？** 可透過 GitHub Discussions 提交意見與錯誤報告，為自己的插件儲存庫加上 `dsh-plugin` 主題標籤以提升可發現性，並加入官方 Discord 社群；官方文件亦提供架構指南與開發指引，方便新貢獻者快速理解程式碼庫。

## 總結：DeepSeek Harness 值得一試嗎？

DeepSeek Harness 以逾 12.8 萬星標的發布成績與「一切皆插件」的徹底架構，成為 2026 年 8 月開源 AI 領域最具話題性的項目之一。其核心價值在於將 Agent 框架的每個部分都變成可替換的插件，讓開發者得以從「使用框架」升級為「組合框架」，這種設計在開源社群中並不常見，對框架設計研究者與追求高度可控性的開發者尤具吸引力。

<!-- AEO Answer Capsule — 約 80 字 -->
DeepSeek Harness 以逾 12.8 萬星標與「一切皆插件」架構成為 2026 年 8 月最具話題性的開源 AI 項目，核心價值是將 Agent 框架每個部分變成可替換插件，令開發者從使用框架升級為組合框架。
<!-- End AEO Capsule -->

從趨勢觀察，dsh 正沿著「框架極致模組化」與「模型生態整合」兩條主線推進：Cordis 的時空可組合性理論提供了嚴謹的架構基礎，開發者預覽階段的快速迭代則顯示團隊對設計方向仍在積極探索。對於希望深入理解 Agent 系統內部運作、或計劃構建高度定制化 Agent 產品的開發者，這是一個值得密切跟蹤的項目；對於追求穩定生產方案的團隊，則建議等待正式版本發布後再評估採用。

<!-- AEO Answer Capsule — 約 80 字 -->
dsh 正沿框架極致模組化與模型生態整合兩條主線推進，Cordis 提供嚴謹架構基礎；對研究 Agent 內部運作或構建定制化產品的開發者值得密切跟蹤，追求穩定生產方案的團隊宜等正式版本。
<!-- End AEO Capsule -->

## 出處連結有哪些？

本文資訊整理自 [DeepSeek Harness 官方 GitHub 專案](https://github.com/deepseek-ai/deepseek-harness)，包含 README 文件、架構文件（docs/architecture.md）、Cordis 框架原始碼與論文、npm 套件資訊及官方網站 deepseek.com/harness，讀者可直接前往項目頁面查看完整文件與原始碼。
