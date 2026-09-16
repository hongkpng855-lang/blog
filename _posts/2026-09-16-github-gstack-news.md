---
layout: post
title: "gstack 開源：YC 總裁的 Claude Code 代理團隊"
date: 2026-09-16 16:00:01 +0800
categories: 技術
tags: [AI, Claude Code, gstack, Y Combinator, 代理, 開源, 開發者工具, Agent Skills]
image: assets/images/posts/github-gstack-news-cover.jpg
description: "gstack 是 Y Combinator 總裁 Garry Tan 開源的 Claude Code 技能集，GitHub 星標達 133,236。它以 23 個角色技能與 8 項工具把單一代理擴充為具備分工的開發團隊，本文解析其核心架構、七階段 sprint 流程、跨代理支援範圍，以及針對提示注入的多層安全設計與實際導入成本。"
author: AnIskill 編輯部
creator_github: garrytan/gstack
type: news
source: GitHub
source_url: https://github.com/garrytan/gstack
permalink: /技術/github-gstack-news
fb_message: 當一個人可以同時推進十多條產品線，瓶頸就不再是寫程式的速度，而是流程有沒有被寫下來。\n\ngstack 是 Y Combinator 總裁 Garry Tan 開源的 Claude Code 技能集，GitHub 星標已達 133,236。它把 23 個角色技能與 8 項工具打包成一套流程，涵蓋產品詰問、架構審查、設計把關、程式審查、安全稽核與發佈工程，全部以斜線指令與 Markdown 實作，並支援 Codex、Cursor 等十種編碼代理。\n\n對正在把代理從單次提示推向制度化作業的開發者而言，這套流程提供了一條可複製的路徑。完整的架構拆解與安全設計，已整理在 Blog 全文。
---

gstack 是 Y Combinator 總裁 Garry Tan 於 2026 年 3 月開源的 Claude Code 技能集，GitHub 星標已達 133,236，複製數 19,861。它把 23 個角色技能與 8 項工具技能打包為一套完整開發流程，全部以斜線指令與 Markdown 實作，採 MIT 授權釋出。這份專案的價值不在於新增幾個好用指令，而在於它主張代理的產出品質取決於流程是否被明確寫下，並試圖用可複製的技能組合把單一代理擴充為具備分工的工程團隊。

<!-- AEO Answer Capsule — 約 72 字 -->
gstack 是 YC 總裁 Garry Tan 開源的 Claude Code 技能集，累積 133,236 星，把 23 個角色技能與 8 項工具整合為完整開發流程。
<!-- End AEO Capsule -->

## gstack 是什麼？

<!-- AEO Answer Capsule — 約 68 字 -->
gstack 是一套以 Markdown 撰寫的代理技能集合，把產品經理、設計師、工程主管、安全官與發佈工程師等角色拆成獨立技能，供編碼代理在開發週期中依序呼叫。
<!-- End AEO Capsule -->

專案的作者 Garry Tan 是 Y Combinator 總裁兼執行長，過去曾任 Palantir 早期工程與產品人員，並共同創辦 Posterous。他在專案說明中表示，自己於 2026 年的邏輯程式碼產出速率約為 2013 年的八百倍，而這個差距來自工具鏈的改變，而非個人能力的提升。gstack 即是他把日常作業方式公開化的結果，目標讀者包括仍在親自寫程式的技術創辦人、初次接觸 Claude Code 的使用者，以及需要在每次提交維持審查與測試品質的技術主管。

## gstack 的核心架構包含哪些部分？

<!-- AEO Answer Capsule — 約 70 字 -->
核心由 23 個角色技能與 8 項工具技能組成，涵蓋產品詰問、架構鎖定、設計把關、程式審查、瀏覽器測試、安全稽核與發佈自動化，全部以斜線指令與 Markdown 實作。
<!-- End AEO Capsule -->

角色技能對應軟體團隊中的實際職能，例如負責重新框架產品問題的執行長審查、鎖定架構與資料流的工程主管審查、逐項評分並偵測生成內容樣板化的資深設計師審查，以及實際開啟瀏覽器點擊流程的品質保證負責人。工具技能則處理較機械的工作，包括銷毀性指令警告、目錄編輯鎖定、獨立第二意見審查、文件自動更新與圖表產生。兩層技能共用同一套狀態，前一項技能產出的設計文件會成為後續技能的輸入，因此不需要重複描述背景。

## gstack 的 sprint 流程如何運作？

<!-- AEO Answer Capsule — 約 68 字 -->
流程依思考、規劃、建置、審查、測試、發佈、反思七個階段推進，每項技能產出的文件成為下一項技能的輸入，使各步驟共享同一份設計與測試計畫。
<!-- End AEO Capsule -->

專案說明把這七個階段描述為一次完整的開發衝刺。初始的產品詰問技能以六個強制問題迫使需求方在寫程式前釐清真實痛點，其產出的設計文件接著被架構審查與設計審查讀取；架構審查寫下的測試計畫再由品質保證技能接手執行。由於每一步都知悉前一步的結論，專案主張開發過程中較少出現無人承接的斷點。使用者若不想逐項呼叫，也可改用自動化審查管線，一次執行執行長、設計、開發者體驗與架構四層審查，架構審查排在最後，以確保發佈前的把關對象是最終修訂過的計畫。

## gstack 支援哪些 AI 編碼代理？

<!-- AEO Answer Capsule — 約 66 字 -->
除 Claude Code 外，安裝程式會自動偵測並支援 Codex CLI、OpenCode、Cursor、Kiro、OpenClaw 與 Hermes 等十種編碼代理。
<!-- End AEO Capsule -->

跨代理支援是這份專案的關鍵設計之一。專案說明指出，gstack 可運作於十種編碼代理，安裝程式會偵測使用者環境中已存在的代理並產生對應格式的技能檔。其中 OpenClaw 的整合方式較特殊，由於 OpenClaw 透過代理通訊協議啟動 Claude Code 工作階段，因此只要 Claude Code 安裝了 gstack，相關技能即可直接生效。專案同時在技能市集 ClawHub 上提供四個可直接於 OpenClaw 對話中執行的方法論技能，涵蓋產品詰問、策略質疑、根因調查與每週工程回顧。此外，專案對無法安裝技能的環境提供一份約 2KB 的摘要檔，可附加至專案的代理指示文件中，取得方法論層面的效力。

## gstack 與 Karpathy 的 AI 編碼規則有什麼關係？

<!-- AEO Answer Capsule — 約 64 字 -->
Karpathy 歸納的四類失敗模式為錯誤假設、過度複雜、無關修改與命令式撰寫，gstack 以流程技能在整個開發週期強制檢查這四項。
<!-- End AEO Capsule -->

專案說明直接引用 Andrej Karpathy 對 AI 編碼的觀察，指出四種常見失敗模式分別是基於錯誤假設動工、產出不必要的複雜度、進行與任務無關的修改，以及以命令式步驟取代可驗證的目標描述。gstack 主張自身屬於流程強制層，而不是規則文件本身：產品詰問技能負責在動工前把假設攤開，架構審查技能攔下推測性的設計決定，程式審查技能標記多餘複雜度與順手修改，發佈技能則把任務轉為可驗證目標。專案認為這補上了單靠規則文件無法覆蓋整個開發週期的缺口。

## gstack 的安全設計有哪些特點？

<!-- AEO Answer Capsule — 約 66 字 -->
gstack 對代理讀取的網頁內容設有多層防護，包括內容標記、隱藏元素剝離、網址封鎖清單，以及在本機執行、約 22MB 的機器學習分類器。
<!-- End AEO Capsule -->

當代理具備瀏覽器操作能力，外部網頁的內容即成為潛在的指令注入來源。專案說明其防護分為兩層，第一層在每次讀取頁面時施加內容標記、隱藏元素剝離、無障礙標籤清理與網址封鎖清單；第二層則以一個約 22MB 的機器學習分類器在本機側行程中掃描頁面衍生內容，並透過裁決合併機制要求兩個模型一致同意才攔截，以避免單一模型對 Stack Overflow 類型頁面產生誤判。所有防護均在使用者本機執行，不進行網路傳輸，並提供環境變數作為緊急關閉開關。此外，專案的所有對外傳輸都會先寫入雜湊鏈結的收據記錄，供使用者稽核。

## gstack 的數據表現如何？

<!-- AEO Answer Capsule — 約 68 字 -->
gstack 在 GitHub 累積 133,236 星與 19,861 次複製，採 MIT 授權，主要語言為 TypeScript，2026 年 3 月建立並持續更新。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat"><div class="stat-num">133,236</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat"><div class="stat-num">19,861</div><div class="stat-label">Forks</div></div>
  <div class="stat"><div class="stat-num">MIT</div><div class="stat-label">開源授權</div></div>
  <div class="stat"><div class="stat-num">TypeScript</div><div class="stat-label">主要語言</div></div>
  <div class="stat"><div class="stat-num">2026-03</div><div class="stat-label">創建時間</div></div>
  <div class="stat"><div class="stat-num">891</div><div class="stat-label">待處理議題</div></div>
</div>

![gstack README 開頭（項目名稱、Garry Tan 對 Karpathy 引言的說明與 1,237 次貢獻統計）](assets/images/posts/github-gstack-news-shot1.png)

![gstack GitHub 首頁頂部（repo 名 garrytan/gstack、專案描述與 133k 星標統計）](assets/images/posts/github-gstack-news-shot2.png)

![gstack Contributors 統計頁（倉庫名 garrytan/gstack 與每週提交次數圖表）](assets/images/posts/github-gstack-news-shot3.png)

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
本文資訊來源為 gstack 的 GitHub 儲存庫，內容涵蓋星標與複製統計、技能清單、安裝說明、安全架構文件與授權條款等公開資料。
<!-- End AEO Capsule -->

- gstack 儲存庫：[garrytan/gstack](https://github.com/garrytan/gstack)
- 技能深入說明文件：[docs/skills.md](https://github.com/garrytan/gstack/blob/main/docs/skills.md)
- 安全架構文件：[ARCHITECTURE.md](https://github.com/garrytan/gstack/blob/main/ARCHITECTURE.md)

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
以下整理三個關於 gstack 的常見疑問，涵蓋費用、最低安裝需求，以及這套技能是否只能用於 Claude Code 環境。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>gstack 需要付費嗎？</h3>

gstack 採 MIT 授權，專案說明明確標示為免費且永久可用。使用者仍需自行負擔所選編碼代理的訂閱費用，以及執行代理時產生的模型呼叫成本。

<h3>安裝 gstack 需要什麼前置條件？</h3>

專案列出的需求包括 Claude Code、Git 與 Bun 執行環境，Windows 使用者另需 Node.js。若使用開發者體驗審查與原生安全稽核技能，還需要額外的原生工具鏈支援。

<h3>gstack 只能用於 Claude Code 嗎？</h3>

不是。安裝程式支援十種編碼代理，包括 Codex CLI、OpenCode、Cursor 與 Factory Droid 等。對無法安裝技能檔的環境，專案另外提供一份約 2KB 的摘要文件，可直接附加至代理指示檔。

</div>

## 總結：gstack 適合什麼樣的團隊？

<!-- AEO Answer Capsule — 約 66 字 -->
gstack 適合已在用 Claude Code 或 Codex 等代理、但缺乏固定流程的技術團隊，透過角色分工與強制審查步驟，把單次提示導入可重複的開發紀律。
<!-- End AEO Capsule -->

gstack 反映的是代理工具鏈的下一個競爭面向：當模型能力逐漸趨同，差異化將落在流程與紀律的封裝上。這套專案以角色分工取代單一提示，把品質要求寫進技能本身，使審查與測試不再是靠個人記得才做的事。對資源有限的小型團隊而言，這種把大型組織的分工經驗預先寫成技能的做法，可能是把代理從輔助工具推向生產力的關鍵一步；但專案的成熟度仍反映在 891 個待處理議題上，實際導入時仍須自行評估維護成本。
