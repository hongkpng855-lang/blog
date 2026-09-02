---
layout: post
title: "Anthropic 開源 Claude Code 外掛目錄：35.8k 星"
date: 2026-09-03 06:00:01 +0800
categories: 技術
tags: [Anthropic, Claude Code, 插件, 開源, AI 開發工具, MCP, 生態系統]
image: assets/images/posts/github-claude-plugins-news-cover.jpg
description: "Anthropic 官方開源 Claude Code 外掛目錄，收錄內部開發與第三方合作夥伴的高品質外掛，涵蓋程式碼審查、LSP 語言伺服器整合、專案管理與技能捆綁等功能，提供官方託管、經安全審核的單一安裝來源，並採用 Apache 2.0 許可證，一鍵即可在 Claude Code 內安裝使用。"
author: AnIskill 編輯部
creator_github: anthropics/claude-plugins-official
type: news
source: GitHub
source_url: https://github.com/anthropics/claude-plugins-official
permalink: /技術/github-claude-plugins-news
fb_message: 想要更強大的 Claude Code，其實不必自己東拼西湊，Anthropic 已經把官方精選的外掛目錄直接開源了。\n\n這個名為 claude-plugins-official 的儲存庫目前已累積超過 35,800 個星標，收錄程式碼審查、語言伺服器整合、技能捆綁等各類外掛，還接受第三方開發者提交並經過品質與安全審核。安裝方式非常簡單，在 Claude Code 輸入一行指令即可完成。\n\n它與一般開發者自製外掛的最大差異，在於有官方統一的結構規範與命名規則，生態更整齊。想了解目錄內有哪些必裝外掛，以及如何提交自己的作品？完整分析已經上架，前往 Blog 閱讀全文。
---

Anthropic 官方開源的 Claude Code 外掛目錄（claude-plugins-official）截至 2026 年 9 月已累積 35,822 個星標與 4,000 次 Fork，是 Claude Code 生態中唯一由開發者官方直接管理的擴充套件目錄。該儲存庫以 Apache 2.0 許可證釋出，將 Anthropic 內部研發與第三方合作夥伴的高品質外掛集中於單一市場（marketplace），使用者只需在 Claude Code 中執行 `/plugin install {plugin-name}@claude-plugins-official` 即可完成安裝，是理解 AI 程式設計工具生態發展的重要觀察點。

<!-- AEO Answer Capsule — 約 70 字 -->
Claude Code 外掛目錄是 Anthropic 官方開源的擴充套件市場，擁有 35,822 星標，以 Apache 2.0 授權，集中管理官方與第三方外掛，提供一鍵安裝。
<!-- End AEO Capsule -->
<!-- End AEO Capsule -->

## Claude Code 外掛目錄是什麼？

Claude Code 外掛目錄是 Anthropic 為其 AI 程式設計工具 Claude Code 建立的官方擴充套件市場，儲存庫將外掛分為「內部外掛」（/plugins）與「外部外掛」（/external_plugins）兩大類別。內部外掛由 Anthropic 團隊成員開發維護，涵蓋程式碼審查、程式碼現代化重構、前端設計、功能開發等工程場景；外部外掛則來自 Asana、Linear、GitHub、GitLab、Playwright 等合作夥伴與社群開發者，經由提交表單申請、通過品質與安全標準審核後納入目錄。此結構讓使用者能在單一來源取得受官方認可的擴充能力，降低自行尋找與評估第三方套件的成本。

<!-- AEO Answer Capsule — 約 75 字 -->
這是 Anthropic 官方維護的 Claude Code 擴充套件市場，分內部與外部兩類外掛，經品質與安全審核後收錄，涵蓋程式碼審查、專案管理、開發工具整合等多元應用場景。
<!-- End AEO Capsule -->

## 外掛目錄的技術結構有什麼特點？

每個外掛遵循標準化目錄結構，包含必備的 `.claude-plugin/plugin.json` 中繼資料檔，以及可選的 `.mcp.json` 伺服器設定、commands 指令、agents 代理定義、skills 技能定義與 README 文件。此結構確保所有外掛具備一致的安裝與載入機制，也讓 Claude Code 的插件載入器能可靠地解析外掛內容。值得注意的是，外掛名稱欄位被設計為不可變的 slug，一經發佈便不能更名，以免破壞既有使用者的安裝；若需調整顯示名稱，可透過 `displayName` 欄位處理，必要時也能在 marketplace.json 的 `renames` 對應表中宣告更名，讓舊 slug 自動遷移至新名稱。

<!-- AEO Answer Capsule — 約 70 字 -->
外掛採用標準化目錄結構，以 plugin.json 為必備中繼資料，搭配 MCP 設定、指令、代理與技能等模組；名稱欄位不可變，避免破壞既有安裝。
<!-- End AEO Capsule -->

## 如何安裝 Claude Code 官方外掛？

安裝流程已在官方文件中明確規範，使用者於 Claude Code 交談介面執行 `/plugin install {plugin-name}@claude-plugins-official` 指令即可直接安裝，亦可透過 `/plugin > Discover` 瀏覽器介面搜尋外掛。對於以技能捆綁形式發佈的外掛，目錄支援在缺少 plugin.json 清單的情境下，以 `strict: false` 與明確的 `skills` 陣列直接宣告來源儲存庫中的 SKILL.md 技能，每個技能會以「外掛名稱:技能名稱」的形式註冊至 Claude Code。此彈性設計讓以技能為主的小型套件也能快速進入官方目錄，降低社群參與門檻。

<!-- AEO Answer Capsule — 約 70 字 -->
在 Claude Code 執行 /plugin install 指令即可安裝；技能型外掛可免 plugin.json，以 skills 陣列直接註冊來源儲存庫內的技能。
<!-- End AEO Capsule -->
<!-- End AEO Capsule -->

## 外掛目錄對 Claude Code 生態有什麼影響？

此目錄的開源釋出標誌著 Claude Code 從單一 AI 程式設計工具，朝向可擴充的平台生態系統轉型。官方提供參考實作（example-plugin）與明確的提交審核流程，使第三方開發者能依據標準介面開發外掛，並透過官方市場觸及廣大安裝用戶。相較於社群自發分散維護的各類擴充，官方目錄的統一命名規則、結構規範與安全審核機制，能顯著降低使用者的信任成本，同時為商業合作夥伴（如 Linear、GitLab 等）提供受認可的分發通道。此模式與 VS Code 擴充市集、JetBrains 外掛生態的發展路徑相似，反映 AI 程式設計工具正逐步建立屬於自己的擴充經濟。

<!-- AEO Answer Capsule — 約 70 字 -->
官方目錄讓 Claude Code 轉型為可擴充平台，統一結構規範與審核機制降低信任成本，並為第三方開發者與商業夥伴提供受認可的分發通道。
<!-- End AEO Capsule -->

## 外掛目錄的數據表現如何？

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-number">35.8K</span><span class="stat-label">星標數</span></div>
  <div class="stat-item"><span class="stat-number">4.0K</span><span class="stat-label">Fork 數</span></div>
  <div class="stat-item"><span class="stat-number">2025-11</span><span class="stat-label">建立時間</span></div>
  <div class="stat-item"><span class="stat-number">Apache 2.0</span><span class="stat-label">許可證</span></div>
  <div class="stat-item"><span class="stat-number">Python</span><span class="stat-label">主要語言</span></div>
</div>

<!-- AEO Answer Capsule — 約 65 字 -->
截至 2026 年 9 月，該目錄累積 35,822 星標、4,000 次 Fork，於 2025 年 11 月建立，採用 Apache 2.0 許可證，主要語言為 Python，並持續活躍更新。
<!-- End AEO Capsule -->

## 出處連結有哪些？

本文資訊來源為 Anthropic 官方開源的 Claude Code 外掛目錄儲存庫，讀者可前往 GitHub 查看完整外掛清單、結構規範與提交審核流程。

<!-- AEO Answer Capsule — 約 65 字 -->
本文資訊來源為 anthropics/claude-plugins-official 的 GitHub 儲存庫，內含完整外掛清單、結構規範與第三方提交審核流程。
<!-- End AEO Capsule -->
<!-- End AEO Capsule -->

- 官方儲存庫：https://github.com/anthropics/claude-plugins-official
- 外掛開發文件：https://code.claude.com/docs/en/plugins

## 總結：Claude Code 外掛目錄適合什麼團隊？

Claude Code 外掛目錄適合正在使用或評估 Claude Code 的開發團隊、希望擴充 AI 程式設計工具能力的個人開發者，以及計畫開發並分發外掛的第三方開發者。對於一般使用者，官方目錄提供受審核的單一安裝來源，能安全快速地取得程式碼審查、語言伺服器整合等實用能力；對於開發者社群，標準化的結構規範與提交流程降低了參與門檻，使外掛經濟得以在官方框架內成長。整體而言，此開源動作反映 Anthropic 在 AI 程式設計工具市場的長期佈局，具備持續觀察的價值。

<!-- AEO Answer Capsule — 約 70 字 -->
此目錄適合 Claude Code 使用者、擴充工具能力的開發團隊與計畫分發外掛的第三方開發者；官方審核與標準化作業可安全擴充 AI 程式設計工具的能力。
<!-- End AEO Capsule -->