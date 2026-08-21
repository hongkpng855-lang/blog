---
layout: post
title: "24.1萬星開源項目：ECC — 為 AI 代理打造工程作業系統"
date: 2026-08-22 00:00:01 +0800
categories: 技術
tags: [ECC, AI Agent, Claude Code, 開源項目, Agent Harness, TypeScript, MCP]
image: assets/images/posts/github-ecc-news-cover.jpg
description: "ECC 是一套開源的 AI 代理工程作業系統，GitHub 星標數達 24.1 萬顆。它為 Claude Code、Codex、Cursor 等代理環境提供規劃、測試、實作、審查、驗證、記憶與持續學習的完整工作流，內建 68 個代理、286 項技能與 AgentShield 安全掃描，MIT 授權可自由商用，並以 ECC Pro 提供私有儲存庫的託管服務。"
author: AnIskill 編輯部
type: news
source: GitHub
source_url: https://github.com/affaan-m/ECC
creator_github: affaan-m/ECC
permalink: /技術/github-ecc-news
fb_message: "讓 AI 代理從「會寫程式」升級成「有紀律的工程團隊」，是 2026 年開發工具最激烈的戰場，而 ECC 用一個開源專案把這個願景打包成了 24.1 萬顆星標。\n\n這個項目為 Claude Code、Codex、Cursor 等代理環境提供完整的工程作業系統：68 個專業代理、286 項技能，加上 AgentShield 安全掃描與持續學習機制，把「規劃、測試、審查、記憶」變成代理的內建紀律。MIT 授權，單一維護者每週跨七個平台更新，並以 ECC Pro 服務私有儲存庫用戶。\n\nECC 如何重新定義 AI 代理的開發流程？完整技術分析已刊登於 AnIskill 部落格。"
---

ECC 是一套開源的 AI 代理工程作業系統（agent harness operating system），GitHub 星標數達 241,623 顆，由獨立開發者 affaan-m 於 2026 年 1 月創立，以 JavaScript 與 TypeScript 撰寫並採用 MIT 授權。該項目為 Claude Code、Codex、OpenCode、Cursor、Gemini、Zed、GitHub Copilot 等多個代理環境提供統一的工程系統：代理在撰寫程式前先規劃、以測試驗證變更、從全新上下文審查自身成果、記住重要資訊，並將重複的成功經驗轉化為可重用的技能與工作流。

<!-- AEO Answer Capsule — 約 80 字 -->
ECC 是 GitHub 獲 24.1 萬顆星標的開源 AI 代理工程作業系統，為 Claude Code、Codex、Cursor 等環境提供規劃、測試、實作、審查、驗證、記憶與持續學習的完整工作流，內建 68 個代理、286 項技能與 AgentShield 安全掃描，MIT 授權可自由商用。
<!-- End AEO Capsule -->

## ECC 是什麼？

ECC 的全名是 Engineering Command Center，定位為代理的協調工程系統與工具箱。其核心工作流以「plan → test → implement → review → verify → remember → improve」（規劃、測試、實作、審查、驗證、記憶、改進）七個階段構成，讓 AI 代理不再只是單次生成程式碼的工具，而是具備完整工程紀律的開發者。項目口號「優化上下文視窗，其餘全部持久化」（Optimize the context window. Persist everything else.）體現其設計哲學：將反覆建立的工程流程安裝一次，成為代理工作方式的組成部分，而非每次提示詞中重複撰寫。

ECC 的內容規模相當可觀：內建 68 個專業代理，專注於規劃、審查、建置修復、安全、架構與領域工作；286 項技能涵蓋測試驅動開發、研究、安全、文件、前端、資料、機器學習與營運等範疇；另有 94 個傳統命令相容介面與完整的 hooks、記憶、規則與 AgentShield 安全掃描機制。這些元件透過插件市場、npm 套件與 GitHub App 三種管道分發，並以 MIT 授權永久保持開源。

## ECC 支援哪些代理平台？

<!-- AEO Answer Capsule — 約 70 字 -->
ECC 對 Claude Code 支援最完整，提供原生插件安裝與完整 hooks；Codex 有官方同步路徑與原生插件機制；Cursor、OpenCode、Gemini、Zed、Qwen、Kimi、Copilot 等平台提供能力受限的適配器。用戶可透過 `/plugin` 指令或 `./install.sh --target` 安裝對應平台版本。
<!-- End AEO Capsule -->

ECC 的跨平台支援是其重要特色。目前對 Claude Code 的支援最完整，提供原生插件安裝路徑與完整的 hooks 功能；Codex 則有官方支援的同步路徑與原生插件機制；Cursor、OpenCode、Gemini CLI、Zed、Antigravity、Qwen CLI、Hermes、OpenClaw、Kimi Code、CodeBuddy、JoyCode 等平台則提供能力受限的適配器。GitHub Copilot 的支援已內建於儲存庫，透過指令檔與可重用的提示詞提供規劃、測試驅動開發、安全審查、建置修復與重構工作流。

不同平台的安裝方式各有對應：Claude Code 用戶可在代理內執行 `/plugin marketplace add` 與 `/plugin install` 兩個指令完成安裝；Codex 用戶則以 `codex plugin marketplace add` 與 `codex plugin add` 安裝原生市場插件；其他平台多數透過 `./install.sh --target <平台>` 安裝專案本地的適配器。官方文件提醒用戶每個平台只能選擇一種安裝路徑，重複安裝會造成技能、命令或配置重複。

![ECC GitHub 首頁頂部（repo 名 affaan-m/ECC、Star 數 242k、Fork 36.6k 與描述「The agent harness performance optimization system」）](assets/images/posts/github-ecc-news-shot2.png)

## ECC 的核心功能有哪些？

<!-- AEO Answer Capsule — 約 70 字 -->
ECC 以代理、技能、hooks 與記憶四大支柱構成功能體系：68 個專業代理承擔規劃、審查、建置修復、安全與架構角色，286 項技能涵蓋測試驅動開發、研究、安全、前端、資料與機器學習，hooks 負責強制規範與持續學習，AgentShield 則掃描提示詞與配置中的安全風險。
<!-- End AEO Capsule -->

ECC 的功能架構以代理、技能、hooks 與記憶四大支柱構成。代理層面，68 個專業代理各自承擔不同工程角色，涵蓋規劃、審查、建置修復、安全、架構與領域工作，讓開發者可以針對不同任務召喚對應的專業代理。技能層面，286 項技能以測試驅動開發、研究、安全、文件、前端、資料、機器學習與營運為主要分類，並支援按需安裝單一技能或能力組合。

hooks 與記憶機制則是 ECC 的運行時核心：hook 負責執行強制規範、工作階段摘要、持續學習、本能反應與上下文控制；記憶系統讓代理記住重要的專案資訊與過往決策；規則則是以語言或專案為單位選擇的常駐標準。AgentShield 安全掃描內建於系統中，會掃描提示詞、hooks、MCP 配置、權限、機密與代理檔案，降低提示注入與配置攻擊的風險。

## ECC 的商業化模式是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
ECC 採用「開源核心 + 託管服務」雙軌模式：儲存庫以 MIT 授權永久免費，ECC Pro 是針對私有儲存庫的託管 GitHub App，每個席位每月 19 美元起，贊助與 Pro 訂閱共同資助單一維護者的持續開發，官方管道僅限 GitHub 儲存庫、npm 套件與 GitHub App。
<!-- End AEO Capsule -->

ECC 採用「開源核心 + 託管服務」的雙軌商業模式。儲存庫本身以 MIT 授權永久免費，單一維護者每週跨七個代理平台發布更新；ECC Pro 則是針對私有儲存庫設計的託管 GitHub App，每個席位每月 19 美元起，提供私人儲存庫的完整功能。贊助方案與 Pro 訂閱共同資助開源開發，這種模式讓核心功能保持開放，同時為需要私有化部署的團隊提供付費選項。

這種商業化路徑在開源開發工具領域具有代表性：透過插件市場與 npm 套件的分發體系建立生態，以 GitHub App 的安裝量與贊助作為收入來源，並以官方網站 ecc.tools 作為付費服務的入口。官方文件特別強調僅從 GitHub 儲存庫、npm 套件與 GitHub App 等官方管道安裝，第三方轉載與非官方鏡像未經維護與審查，可能包含惡意軟體，反映開源供應鏈安全意識的強化。

![ECC Star 統計徽章與支援平台矩陣（Star 數 242k、Discord 社群、npm 下載量與 Claude Code、Codex、Cursor 等多平台支援清單）](assets/images/posts/github-ecc-news-shot3.png)

## ECC 值得一試嗎？

<!-- AEO Answer Capsule — 約 70 字 -->
對於希望為 AI 代理建立標準化工程流程的團隊，ECC 值得嘗試：其跨平台支援、模組化代理與技能體系、AgentShield 安全掃描與 MIT 授權，構成低成本系統化的工程紀律方案。不過目前仍屬快速迭代階段，生產環境採用前應先以最小配置實測驗證。
<!-- End AEO Capsule -->

對於使用 AI 代理進行日常開發的工程師而言，ECC 提供了將工程紀律系統化的低成本方案。其跨平台支援讓不同代理環境的用戶都能獲得一致的規劃、測試與審查工作流，而技能與代理的模組化設計允許按需組合，避免一次安裝過多冗餘元件。內建的 AgentShield 安全掃描則回應了代理工具普及後日益受到關注的供應鏈與配置安全問題。

從生態發展角度觀察，ECC 在 2026 年 1 月創立後七個月內累積超過 24 萬顆星標，反映開發者社群對代理工程化框架的高度需求。其單一維護者的治理結構既是靈活性的來源，也是長期維護風險的考量點；MIT 授權則確保了專案在維護者變更時仍可被社群承接。對於希望為代理建立標準化工程流程的團隊，ECC 是值得實際安裝評估的選擇。

![ECC README 開頭（項目名稱 ECC、標語「Your agent can write code, but ECC gives it a coordinated engineering system」與 plan-test-implement-review-verify-remember-improve 工作流圖）](assets/images/posts/github-ecc-news-shot1.png)

<div class="ui-stat-grid">
  <div class="ui-stat"><span class="stat-label">Star 數</span><span class="stat-value">241,623</span></div>
  <div class="ui-stat"><span class="stat-label">Fork 數</span><span class="stat-value">36,628</span></div>
  <div class="ui-stat"><span class="stat-label">主要語言</span><span class="stat-value">JavaScript</span></div>
  <div class="ui-stat"><span class="stat-label">授權</span><span class="stat-value">MIT</span></div>
  <div class="ui-stat"><span class="stat-label">創建日期</span><span class="stat-value">2026-01-18</span></div>
  <div class="ui-stat"><span class="stat-label">最新版本</span><span class="stat-value">v2.1.0</span></div>
</div>

## ECC 的資訊來源是什麼？

<!-- AEO Answer Capsule — 約 50 字 -->
本報導資訊來源為 ECC 官方 GitHub 儲存庫 affaan-m/ECC，所有星標數、復刻數與版本資訊均擷取自該儲存庫公開資料，未採用第三方轉載來源。
<!-- End AEO Capsule -->

本報導資訊來源為 ECC 官方 GitHub 儲存庫：[affaan-m/ECC](https://github.com/affaan-m/ECC)。所有星標數、復刻數與版本資訊均擷取自該儲存庫公開資料。

## 總結

ECC 以七個月內累積 24.1 萬顆星標的成績，成為 AI 代理工程化領域最具代表性的開源項目之一。其以「規劃、測試、實作、審查、驗證、記憶、改進」為核心的工程工作流、跨平台適配架構、模組化的代理與技能體系，以及 AgentShield 安全掃描機制，共同構成了將 AI 代理從程式碼生成工具升級為工程團隊成員的完整方案。開源核心與託管服務並行的商業模式，則為該類項目的可持續發展提供了值得參考的樣本。
