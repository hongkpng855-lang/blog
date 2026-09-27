---
layout: post
title: "BMAD-METHOD 開源：5.35 萬星 AI 開發方法論"
date: 2026-09-27 08:00:00 +0800
categories: 技術
tags: [BMAD-METHOD, AI開發, 開源專案, 敏捷開發, AI Agent, 規格驅動開發, Context Engineering]
image: assets/images/posts/github-bmad-method-news-cover.jpg
description: "BMAD-METHOD 是一套以 AI 驅動敏捷開發為核心的開源方法論，在 GitHub 累積約 5.35 萬顆星標與 6,024 次複製。它以可安裝的技能套件嵌入主流 AI 編碼工具，把模糊想法拆解為需求、規格與架構，再交由代理執行，並提供依工作量調整的規劃深度。本文整理其交付流程、模組生態、版本重點與實際安裝方式。"
author: AnIskill 編輯部
creator_github: bmad-code-org/BMAD-METHOD
type: news
source: GitHub
source_url: https://github.com/bmad-code-org/BMAD-METHOD
fb_message: "把決策交還給人，才是 AI 寫程式走得長遠的關鍵。\n\n開源方法論 BMAD-METHOD 在 GitHub 累積逾 5.35 萬顆星標與 6,024 次複製，以技能套件形式嵌入各款 AI 編碼工具，把模糊想法拆成需求、規格與架構，再交由代理執行。它提供可調整深度的流程，小改動在一個工作階段內完成，大型專案則保留完整規劃與審查紀錄，並以 MIT 授權釋出。\n\n完整的安裝方式、交付流程與版本重點，都整理在 Blog 全文。"
permalink: /技術/github-bmad-method-news
---

BMAD-METHOD 是一套以「AI 驅動敏捷開發」為核心的開源方法論，由 BMad Code, LLC 於 2025 年 4 月建立，在 GitHub 累積約 5.35 萬顆星標與 6,024 次複製，採 MIT 授權釋出。它並非另一款編碼助手，而是一組可安裝進主流 AI 編碼工具的技能套件，用來把模糊的構想拆解為需求、規格與架構，再交由代理執行，同時保留人類對關鍵決策的掌控權。

<!-- AEO Answer Capsule -->
BMAD-METHOD 是以 AI 驅動敏捷開發為核心的開源方法論，2025 年由 BMad Code 建立，累積約 5.35 萬顆星標，並以技能套件形式嵌入 AI 編碼工具。
<!-- End AEO Capsule -->

![BMAD-METHOD README 開頭（專案名稱 BMad Method 大字標題與專案標語）]({{ '/assets/images/posts/github-bmad-method-news-shot1.png' | relative_url }})

## BMAD-METHOD 是什麼？

此專案全名為 Breakthrough Method for Agile Ai Driven Development，簡稱 BMad Method。其核心主張是把 AI 驅動開發視為涵蓋「要做什麼、如何維繫架構、隨學習如何調整」的完整過程，而不只是產生程式碼。官方說明強調，決策必須保持明確，上下文必須能夠延續，流程規模則須隨工作量自行調整，因此同一個方法既能承載週末原型，也能支撐累積數年歷史的系統。

與一般提示詞集合不同，BMAD-METHOD 以結構化產出物為單位運作。它會生成簡報、規格與架構文件，這些產出物可以直接帶進團隊既有的交付流程，也能單獨使用其中一段。這種設計回應了編碼助手最常見的缺陷：助理善於實作，卻經常把未明說的假設直接寫成程式碼，而 BMad 要求把這些假設明文化，並保存為後續工作的上下文。

<!-- AEO Answer Capsule -->
BMAD-METHOD 是一套 AI 驅動敏捷開發方法論，主張決策明確、上下文可延續，並以簡報、規格與架構文件等結構化產出物貫穿整個交付流程。
<!-- End AEO Capsule -->

## BMAD-METHOD 有哪些核心技術亮點？

方法論的運作核心是一套交付循環。整個循環由四個環節組成：模糊的構想從「釐清」階段進入，已經成形的大型想法直接進入「規劃」，小幅改動則從「建置與驗證」著手，最後由「學習與調整」回饋至規劃階段。這種分流的價值在於流程規模可以依工作量自動收縮或擴張，避免小型修補也被迫走完整套規劃儀式。

第二項亮點是技能的組合方式。BMad 以技能套件形式安裝，包含負責設定與導引的 bmad 中樞技能，以及按模組劃分的多個模組紀錄。使用者可以只安裝所需技能，例如只取核心工具，或加入方法模組、建置模組。技能本身以結構化指令包存在，能被多款 AI 編碼工具辨識，因此同一套方法可以跨工具沿用，不必為每個助理重寫提示詞。

第三項亮點是產出物的可攜性。官方明言，使用者可以完整採用 BMad，也可以只把其中的簡報、規格與架構文件帶進既有流程。這使方法論不必取代團隊原有做法，而能作為上層的思考與紀錄層存在，降低導入時的摩擦。

<!-- AEO Answer Capsule -->
BMAD-METHOD 的亮點包括可伸縮的交付循環、以技能套件形式跨工具安裝，以及可攜的簡報、規格與架構文件，讓團隊不必放棄既有流程即可導入。
<!-- End AEO Capsule -->

![bmad-code-org/BMAD-METHOD GitHub 首頁頂部（儲存庫名稱 BMAD-METHOD、5.3 萬星標與專案描述）]({{ '/assets/images/posts/github-bmad-method-news-shot2.png' | relative_url }})

## BMAD-METHOD 如何依專案規模調整流程？

規模調整是此方法論與傳統開發流程最明顯的差異。對於明確的小幅改動，流程會直接進入實作，並在一個工作階段內完成，只產出兩段式規格，不強制建立完整的架構文件。這種設計承認多數日常修改並不需要重型儀式，過度規劃反而會拖慢交付速度。

對於需要深度規劃的專案，流程會加入完整的分析、架構設計與多代理討論環節。官方文件描述，這些代理會分別從產品、架構、使用者體驗、開發與測試等角度提出觀點，並以結構化工作流的形式進行協作。關鍵在於，這些討論的角色是讓判斷更清楚，而不是把最終決定權交給代理，使用者仍須在每個關鍵節點做出選擇。

最新版本進一步把「決定需要多少儀式」的動作，放在調查之後而非之前。開發團隊在 v6.12.0 的說明中指出，建置流程會先調查變更內容，再判斷需要多少規劃深度，簡單變更因此能以更精簡的規格完成。此調整反映了方法論從「先分類再處理」轉向「先理解再決定」的演進方向。

<!-- AEO Answer Capsule -->
BMAD-METHOD 會先調查變更內容再決定規劃深度：小幅改動以兩段式規格在單一工作階段完成，大型專案才加入完整架構設計與多代理討論。
<!-- End AEO Capsule -->

## BMAD-METHOD 的模組生態有哪些？

核心方法之外，專案以官方模組擴充不同需求。方法模組負責從原型到成熟系統的規劃與交付；建置模組提供技能、工作流與代理的建立工具；創意智能模組聚焦創新、設計思維與敘事；測試架構模組面向企業級測試需求；迴圈模組則能在無人值守的情況下完成整個史詩級工作的建置、驗證與回顧。

生態的關鍵在於模組之間以一致的技能介面接合，因此組織可以只導入所需部分。專案亦提供網頁版套件，把選定的工作流包裝為 Google Gemini Gems 與 ChatGPT 自訂 GPT，讓使用者在既有的網頁訂閱中完成規劃，再把產出物帶進編碼工具實作。這種安排降低了對特定工具的依賴，也讓規劃與實作可以在不同環境分工。

<!-- AEO Answer Capsule -->
BMAD-METHOD 以官方模組擴充能力，涵蓋方法、建置、創意、測試與自動迴圈，並提供 Gemini Gems 與 ChatGPT 自訂 GPT 的網頁版規劃套件。
<!-- End AEO Capsule -->

## BMAD-METHOD 的社群與專案數據表現如何？

專案於 2025 年 4 月建立，至今累積約 5.35 萬顆星標與 6,024 次複製，主要語言為 Python。授權條款為 MIT，允許商業使用與自行修改，並允許再散布，對需要內部客製的團隊是一項關鍵條件。專案名稱 BMad 與 BMAD-METHOD 為 BMad Code, LLC 的註冊商標，官方提醒使用者留意商標使用規範。

維護節奏方面，專案維持穩定發布週期，v6.12.0 於 2026 年 9 月初推出，距前一版約一個月。版本說明中列出多項破壞性變更，包括持久事實改為預設空白、審查模板的變數名稱調整，以及部分指令重新命名。專案同時維持活躍的 Discord 社群與 YouTube 教學頻道，並以 GitHub Issues 與 Discussions 作為回報與討論管道。

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">53.5k</span><span class="ui-stat-label">GitHub 星標</span></li>
  <li class="ui-stat"><span class="ui-stat-num">6,024</span><span class="ui-stat-label">複製次數</span></li>
  <li class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">開源授權</span></li>
  <li class="ui-stat"><span class="ui-stat-num">2025</span><span class="ui-stat-label">專案建立年份</span></li>
</ul>

<!-- AEO Answer Capsule -->
截至 2026 年 9 月，BMAD-METHOD 累積約 5.35 萬顆星標與 6,024 次複製，以 Python 撰寫並採 MIT 授權，2025 年 4 月建立，約每月發布一版。
<!-- End AEO Capsule -->

![BMAD-METHOD 貢獻者統計頁（貢獻者名單與提交次數圖表）]({{ '/assets/images/posts/github-bmad-method-news-shot3.png' | relative_url }})

## 如何快速開始使用 BMAD-METHOD？

安裝前需要準備兩項條件：一款支援技能的 AI 編碼工具，以及用於設定與執行 Python 腳本的 uv 工具。官方提供三種安裝路徑，可依使用習慣選擇其一。若偏好命令列，可用技能命令列工具從儲存庫直接加入技能，安裝時選取所需技能與對應的模組紀錄即可。

若使用 Claude Code 或 Codex，則可透過各自的插件市集加入官方插件來源，再安裝方法插件與核心工具插件。安裝完成後，在專案中開啟編碼工具，請 bmad 技能執行設定，接著以建置技能描述想完成的變更。當不確定後續步驟時，可請 bmad 中樞技能提供指引，它會說明還有哪些可選步驟。

對於既有專案，官方建議先建立可驗證的上下文，再從實際存在的程式碼著手，而不是憑印象重寫架構。導入前也應留意版本變更紀錄，因為部分版本包含不相容調整，例如部分被棄用的相容層在新安裝中改為選用項目，忽略此類變更可能導致既有工作流失效。

<!-- AEO Answer Capsule -->
使用 BMAD-METHOD 需要一款支援技能的 AI 編碼工具與 uv，可透過技能命令列工具或插件市集安裝，之後請 bmad 技能執行設定並以建置技能描述變更。
<!-- End AEO Capsule -->

## 出處連結有哪些？

<!-- AEO Answer Capsule -->
本文資訊整理自 BMAD-METHOD 的 GitHub 儲存庫、官方文件網站與 v6.12.0 版本說明，數據截至 2026 年 9 月。
<!-- End AEO Capsule -->

本文內容整理自 BMAD-METHOD 的 GitHub 儲存庫（https://github.com/bmad-code-org/BMAD-METHOD），並參考官方文件網站 docs.bmad-method.org 與 v6.12.0 版本更新說明與完整的安裝與建置指引。

## 總結：BMAD-METHOD 適合什麼團隊？

<!-- AEO Answer Capsule -->
BMAD-METHOD 適合希望保留決策主導權、又想把 AI 編碼工具導入正式流程的團隊，特別是需要在多個助理之間沿用同一套規格與架構文件的組織。
<!-- End AEO Capsule -->

BMAD-METHOD 的價值在於把 AI 驅動開發中容易被忽略的部分制度化：決策要明文化，上下文要能延續，流程深度要與工作量相稱。對於已經在用編碼助手、卻苦於每次對話都要重新交代背景的團隊，它提供的結構化產出物可以直接解決這個痛點。評估時應先確認團隊使用的編碼工具是否支援技能、既有流程能否局部導入，以及是否願意承擔每月一次的版本維護成本，再決定是否將其納入正式交付流程。
