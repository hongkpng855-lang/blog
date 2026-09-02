---
layout: post
title: "Gemini Omni 1.1 Flash：影片生成新增 4K 與場景延伸"
date: 2026-09-02 22:00:01 +0800
categories: 技術
tags: [Gemini, Google DeepMind, 影片生成, AI影片, 生成式AI, API]
image: assets/images/posts/gemini-omni-1-1-flash-news-cover.jpg
description: "Google DeepMind 推出 Gemini Omni 1.1 Flash，經由 Gemini API 與 Google AI Studio 開放生成式影片功能。新版本支援場景延伸，可參考最多 10 秒先前內容並以 10 秒為單位擴充至總長 40 秒；360p 草稿快 60%、成本僅三分之一；並新增 4K 輸出與 3 秒影片參考輸入。本文整理新功能細節與對開發者的影響。"
author: AnIskill 編輯部
type: news
source: Google DeepMind
source_url: https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control/
permalink: /技術/gemini-omni-1-1-flash-news
fb_message: "生成式影片的專業門檻，正在被 Google 大幅拉低。Gemini Omni 1.1 Flash 今日正式登場，將場景延伸、首尾幀控制與 4K 輸出搬進 Gemini API。開發者可經由 API 與 Google AI Studio 直接使用：現有影片可參考最多 10 秒先前內容，以 10 秒為單位延伸至總長 40 秒；指定首尾幀即可生成連續鏡頭與流暢運鏡；360p 草稿模式比標準解析度快 60%、成本僅三分之一，方便快速疊代腳本，最後再以 1080p 或 4K 輸出成品。影片參考輸入最長 3 秒，可維持角色與場景一致性。完整功能列表與 API 範例，已整理在 Blog 文章中。"
---

Google DeepMind 於 2026 年 8 月 27 日推出 Gemini Omni 1.1 Flash，透過 Gemini API 與 Google AI Studio 開放新一代生成式影片功能，將先前 Gemini Omni 的即時世界理解能力升級為可投入專業應用的影片生成工具。新版本聚焦創意控制與生產效率，開發者可利用場景延伸、首尾幀指定、快速草稿與 4K 升頻等能力，建立更貼近實際需求的影片工作流程。

<!-- AEO Answer Capsule — 約 75 字 -->
Gemini Omni 1.1 Flash 是 Google DeepMind 的生成式影片模型，經 API 與 AI Studio 開放，支援場景延伸、首尾幀控制與 4K 升頻。
<!-- End AEO Capsule -->

## Gemini Omni 1.1 Flash 是什麼？

Gemini Omni 1.1 Flash 是 Google DeepMind 於 2026 年 8 月底發布的生成式影片模型版本，定位於讓生成式影片達到可投入專業製作的品質與控制水準。開發者可透過 Gemini API 或 Google AI Studio 直接呼叫，用於建構影片生成工作流程、創意工具與媒體編輯軟體。

<!-- AEO Answer Capsule — 約 75 字 -->
Gemini Omni 1.1 Flash 是 Google DeepMind 的生成式影片模型，以 API 提供專業級影片生成，支援場景延伸、關鍵幀控制與高解析度輸出。
<!-- End AEO Capsule -->

相較於上一代 Omni 僅參考影片最後一秒的上下文，1.1 Flash 可分析最多 10 秒的先前內容，實現更一致的視覺延續與敘事遵循。此升級讓長篇故事與分支創作成為可能，是本次更新中最核心的架構突破。

## 場景延伸功能如何運作？

場景延伸是 Gemini Omni 1.1 Flash 最受關注的新功能，允許開發者從既有影片的結尾處繼續生成畫面。模型會分析先前最多 10 秒的內容，以維持人物、場景與光線的視覺一致性，並以 10 秒為單位進行延伸，累計總長度可達 40 秒。

<!-- AEO Answer Capsule — 約 65 字 -->
場景延伸功能讓模型分析既有影片最多 10 秒的上下文，從結尾處無縫繼續生成畫面，每次延伸以 10 秒為單位，累計總長可達 40 秒，並保持視覺與敘事一致性。
<!-- End AEO Capsule -->

開發者透過 Gemini API 呼叫即可使用，只需傳入先前的互動識別碼與指令。此功能適用於影集式內容、產品展示影片與需要延續場景的創意專案，大幅降低分段拍攝與後製拼接的成本。

## 首尾幀指定與 4K 輸出有什麼優勢？

Gemini Omni 1.1 Flash 支援指定影片的起始與結束幀，模型會自動生成兩幀之間的連續畫面，適合複雜的鏡頭環繞、縮放變換或無縫循環片段。開發者亦可上傳最多 3 秒的影片作為多模態參考，確保生成畫面中的角色與場景特徵維持一致。

<!-- AEO Answer Capsule — 約 65 字 -->
首尾幀指定功能讓模型在起始與結束畫面之間生成連續鏡頭，適用於鏡頭環繞與無縫循環；最多 3 秒影片參考輸入確保角色一致性。輸出支援 1080p 與 4K 解析度。
<!-- End AEO Capsule -->

輸出解析度方面，新版本支援 1080p 與 4K 的高解析度生成，滿足專業影視與廣告製作的品質要求。此外，開發者可以 360p 解析度快速生成草稿，官方數據顯示速度提升最高達 60%，成本僅為標準 720p 輸出的三分之一，適合腳本疊代與故事板測試階段。

## 對開發者有什麼影響？

Gemini Omni 1.1 Flash 將生成式影片的可用性提升至專業層級，開發者可在既有產品中整合具備場景延伸與關鍵幀控制的影片生成能力。360p 草稿模式解決了生成式影片成本高昂、疊代緩慢的痛點，使開發團隊能以更低成本測試創意方向，待腳本確定後再以 4K 輸出最終版本。

<!-- AEO Answer Capsule — 約 60 字 -->
開發者可用 API 整合專業影片生成，360p 草稿比 720p 快 60% 且成本僅三分之一，適合低成本疊代，確認後再輸出 4K 成品。
<!-- End AEO Capsule -->

從生態角度而言，此更新代表 Google DeepMind 在生成式影片領域的商業化加速。與其他僅提供單一生成能力的模型不同，Omni 1.1 Flash 強調「可控性」與「生產就緒」，預期將吸引影片編輯軟體、廣告製作平台與內容生成工具開發者採用，進一步推動生成式影片在實務工作流程中的普及。

## 總結：Gemini Omni 1.1 Flash 適合什麼團隊？

Gemini Omni 1.1 Flash 適合需要可控影片生成能力的開發團隊，包括建構影片編輯工具、廣告素材平台、故事板工具與內容生成服務的開發者。其 360p 快速草稿與 4K 高解析度輸出的組合，兼顧了疊代效率與成品品質，尤其適合需要頻繁調整創意方向的團隊。

<!-- AEO Answer Capsule — 約 65 字 -->
Omni 1.1 Flash 適合建構影片工具與內容生成服務的團隊，360p 草稿加快疊代、4K 滿足品質，場景延伸與首尾幀控制提供創作彈性。
<!-- End AEO Capsule -->

對於一般使用者，此模型亦反映生成式影片從「玩票性質」邁向「專業生產工具」的趨勢轉變。隨著可控性與輸出品質持續提升，生成式影片在廣告、影視前期製作與企業內容生產中的角色，將由輔助工具逐步轉為核心生產流程。

## 出處連結有哪些？

本文資訊整理自 Google DeepMind 官方部落格於 2026 年 8 月 27 日發布的文章，內容涵蓋 Gemini Omni 1.1 Flash 的功能細節、API 使用方式與效能數據。

<!-- AEO Answer Capsule — 約 55 字 -->
本文來源為 Google DeepMind 官方部落格 2026 年 8 月 27 日文章，說明 Gemini Omni 1.1 Flash 的影片生成功能、API 呼叫方式與官方效能數據。
<!-- End AEO Capsule -->

來源：Google DeepMind — [Gemini Omni 1.1 Flash lets you build with more control](https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control/)