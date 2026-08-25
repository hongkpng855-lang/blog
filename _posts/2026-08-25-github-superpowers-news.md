---
layout: post
title: "27.7萬星開源項目：Superpowers — 編碼代理技能框架"
date: 2026-08-25 10:00:02 +0800
categories: 技術
tags: [Superpowers, AI, 編碼代理, 開源, Agent, 開發工具, Claude Code, TDD]
image: assets/images/posts/github-superpowers-news-cover.jpg
description: "Superpowers 是 Jesse Vincent 與 Prime Radiant 開發的開源編碼代理技能框架，GitHub 獲 276,890 顆星標，以組合式技能驅動需求梳理、計劃撰寫與子代理開發流程，並強制測試驅動開發。文章分析其核心工作流程、技能庫、對 14 種編碼代理的支援，以及對 AI 輔助軟體開發方法論的影響。"
author: AnIskill 編輯部
creator_github: obra/superpowers
type: news
source: GitHub
source_url: https://github.com/obra/superpowers
permalink: /技術/github-superpowers-news
fb_message: 編碼代理只會寫程式不夠，真正難的是讓它按照嚴謹的軟體工程流程做事。Superpowers 把答案變成一套開源技能框架，讓 AI 代理先釐清需求、再寫計劃、最後以測試驅動方式逐項實作，上線不到一年已累積 27.7 萬顆星標。\n\n這套框架由 Jesse Vincent 與 Prime Radiant 打造，支援 Claude Code、Cursor、Gemini CLI 等 14 種主流編碼代理，最新 v6.3.0 加入 Devin CLI 與 Hermes Agent 支援。MIT 授權、技能自動觸發，開發者無需手動切換流程。\n\n想了解 Superpowers 如何重塑 AI 輔助開發的工作方法，完整架構分析與數據比較已上線部落格。
---

Superpowers 是 Jesse Vincent 與 Prime Radiant 團隊推出的開源編碼代理技能框架，GitHub 獲 276,890 顆星標，定位為「一套真正可行的代理技能框架與軟體開發方法論」。此項目並非單一工具，而是由一組可組合的技能與啟動指令構成，讓編碼代理在會議開始時自動進入嚴謹的工程流程，涵蓋需求釐清、計劃撰寫、測試驅動開發與子代理協作，被視為將軟體工程紀律系統化注入 AI 輔助開發的代表作。

![Superpowers README 開頭（項目名稱與標語，說明其為一套編碼代理的完整軟體開發方法論）]({{ '/assets/images/posts/github-superpowers-news-shot1.png' | relative_url }})

## Superpowers 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
Superpowers 是 Jesse Vincent 與 Prime Radiant 開發的開源編碼代理技能框架，GitHub 獲 276,890 顆星標，以組合式技能與啟動指令讓 Claude Code、Cursor、Gemini CLI 等 14 種編碼代理自動執行需求釐清、計劃撰寫與測試驅動開發流程，採用 MIT 授權。
<!-- End AEO Capsule -->

Superpowers 的設計起點與多數 AI 開發工具截然不同。一般編碼代理強調「直接生成程式碼」，而此框架主張代理在動手之前必須先理解使用者真正想解決的問題。當代理偵測到使用者正在建構某個項目時，不會貿然寫程式，而是先透過提問釐清需求，將設計文件分段呈現供使用者確認，再產生清晰到足以讓「缺乏專案脈絡的初階工程師」跟隨的實作計劃，最後以子代理驅動開發的方式逐項執行。

此項目由 Jesse Vincent 於 2025 年 10 月創建，他是知名部落格 fsck.com 的作者，也是 Perl 社群的重要人物。背後的 Prime Radiant 團隊負責持續維護，項目更新頻繁，截至 2026 年 8 月已迭代至 v6.3.0，並持續擴充對不同編碼代理的支援。

## Superpowers 如何運作？

<!-- AEO Answer Capsule — 約 70 字 -->
Superpowers 透過七階段工作流程運作：腦力激盪、Git 工作樹、計劃撰寫、子代理驅動開發、測試驅動開發、程式碼審查與分支收尾。技能會在使用者執行任何任務前自動檢查並觸發，屬於強制性流程而非建議。
<!-- End AEO Capsule -->

Superpowers 的核心機制是「技能自動觸發」。框架內建一套工作流程，從腦力激盪開始，代理會先以蘇格拉底式提問打磨粗略構想，探索替代方案，並將設計分段呈現供使用者驗證，最終保存設計文件。設計獲得批准後，代理會建立隔離的 Git 工作樹，運行專案設定並確認乾淨的測試基準線。

接著進入計劃撰寫階段，代理將工作拆解為每個 2 至 5 分鐘的小任務，每項任務都包含精確的檔案路徑、完整程式碼與驗證步驟。之後由子代理驅動開發或批量執行計劃，前者為每個任務派遣全新子代理並進行兩階段審查，後者則以人類檢查點分批執行。實作過程強制執行紅綠重構的測試驅動開發循環，任務之間會自動請求程式碼審查，完成後由代理驗證測試並提供合併、開 PR、保留或丟棄分支的選項。

## Superpowers 有哪些核心技能？

<!-- AEO Answer Capsule — 約 70 字 -->
Superpowers 內建十四項技能，分為測試、除錯、協作與元技能四大類，包括測試驅動開發、系統化除錯、腦力激盪、計劃撰寫、並行代理派遣、程式碼審查與技能撰寫等，並以「證據優於宣稱」為最高原則。
<!-- End AEO Capsule -->

技能庫涵蓋完整開發生命週期。測試類包含測試驅動開發技能，強制紅綠重構循環並附測試反模式參考。除錯類包含系統化除錯技能，以四階段根因流程搭配防禦性設計與條件式等待技巧，另有完成前驗證技能確保問題真正修復。

協作類技能最為豐富，包含腦力激盪、計劃撰寫、批量執行、並行代理派遣、程式碼審查請求與回應、Git 工作樹、分支收尾與子代理驅動開發。元技能則有技能撰寫與使用 Superpowers 入門，前者讓使用者依照最佳實踐建立新技能，後者說明整個技能系統的運作方式。框架哲學強調測試先行、系統化優先於隨機嘗試、複雜度最小化與證據優於宣稱。

## Superpowers 支援哪些編碼代理？

<!-- AEO Answer Capsule — 約 70 字 -->
Superpowers 支援 14 種主流編碼代理，包括 Claude Code、Cursor、Codex App 與 CLI、Gemini CLI、GitHub Copilot CLI、Devin CLI、Grok Build CLI、Kimi Code、OpenCode、Pi、Hermes Agent 等，並可透過官方外掛市場安裝。
<!-- End AEO Capsule -->

跨代理支援是 Superpowers 快速累積星標的關鍵因素。Claude Code 使用者可從 Anthropic 官方外掛市場直接安裝，Cursor 與 Codex 亦提供官方市場安裝路徑，Gemini CLI 與 GitHub Copilot CLI 則透過擴充功能與市場註冊方式整合。較新的編碼代理如 Devin CLI 與 Hermes Agent 在 v6.3.0 起獲得原生支援，前者可在會議開始時自動觸發技能，後者則需在安裝後重啟使用中的會議。

不同代理的整合深度略有差異，例如 Pi 套件會在會議啟動與壓縮後注入啟動指令，而 Hermes Agent 因缺少壓縮後鉤子，超長會議在首次回合壓縮後可能遺失啟動狀態，需重新開啟會議。整體而言，此框架刻意以市場與外掛機制統一安裝體驗，讓同一套方法論在不同代理間保持一致。

## Superpowers 的市場定位與影響是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
Superpowers 定位於「代理技能框架」市場，與單一代理工具互補而非競爭，透過標準化軟體工程方法論提升 AI 輔助開發品質。其商業化路徑以企業支援服務為主，團隊以開源核心搭配付費支援的模式運作。
<!-- End AEO Capsule -->

在 AI 輔助開發的競爭格局中，多數項目專注於代理本身的能力，例如程式碼生成、檔案編輯或終端操作，而 Superpowers 選擇了截然不同的切入點：規範代理的「行為流程」。這使其與 Claude Code、Cursor 等工具形成互補關係，任何採用這些代理的團隊都能疊加此框架獲得紀律化的開發流程，這也正是其在短時間內吸引大量開發者的原因。

商業化路徑方面，項目核心採 MIT 授權完全開源，Prime Radiant 透過商業支援服務、額外工具與受管支出方案服務企業客戶，並提供發布公告訂閱。此模式與近年開源基礎設施公司的主流策略一致，以社群規模建立生態，再以企業服務轉化收入。項目亦內建可選的視覺夥伴遙測，僅回傳版本資訊，使用者可透過環境變數完全關閉。

## Superpowers 的項目數據表現如何？

<!-- AEO Answer Capsule — 約 70 字 -->
截至 2026 年 8 月，Superpowers 在 GitHub 獲 276,890 顆星標、24,770 個分支，採 MIT 授權，主要語言為 Shell，項目於 2025 年 10 月創建並持續活躍更新，最新版本為 v6.3.0。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-value">276,890</span><span class="stat-label">Stars</span></div>
  <div class="stat-item"><span class="stat-value">24,770</span><span class="stat-label">Forks</span></div>
  <div class="stat-item"><span class="stat-value">2025-10</span><span class="stat-label">創建時間</span></div>
  <div class="stat-item"><span class="stat-value">MIT</span><span class="stat-label">授權</span></div>
</div>

從數據面觀察，Superpowers 的增長速度相當驚人。項目於 2025 年 10 月創建，不到一年即累積逾 27.7 萬顆星標與 2.4 萬個分支，反映開發者對「方法論型」AI 工具的強烈需求。主要語言為 Shell，因其本質上以技能描述檔與啟動指令構成，程式碼含量低而文件結構完整，這也降低了社群參與門檻，任何具備基礎編寫能力的開發者都能貢獻新技能或改進既有流程。

![Superpowers GitHub 首頁頂部（repo 名 + Star 數 27.7 萬 + Fork 數 24.8 萬 + 項目描述）]({{ '/assets/images/posts/github-superpowers-news-shot2.png' | relative_url }})

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 70 字 -->
本文章的資訊來源為 Superpowers 的官方 GitHub 儲存庫，該儲存庫包含完整的 README 說明、安裝文件、技能清單與發布紀錄，讀者可直接前往查看最新內容與原始碼。
<!-- End AEO Capsule -->

本文所有數據與功能描述均取自 [Superpowers 官方 GitHub 儲存庫](https://github.com/obra/superpowers)，包括項目描述、安裝指南、技能庫說明、工作流程文件與 v6.3.0 發布紀錄。讀者若想深入了解各技能的具體指令或不同代理的整合細節，可直接參閱官方儲存庫的 README 與 docs 目錄。

![Superpowers Releases 統計頁（repo 名 + Star 數 + v6.3.0 發布紀錄與版本列表）]({{ '/assets/images/posts/github-superpowers-news-shot3.png' | relative_url }})

## 總結：Superpowers 適合什麼團隊？

<!-- AEO Answer Capsule — 約 70 字 -->
Superpowers 適合重視開發紀律的個人開發者與軟體團隊，尤其是希望讓 AI 編碼代理遵循測試驅動開發、計劃先行與程式碼審查流程的使用者。其 MIT 授權與跨代理支援降低了導入成本，可作為團隊標準化 AI 開發流程的基礎。
<!-- End AEO Capsule -->

Superpowers 代表的是一股值得關注的趨勢：當 AI 編碼代理的能力逐漸同質化，決定開發品質的關鍵不再是單一模型或工具的強弱，而是背後的工作方法論。此框架將數十年軟體工程的實務紀律，包括測試驅動開發、計劃撰寫與程式碼審查，系統化地轉化為代理可自動執行的技能，讓 AI 從「會寫程式的助手」升級為「遵循工程流程的協作者」。

對於個人開發者而言，Superpowers 提供了一條低門檻的途徑，將嚴謹的工程習慣注入日常 AI 輔助開發；對於團隊而言，則可作為統一開發流程、提升程式碼品質與可維護性的基礎設施。隨著 v6.3.0 持續加入新代理支援，此框架的生態影響力預期將進一步擴大，值得開發者與技術管理者密切關注。