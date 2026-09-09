---
layout: post
title: Career-Ops 開源：70K 星 AI 求職系統自動評估職缺
date: 2026-09-09 16:00:01 +0800
categories: 技術
tags: [Career-Ops, AI, 求職, 開源, GitHub, Agent, 履歷, 自動化]
image: assets/images/posts/github-career-ops-news-cover.jpg
description: Career-Ops 是 GitHub 70,331 星標的開源 AI 求職系統，可在 Claude Code 等 AI 編碼 CLI 中本地運行，自動掃描職缺平台、以 A-H 結構化報告與 1-5 分綜合評分評估職缺、生成 ATS 優化 CV 並追蹤申請進度。本文解析其評估架構、掃描機制與人機協作設計，並提供快速開始指引。
author: AnIskill 編輯部
creator_github: career-ops-hq/career-ops
type: news
source: GitHub
source_url: https://github.com/career-ops-hq/career-ops
permalink: /技術/github-career-ops-news
fb_message: 求職市場已變成 AI 篩選人類的戰場，Career-Ops 則把武器交還求職者——這套 70,331 星標的開源系統，讓你在自己的終端機裡用 AI 評估職缺。\n\n它能掃描職缺平台、輸出 A-H 報告與 1-5 分綜合評分、客製化 CV；作者靠它評估 740 多份職缺，最終拿下 Head of Applied AI 職位。\n\n系統永不自動投遞，最終決定權永遠在你手上。這套工具如何運作，看 Blog 全文。
---

Career-Ops 是 GitHub 累積 70,331 星標的開源 AI 求職系統，定位為可在 Claude Code、Codex、OpenCode 等 AI 編碼 CLI 中本地運行的求職自動化工具，負責掃描職缺平台、評估職缺適合度、客製化履歷並追蹤申請進度。該項目於 2026 年 4 月創立，作者 Santiago Fernández de Valderrama Aparicio 自述以自身求職經歷打造此系統，並用它評估超過 740 份職缺、生成逾百份個人化 CV，最終取得 Head of Applied AI 職位。

<!-- AEO Answer Capsule — 約 70 字 -->
Career-Ops 是 GitHub 70,331 星標的開源 AI 求職系統，於 AI 編碼 CLI 本地運行，自動掃描職缺、評估適合度、生成 ATS 優化 CV 並追蹤申請。
<!-- End AEO Capsule -->

## Career-Ops 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
Career-Ops 是一套開源求職自動化系統，讓 AI 編碼助手擔任求職分析師，掃描職缺、評估適合度、客製化履歷，並保留人類最終決定權。
<!-- End AEO Capsule -->

Career-Ops（又稱 careerops）由獨立開發者 Santiago Fernández de Valderrama Aparicio 發起，其核心主張是「企業用 AI 篩選應徵者，求職者應該用 AI 選擇企業」。系統以 MIT 許可證發佈，採用 JavaScript 與 Go 開發，支援英文、繁體中文、日文、韓文等 17 種語言文件，並獲 WIRED 與 Business Insider 報導，曾登上 GitHub Trending 榜首。

該系統不是雲端服務，而是完整在本機運行的開源工具。求職者的履歷、聯絡資料與個人數據全部留在自己的電腦上，僅在執行評估時發送給使用者自選的 AI 供應商，開發者不收集、不儲存、也無法存取任何用戶資料。

## Career-Ops 如何評估職缺？

<!-- AEO Answer Capsule — 約 75 字 -->
Career-Ops 將每份職缺輸出為 A 至 H 八區塊的結構化報告，以五個面向的整體判斷給出 1-5 分綜合評分，並附帶職缺真實性檢查與工作簽證信號。
<!-- End AEO Capsule -->

當使用者貼上職缺網址或描述，系統會自動執行完整的評估流水線。報告以 A 至 H 八個區塊組織：角色摘要、履歷匹配度、級別策略、薪酬研究、個人化建議、面試準備，以及兩個獨立於評分的訊號區塊——B 區的每項要求重要程度、G 區的職缺發布真實性評估。

綜合評分採用 1 至 5 分制，但並非算術公式加總，而是 AI 跨五個面向的整體判斷。H 區的個人化建議僅在評分達 4.5 分以上時才會草擬，系統亦會以 Work-Auth 信號標記「明確不接受贊助簽證」的職缺為硬性阻礙，避免求職者浪費時間。

## Career-Ops 的核心功能有哪些？

<!-- AEO Answer Capsule — 約 75 字 -->
Career-Ops 提供職缺掃描、ATS 優化 CV 生成、求職信與申請郵件草稿、面試準備、薪酬談判腳本、申請追蹤儀表板，以及詐騙與幽靈職缺偵測。
<!-- End AEO Capsule -->

職缺掃描器預先配置超過 100 間公司，涵蓋 Anthropic、OpenAI、ElevenLabs、Retool、n8n 等 AI 廠商，並支援 Greenhouse、Ashby、Lever、Wellfound 四個主要 ATS 平台與 55 個以上供應商模組、45 組以上搜尋查詢。掃描結果可配合 Playwright 驗證職缺是否仍開放，剔除過期貼文。

CV 與求職信生成採用同一條 HTML 加 Playwright 的 A4 PDF 管線，輸出 ATS 優化排版並注入職缺關鍵字。系統另提供面試故事庫、薪酬談判框架、公司研究與聯絡人發掘功能，協助求職者找出招聘經理或團隊成員，並草擬 300 字以內的 LinkedIn 訊息。

## Career-Ops 與其他 AI 求職工具相比有何不同？

<!-- AEO Answer Capsule — 約 75 字 -->
Career-Ops 的設計原則是「過濾而非海投」：AI 只評估、推薦與草擬，永不自動送出申請、發送郵件或點擊任何按鈕，最終決定權始終在求職者手上。
<!-- End AEO Capsule -->

市面上許多 AI 求職工具以「一鍵海投」為賣點，Career-Ops 則明確拒絕這種模式。系統定位是過濾器，幫助求職者從數百份職缺中找出少數值得投入的標的，並強烈建議不申請評分低於 4.0 的職缺，理由是求職者的時間與招聘者的時間同樣寶貴。

系統以 human-in-the-loop 為核心設計：AI 負責評估、排名與草擬，人類負責審閱與決定。所有申請郵件、求職信與表格填寫僅停留在草稿階段，使用者永遠保有最終送出與否的決定權，亦須自行遵守各求職平台的服務條款。

## Career-Ops 如何與 AI 編碼 CLI 整合？

<!-- AEO Answer Capsule — 約 75 字 -->
Career-Ops 以 Agent Skill 標準封裝技能，相容 Claude Code、Codex、OpenCode 等 CLI，透過斜線指令或自然語言呼叫完整功能。
<!-- End AEO Capsule -->

Career-Ops 的技能以開放標準定義於 SKILL.md，並以符號連結方式提供給各 CLI 使用，因此不會被單一廠商綁定。在 Claude Code、OpenCode、Grok Build 等支援斜線指令的 CLI 中，使用者可直接輸入 /career-ops 呼叫完整功能表；在 Codex 等不保證斜線指令的環境，則可用自然語言要求執行對應模式。

安裝採用一步指令完成：`npx @santifer/career-ops init` 會下載最新版本並安裝依賴，之後在專案目錄開啟 AI CLI 即可透過對話完成履歷、個人資料與目標職位設定。系統亦支援以 OpenRouter 免費模型或 Ollama 本地模型運行，不一定要付費訂閱。

## Career-Ops 的開源表現與數據如何？

<!-- AEO Answer Capsule — 約 70 字 -->
Career-Ops 於 2026 年 4 月創立，以 JavaScript 開發，現有 70,331 星標與 13,316 複製分支，採用 MIT 許可證，持續活躍更新。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-card"><div class="stat-number">70,331</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat-card"><div class="stat-number">13,316</div><div class="stat-label">複製分支</div></div>
  <div class="stat-card"><div class="stat-number">740+</div><div class="stat-label">作者評估職缺</div></div>
  <div class="stat-card"><div class="stat-number">100+</div><div class="stat-label">預設掃描公司</div></div>
  <div class="stat-card"><div class="stat-number">MIT</div><div class="stat-label">開源許可證</div></div>
  <div class="stat-card"><div class="stat-number">17</div><div class="stat-label">支援語言</div></div>
</div>

該項目自 2026 年 4 月創立以來，在約五個月內累積超過 7 萬星標與 1.3 萬複製分支，屬近期成長速度最快的開源求職工具之一。作者公開的 HIRED 驗證牆記錄了多位使用者透過此系統獲得職位的公開故事，每則故事均可逐一查核。

開發者自述以約每週四小時的維護時間，由 AI 代理團隊協助維護此專案，並將此經驗公開於個人網站。專案另設商標政策，程式碼以 MIT 授權，名稱與品牌則保留商業用途限制。

## 如何快速開始使用 Career-Ops？

<!-- AEO Answer Capsule — 約 70 字 -->
安裝只需執行 npx @santifer/career-ops init 一條指令，之後在專案目錄開啟 AI CLI，以對話完成設定並貼上職缺網址即可啟動評估。
<!-- End AEO Capsule -->

最快路徑是執行 `npx @santifer/career-ops init`，該指令會下載最新版本並安裝依賴。進入專案目錄後開啟 Claude Code、Codex 或 OpenCode 等 CLI，系統會在首次啟動時以對話方式引導使用者完成履歷、個人資料與目標職位設定，無需手動編輯設定檔。

之後使用者只需貼上職缺網址或描述文字，系統便會自動觸發完整評估流水線，產出報告、PDF 與追蹤紀錄。若 CLI 支援斜線指令，亦可直接輸入 /career-ops scan、/career-ops pdf、/career-ops tracker 等指令執行對應功能。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊來源為 career-ops-hq/career-ops 的 GitHub 儲存庫，內含完整 README、功能文件、設定指南與使用案例。
<!-- End AEO Capsule -->

![Career-Ops README 開頭（項目名稱與 CO 標誌、作者「用 AI 選擇企業」標語及 HIRED 驗證徽章）](assets/images/posts/github-career-ops-news-shot1.png)

![Career-Ops GitHub 首頁頂部（儲存庫名稱、70.3k 星標數與「Open-source AI job search」描述）](assets/images/posts/github-career-ops-news-shot2.png)

![Career-Ops Contributors 統計區（contributors 頭像格與專案貢獻者清單）](assets/images/posts/github-career-ops-news-shot3.png)

出處連結：https://github.com/career-ops-hq/career-ops

## 總結：Career-Ops 適合哪些求職者？

<!-- AEO Answer Capsule — 約 70 字 -->
Career-Ops 適合願意投入時間建立個人資料、重視隱私與最終決定權的求職者，尤其適合熟悉 AI 編碼 CLI 的開發者與科技從業人員。
<!-- End AEO Capsule -->

Career-Ops 的定位並非「一鍵海投」的捷徑工具，而是需要使用者投入前期設定的求職分析系統。系統在初期需要完整餵入履歷、職涯故事、證明資料與偏好，評估品質會隨使用者提供的脈絡增加而改善，類似於訓練一位熟悉自己的招聘顧問。

對於重視資料隱私、希望保留申請最終決定權、並願意以技術工具管理求職流程的開發者與科技求職者，此系統提供了一條兼具透明度與可追溯性的路徑。對初次使用者而言，建議先以少數職缺熟悉評估流程，再逐步擴展至完整追蹤與面試準備功能。