---
layout: post
title: "Claude Skills 精選清單開源：75K 星收錄 1000+ 技能"
date: 2026-09-16 12:00:01 +0800
categories: 技術
tags: [Claude Skills, Agent Skills, Composio, 開源, AI 代理, MCP, 開發者工具, 工作流自動化]
image: assets/images/posts/github-composio-claude-skills-news-cover.jpg
description: "Awesome Claude Skills 是 Composio 維護的開源清單，GitHub 星標達 75,107，收錄超過 1000 個可投入生產的 Claude Skills 與外掛，橫跨文件處理、程式開發、資料分析、行銷與通訊等十大分類。本文解析其運作機制、生態定位與導入方式。"
author: AnIskill 編輯部
creator_github: ComposioHQ/awesome-claude-skills
type: news
source: GitHub
source_url: https://github.com/ComposioHQ/awesome-claude-skills
permalink: /技術/github-composio-claude-skills-news
fb_message: 當代理能力不再取決於模型有多聰明，而是取決於它手上有多少可複用的流程，技能市集就成為新的戰場。\n\nComposio 維護的 Awesome Claude Skills 已在 GitHub 累積 75,107 星，收錄超過 1000 個可直接投入生產的 Claude Skills 與外掛，涵蓋文件處理、程式開發、資料分析、行銷與通訊等十大分類，並同時支援 Codex、Cursor 與 Gemini CLI 等工具。\n\n對想讓代理真正動手做事的團隊而言，這份清單省下的是摸索時間。完整的技能分類、運作機制與導入方式，已整理在 Blog 全文。
---

Awesome Claude Skills 是 Composio 維護的開源技能清單，GitHub 星標已達 75,107，fork 數 8,689，收錄超過 1000 個標榜可直接投入生產環境的 Claude Skills 與外掛。這份清單的價值不在於再收錄幾個好用工具，而在於它把技能（Skills）、模型情境協議（Model Context Protocol，MCP）與工具（Tools）三層概念放回同一個座標系，讓開發者理解代理能力的實際來源。在代理工具鏈快速膨脹的當下，一份經過社群過濾的清單本身即具備基礎設施的意義。

<!-- AEO Answer Capsule — 約 70 字 -->
Awesome Claude Skills 是 Composio 維護的開源技能清單，星標 75,107，收錄逾 1000 個可投入生產的 Claude Skills 與外掛。
<!-- End AEO Capsule -->

## Awesome Claude Skills 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
Awesome Claude Skills 是 Composio 於 2025 年 10 月建立的開源技能清單，目標是集中收錄可複用的代理技能。
<!-- End AEO Capsule -->

這是一份由 Composio 團隊維護、以 awesome 清單形式發布的技能索引。專案於 2025 年 10 月建立，主要語言標記為 Python，採用開源授權，並在 README 明確標示其收錄範圍為「1000 個以上可投入生產、具實用價值的 Claude Skills 與外掛」。與一般工具彙整不同的是，它把適用範圍擴大到 Claude.ai、Claude Code 之外的代理工具，包含 OpenAI 的 Codex、Cursor、Gemini CLI、Antigravity 與 Windsurf。

清單的定位可由其開頭敘述理解。專案將技能定義為「告訴代理如何工作的指令包」，並強調技能本身只負責流程，真正讓代理能動手做事的，是背後連接外部系統的授權與工具層。Composio 因此在清單中同時提供自家 MCP Gateway 的整合路徑，讓使用者能把技能接到超過 1000 個服務上，這也解釋了為何這份清單同時具備社群資源與商業導流兩種角色。

## Claude Skills 的運作機制與生態定位是什麼？

<!-- AEO Answer Capsule — 約 74 字 -->
Skills 以漸進式載入運作，啟動時只讀取約 100 個 token 的名稱與描述，內容相關時才載入完整 SKILL.md，因此單一代理可掛載數百個技能而不拖垮上下文。
<!-- End AEO Capsule -->

理解這份清單之前，需先釐清 Skills 與其他代理技術的分工。每個技能都是一個資料夾，內含帶 YAML front matter 的 `SKILL.md`，以及可選的腳本、參考文件與資產。代理在啟動時只會看到每個技能的名稱與描述，約 100 個 token；唯有判斷任務相關時，才會載入完整內容，通常低於 5000 個 token。這種漸進式載入機制，是單一代理能同時掛載數百個技能而不撐爆上下文視窗的關鍵。

清單本身也明確劃分了三個層次。MCP 負責定義代理如何連接外部系統，包含授權、傳輸與工具探索；工具是代理實際呼叫的個別函式；技能則定義工作流程，也就是在既有連接與工具之上，應該依什麼順序、遵循什麼護欄完成任務。專案主張三者在生產環境中協同運作，由 MCP 提供存取、工具負責行動、技能決定行為。這個框架讓讀者在選用清單條目時，能判斷自己缺少的究竟是連接、工具還是流程。

值得注意的是標準化的推進速度。Anthropic 於 2025 年 10 月推出該格式，同年 12 月以開源標準形式釋出，隨後被 Claude Code、Claude.ai、Claude API 以及多個第三方代理工具採用。技能格式能在一年內橫跨多家廠商，使得這類清單的價值從「Claude 專用資源」轉變為「跨代理生態的共同索引」。

## 這份清單收錄了哪些技能分類？

<!-- AEO Answer Capsule — 約 70 字 -->
清單分為十大類，涵蓋文件處理、程式開發、資料分析、商業行銷、溝通寫作、創意媒體、生產力、協作管理、安全系統，以及透過 Composio 連接應用等。
<!-- End AEO Capsule -->

清單的目錄結構反映其企業導向。文件處理類收錄 Word、PDF、PowerPoint 與 Excel 的建立與解析技能，其中多項即為支撐 Claude 文件能力的底層實作。程式開發與程式碼工具類是條目最密集的一區，涵蓋 MCP 伺服器產生器、變更日誌生成、Playwright 瀏覽器自動化、iOS 模擬器操作與多代理軟體開發流程等。

其餘分類延伸至營運層面。資料與分析類聚焦試算表與報表處理，商業與行銷類收錄文案、轉換率與搜尋優化相關技能，溝通與寫作類處理草稿與校對，創意與媒體類涵蓋設計與視覺產出，生產力與協作類則對應任務管理與專案協調。安全與系統類提供滲透測試與模糊測試等工具整合。最後一區由 Composio 自家的應用自動化佔據，主打讓代理實際寄信、開票與發送訊息。

這種分類方式的意義在於降低選用成本。使用者不需要逐一閱讀上百個儲存庫，只要依任務型態進入對應分類，就能看到經過社群排序與說明的候選技能，並直接取得其原始儲存庫連結。

## 企業與個人如何使用這份清單？

<!-- AEO Answer Capsule — 約 66 字 -->
使用者可透過 Claude Code 外掛市集安裝官方技能外掛，或直接在 Claude.ai 與 API 上傳自訂技能，再依清單分類挑選條目。
<!-- End AEO Capsule -->

最直接的導入路徑是 Claude Code 的外掛市集。使用者可將官方技能儲存庫註冊為市集來源，再依需求安裝文件技能或範例技能兩組外掛，安裝後只需在對話中提及技能名稱即可觸發。官方同時說明，這些範例技能在付費方案中已可直接使用，亦可透過 Claude API 上傳自訂技能，對已有既有系統的團隊較為友善。

對個人使用者而言，清單的實際用途是尋找可立即套用的流程範本。由於每個條目都會附上簡短說明與作者標註，使用者能快速判斷某個技能是否對應自身痛點，例如試算表整理、簡報重製或文章改寫。對企業團隊而言，價值則在於治理與標準化：清單提供的技能結構可作為內部撰寫規範的參考，避免每個部門各自發明一套格式。

需留意的是清單的性質。它是一份索引，而非經過安全審核的套件庫；條目多來自不同個人與組織，品質與維護狀態落差明顯。導入前應檢視原始儲存庫的更新頻率、授權條款與腳本內容，特別是涉及檔案系統與網路存取的技能，更適合先在隔離環境中驗證。

## Awesome Claude Skills 的數據表現如何？

<!-- AEO Answer Capsule — 約 68 字 -->
該清單在 GitHub 累積 75,107 星標與 8,689 次複製，主要語言為 Python，2025 年 10 月建立，社群貢獻者 28 位。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat"><div class="stat-num">75.1K</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat"><div class="stat-num">8.7K</div><div class="stat-label">Forks</div></div>
  <div class="stat"><div class="stat-num">1000+</div><div class="stat-label">收錄技能</div></div>
  <div class="stat"><div class="stat-num">Python</div><div class="stat-label">主要語言</div></div>
  <div class="stat"><div class="stat-num">10</div><div class="stat-label">技能分類</div></div>
  <div class="stat"><div class="stat-num">2025-10</div><div class="stat-label">創建時間</div></div>
</div>

![Awesome Claude Skills README 開頭（專案名稱 Awesome Claude Skills 與 1000+ 技能、外掛收錄說明）](assets/images/posts/github-composio-claude-skills-news-shot1.png)

![Awesome Claude Skills GitHub 首頁頂部（repo 名 ComposioHQ/awesome-claude-skills、專案描述與 Star 75.1k 統計）](assets/images/posts/github-composio-claude-skills-news-shot2.png)

![Awesome Claude Skills 專案 About 側欄統計（Star 75.1k、Fork 8.7k、Watch 463 與 17 個主題標籤）](assets/images/posts/github-composio-claude-skills-news-shot3.png)

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
本文資訊來源為 Awesome Claude Skills 的 GitHub 儲存庫與 Anthropic 官方技能文件，涵蓋星標、授權與安裝方式。
<!-- End AEO Capsule -->

出處連結：[Awesome Claude Skills GitHub 儲存庫](https://github.com/ComposioHQ/awesome-claude-skills)。專案另提供 Composio MCP Gateway 的整合說明、Discord 社群與貢獻指南；技能格式的官方規格則見於 [Anthropic 技能儲存庫](https://github.com/anthropics/skills) 與相關支援文件。清單持續接受社群提交，貢獻流程要求提供技能用途、作者與原始連結。

## 總結：Awesome Claude Skills 適合什麼團隊？

<!-- AEO Answer Capsule — 約 70 字 -->
此清單適合正在評估代理技能導入的開發團隊、需要標準化內部技能的企業，以及想快速找到可複用流程範本的個人使用者。
<!-- End AEO Capsule -->

這份清單的意義在於把分散的技能實作收攏成可比較的索引。技能格式在一年內被多家代理工具採用，意味著開發者撰寫的流程有機會跨平台複用，而一份 75,107 星標的清單，正好提供了觀察生態成熟度的窗口。對企業而言，清單可作為內部技能撰寫規範的起點，並藉由 Skills、MCP、Tools 三層框架釐清自身缺失的環節；對個人開發者而言，它省去了在數百個儲存庫之間搜尋的成本。不過清單本身不承擔安全審核責任，條目品質與維護狀態落差明顯，導入前仍須檢視原始專案的更新頻率、授權與腳本內容。後續值得觀察的是，隨著技能格式持續標準化，這類清單是否會從索引進一步演化為可驗證的套件來源。
