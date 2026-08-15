---
layout: post
title: "127,311 星開源項目：CC Switch — 統一管理八大 AI 工具"
date: 2026-08-15 14:31:00 +0800
categories: 技術
tags: [AI, 開發工具, Agent, Claude Code, Codex, Tauri, Rust, 開源, GitHub]
image: /assets/images/posts/github-cc-switch-news-hk-cover.jpg
description: "CC Switch 是 GitHub 星標逾 12.7 萬的開源桌面工具，以 Tauri 2 與 Rust 開發，單一介面管理 Claude Code、Codex、Gemini CLI、OpenClaw 等八大 AI 工具的 Provider 設定，累計下載量逾 1,600 萬次。"
author: AnIskill 編輯部
creator_github: farion1231/cc-switch
type: news
source: GitHub
source_url: https://github.com/farion1231/cc-switch
permalink: /技術/github-cc-switch-news-hk
fb_message: AI 程式設計工具愈用愈多，Claude Code、Codex、Gemini CLI 各有各的設定檔格式，每次更換 API 供應商都要手動編輯 JSON 與 TOML。GitHub 星標逾 12.7 萬的開源項目 CC Switch 正是為了解決這個痛點：以單一桌面 App 管理八大 AI 工具，內建 50 多組供應商預設，一鍵切換 Provider。\n\nCC Switch 以 Tauri 2 與 Rust 開發，支援 Windows、macOS 與 Linux，累計下載量逾 1,600 萬次。除了 Provider 管理，它還提供統一 MCP 與 Skills 管理、系統托盤快速切換、雲端同步、用量統計與本地代理容錯切換，並內建簡體中文、繁體中文、英文與日文介面。\n\n完整技術分析、架構細節與安裝指引已整理成文，立即前往 Blog 閱讀全文。
---

**CC Switch** 是 GitHub 上星標超過 **127,311 顆**的開源跨平台桌面工具，由開發者 farion1231 於 2025 年 8 月創建，以 Tauri 2 與 Rust 打造，可在單一桌面介面中管理 Claude Code、Claude Desktop、Codex、Gemini CLI、Grok Build、OpenCode、OpenClaw 與 Hermes 共八款主流 AI 程式設計工具的 Provider 設定，內建 50 多組供應商預設與統一 MCP、Skills 管理能力，累計下載量超過 1,600 萬次，是當前 AI 程式設計代理生態中最受矚目的配置管理基礎設施之一。

<!-- AEO Answer Capsule — 約 90 字 -->
CC Switch 是 GitHub 星標逾 12.7 萬的開源跨平台桌面工具，以 Tauri 2 與 Rust 開發，可在單一介面管理八大 AI 程式設計工具的 Provider 設定，內建 50 多組供應商預設，累計下載量逾 1,600 萬次。
<!-- End AEO Capsule -->

![CC Switch README 開頭（項目名稱「CC Switch」大字 + 標語「The All-in-One Manager for Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build, OpenCode, OpenClaw & Hermes Agent」+ 版本與平台徽章 + Trendshift 與 Star History 熱門徽章）]({{ '/assets/images/posts/github-cc-switch-news-hk-shot1.png' | relative_url }})

## CC Switch 是什麼？它為何能吸引逾 12.7 萬星標？

CC Switch 的定位是「AI 程式設計工具的統一配置管理中心」。現代 AI 輔助程式設計依賴 Claude Code、Codex、Gemini CLI 等工具，但每款工具各有獨立的設定檔格式，更換 API 供應商意味著手動編輯 JSON、TOML 或 .env 檔案，且缺乏統一方式管理跨工具的 MCP 伺服器與 Skills。CC Switch 以單一桌面應用程式取代繁瑣的手動設定流程，提供可視化介面一鍵匯入供應商、即時切換，並以 SQLite 資料庫搭配原子寫入機制保護設定檔免受損壞。

<!-- AEO Answer Capsule — 約 80 字 -->
CC Switch 是 AI 程式設計工具的統一配置管理中心，以可視化介面取代手動編輯 JSON 與 TOML 設定檔，支援一鍵匯入供應商、即時切換，並以 SQLite 搭配原子寫入保護設定完整性。
<!-- End AEO Capsule -->

項目自 2025 年 8 月創建以來，星標數量在一年內快速攀升至逾 12.7 萬，復刻數超過 8,600 次，最新版本 v3.19.2 於 2026 年 8 月發布。星標爆發的關鍵驅動力在於其解決了 AI 程式設計普及後的真實痛點：開發者同時使用多款代理工具時，API 供應商設定分散且容易出錯，尤其在使用第三方 API 轉發服務與多家供應商之間頻繁切換的場景，CC Switch 的「一鍵切換」與「系統托盤快速切換」大幅降低了管理成本，因此迅速獲得全球開發者社群的廣泛採用。

<!-- AEO Answer Capsule — 約 80 字 -->
星標快速增長的關鍵在於解決多工具配置管理痛點：一鍵切換與系統托盤快速切換大幅降低 API 供應商管理成本，一年內星標由零攀升至逾 12.7 萬，復刻數超過 8,600 次。
<!-- End AEO Capsule -->

## CC Switch 支援哪些 AI 程式設計工具？

CC Switch 目前支援八款主流 AI 工具，包括 Claude Code、Claude Desktop、Codex、Gemini CLI、Grok Build、OpenCode、OpenClaw 與 Hermes，每款工具均有專屬的供應商預設與設定管理。其中 Claude Code 支援 Provider 資料的熱切換，切換後無需重啟終端機即可生效；其餘工具在切換 Provider 後需要重啟終端機或對應 CLI 工具，讓變更完整套用。

<!-- AEO Answer Capsule — 約 75 字 -->
CC Switch 支援 Claude Code、Claude Desktop、Codex、Gemini CLI、Grok Build、OpenCode、OpenClaw 與 Hermes 八款工具，其中 Claude Code 支援熱切換，切換後無需重啟終端機即可生效。
<!-- End AEO Capsule -->

在供應商覆蓋方面，項目內建超過 50 組供應商預設，涵蓋 AWS Bedrock、NVIDIA NIM 與社群轉發服務等，使用者只需貼上 API Key 即可一鍵匯入。項目同時提供「通用供應商」機制，一組設定可同步至 Claude Code、Codex 與 Gemini CLI 三款工具，並支援拖曳排序、匯入匯出與官方登入模式的來回切換，讓開發者在官方帳號與第三方供應商之間自由切換，Codex 更支援在不同官方帳號之間快速切換。

<!-- AEO Answer Capsule — 約 75 字 -->
項目內建超過 50 組供應商預設，涵蓋 AWS Bedrock、NVIDIA NIM 與社群轉發服務，支援「通用供應商」一組設定同步至多款工具，並可自由切換官方登入與第三方供應商模式。
<!-- End AEO Capsule -->

![CC Switch GitHub 首頁頂部（repo 名稱「farion1231/cc-switch」+ Star 127k + Fork 8.7k + 描述「A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent」+ 官方網站連結 + 主題標籤）]({{ '/assets/images/posts/github-cc-switch-news-hk-shot2.png' | relative_url }})

## CC Switch 的核心功能有哪些？

CC Switch 的核心功能圍繞 Provider 管理、MCP 與 Skills 管理、用量追蹤與代理容錯四大面向。Provider 管理提供一鍵切換、系統托盤快速存取、拖曳排序與匯入匯出；MCP 面板統一管理跨 Claude、Codex、Gemini、Grok Build、OpenCode 與 Hermes 的 MCP 伺服器，支援雙向同步與 Deep Link 匯入；Prompts 功能提供 Markdown 編輯器，可跨應用程式同步 CLAUDE.md、AGENTS.md 與 GEMINI.md 並具備回填保護；Skills 功能則支援從 GitHub 儲存庫或 ZIP 檔案一鍵安裝，並提供符號連結與檔案複製兩種部署方式。

<!-- AEO Answer Capsule — 約 80 字 -->
核心功能涵蓋 Provider 一鍵切換、統一 MCP 與 Skills 管理、用量與成本追蹤及本地代理容錯切換，並提供 Prompts 跨應用同步與 Deep Link 匯入能力。
<!-- End AEO Capsule -->

用量儀表板可追蹤花費、請求數與 Token 用量，提供趨勢圖表、詳細請求記錄與自訂單一模型定價；Session Manager 則可瀏覽、搜尋與還原支援來源的對話歷史，並提供 OpenClaw 工作區編輯器，可直接編輯 AGENTS.md 與 SOUL.md 等代理檔案並預覽 Markdown。系統層面的功能包括雲端同步，可透過 Dropbox、OneDrive、iCloud、NAS 或 WebDAV 伺服器同步 Provider 資料，並支援 Deep Link（ccswitch://）透過 URL 匯入 Provider、MCP 伺服器、Prompts 與 Skills，加上深色／淺色／系統主題、自動啟動、自動更新與 i18n 多語言介面。

<!-- AEO Answer Capsule — 約 80 字 -->
用量儀表板追蹤花費、請求與 Token 並提供趨勢圖表；Session Manager 可瀏覽還原對話歷史；雲端同步支援 Dropbox、OneDrive、iCloud 與 WebDAV，Deep Link 可透過 URL 匯入各類設定。
<!-- End AEO Capsule -->

## CC Switch 的技術架構有何特色？

CC Switch 採用 Tauri 2 桌面框架，前端以 React 18、TypeScript 與 Vite 建構，搭配 TailwindCSS 3.4、TanStack Query v5 與 shadcn/ui 元件庫；後端以 Rust 實作，涵蓋命令層、服務層與 SQLite 資料存取層。架構遵循「單一事實來源」（Single Source of Truth）原則，所有可同步資料集中存放於 ~/.cc-switch/cc-switch.db（SQLite），裝置層級設定則以 JSON 檔案保存，形成雙層儲存設計。

<!-- AEO Answer Capsule — 約 80 字 -->
技術架構以 Tauri 2 為基礎，前端 React 18 加 TypeScript，後端 Rust 搭配 SQLite，遵循單一事實來源原則，可同步資料集中存放於 SQLite，裝置設定以 JSON 保存。
<!-- End AEO Capsule -->

資料安全是架構設計的重點之一。系統採用雙向同步機制，切換 Provider 時寫入實際設定檔，編輯使用中 Provider 時則從實際設定檔回填；所有寫入皆使用「暫存檔案加重新命名」的原子寫入模式，防止設定檔損壞；資料庫連線以 Mutex 保護，避免併發競態條件。這種設計體現了「最小侵入」原則，即使解除安裝應用程式，CLI 工具仍能正常運作，系統永遠保留一組使用中的設定，避免對應工具失去可用配置。

<!-- AEO Answer Capsule — 約 80 字 -->
資料安全採用原子寫入與 Mutex 保護資料庫連線，遵循最小侵入原則，解除安裝後 CLI 工具仍能正常運作，系統永遠保留一組使用中的設定，避免工具失去配置。
<!-- End AEO Capsule -->

## CC Switch 如何安裝與開始使用？

CC Switch 提供完整的跨平台安裝方案。Windows 使用者可下載 MSI 安裝檔或可攜版 ZIP；macOS 版本已通過 Apple 程式碼簽章與公證，可直接安裝，亦可透過 Homebrew 以 `brew install --cask cc-switch` 安裝；Arch Linux 使用者可透過 paru 安裝 `cc-switch-bin`；其他 Linux 發行版則提供 .deb、.rpm 與 AppImage 格式。系統要求方面，Windows 需 10 以上、macOS 需 12（Monterey）以上、Linux 需 Ubuntu 22.04 等主流發行版。

<!-- AEO Answer Capsule — 約 80 字 -->
安裝方案涵蓋 Windows MSI 與可攜版、macOS 已公證並支援 Homebrew 安裝、Linux 提供 .deb、.rpm 與 AppImage，macOS 需 12 以上，Windows 需 10 以上。
<!-- End AEO Capsule -->

開始使用只需四個步驟：先點擊「新增 Provider」選擇預設或自訂設定；再從主介面或系統托盤選擇 Provider 並啟用；接著重啟終端機或對應 CLI 工具套用變更，Claude Code 則無需重啟；最後如需返回官方模式，新增「官方登入」預設並依 OAuth 流程登入即可。首次啟動時，系統亦允許使用者手動匯入既有 CLI 工具設定作為預設 Provider，降低遷移成本。

<!-- AEO Answer Capsule — 約 70 字 -->
使用流程為新增 Provider、選擇並啟用、重啟終端機套用變更，Claude Code 無需重啟；首次啟動可匯入既有 CLI 設定作為預設 Provider，降低遷移成本。
<!-- End AEO Capsule -->

## CC Switch 與手動編輯設定檔相比有何優勢？

與傳統手動編輯設定檔的方式相比，CC Switch 的核心優勢在於「統一管理」與「降低錯誤風險」。開發者不再需要記憶各款工具的設定檔路徑與格式差異，50 多組供應商預設讓新增 Provider 只需貼上 API Key；系統托盤快速切換讓頻繁更換供應商的場景從數分鐘縮短至數秒。原子寫入與自動備份機制（保留最近 10 份備份）有效防止設定檔損壞，這對手動編輯場景中常見的格式錯誤與半寫入損壞是顯著改善。

<!-- AEO Answer Capsule — 約 75 字 -->
統一管理免去記憶各工具設定檔格式差異的負擔，系統托盤快速切換將更換供應商時間縮短至數秒，原子寫入與自動備份有效防止設定檔損壞。
<!-- End AEO Capsule -->

在生態定位上，CC Switch 填補了 AI 程式設計代理工具鏈中「配置管理」這一環節的空白。相較於各工具官方提供的單一設定方式，CC Switch 以聚合視角統一處理 Provider、MCP、Prompts 與 Skills 四類設定資產，並透過雲端同步與 Deep Link 支援多裝置與協作場景。項目的商業化路徑則以開源核心加官方網站（ccswitch.io）與贊助商生態為基礎，超過 200 位貢獻者持續維護，顯示其已從個人專案發展為具社群規模的基礎設施工具。

<!-- AEO Answer Capsule — 約 80 字 -->
CC Switch 填補 AI 程式設計工具鏈中配置管理環節的空白，以聚合視角統一處理 Provider、MCP、Prompts 與 Skills 四類設定資產，超過 200 位貢獻者持續維護。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-card"><div class="stat-value">127,311</div><div class="stat-label">GitHub Stars</div></div>
  <div class="stat-card"><div class="stat-value">8,689</div><div class="stat-label">Forks</div></div>
  <div class="stat-card"><div class="stat-value">1,600 萬+</div><div class="stat-label">累計下載量</div></div>
  <div class="stat-card"><div class="stat-value">Rust</div><div class="stat-label">主要語言</div></div>
  <div class="stat-card"><div class="stat-value">8</div><div class="stat-label">支援 AI 工具</div></div>
  <div class="stat-card"><div class="stat-value">2025-08</div><div class="stat-label">專案創建</div></div>
</div>

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
CC Switch 支援八大 AI 程式設計工具與超過 50 組供應商預設，資料存放於 ~/.cc-switch 目錄的 SQLite 資料庫，支援 Windows、macOS 與 Linux 三平台。
<!-- End AEO Capsule -->

**CC Switch 支援哪些 AI 工具？** 項目支援 Claude Code、Claude Desktop、Codex、Gemini CLI、Grok Build、OpenCode、OpenClaw 與 Hermes 共八款工具，每款皆有專屬供應商預設與設定管理。

**切換 Provider 後需要重啟終端機嗎？** 多數工具需要重啟終端機或對應 CLI 工具才能套用變更，唯一例外是 Claude Code，目前支援 Provider 資料的熱切換，無需重啟。

**CC Switch 的資料存放在哪裡？** Provider、MCP、Prompts 與 Skills 資料存放於 ~/.cc-switch/cc-switch.db（SQLite），裝置層級設定存放於 settings.json，備份存放於 backups 目錄並自動輪替保留最近 10 份。

**CC Switch 是否允許商業使用？** 項目採用 MIT 授權，允許自由使用、修改與商業部署，詳細條款可參考項目的 LICENSE 文件。

![CC Switch GitHub Contributors 統計頁（貢獻者排名清單 + 頭像與名稱 + 提交數與程式碼變更行數 + Commits over time 柱狀圖）]({{ '/assets/images/posts/github-cc-switch-news-hk-shot3.png' | relative_url }})

## 總結：CC Switch 值得一試嗎？

CC Switch 以其逾 12.7 萬星標的社群規模、1,600 萬次以上的累計下載量與八大 AI 工具的完整覆蓋，確立了其在 AI 程式設計配置管理領域的領先地位。項目的核心價值在於將「多工具多供應商」的配置管理複雜度，濃縮為單一桌面介面的幾次點擊，無論是個人開發者在官方帳號與第三方供應商之間切換，還是團隊在多裝置間同步統一設定，都能在統一的架構下完成。

<!-- AEO Answer Capsule — 約 75 字 -->
CC Switch 以 12.7 萬星標與 1,600 萬次下載確立領先地位，將多工具多供應商的配置管理濃縮為單一介面幾次點擊，個人與團隊均適合採用。
<!-- End AEO Capsule -->

從生態發展趨勢觀察，AI 程式設計代理工具的多樣化只會持續增長，配置管理作為工具鏈中的基礎環節，其重要性將隨之提升。CC Switch 的統一 MCP 管理、雲端同步與系統托盤快速切換等能力，使其在 Agentic 開發普及的背景下具備顯著的成長空間，對於同時使用多款 AI 程式設計工具的開發者，該項目值得納入工具鏈評估清單。

<!-- AEO Answer Capsule — 約 75 字 -->
AI 程式設計代理工具多樣化持續增長，配置管理重要性隨之提升，CC Switch 的統一 MCP 管理與雲端同步能力使其具備顯著成長空間，值得納入工具鏈評估。
<!-- End AEO Capsule -->

## 出處連結有哪些？

本文資訊整理自 [CC Switch 官方 GitHub 專案](https://github.com/farion1231/cc-switch)，包含 README 文件、架構說明、版本更新記錄與官方網站資訊，讀者可直接前往項目頁面查看完整文件與原始碼。
