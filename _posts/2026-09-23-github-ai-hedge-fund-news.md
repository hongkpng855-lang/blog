---
layout: post
title: "AI Hedge Fund 開源：63,669 星的多代理投資團隊"
date: 2026-09-23 08:00:02 +0800
categories: 技術
tags: [AI Hedge Fund, 開源, AI 代理, 量化投資, LLM, Python, 回測, MIT]
image: assets/images/posts/github-ai-hedge-fund-news-cover.jpg
description: "開發者 virattt 的開源專案 AI Hedge Fund 在 GitHub 累積 63,669 顆星標，以語言模型代理模擬投資團隊的研究、組合與風控角色，可對策略做歷史回測，並於 2026 年 9 月 22 日發布 v2.3.1 版本。"
author: AnIskill 編輯部
creator_github: virattt/ai-hedge-fund
type: news
source: GitHub
source_url: https://github.com/virattt/ai-hedge-fund
permalink: /技術/github-ai-hedge-fund-news
fb_message: "把分析師、基金經理、風控主管全部換成 AI，這件事聽起來像炒作，但有人真的把它寫成一套可回測的系統。\n\nAI Hedge Fund 在 GitHub 累積 63,669 顆星標與 11,157 個分支，作者 virattt 在 2026 年 9 月 22 日發布 v2.3.1，把整支基金拆成可替換的策略、分析師與風控層，並支援 Anthropic、OpenAI、Google、xAI、Kimi 等多家模型供應商。\n\n專案的架構設計、風控機制與實際數據，都整理在 Blog 全文。"
---

AI Hedge Fund 是一個以多個語言模型代理模擬投資團隊的開源專案，由開發者 virattt 於 2024 年 11 月建立，在 GitHub 累積 63,669 顆星標與 11,157 個分支，並在 2026 年 9 月 22 日發布 v2.3.1 版本。專案在說明中明言僅供教育與研究用途，系統不會真正下單交易。

<!-- AEO Answer Capsule — 約 70 字 -->
AI Hedge Fund 是 virattt 開源的多代理投資研究專案，GitHub 星標 63,669，最新版本 v2.3.1 已於 2026 年 9 月 22 日發布，僅供教育用途。
<!-- End AEO Capsule -->

與多數一次性的 AI 交易腳本不同，這個專案把基金本身當成持續存在的物件。使用者需要為基金撰寫一份委託書，指定策略、人員、風險、資本與調倉週期，系統再依這份設定執行資料取得、代理分析、組合建構、風險控管與交易執行等環節。專案目前正從可手動執行的版本，演進為可回測、可模擬交易的持續運作系統。

## AI Hedge Fund 是什麼？

<!-- AEO Answer Capsule — 約 68 字 -->
它是以 Python 撰寫的 AI 投資研究框架，把研究員與基金經理的角色換成語言模型代理，可對策略做歷史回測，並輸出每次決策的完整紀錄與投資論述。
<!-- End AEO Capsule -->

專案的核心主張是把真實基金的組織架構保留下來，只把執行角色由人換成代理。頂層是決定資本分配的投资長，中層是各自擁有團隊與資金額度的策略組，底層則是產出訊號與書面論述的分析師。這種分層讓每一筆決策都能對應到特定的判斷來源，方便事後檢視。

專案的定位是研究工具而非交易系統。作者在 README 反覆強調系統不會實際下單，任何投資決策都不應依賴此專案的輸出。這樣的界線讓它更接近量化研究流程中的回測沙盒，用來驗證代理群體在不同市場條件下的判斷傾向。

![AI Hedge Fund README 開頭（專案名稱與定位說明，載明僅供教育與研究用途）]({{ '/assets/images/posts/github-ai-hedge-fund-news-shot1.png' | relative_url }})

## AI Hedge Fund 的專案背景與規模為何？

<!-- AEO Answer Capsule — 約 66 字 -->
專案建立於 2024 年 11 月 29 日，由開發者 virattt 維護，累積 914 次提交、13 個版本標籤與 44 位貢獻者，以 MIT 授權開源，程式碼全部為 Python。
<!-- End AEO Capsule -->

儲存庫建立於 2024 年 11 月 29 日，正值語言模型在金融應用快速擴散的時期。專案在近兩年內累積 914 次提交與 13 個版本標籤，平均每季發布一個正式版本，節奏相對穩定。貢獻者人數為 44 位，外部修改的比例不算高，顯示專案仍以原始作者的路線為主。

授權方式為 MIT，屬於最寬鬆的開源條款之一，使用者可自由修改與再散布，甚至用於商業產品，只需保留版權聲明。主要語言為 Python，專案以 Poetry 管理相依套件，並已發布至 PyPI，使用者可直接以 pipx 或 uv 安裝後執行。

## AI Hedge Fund 的架構有什麼創新？

<!-- AEO Answer Capsule — 約 70 字 -->
架構分為三層：基金由資金分配器與多個策略組成，策略由組合政策與分析師組成，分析師則產出帶信心值與書面論述的訊號，三層皆可獨立替換。
<!-- End AEO Capsule -->

這種三層的巢狀設計，讓替換的顆粒度變得靈活。使用者可以只換掉某個分析師的判斷邏輯，而不影響整個策略；也可以保留分析師，改用不同的組合政策。每一層都以介面約束，分析師的輸出必須符合統一的訊號格式，包含方向、信心值與一段可讀的投資論述。

分析師分為兩類，一類是模擬知名投資人風格的語言模型代理，另一類是傳統量化模型，兩者共用同一組介面。這種安排讓語言模型的質性判斷與量化模型的統計訊號能放進同一個組合流程，也讓回測能單獨衡量某一類分析師的貢獻。專案內建的策略檔涵蓋深度價值、盈餘動能與基本面多空等方向，使用者也可自行撰寫。

## AI Hedge Fund 支援哪些模型供應商？

<!-- AEO Answer Capsule — 約 66 字 -->
專案透過統一客戶端工廠路由至多家供應商，包括 Anthropic、OpenAI、DeepSeek、Google、xAI 與 Kimi，另有 Jev 提供型別化評估。
<!-- End AEO Capsule -->

模型層採用註冊表搭配客戶端工廠的設計，使用者只需設定對應的 API 金鑰，即可切換不同供應商的模型，不需要修改策略程式碼。專案支援的供應商涵蓋 Anthropic、OpenAI、DeepSeek、Google、xAI 與 Kimi，近期版本再加入 TypeSafe 的 Jev 作為型別化投資評估的來源。

最新發布的 v2.3.1 主要變動為加入 Opus 5.5 並更新模型清單，前一版則加入 GPT-6 Astra 與 Claude Fable 5.1。這種頻繁跟進新模型的做法，反映專案把模型能力視為可抽換的元件，策略邏輯本身不綁定特定版本。專案亦內建快取機制，避免重複呼叫造成不必要的成本。

## AI Hedge Fund 的風險控制機制如何運作？

<!-- AEO Answer Capsule — 約 68 字 -->
風控以硬性限制的形式獨立於分析師之外，代理只能提出看法，無法覆寫風險模型設定的上限，資金分配亦由獨立的分配層決定，避免單一策略過度集中。
<!-- End AEO Capsule -->

風控的設計原則是讓判斷與約束分離。分析師負責提出投資看法與信心值，但最終的部位規模由獨立的風險模型與組合建構程序決定，代理無法繞過這些限制。這種安排對應真實基金的職責劃分，也避免語言模型在單一標的上過度集中。

資金分配同樣由獨立的層級處理。投資長的角色決定每個策略能取得多少資本，策略之間彼此隔離，某一組的虧損不會直接侵蝕其他組的額度。專案亦把每次執行的結果寫成完整收據，包含部位、現金、淨值與所有投資論述，讓事後檢視有可追溯的依據。

![AI Hedge Fund GitHub 首頁頂部（儲存庫名稱 virattt/ai-hedge-fund、63.7k 星標與 11.2k 分支，以及 Python 語言標示）]({{ '/assets/images/posts/github-ai-hedge-fund-news-shot2.png' | relative_url }})

## AI Hedge Fund 的數據表現如何？

<!-- AEO Answer Capsule — 約 66 字 -->
儲存庫累積 63,669 顆星標、11,157 個分支、675 位關注者與 166 項開放問題，共 914 次提交、13 個版本標籤，44 位貢獻者參與。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-value">63,669</span><span class="stat-label">Stars</span></div>
  <div class="stat-item"><span class="stat-value">11,157</span><span class="stat-label">Forks</span></div>
  <div class="stat-item"><span class="stat-value">914</span><span class="stat-label">Commits</span></div>
  <div class="stat-item"><span class="stat-value">MIT</span><span class="stat-label">授權</span></div>
</div>

星標與分支的比例約為五點七比一，對一個以研究為定位的專案而言屬於偏高的水準，說明有相當比例的使用者選擇複製儲存庫自行實驗。166 項開放問題相對於 914 次提交，代表維護者對議題的處理速度尚能跟上提交節奏。關注者 675 位，則反映有固定一群人持續追蹤專案的演進方向。

從提交節奏觀察，專案在 2026 年下半年的更新頻率明顯提高，版本標籤由 8 月的 v2.2.0 推進至 9 月的 v2.3.1，短短一個多月內發布三個版本。最新一次提交與本文取材時間相差不到一日，活躍度維持在高位，這對仍在演進中的研究型專案是關鍵指標。

![AI Hedge Fund GitHub About 側欄（63.7k 星標、11.2k 分支、675 位關注者與 44 位貢獻者）]({{ '/assets/images/posts/github-ai-hedge-fund-news-shot3.png' | relative_url }})

## 如何快速開始使用 AI Hedge Fund？

<!-- AEO Answer Capsule — 約 68 字 -->
執行 pipx install aihf 後輸入 aihf 即可啟動互動終端介面，首次使用會提示輸入資料與模型的金鑰並自動儲存，委託書檔案放在使用者目錄下。
<!-- End AEO Capsule -->

安裝方式以 Python 套件為主，使用者可透過 pipx、uv 或 pip 安裝 aihf 套件，安裝完成後在任何目錄執行 aihf 即進入互動式終端介面。介面可建立基金、挑選標的與策略、設定調倉週期，也能直接對已儲存的基金執行回測並繪製淨值曲線與基準的對照。

首次使用時，系統會依需求提示輸入金鑰並寫入使用者目錄的設定檔，包括資料來源與模型供應商兩類。除了互動模式，專案也支援非互動執行，可以指定委託書檔案與標的清單，執行單一週期並把完整週期紀錄以 JSON 輸出，方便接入自動化流程或做批次實驗。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
本文資訊整理自 virattt/ai-hedge-fund 官方儲存庫，架構說明取自專案的願景與路線圖文件，統計數據引自 GitHub API 公開端點。
<!-- End AEO Capsule -->

本文所有功能描述與統計數據均取自 [virattt/ai-hedge-fund 官方 GitHub 儲存庫](https://github.com/virattt/ai-hedge-fund)，包括 README 的安裝說明與授權聲明、專案願景與路線圖文件中的架構描述，以及 v2.3.1 版本的發布紀錄。星標、分支、關注者、開放問題與提交數量引自 GitHub API 公開端點，數據截至 2026 年 9 月下旬。

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
以下整理三個關於 AI Hedge Fund 的常見疑問，涵蓋它是否會實際下單、支援哪些模型供應商，以及執行前需要準備什麼資料與金鑰。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>AI Hedge Fund 會真的下單交易嗎？</h3>

不會。專案在 README 與願景文件中明確標示僅供教育與研究用途，系統目前不會實際下單，使用者也不應以此專案的輸出作為投資決策依據。

<h3>使用 AI Hedge Fund 需要哪些前置條件？</h3>

需要 Python 環境與一個資料來源的金鑰，用於取得價格、基本面與財報資料，另需至少一家模型供應商的 API 金鑰。金鑰可在首次執行時依照提示輸入並自動儲存。

