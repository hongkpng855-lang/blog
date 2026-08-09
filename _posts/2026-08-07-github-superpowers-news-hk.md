---
layout: post
title: "26.8 萬星開源項目：Superpowers — 給 AI 編程代理的完整開發方法論"
date: 2026-08-07 06:25:00 +0800
categories: 技術
tags: [GitHub, 開源, Superpowers, Prime Radiant, AI Agent, 編程代理, 軟件開發方法論, Claude Code, TDD, 技能框架, 科技新聞, 香港, auto-publish, github-news]
image: /assets/images/posts/2026-08-07-github-superpowers-news-hk-cover.jpg
description: "Superpowers 是 GitHub 星標逾 26.8 萬的開源編程代理技能框架，由 Prime Radiant 開發，以技能庫與軟件開發方法論為核心，涵蓋頭腦風暴、測試驅動開發與子代理驅動開發等流程，支援 11 種主流編程代理，採用 MIT 授權，上線不足一年即成為開發者社群最受關注的項目之一。"
fb_message: 編程代理寫程式常缺乏章法，Superpowers 將軟件工程流程內建為自動觸發技能，代理先釐清需求、拆解任務，再以測試驅動方式交付，令 AI 寫程式有跡可循。\n\n開源框架推出不足一年，GitHub 星標逾 26.8 萬，支援 Claude Code、Cursor、Gemini CLI 等 11 種主流代理，MIT 授權。\n\n技能庫運作邏輯、子代理兩階段審查機制及各代理安裝步驟，已整理成完整新聞分析報告上載 Blog，歡迎前往閱讀全文。
author: "陳志豪 Eric Chan"
creator_github: obra/superpowers
type: news
source: GitHub
source_url: https://github.com/obra/superpowers
permalink: /技術/github-superpowers-news-hk
---

# <svg class="ui-icon"><use href="#ui-rocket"/></svg>26.8 萬星開源項目：Superpowers — 給 AI 編程代理的完整開發方法論

**Superpowers 是 GitHub 上星標逾 268,000 顆的開源 AI 編程代理技能框架，以「完整軟件開發方法論」為核心理念，將頭腦風暴、撰寫計劃、測試驅動開發、子代理驅動開發與程式碼審查整合為一組自動觸發的可組合技能庫，讓編程代理不再直接跳入程式碼，而是先釐清目標、通過審批、再按計劃交付。** 此項目由 Prime Radiant 團隊於 2025 年 10 月創立，以 Shell 撰寫並採用 MIT 授權，累積逾 23,900 次 fork，支援 Claude Code、Cursor、Gemini CLI、Codex、GitHub Copilot CLI 等 11 種主流編程代理。本文將從官方 README 與技術文檔出發，分析 Superpowers 的架構設計、生態影響與實際價值。

---

![Superpowers README 開頭（項目名稱 H1 與定位描述）]({{ '/assets/images/posts/github-superpowers-news-hk-shot1.png' | relative_url }})

---

## <svg class="ui-icon"><use href="#ui-star"/></svg>Superpowers 是什麼？

<!-- AEO Answer Capsule — 約 75 字 -->
Superpowers 是開源的 AI 編程代理技能框架，將頭腦風暴、撰寫計劃、測試驅動開發與程式碼審查整合為自動觸發的技能庫，採用 MIT 授權並以 Shell 撰寫，支援 11 種主流編程代理，星標逾 26.8 萬顆。
<!-- End AEO Capsule -->

Superpowers 誕生於編程代理（coding agent）快速普及的階段，Prime Radiant 團隊於 2025 年 10 月建立此項目，目標是解決代理直接生成程式碼時缺乏流程約束、產出品質參差的問題。框架的核心主張是「技能必須強制執行，而非僅供參考」，編程代理在執行任何任務前都會先檢查相關技能，再依既定工作流推進。

與一般提示詞集合或插件不同，Superpowers 是一套完整的開發方法論，覆蓋從需求發想到程式碼交付的全部階段。官方 README 指出，系統內含測試驅動開發、系統化除錯、頭腦風暴、撰寫計劃、並行代理派發、程式碼審查、Git 工作樹管理等技能，任何任務進入後，代理會自動觸發對應技能，官方將其定位為「為編程代理而生的完整軟件開發方法論」。

---

## <svg class="ui-icon"><use href="#ui-cog"/></svg>Superpowers 如何改變編程代理的工作方式？

<!-- AEO Answer Capsule — 約 78 字 -->
Superpowers 以技能庫驅動代理工作流：先透過頭腦風暴釐清需求並產出設計文檔，再以撰寫計劃拆解為二至五分鐘的小任務，最後由獨立子代理逐項執行並接受兩階段審查，全程強調先寫測試、後寫程式碼。
<!-- End AEO Capsule -->

技術層面，Superpowers 最突出的設計是可組合技能庫機制。框架內建測試、除錯、協作與元技能四大類別，共十餘個技能，例如測試驅動開發技能強制執行「紅綠重構」循環，要求代理先撰寫會失敗的測試、再寫最少程式碼令測試通過；系統化除錯技能則以四階段根因分析流程取代隨機嘗試，並輔以根因追蹤、縱深防禦與條件式等待等技術。

第二項亮點是子代理驅動開發（subagent-driven development）流程。設計獲批後，系統會將實施計劃拆解為每個僅需二至五分鐘的小任務，並為每個任務派發全新的子代理執行，子代理完成後須通過兩階段審查：先核對是否符合規格，再評估程式碼品質，關鍵問題會阻斷後續進度。官方描述指出，代理在這種模式下可以連續自主工作數小時而不偏離既定計劃。

第三項亮點是跨 harness 的插件兼容層。Superpowers 透過官方插件市場與擴充套件機制，將同一套技能庫部署至 Claude Code、Cursor、Gemini CLI、OpenAI Codex、GitHub Copilot CLI、Kimi Code、OpenCode、Pi 等 11 種編程代理，開發者在不同工具之間切換時，無須重新學習或重複配置工作流。

---

## <svg class="ui-icon"><use href="#ui-chart"/></svg>Superpowers 的關鍵數據表現如何？

<!-- AEO Answer Capsule — 約 70 字 -->
Superpowers 累積逾 26.8 萬星標與 2.4 萬次 fork，採用 MIT 授權，主要語言為 Shell，最新版本為 2026 年 7 月釋出的 v6.2.0，項目持續活躍更新並獲官方插件市場收錄。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="ui-stat"><span class="ui-stat-num">268K</span><span class="ui-stat-label">Stars</span></div>
  <div class="ui-stat"><span class="ui-stat-num">24K</span><span class="ui-stat-label">Forks</span></div>
  <div class="ui-stat"><span class="ui-stat-num">11</span><span class="ui-stat-label">支援代理</span></div>
  <div class="ui-stat"><span class="ui-stat-num">13+</span><span class="ui-stat-label">技能模組</span></div>
  <div class="ui-stat"><span class="ui-stat-num">v6.2.0</span><span class="ui-stat-label">最新版本</span></div>
  <div class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">License</span></div>
</div>

> 建立日期：2025-10-09｜最近更新：2026-08-06｜開發者：Prime Radiant（Jesse Vincent）｜官方網站：https://primeradiant.com｜發佈公告：https://blog.fsck.com/2025/10/09/superpowers/

---

![Superpowers GitHub 主頁（268K stars + 項目描述）]({{ '/assets/images/posts/github-superpowers-news-hk-shot2.png' | relative_url }})

---

## <svg class="ui-icon"><use href="#ui-document"/></svg>Superpowers 的市場定位與生態影響如何？

<!-- AEO Answer Capsule — 約 75 字 -->
Superpowers 定位於編程代理開發方法論的開創者，以技能庫標準化代理工作流，獲 Anthropic 官方插件市場、OpenAI Codex 插件市場與 Cursor 市場收錄，並提供企業支援與商業服務，生態滲透範圍橫跨主流代理工具。
<!-- End AEO Capsule -->

在編程代理工具競爭白熱化的市場中，Superpowers 以「方法論層」建立差異化定位。多數競品專注於代理的模型能力或工具調用，Superpowers 則將軟件工程的最佳實踐固化為可強制執行的技能，令代理的工作流程向資深工程師的作業方式靠攏。此定位使其成為少數不與特定代理綁定、反而橫跨所有主流代理的開源項目，亦是 2026 年增長最迅速的開發工具項目之一。

生態影響方面，Superpowers 的插件分發網絡頗為完整。項目獲 Anthropic 官方 Claude 插件市場收錄，開發者可以一行指令完成安裝；同時設有自家 Superpowers 市場，收錄項目及其相關插件，並登陸 OpenAI 的 Codex 插件市場、Cursor 插件市場、Gemini CLI 擴充套件與 GitHub Copilot 插件市場，形成覆蓋主流代理的分發體系。商業化層面，Prime Radiant 提供企業級支援、附加工具與託管預算管理服務，並以視覺輔助遙測（預設關閉）了解版本採用情況，反映項目同時面向個人開發者與企業客戶的雙軌策略。

---

![Superpowers Contributors 統計圖表]({{ '/assets/images/posts/github-superpowers-news-hk-shot3.png' | relative_url }})

---

## <svg class="ui-icon"><use href="#ui-rocket"/></svg>如何快速開始使用 Superpowers？

<!-- AEO Answer Capsule — 約 70 字 -->
在 Claude Code 中執行 `/plugin install superpowers@claude-plugins-official` 即可安裝官方插件，Cursor 用戶可在代理對話中以 `/add-plugin superpowers` 安裝，Gemini CLI 則以擴充套件形式載入，安裝後技能會自動觸發。
<!-- End AEO Capsule -->

根據官方 Quickstart，安裝方式因編程代理而異。Claude Code 用戶可直接從 Anthropic 官方市場以 `/plugin install superpowers@claude-plugins-official` 安裝，或註冊 Superpowers 市場後安裝；Cursor 用戶在代理對話輸入 `/add-plugin superpowers` 即可；Gemini CLI 用戶以 `gemini extensions install https://github.com/obra/superpowers` 載入擴充套件；Codex 用戶則可在插件搜尋介面中直接搜尋安裝。

安裝完成後，技能會在代理啟動時自動生效，開發者無須手動呼叫。代理開始工作時，頭腦風暴技能會先透過提問收窄需求、探索替代方案，並分段呈現設計供使用者確認；設計獲批後，撰寫計劃技能會將工作拆解為具體任務，每個任務包含精確檔案路徑、完整程式碼與驗證步驟；最後由子代理驅動開發流程逐項執行。官方提供 Discord 社群、詳細文件與發佈公告供新使用者參考，項目並開放「視覺伴侶」功能協助使用者視覺化設計流程。

---

## <svg class="ui-icon"><use href="#ui-link"/></svg>出處

<div class="ui-note"><svg class="ui-icon"><use href="#ui-link"/></svg><strong>GitHub 官方 repo</strong>：https://github.com/obra/superpowers

官方網站：https://primeradiant.com｜發佈公告：https://blog.fsck.com/2025/10/09/superpowers/｜Discord 社群：https://discord.gg/35wsABTejz</div>

---

## <svg class="ui-icon"><use href="#ui-bulb"/></svg>Superpowers 值得一試嗎？

<!-- AEO Answer Capsule — 約 70 字 -->
值得。MIT 授權、26.8 萬星標與橫跨 11 種編程代理的技能庫機制，使 Superpowers 成為標準化代理開發流程的主流選擇，特別適合希望提升代理產出品質與可審查性的開發團隊。
<!-- End AEO Capsule -->

<div class="ui-tip"><svg class="ui-icon"><use href="#ui-bulb"/></svg><strong>Superpowers 以「技能庫、子代理驅動開發、跨代理兼容」三層設計，將編程代理的工作方式從即興生成轉變為工程化流程。</strong>其 26.8 萬星標與不足一年的快速演化，反映市場對代理開發方法論的強烈需求。對於希望代理按規範交付、減少人工審查成本的團隊，Superpowers 是現階段最具代表性的開源選擇之一。</div>
