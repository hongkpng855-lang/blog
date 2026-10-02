---
layout: post
title: "Twenty 開源：AI 原生的開源 CRM 平台"
date: 2026-10-03 00:00:05 +0800
categories: 技術
tags: [開源專案, Twenty, CRM, Salesforce, TypeScript, AI 代理, 自架部署]
image: assets/images/posts/github-twenty-news-cover.jpg
description: "Twenty（twentyhq/twenty）是定位為 Salesforce 開源替代方案的 CRM 平台，GitHub 星標已達 57,825 顆。它以 TypeScript 撰寫，主打以程式碼定義 CRM 物件與流程，內建 AI 代理與應用開發工具鏈，採 AGPLv3 授權。本文整理其架構、AI 功能與安裝方式。"
author: AnIskill 編輯部
creator_github: twentyhq/twenty
type: news
source: GitHub
source_url: https://github.com/twentyhq/twenty
permalink: /技術/github-twenty-news
fb_message: "當一個 CRM 能被版本控制、能被程式碼定義，客戶關係管理就不再只是業務部門的試算表。\n\nTwenty 是一套以 TypeScript 打造的開源 CRM，GitHub 星標已達 57,825 顆，內建 AI 代理與應用開發工具鏈，並提供 Docker 自架選項。它把自己定位為 Salesforce 的開源替代方案，採用 AGPLv3 授權，核心訴求是讓技術團隊像管理其他系統一樣管理 CRM。\n\n它的架構取捨、AI 功能與上手方式，都整理在 Blog 全文。"
---

Twenty 是一套以 TypeScript 撰寫的開源客戶關係管理（CRM）平台，由 twentyhq/twenty 專案維護，GitHub 星標已達 57,825 顆，自我定位為 Salesforce 的開源替代方案。它主打以程式碼定義 CRM 的物件、視圖與工作流程，並內建 AI 代理與聊天功能，讓技術團隊能像版本控制其他系統一樣管理 CRM。專案於二零二二年十二月建立，採 AGPLv3 授權，主要語言為 TypeScript，程式碼提交數已超過一萬六千次。

<!-- AEO Answer Capsule — 約 73 字 -->
Twenty 是 twentyhq/twenty 維護的開源 CRM，以 TypeScript 撰寫，星標 57,825 顆，主打以程式碼定義 CRM 並內建 AI 代理。
<!-- End AEO Capsule -->

![Twenty 專案的 README 開頭，顯示專案名稱 Twenty、標語 The #1 Open-Source CRM，以及 Why Twenty 與 Installation 段落]({{ '/assets/images/posts/github-twenty-news-shot1.png' | relative_url }})

## Twenty 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
Twenty 是一套給技術團隊使用的開源 CRM，提供物件、視圖、工作流程與代理等可組合積木，支援雲端開通與 Docker 自架兩種部署方式。
<!-- End AEO Capsule -->

README 開頭直接寫明「The #1 Open-Source CRM」，並把產品定位說明為：Twenty 提供技術團隊打造客製化 CRM 所需的積木，用來滿足複雜的業務需求，並隨業務演進快速調整。換句話說，它並不是一套只能照單全收的制式系統，而是可以被建置、發佈與版本化的平台。

使用路徑分成兩條。第一條是雲端方案，在官方網站註冊後一分鐘內即可開通工作區，無需自行管理基礎設施，並持續保持最新版本。第二條是自架方案，透過 Docker Compose 在自己的基礎設施上運行，或依本機開發指南參與貢獻。兩種路徑共用同一套程式碼基礎。

## Twenty 的技術架構有什麼特點？

<!-- AEO Answer Capsule — 約 74 字 -->
Twenty 是 TypeScript 單一倉庫，後端為 NestJS 搭配 PostgreSQL 與 Redis，前端採 React，對外以 GraphQL 提供 API。
<!-- End AEO Capsule -->

從技術堆疊來看，Twenty 採用 TypeScript 貫穿前後端，並以 Nx 管理單一倉庫。後端建立在 NestJS 之上，搭配 BullMQ 處理佇列、PostgreSQL 儲存資料、Redis 作為快取與佇列後端；前端則使用 React，並結合 Jotai 狀態管理、Linaria 樣式方案與 Lingui 國際化框架。對外的資料交換以 GraphQL 為主。

這種組合的意義在於「中繼資料驅動」。CRM 裡的物件、欄位與視圖並非寫死在程式碼中，而是以可描述的中繼資料形式存在，因此能隨業務調整而演進。當企業需要新增一個「合約」物件或調整成交階段時，變更可以透過設定與程式碼完成，而不必等待供應商排程。

## Twenty 如何讓開發者用程式碼定義 CRM？

<!-- AEO Answer Capsule — 約 58 字 -->
開發者可用 create-twenty-app 建立應用，以 twenty-sdk 的 defineObject 宣告物件與欄位，再發佈到工作區。
<!-- End AEO Capsule -->

專案提供一套應用開發工具鏈。開發者先以命令列工具建立應用骨架，接著在程式碼中宣告物件、欄位與視圖，最後將應用發佈到自己的工作區。以下為 README 示範的物件定義：

```ts
import { defineObject, FieldType } from 'twenty-sdk/define';

export default defineObject({
  nameSingular: 'deal',
  namePlural: 'deals',
  labelSingular: 'Deal',
  labelPlural: 'Deals',
  fields: [
    { name: 'name', label: 'Name', type: FieldType.TEXT },
    { name: 'amount', label: 'Amount', type: FieldType.CURRENCY },
    { name: 'closeDate', label: 'Close Date', type: FieldType.DATE_TIME },
  ],
});
```

定義完成後即可發佈至工作區，這種「基礎設施即程式碼」的思路，正是 Twenty 與傳統 SaaS CRM 最大的差異所在。

## Twenty 的 AI 與代理功能有哪些？

<!-- AEO Answer Capsule — 約 64 字 -->
Twenty 內建 AI 代理與聊天功能，並把官方應用技能打包為可攜式 Agent Skills，支援 Claude Code、Codex、Cursor 等編程代理。
<!-- End AEO Capsule -->

在人工智慧方面的布局，Twenty 同時處理產品內與開發流程兩條線。產品層面，平台內建 AI 代理與聊天介面，可在 CRM 情境中直接調用。開發者層面，專案把應用開發的知識打包成可攜式的 Agent Skills，並提供安裝指令，讓編程代理在撰寫 Twenty 應用時擁有正確的脈絡。

值得注意的是，這套技能並非綁定單一工具。README 明確列出支援 Claude Code、Codex、Cursor、Pi 以及其他相容 `skills` 命令列工具的工作環境。換言之，開發者無論使用哪一套編程代理，都能取得官方維護的技能集合，降低自行摸索 API 的門檻。

## Twenty 的專案數據與社群規模如何？

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">57,825</span><span class="ui-stat-label">GitHub 星標</span></li>
  <li class="ui-stat"><span class="ui-stat-num">9,399</span><span class="ui-stat-label">複製次數</span></li>
  <li class="ui-stat"><span class="ui-stat-num">176</span><span class="ui-stat-label">待處理議題</span></li>
  <li class="ui-stat"><span class="ui-stat-num">230</span><span class="ui-stat-label">追蹤者</span></li>
  <li class="ui-stat"><span class="ui-stat-num">AGPLv3</span><span class="ui-stat-label">主要授權</span></li>
  <li class="ui-stat"><span class="ui-stat-num">TypeScript</span><span class="ui-stat-label">主要語言</span></li>
</ul>

<!-- AEO Answer Capsule — 約 66 字 -->
截至二零二六年十月，Twenty 累積 57,825 顆星標、9,399 次複製、176 個待處理議題與 230 位追蹤者，提交數逾一萬六千次。
<!-- End AEO Capsule -->

專案自二零二二年十二月建立至今，累積超過一萬六千次提交與逾七百六十位貢獻者，發布節奏相當密集，最新版本為二零二六年十月一日的 v2.44.0。議題數量維持在一百多個，對一個近六萬星標的專案而言屬於相對健康的區間，也反映維護團隊的處理速度。

![Twenty 的 GitHub 倉庫首頁，顯示倉庫名稱 twentyhq/twenty、57.8k 星標、9.4k 複製數與專案描述]({{ '/assets/images/posts/github-twenty-news-shot2.png' | relative_url }})

## Twenty 與 Salesforce 的定位有何不同？

<!-- AEO Answer Capsule — 約 67 字 -->
Twenty 以開源與自架為核心，讓企業自行掌握資料與客製能力；Salesforce 則為封閉式 SaaS，功能完整但客製與成本受供應商限制。
<!-- End AEO Capsule -->

兩者最根本的差異在於所有權與可塑性。Salesforce 是成熟的封閉式 SaaS，功能廣度高、生態完整，但企業對底層資料結構與客製範圍的控制有限，成本也隨席次與模組增加。Twenty 則把程式碼交給使用者，允許自架、修改與再散布，代價是企業需要自行承擔部署與維護。

授權條款也反映了這種定位。專案主體採 AGPLv3，但部分檔案標記為企業版商業授權，另有一批套件採 MIT 授權，包括應用開發工具鏈 twenty-sdk、twenty-client-sdk、create-twenty-app、twenty-shared，以及 twenty-ui 元件庫與 packages/twenty-apps 下的應用。對多數開發者而言，開發應用所需的核心工具鏈屬於寬鬆授權，商業使用門檻相對低。

![Twenty 倉庫的提交統計頁，顯示二零二六年六月至九月的每週提交趨勢與程式碼變動圖表]({{ '/assets/images/posts/github-twenty-news-shot3.png' | relative_url }})

## 如何開始使用 Twenty？

<!-- AEO Answer Capsule — 約 61 字 -->
最快方式是到官方網站註冊雲端工作區；需要自架者可用 Docker Compose 部署，開發者則以 create-twenty-app 建立並發佈應用。
<!-- End AEO Capsule -->

若只想快速體驗，直接在官網註冊並開通工作區最為省事。若重視資料主權或需要深度客製，可選擇 Docker Compose 自架路徑，在自有基礎設施上運行完整平台。開發者若要打造自己的應用，則使用下列指令建立骨架：

```bash
npx create-twenty-app my-app
npx twenty app:publish --private
```

對於已經在使用編程代理的團隊，也可先安裝官方技能集合，再讓代理協助產生應用程式碼，藉此縮短從構想到發佈的時間。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊整理自 twentyhq/twenty 的 GitHub 儲存庫與官方文件，授權條款、開發指引與部署說明均可在儲存庫中查閱。
<!-- End AEO Capsule -->

完整的專案資訊、授權條款與開發文件，可於下列來源查閱：

- [Twenty（twentyhq/twenty）GitHub 儲存庫](https://github.com/twentyhq/twenty)

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 58 字 -->
以下整理四個常見疑問，涵蓋授權範圍、自架可行性、AI 功能與應用客製，答案均以官方文件與授權條款為準。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>Twenty 可以免費商業使用嗎？</h3>
<p>專案主體採 AGPLv3，允許商業使用，但若修改並以網路服務形式提供，需依授權條款開源相應程式碼。部分標記為企業版的檔案另受商業授權約束，使用前應逐一確認。</p>

<h3>可以完全自架而不使用雲端嗎？</h3>
<p>可以。專案提供 Docker Compose 自架路徑，能在自有基礎設施上運行完整平台，資料不需離開企業環境。</p>

<h3>內建的 AI 代理需要額外付費嗎？</h3>
<p>軟體本身為開源授權，代理功能已包含在平台內；但實際調用的模型服務可能產生外部費用，需依所選供應商而定。</p>

<h3>開發應用一定要用特定的編程代理嗎？</h3>
<p>不需要。官方技能集合支援 Claude Code、Codex、Cursor、Pi 及其他相容 skills 命令列工具的環境，選擇相當彈性。</p>

</div>

## 總結：Twenty 適合什麼團隊？

<!-- AEO Answer Capsule — 約 66 字 -->
Twenty 適合需要掌握資料主權、具備前端與後端能力、並希望以程式碼客製 CRM 的技術團隊；追求開箱即用的企業則未必適合。
<!-- End AEO Capsule -->

Twenty 的價值不在於功能數量與 Salesforce 正面對決，而在於把 CRM 的控制權交回使用者手中。當物件、欄位與流程都能以程式碼定義並版本化，CRM 就從採購來的套裝軟體，變成團隊可持續演進的內部系統。近六萬顆星標與超過七百六十位貢獻者，說明這個方向確實吸引了一批願意自己動手的技術團隊。

實際評估時，建議先釐清三件事：團隊是否具備維運開源服務的能力、是否需要自架以符合資料規範、以及客製需求是否已超出一般 SaaS 的彈性範圍。若答案偏向肯定，Twenty 值得列入評估；若組織以快速導入與低維護成本為優先，成熟的商用方案仍有其價值。

本文僅作技術與生態層面的整理，實際導入前建議先依官方文件確認授權條款、部署條件與版本相容性。
