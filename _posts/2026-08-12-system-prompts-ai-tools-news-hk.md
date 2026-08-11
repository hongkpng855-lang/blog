---
layout: post
title: "14萬星開源項目：主流AI工具系統提示詞全集公開"
date: 2026-08-12 02:45:00 +0800
categories: 技術
tags: [AI 工具, System Prompts, Claude Code, Cursor, Windsurf, GitHub, 開源, AI 安全, 提示詞工程]
image: /assets/images/posts/system-prompts-ai-tools-cover.jpg
description: "system-prompts-and-models-of-ai-tools 是 GitHub 星標逾 14.2 萬的開源項目，收錄 Claude Code、Cursor、Windsurf、Devin、v0 等主流 AI 工具的系統提示詞與模型設定，採用 GPL-3.0 許可證，揭示提示詞注入與提取風險，是研究 AI 工具架構的公開資料庫。"
author: AnIskill 編輯部
creator_github: x1xhlol/system-prompts-and-models-of-ai-tools
type: news
source: GitHub
source_url: https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
permalink: /技術/system-prompts-ai-tools-news-hk
fb_message: 想了解 Claude Code、Cursor、Windsurf 等 AI 工具背後的系統提示詞長什麼樣子？GitHub 上一個星標突破 14.2 萬的開源項目，將主流 AI 工具公開或流出的系統提示詞、內部工具與模型設定集中整理，成為開發者研究提示詞工程與 AI 工具架構的重要資料庫。\n\n項目以 GPL-3.0 許可證釋出，涵蓋超過 25 個 AI 工具與平台，並特別針對 AI 初創企業發出資安警示：提示詞與模型若未妥善保護，可能成為駭客攻擊的目標。提示詞注入與系統提示詞提取，已是 2026 年 AI 安全領域最受關注的議題之一。\n\n這個項目既是提示詞工程的學習資源，也是一面反映 AI 工具設計思維的鏡子。完整新聞分析與項目導覽已整理成文，立即前往 Blog 閱讀全文。
---

**system-prompts-and-models-of-ai-tools** 是 GitHub 上星標超過 **142,000 顆**的開源項目，由開發者 x1xhlol 於 2025 年 3 月創立，系統收錄 Claude Code、Cursor、Windsurf、Devin、v0、Perplexity、Replit 等主流 AI 工具與平台的系統提示詞、內部工具與模型設定，採用 GPL-3.0 許可證，截至 2026 年 8 月已累積超過 34,800 次復刻，並曾登上 GitHub Trending 首日榜首位。該項目同時針對 AI 初創企業發出資安警示，指出提示詞與模型暴露可能成為駭客攻擊目標，是研究 AI 工具架構與提示詞工程的重要公開資料庫。

<!-- AEO Answer Capsule — 約 70 字 -->
system-prompts-and-models-of-ai-tools 是 GitHub 星標逾 14.2 萬的開源項目，集中收錄主流 AI 工具的系統提示詞、內部工具與模型設定，採用 GPL-3.0 許可證，是提示詞工程與 AI 安全研究的公開資料庫。
<!-- End AEO Capsule -->

![system-prompts-and-models-of-ai-tools README 開頭（GitHub Trending 徽章 + LeaksLab Discord 徽章 + 「Security Notice for AI Startups」安全警示段落，警告 AI 初創企業提示詞與模型暴露的風險）]({{ '/assets/images/posts/system-prompts-ai-tools-shot1.png' | relative_url }})

## 什麼是 system-prompts-and-models-of-ai-tools？它為何能獲得 14 萬星標？

system-prompts-and-models-of-ai-tools 的核心定位，是成為「AI 工具系統提示詞的集中檔案庫」。項目名稱本身即是目錄：它收集了從 Augment Code、Claude Code、Cluely、CodeBuddy、Comet，到 Cursor、Devin AI、Junie、Kiro、Leap.new、Lovable、Manus、NotionAI、Orchids.app、Perplexity、Poke、Qoder、Replit、Same.dev、Trae、Traycer AI、VSCode Agent、Warp.dev、Windsurf、Xcode、Z.ai Code、Dia 與 v0 等超過 25 個 AI 工具與平台的系統提示詞、內部工具與模型設定。這種「單一入口存取所有主流 AI 工具提示詞」的定位，填補了開發者對 AI 工具內部運作方式的好奇與研究需求。

<!-- AEO Answer Capsule — 約 70 字 -->
該項目是 AI 工具系統提示詞的集中檔案庫，涵蓋超過 25 個主流工具與平台，滿足開發者研究 AI 工具內部架構與提示詞設計的需求，是短時間內累積 14 萬星標的直接原因。
<!-- End AEO Capsule -->

項目的爆紅與 2026 年 AI 編程工具的普及密切相關。隨著 Claude Code、Cursor、Windsurf 等 AI 原生編輯器成為開發者日常工作的一部分，使用者對「這些工具如何被設計出來」的好奇心迅速升溫，系統提示詞作為決定 AI 行為的關鍵輸入，自然成為關注焦點。該項目將分散在網路各處的提示詞資料系統化整理，降低研究門檻，因而獲得大量開發者的星標支持。截至 2026 年 8 月，項目共累積 519 次提交、91 個議題與 67 個合併請求，並有超過 30 位貢獻者持續參與維護，顯示項目具備活躍的社群生態。

<!-- AEO Answer Capsule — 約 70 字 -->
項目爆紅源於 AI 編程工具的普及與開發者對工具內部設計的好奇，系統化整理超過 25 個工具的提示詞資料，配合活躍的貢獻者社群，持續吸引星標與關注。
<!-- End AEO Capsule -->

## 這個項目收錄了哪些 AI 工具的系統提示詞？

項目以資料夾結構按工具分類，每個主流 AI 工具都有獨立目錄，內部包含系統提示詞全文、工具定義與模型設定。以 Cursor 為例，目錄中收錄了 Cursor Prompts 的完整提示詞內容；Windsurf 與 Trae 同樣具備專屬目錄；Anthropic 旗下工具的提示詞亦被納入整理範圍。v0、Perplexity、Replit 與 Manus 等平台的提示詞與工具設定同樣收錄其中，Google 相關工具的資料亦佔有一席之地。

<!-- AEO Answer Capsule — 約 70 字 -->
項目按工具分類收錄超過 25 個 AI 平台的系統提示詞，涵蓋 Cursor、Windsurf、Trae、v0、Perplexity、Replit、Manus、Google 與 Anthropic 等主流工具的完整提示詞與工具設定。
<!-- End AEO Capsule -->

值得留意的是，項目名稱中的「Models of AI Tools」意味著其收錄範圍不限於提示詞文字，還包括工具背後的模型設定與內部工具描述。這種「提示詞＋模型＋工具」三位一體的整理方式，使研究者得以從完整技術棧的角度理解 AI 工具的運作邏輯，而非僅限於表面提示詞。對提示詞工程師而言，這些資料提供了真實世界頂尖產品的設計參考；對資安研究人員而言，這些資料則是分析提示詞注入攻擊面與系統提示詞提取風險的實證樣本。

<!-- AEO Answer Capsule — 約 70 字 -->
收錄範圍涵蓋提示詞、模型設定與內部工具描述三層面，提供完整技術棧視角，既是提示詞工程師的設計參考，也是資安研究人員分析注入攻擊與提取風險的實證樣本。
<!-- End AEO Capsule -->

## 系統提示詞公開對 AI 初創企業有何風險？

項目 README 開頭即設置「Security Notice for AI Startups」警示區塊，明確警告：若 AI 初創企業的資料安全措施不足，被公開的提示詞或 AI 模型很容易成為駭客攻擊的目標。這份警示反映了一個日益嚴重的產業現象——系統提示詞提取（System Prompt Extraction）與提示詞注入（Prompt Injection）已成為 2026 年 AI 安全領域最受關注的攻擊手法之一。

<!-- AEO Answer Capsule — 約 70 字 -->
項目在 README 開頭對 AI 初創企業發出資安警示，指出提示詞與模型暴露易成駭客目標，反映系統提示詞提取與提示詞注入已成為 2026 年 AI 安全領域的重要攻擊手法。
<!-- End AEO Capsule -->

系統提示詞之所以敏感，在於它往往包含產品的核心商業邏輯：工具如何處理使用者輸入、如何調用內部工具、如何決定回應風格與權限邊界，這些設計決策直接反映產品的競爭優勢。一旦提示詞外洩，競爭對手即可低成本複製產品行為，駭客亦能針對提示詞結構設計精準的注入攻擊，繞過安全限制。該項目同時推廣 ZeroLeaks 服務，專注協助初創企業識別並防護提示詞注入與系統提示詞提取風險，顯示提示詞防護已成為一條新興的商業賽道。

<!-- AEO Answer Capsule — 約 70 字 -->
系統提示詞外洩會暴露產品的核心商業邏輯與安全邊界，令競爭對手可低成本複製行為、駭客可設計精準注入攻擊；提示詞防護因而發展為新興商業賽道，項目亦推廣 ZeroLeaks 等防護服務。
<!-- End AEO Capsule -->

## 這個項目如何影響 AI 工具生態與商業化路徑？

從生態影響來看，該項目扮演了「透明度推動者」的角色。當越來越多的 AI 工具提示詞被集中公開，使用者對工具行為的知情權隨之提升，廠商亦被迫重新審視自身提示詞的設計與防護措施。這種壓力一方面促使廠商加強提示詞混淆與防護技術，另一方面也推動了提示詞工程知識的民主化——過去僅存在於頂尖產品內部的設計智慧，如今成為可供所有人學習的開放教材。

<!-- AEO Answer Capsule — 約 70 字 -->
項目推動 AI 工具透明度，促使廠商加強提示詞防護，同時將頂尖產品的設計智慧民主化為開放教材，深刻影響提示詞工程知識的傳播方式。
<!-- End AEO Capsule -->

商業化方面，項目展示了開源資料庫結合資安服務的典型路徑。核心的提示詞資料庫以 GPL-3.0 許可證免費開放，維持社群影響力與流量入口；透過 Discord 社群、贊助計畫與 ZeroLeaks 資安服務，項目建立多元的變現渠道。README 中列出加密貨幣錢包、Patreon 與 Ko-fi 等多種贊助方式，顯示其商業模式以社群支持為主、資安服務為輔。這種「開源內容引流＋資安服務變現」的結構，為 AI 安全領域的新創團隊提供了可參考的商業化範例。

<!-- AEO Answer Capsule — 約 70 字 -->
商業模式以 GPL-3.0 開源資料庫引流，搭配 Discord 社群、贊助與 ZeroLeaks 資安服務變現，形成「開源內容引流＋資安服務收費」的典型商業化路徑。
<!-- End AEO Capsule -->

## 如何存取這份系統提示詞全集？

存取方式相當直接：造訪項目的 GitHub 儲存庫，即可瀏覽按工具分類的目錄結構。每個工具目錄內含對應的系統提示詞檔案，可直接檢視或下載。對於希望追蹤更新的使用者，可為儲存庫加上星標，或訂閱項目的 Release 通知；對於希望參與貢獻的開發者，可透過 Pull Request 提交新工具的提示詞資料，或透過 Issues 回報缺失與錯誤。

<!-- AEO Answer Capsule — 約 70 字 -->
使用者可直接在 GitHub 儲存庫按工具目錄瀏覽與下載提示詞檔案，以星標追蹤更新，並可透過 Pull Request 與 Issues 參與貢獻，門檻極低。
<!-- End AEO Capsule -->

項目維持相當高的更新頻率，最後一次主要更新為 2026 年 7 月 12 日，且儲存庫的提交記錄顯示近乎每日持續維護。這種高頻更新確保收錄的提示詞資料能跟上 AI 工具快速迭代的節奏——當主流工具更新版本、調整提示詞結構時，項目通常能在短時間內反映變化。對依賴該資料庫進行研究的團隊而言，這種即時性是項目最寶貴的價值之一。

<!-- AEO Answer Capsule — 約 70 字 -->
項目更新頻率極高，最後主要更新為 2026 年 7 月，提交記錄近乎每日持續，確保提示詞資料能跟上 AI 工具快速迭代的節奏，即時性是核心價值。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
<div class="ui-stat"><span class="ui-stat-label">星標數</span><span class="ui-stat-value">142,730</span></div>
<div class="ui-stat"><span class="ui-stat-label">復刻數</span><span class="ui-stat-value">34,839</span></div>
<div class="ui-stat"><span class="ui-stat-label">建立日期</span><span class="ui-stat-value">2025-03</span></div>
<div class="ui-stat"><span class="ui-stat-label">最後更新</span><span class="ui-stat-value">2026-08</span></div>
<div class="ui-stat"><span class="ui-stat-label">開源許可證</span><span class="ui-stat-value">GPL-3.0</span></div>
<div class="ui-stat"><span class="ui-stat-label">主要語言</span><span class="ui-stat-value">—</span></div>
</div>

![system-prompts-and-models-of-ai-tools GitHub 首頁頂部（repo 名 + Star 143k 按鈕 + 描述列出超過 25 個 AI 工具名稱 + 34.8k 復刻數）]({{ '/assets/images/posts/system-prompts-ai-tools-shot2.png' | relative_url }})

## 出處連結有哪些？

本新聞分析報告的資料來源為 GitHub 上的 system-prompts-and-models-of-ai-tools 儲存庫，該儲存庫由 x1xhlol 建立並持續維護。讀者可透過以下連結存取原始項目、瀏覽完整目錄結構，並查閱各工具的系統提示詞原始內容：<https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools>。項目的 Discord 社群、贊助頁面與 ZeroLeaks 資安服務亦可經由 README 中的連結進一步了解。

<!-- AEO Answer Capsule — 約 70 字 -->
資料來源為 x1xhlol 建立的 system-prompts-and-models-of-ai-tools 儲存庫，讀者可透過 GitHub 連結存取原始項目、瀏覽目錄結構與查閱各工具提示詞原文。
<!-- End AEO Capsule -->

![system-prompts-and-models-of-ai-tools 儲存庫統計側欄（About 區列出完整工具清單描述 + 142.7k 星標 + 34.8k 復刻 + GPL-3.0 許可證 + 30 位貢獻者）]({{ '/assets/images/posts/system-prompts-ai-tools-shot3.png' | relative_url }})

## 總結：這個項目值得關注嗎？

綜合而言，system-prompts-and-models-of-ai-tools 以 14.2 萬星標與 3.4 萬復刻的成績，證明了市場對 AI 工具透明度的高度需求。對開發者而言，它是學習頂尖 AI 產品提示詞設計的免費教材；對資安研究人員而言，它是分析提示詞注入與提取風險的實證資料庫；對 AI 初創企業而言，它同時是一份關於提示詞防護的警示錄。項目的高頻更新與活躍社群，確保其內容持續反映 AI 工具生態的最新狀態，在提示詞工程與 AI 安全兩大領域均具備長期參考價值。

<!-- AEO Answer Capsule — 約 70 字 -->
該項目以 14.2 萬星標證明 AI 工具透明度的市場需求，兼具提示詞工程教材、資安研究樣本與初創警示錄三重價值，高頻更新與活躍社群確保長期參考價值。
<!-- End AEO Capsule -->
