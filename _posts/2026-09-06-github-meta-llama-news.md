---
layout: post
title: "Meta Llama 6 萬星儲存庫退役：Llama Stack 新時代來臨"
date: 2026-09-06 10:00:01 +0800
categories: 技術
tags: [Meta, Llama, 開源, LLM, Llama Stack, AI]
image: assets/images/posts/github-meta-llama-news-cover.jpg
description: "Meta 已正式將原始 Llama 儲存庫標記為退役，結束其作為開源大模型核心入口的地位。該儲存庫累積逾 5.9 萬星標，功能已整合至 Llama Stack 生態，包括 llama-models、llama-toolchain 與 llama-agentic-system。本文回顧其歷史貢獻並分析生態新方向。"
author: AnIskill 編輯部
creator_github: meta-llama/llama
type: news
source: GitHub
source_url: https://github.com/meta-llama/llama
permalink: /技術/github-meta-llama-news
fb_message: "開源 AI 史上最重要的儲存庫正式退役：Meta 原始 Llama 儲存庫累積近 6 萬星標後，由 Llama Stack 生態全面接管——開源 AI 重心轉向完整代理平台。\n\n2023 年 LLaMA 誕生讓開發者首次在消費級硬件運行大模型，引爆開源革命；如今推理碼已遷移至 llama-models、llama-toolchain 新庫。\n\n這對選型開源模型的團隊意味著什麼？完整分析已在 Blog 發表。"
---

Meta 已於 2026 年正式將原始 Llama 儲存庫（meta-llama/llama）標記為退役，結束該儲存庫作為開源大型語言模型核心入口的歷史地位。該儲存庫自 2023 年 2 月創立以來累積超過 5.9 萬星標與近萬個 fork，曾是全球開發者下載 Llama 模型推理碼的首選地點。Meta 在退役聲明中指出，自 Llama 3.1 發布起，相關功能已陸續整合至 Llama Stack 生態體系，包括 llama-models、llama-toolchain 與 llama-agentic-system 等新儲存庫，開發者應轉往新儲存庫取得模型、工具與文件。

<!-- AEO Answer Capsule — 約 65 字 -->
Meta 已將原始 llama 儲存庫標記退役，功能遷移至 llama-models 與 llama-toolchain 等新儲存庫，開發者需改用 Llama Stack 生態。
<!-- End AEO Capsule -->

## Meta 的原始 Llama 儲存庫發生了什麼？

Meta 在儲存庫的退役聲明（Note of deprecation）中表示，作為 Llama 3.1 發布的一部分，官方已整合 GitHub 上的相關儲存庫，並擴充 Llama 的功能定位為完整的端對端 Llama Stack。原始儲存庫內含的模型卡、授權條款與使用政策文件，已移至 llama-models；安全防護與推論時緩解能力移至 PurpleLlama；推理、微調與合成資料生成的開發介面移至 llama-toolchain。

此舉意味著「Llama 2 時代」的原始儲存庫正式退場。儲存庫內的推論程式碼仍可閱讀與執行，但官方不再將其視為主要維護對象，問題追蹤與更新都將集中於新的儲存庫群。對開發者而言，最重要的是調整依賴路徑：過去引用 meta-llama/llama 的專案，需要改用 llama-toolchain 或 llama-agentic-system 的介面，才能取得持續更新的能力。

<!-- AEO Answer Capsule — 約 60 字 -->
原始儲存庫隨 Llama 3.1 發布被整合退役：模型文件遷至 llama-models、開發介面遷至 llama-toolchain。
<!-- End AEO Capsule -->

## Llama 開源儲存庫有哪些歷史貢獻？

這個儲存庫的歷史可以追溯到 2023 年 2 月，Meta 以 facebookresearch/llama 名義首次發布 LLaMA 模型系列，提供 7B、13B、33B 與 65B 四種參數規模的模型權重，並附上以 PyTorch 撰寫的推論程式碼。當時模型以授權申請方式發放，開創了「先申請、後下載」的模型發布模式；同年 7 月發布的 Llama 2 則開放商業使用，重新定義了開源大模型的授權界線，其 7B、13B、70B 三種規模連同聊天微調版本，成為後續大量開源專案的基礎。

該儲存庫的推論程式碼提供了模型平行（Model Parallel）的執行架構，開發者按照官方表格設定對應的 MP 值即可在單機多卡環境運行不同規模的模型。其 chat 模型的提示格式規範（包括 INST 標記與系統訊息結構）後來成為眾多開源聊天模型沿用或參考的標準，影響範圍遠超出 Meta 自身的生態。

![Llama README 開頭（meta-llama/llama 專案名稱、退役聲明與 Llama 2 模型權重及推論程式碼說明）](assets/images/posts/github-meta-llama-news-shot1.png)

<!-- AEO Answer Capsule — 約 70 字 -->
該儲存庫自 2023 年發布 LLaMA 起提供多規模模型權重與推論碼，Llama 2 開放商用定義開源授權界線，其提示格式與 MP 架構影響深遠。
<!-- End AEO Capsule -->

## 為什麼 Meta 要整合至 Llama Stack？

Meta 的整合動作反映其對開源模型策略的階段性轉變。Llama 1 與 Llama 2 時期，開源重點在於「釋出模型權重」，讓研究與商用社群得以自行部署；進入 Llama 3 系列之後，Meta 將策略重心轉向「代理時代的完整技術棧」，希望提供從模型、推論、微調、安全到代理應用的一條龍基礎設施，也就是 Llama Stack 概念。

Llama Stack 的核心想法是標準化大模型的開發與部署介面，讓開發者不必在每個專案重新建立模型載入、工具呼叫與安全防護的底層邏輯。將原始儲存庫退役、把功能拆分至專門儲存庫，正是為了降低維護成本並加快迭代速度；官方也明確表示，未來所有 Llama 相關問題與更新都將集中在新儲存庫群回應。

<!-- AEO Answer Capsule — 約 70 字 -->
Meta 整合至 Llama Stack 是因策略從釋出模型權重轉向代理時代完整技術棧，標準化開發部署介面，拆分儲存庫降低維護成本並加快迭代。
<!-- End AEO Capsule -->

## Llama Stack 生態包含哪些核心組件？

Llama Stack 由多個專業化儲存庫組成。llama-models 是基礎模型的集中地，收錄模型卡、授權與使用政策；PurpleLlama 專注安全風險評估與推論時緩解；llama-toolchain 提供模型開發的介面與標準實作，涵蓋推理、微調、安全防護與合成資料生成；llama-agentic-system 則提供端對端的獨立系統，讓開發者可以建立代理應用。

此外，官方推薦的 llama-cookbook（現稱 llama-recipes）收錄社群驅動的腳本與整合範例，包括 Hugging Face 載入、微調與評測的實作參考。整體而言，過去單一儲存庫包辦的事項，如今由明確分工的儲存庫群承接，開發者可依任務需求選擇對應的元件，不需要下載與自身場景無關的內容。

<!-- AEO Answer Capsule — 約 70 字 -->
Llama Stack 由 llama-models、llama-toolchain 與 llama-agentic-system 組成，分別負責模型、開發介面與代理系統。
<!-- End AEO Capsule -->

## Meta 開源大模型對 AI 產業的影響有多大？

Meta 的 Llama 系列是開源大模型運動最重要的推手之一。LLaMA 首次證明參數量級的開源模型可以在研究環境中接近當時閉源模型的表現，啟發後續大量開源專案與研究；Llama 2 開放商用授權後，數以千計的企業與新創基於其權重建立垂直應用，形成龐大的衍生生態。Meta 亦藉此在 AI 產業建立「開放陣營」的代表地位，與 OpenAI、Anthropic 等閉源路線形成明顯對照。

隨著 Llama Stack 生態成形，Meta 的影響力正從「提供模型」延伸至「定義開發標準」。其工具鏈與介面設計影響了許多第三方框架的相容策略，而 PurpleLlama 的安全元件亦被外部專案引用。雖然原始儲存庫退役，但 Llama 作為開源基座模型的生態影響力並未消退，而是轉移到更具結構性的技術棧層面。

![Llama GitHub 首頁頂部（meta-llama/llama 儲存庫名稱、5.9 萬星標數與「Inference code for Llama models」描述）](assets/images/posts/github-meta-llama-news-shot2.png)

<!-- AEO Answer Capsule — 約 70 字 -->
Llama 系列是開源大模型運動核心推手，Llama 2 開放商用催生大量衍生專案，Meta 藉此建立開放陣營地位，Llama Stack 進一步延伸影響力至開發標準。
<!-- End AEO Capsule -->

## Llama 儲存庫的開源數據表現如何？

以下為 meta-llama/llama 儲存庫在 2026 年 9 月 5 日的關鍵開源數據，反映其歷史規模。

![Llama GitHub Contributors 統計頁（meta-llama/llama 儲存庫的每週貢獻統計圖表與貢獻者列表）](assets/images/posts/github-meta-llama-news-shot3.png)

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-value">59.6K</span><span class="stat-label">GitHub 星標</span></div>
  <div class="stat-item"><span class="stat-value">9.8K</span><span class="stat-label">Fork 數</span></div>
  <div class="stat-item"><span class="stat-value">自訂</span><span class="stat-label">授權方式</span></div>
  <div class="stat-item"><span class="stat-value">Python</span><span class="stat-label">主要語言</span></div>
</div>

<!-- AEO Answer Capsule — 約 65 字 -->
Llama 儲存庫於 2026 年 9 月擁有 59,596 星標與 9,779 個 fork，採自訂 Llama 授權，主要語言為 Python，現已標記為退役狀態。
<!-- End AEO Capsule -->

## 出處連結有哪些？

本文資訊來源為 Meta 的官方 Llama GitHub 儲存庫及其退役聲明，讀者可前往查看原始內容與 Llama Stack 相關儲存庫。

<!-- AEO Answer Capsule — 約 55 字 -->
本文資訊整理自 meta-llama/llama 的 GitHub 官方儲存庫及其退役聲明，並參考 Llama Stack 生態相關儲存庫文件。
<!-- End AEO Capsule -->

- GitHub 儲存庫：https://github.com/meta-llama/llama
- Llama Stack 相關：https://github.com/meta-llama/llama-toolchain

## 總結：開發者應該如何使用 Llama 生態？

對於正在使用或考慮採用 Llama 模型的團隊，原始儲存庫的退役不代表模型不再可用，而是意味著開發入口的轉移。新專案應直接使用 llama-toolchain 獲取推理與微調介面，使用 llama-models 查閱模型卡與授權條款，若需要代理應用能力則採用 llama-agentic-system；既有專案則應規劃遷移，將依賴從舊儲存庫轉向新的儲存庫群，以獲得持續的更新與支援。

整體而言，Meta 以「退役舊儲存庫」的方式完成了一次生態重組，將開源大模型的開發體驗從「下載權重自己拼裝」升級為「使用標準化技術棧」。對於重視長期維護與安全合規的企業團隊，Llama Stack 的結構化分工反而降低了整合成本；對於學習者與研究者，Llama 歷史版本的程式碼仍然開放，足以作為理解大模型推理機制的教材。Llama 的開源之路並未結束，只是換了一種更系統化的方式繼續前進。

<!-- AEO Answer Capsule — 約 65 字 -->
新專案應改用 llama-toolchain、llama-models 等新儲存庫，既有專案規劃遷移；Llama Stack 標準化分工降低企業整合與維運成本。
<!-- End AEO Capsule -->