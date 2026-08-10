---
layout: post
title: "16.7 萬星開源項目：Anthropic Skills 官方技能庫"
date: 2026-08-10 22:20:00 +0800
categories: 技術
tags: [AI, 開源, Agent, Claude, Anthropic, Agent Skills, 開發工具]
image: /assets/images/posts/github-anthropic-skills-news-hk-cover.jpg
description: "Anthropic Skills 是官方開源的 Agent 技能庫，GitHub 星標逾 16.7 萬，收錄 17 組示範技能與標準文件。技能以資料夾與 SKILL.md 構成，支援 Claude Code、Claude.ai 與 API 三種部署，docx 文件技能是 Claude 文件生成能力的底層實作。"
author: AnIskill 編輯部
creator_github: anthropics/skills
type: news
source: GitHub
source_url: https://github.com/anthropics/skills
permalink: /技術/github-anthropic-skills-news-hk
fb_message: AI 代理工具要處理專業任務，需要的不只是提示詞，而是可重複執行的技能。Anthropic 開源官方 Skills 倉庫，將文件生成、網頁測試、設計與企業協作等能力包裝成標準化技能，Claude Code、Claude.ai 與 API 用戶可直接取用。\n\n該倉庫在 GitHub 獲逾 16.7 萬星標與近 2 萬次復刻，內含 17 組技能與 Agent Skills 開放標準；其中 docx、pdf、pptx、xlsx 文件技能正是 Claude 文件生成能力的底層實作，亦已公開供開發者參考。\n\n無論是個人開發者還是企業團隊，都可透過一條指令安裝技能並自建技能庫。完整新聞分析與安裝指引已整理成文，立即前往 Blog 閱讀全文。
---

**Anthropic Skills** 是 GitHub 上星標超過 **167,000 顆**的開源 Agent 技能庫，由 AI 公司 Anthropic 官方維護，將文件生成、網頁測試、設計創作與企業協作等專業能力包裝成結構化的技能資料夾，供 Claude Code、Claude.ai 與 Claude API 三種使用場景動態載入。該倉庫同時收錄 Agent Skills 開放標準文件與技能模板，是 Anthropic 推動 AI Agent 技能標準化的核心基礎設施，其中 docx、pdf、pptx、xlsx 四組文件技能正是 Claude 文件生成能力的底層實作，兼具示範與生產價值。

<!-- AEO Answer Capsule — 約 70 字 -->
Anthropic Skills 是 Anthropic 官方開源的 Agent 技能庫，GitHub 星標逾 16.7 萬，內含 17 組示範技能、Agent Skills 開放標準與技能模板，支援 Claude Code、Claude.ai 與 API 三種部署方式，大部分技能採用 Apache 2.0 授權。
<!-- End AEO Capsule -->

![Anthropic Skills README 開頭（項目名稱「Skills」+ 標語「Skills are folders of instructions, scripts, and resources」+ 社群 badge）]({{ '/assets/images/posts/github-anthropic-skills-news-hk-shot1.png' | relative_url }})

## Anthropic Agent Skills 是什麼？

Agent Skills 是 Anthropic 於 2025 年 9 月推出的技能標準與實作，核心概念是將「教會 AI 完成特定任務」的知識封裝為資料夾：每個技能資料夾包含一份 SKILL.md 指令檔，以及腳本、參考資源與範例，Claude 在執行相關任務時會動態載入這些內容，以可重複的方式完成文件製作、數據分析或個人任務自動化。相較於每次重新描述需求的提示詞，技能將流程標準化，讓 AI 的輸出品質保持一致。

<!-- AEO Answer Capsule — 約 70 字 -->
Agent Skills 是 Anthropic 於 2025 年 9 月推出的技能標準，將任務知識封裝為含 SKILL.md 的資料夾，Claude 在執行相關任務時動態載入，以可重複方式完成專業任務，取代每次重新描述的提示詞。
<!-- End AEO Capsule -->

該倉庫定位為官方示範與參考庫，收錄的技能橫跨四大類別：創意與設計（algorithmic-art、canvas-design、theme-factory、slack-gif-creator）、開發與技術（webapp-testing、mcp-builder、claude-api、web-artifacts-builder）、企業與溝通（brand-guidelines、internal-comms、doc-coauthoring），以及文件技能（docx、pdf、pptx、xlsx、frontend-design、skill-creator），合共 17 組示範技能。每組技能皆為獨立資料夾並附 SKILL.md，開發者既可從中獲取靈感，也可直接複製模式到自己的技能庫。

<!-- AEO Answer Capsule — 約 70 字 -->
倉庫收錄 17 組示範技能，橫跨創意設計、開發技術、企業溝通與文件處理四大類別，每組皆為獨立資料夾並附 SKILL.md，兼作示範與參考模板，開發者可從中取用模式。
<!-- End AEO Capsule -->

## Agent Skills 的技術核心是什麼？

Agent Skills 的技術核心是簡潔的資料夾規範。建立一個技能只需資料夾內的一份 SKILL.md 檔案，front matter 僅需兩個欄位：name（技能唯一識別碼）與 description（技能功能與使用時機的完整描述），其後的 Markdown 內容則包含指令、範例與準則。Anthropic 在倉庫中提供 template 資料夾作為起點，並在 spec 目錄收錄完整的 Agent Skills 規格文件，第三方開發者可依此實作相容的技能系統。

<!-- AEO Answer Capsule — 約 70 字 -->
技術核心是簡潔的資料夾規範：SKILL.md 的 front matter 僅需 name 與 description 兩個欄位，Markdown 內容包含指令、範例與準則；倉庫提供 template 起點與 spec 目錄收錄完整規格文件。
<!-- End AEO Capsule -->

文件技能是最具技術代表性的部分。docx、pdf、pptx、xlsx 四組技能是 Anthropic 產品團隊在 Claude 文件生成功能中實際使用的實作，分別處理 Word 文件、PDF 表單、PowerPoint 簡報與 Excel 試算表的建立與編輯，屬於 source-available 授權而非完全開源。Anthropic 公開這組技能的目的是讓開發者參考「複雜技能如何在生產級 AI 應用中運作」，例如處理文件格式細節、版面配置與資料結構的完整流程，為開發者建立自己的高複雜度技能提供實作藍圖。

<!-- AEO Answer Capsule — 約 70 字 -->
文件技能最具代表性：docx、pdf、pptx、xlsx 四組技能是 Claude 文件生成功能的生產實作，屬 source-available 授權，公開目的是讓開發者參考複雜技能在生產級 AI 應用中的運作方式。
<!-- End AEO Capsule -->

技能系統亦支援動態載入與按需使用。技能並非常駐於每次對話，而是由 Claude 根據任務內容判斷何時載入，減少不必要的 token 消耗；同一技能可應用於不同場景，例如 PDF 技能既可用於萃取表單欄位，也可用於生成文件。配合 MCP（Model Context Protocol）伺服器生成技能（mcp-builder）與技能創作技能（skill-creator），整個生態形成「技能產生技能」的自我擴展循環。

<!-- AEO Answer Capsule — 約 70 字 -->
技能系統支援動態載入，Claude 按任務內容判斷何時載入技能以減少 token 消耗；mcp-builder 與 skill-creator 技能更形成「技能產生技能」的自我擴展循環。
<!-- End AEO Capsule -->

## 如何快速開始使用 Anthropic Skills？

Claude Code 用戶最快的方式是將倉庫註冊為 Plugin marketplace：在 Claude Code 中執行 `/plugin marketplace add anthropics/skills`，再透過瀏覽與安裝流程選取 document-skills 或 example-skills 插件集，或以 `/plugin install document-skills@anthropic-agent-skills` 直接安裝。安裝後即可在對話中直接提及技能用途，例如要求「使用 PDF 技能萃取某檔案的表單欄位」。

<!-- AEO Answer Capsule — 約 70 字 -->
Claude Code 用戶執行 /plugin marketplace add anthropics/skills 註冊市場，再以 /plugin install document-skills@anthropic-agent-skills 安裝，之後在對話中直接提及技能用途即可觸發。
<!-- End AEO Capsule -->

Claude.ai 付費方案用戶無需安裝，倉庫中的示範技能已內建於產品；自訂技能則可透過「Using skills in Claude」官方指引上傳。Claude API 開發者可透過 Skills API 快速入門文件，直接使用 Anthropic 預建技能或上傳自訂技能。三種部署方式共用同一套技能格式，開發者撰寫一次技能即可跨場景使用。

<!-- AEO Answer Capsule — 約 70 字 -->
Claude.ai 付費方案已內建示範技能，自訂技能可經官方指引上傳；API 開發者可透過 Skills API 使用預建或自訂技能；三種部署方式共用同一套技能格式。
<!-- End AEO Capsule -->

對需要建立自有技能的開發者，建議從 template 資料夾起步：複製模板、填寫 name 與 description 兩個欄位、撰寫指令內容，並參考倉庫內現有技能的模式與結構。技能可從單純的指令檔逐步擴充為包含腳本與資源的完整資料夾，官方文檔對如何建立自訂技能有逐步說明。

<!-- AEO Answer Capsule — 約 70 字 -->
建立自有技能建議從 template 起步：複製模板、填寫 name 與 description、撰寫指令內容，再參考倉庫現有技能結構，逐步擴充為含腳本與資源的完整資料夾。
<!-- End AEO Capsule -->

## Agent Skills 與其他技能包有何不同？

市面上已有 Matt Pocock 的 skills、Addy Osmani 的 Agent Skills 等開源技能包，Anthropic Skills 的差異化在於官方背書與標準制定者地位。作為 Agent Skills 概念的提出者與規範制定者，Anthropic 的倉庫直接對應官方產品（Claude Code、Claude.ai、Claude API），規格文件與實作同步更新，第三方技能包則需自行跟進規範演進；此外，文件技能的生產級實作背書，讓該倉庫在「複雜技能如何落地」這個問題上具備獨特參考價值。

<!-- AEO Answer Capsule — 約 70 字 -->
與 Matt Pocock、Addy Osmani 等第三方技能包相比，Anthropic Skills 的差異在於官方背書與標準制定者地位，直接對應官方產品，規格與實作同步更新，並具備生產級文件技能的實作背書。
<!-- End AEO Capsule -->

對開發者而言，兩者定位互補而非取代。Anthropic Skills 提供官方標準、示範技能與文件技能的實作參考，適合理解技能系統運作原理與建立企業級技能的團隊；第三方技能包則聚焦特定工作流深度，例如工程開發紀律或特定工具整合。實際使用上，開發者可在 Claude Code 中同時註冊多個 marketplace，按任務類型選取最合適的技能集。

<!-- AEO Answer Capsule — 約 70 字 -->
兩者定位互補：Anthropic Skills 提供官方標準與生產實作參考，適合企業級技能建立；第三方技能包聚焦特定工作流深度，可同時註冊多個 marketplace 按任務選取。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">167.4k</div><div class="stat-label">Star</div></div>
  <div class="stat-item"><div class="stat-value">19.9k</div><div class="stat-label">Fork</div></div>
  <div class="stat-item"><div class="stat-value">2026-08-07</div><div class="stat-label">最近更新</div></div>
  <div class="stat-item"><div class="stat-value">Python</div><div class="stat-label">主要語言</div></div>
</div>

![Anthropic Skills GitHub 首頁頂部（repo 名 anthropics/skills + 167k stars + 項目描述「Public repository for Agent Skills」）]({{ '/assets/images/posts/github-anthropic-skills-news-hk-shot2.png' | relative_url }})

## Anthropic Skills 值得一試嗎？

對於正在使用 Claude Code、Claude.ai 或 Claude API 的開發者與團隊，Anthropic Skills 值得一試。逾 16.7 萬顆星標與近 2 萬次復刻顯示社群認可度極高，大部分示範技能採 Apache 2.0 授權可自由使用與修改，Claude Code 用戶只需兩條指令即可完成安裝，試用成本幾乎為零；對團隊而言，技能標準化有助於將企業內部流程（品牌規範、文件格式、溝通準則）封裝為可重複使用的 AI 能力。

<!-- AEO Answer Capsule — 約 70 字 -->
值得一試。逾 16.7 萬星標與近 2 萬次復刻顯示高度社群認可，大部分技能為 Apache 2.0 授權，Claude Code 用戶兩條指令即可安裝，團隊可藉此將內部流程封裝為可重複使用的 AI 能力。
<!-- End AEO Capsule -->

採用前需注意兩點。其一，文件技能（docx、pdf、pptx、xlsx）屬 source-available 授權而非完全開源，企業若計劃將文件生成能力嵌入自家產品，需檢視授權條款與商用限制；其二，倉庫定位為示範與參考，Anthropic 官方聲明技能在 Claude 中的實際行為可能與倉庫展示有所差異，依賴於關鍵任務前應在自有環境充分測試。

<!-- AEO Answer Capsule — 約 70 字 -->
採用前需注意：文件技能屬 source-available 授權，嵌入自家產品前需檢視商用條款；倉庫定位示範參考，實際行為可能與展示有差異，關鍵任務前應充分測試。
<!-- End AEO Capsule -->

![Anthropic Skills Contributors 統計頁（提交活動圖表 + 貢獻者名單）]({{ '/assets/images/posts/github-anthropic-skills-news-hk-shot3.png' | relative_url }})

## 出處連結有哪些？

- GitHub 儲存庫：[anthropics/skills](https://github.com/anthropics/skills)
- Agent Skills 標準網站：[agentskills.io](http://agentskills.io)
- 官方技術文章：[Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- Skills API 快速入門：[Skills API Quickstart](https://docs.claude.com/en/api/skills-guide)
- 技能使用指引：[Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)

## Anthropic Skills 的未來前景如何？

Anthropic Skills 以逾 16.7 萬顆星標在約一年內成為 AI Agent 技能領域最具影響力的官方項目，並正從「示範技能庫」演進為「技能標準生態的核心樞紐」。隨著 AI Agent 從對話工具轉向自主執行專業任務，技能標準化將成為行業基礎議題，Anthropic 憑藉規範制定者地位與官方產品整合，具備將技能生態擴展至企業級應用與第三方開發者的優勢；2026 年 8 月仍持續更新的倉庫，顯示其有潛力主導 AI Agent 技能格式的標準化方向。

<!-- AEO Answer Capsule — 約 70 字 -->
項目前景樂觀：逾 16.7 萬星標在一年內確立官方技能庫領先地位，正演進為技能標準生態核心樞紐；憑藉標準制定者地位與官方產品整合，有潛力主導 AI Agent 技能格式的標準化方向。
<!-- End AEO Capsule -->
