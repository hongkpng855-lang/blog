---
layout: post
title: "Google 發布 Gemini 3.8 Live：語音代理即時推理"
date: 2026-09-16 14:00:01 +0800
categories: 技術
tags: [AI, Google, DeepMind, Gemini, 語音代理, Live API, 開發者工具]
image: assets/images/posts/gemini-3-8-live-news-cover.jpg
description: "Google DeepMind 於 2026 年 9 月 15 日推出 Gemini 3.8 Live 與 Gemini 3.8 Live Extended Thinking 兩款即時對話模型，分別針對規模化成本效率與高複雜度推理。新模型可在對話期間背景執行工具呼叫，並支援 97 種語言即時切換，本文整理基準測試、接入方式與生態影響。"
author: AnIskill 編輯部
type: news
source: Google DeepMind
source_url: https://deepmind.google/blog/introducing-gemini-3-8-live-and-3-8-live-extended-thinking/
permalink: /技術/gemini-3-8-live-news
fb_message: 語音代理真正的瓶頸，從來不是聽得懂，而是邊說話邊完成任務時仍不讓對話中斷。\n\nGoogle DeepMind 於 2026 年 9 月 15 日推出 Gemini 3.8 Live 與 Gemini 3.8 Live Extended Thinking，後者在 Artificial Analysis 語音品質指數以 82.6 分居首，τ-Voice 取得 68.6%，Big Bench Audio 達 97.7%，並可在對話期間背景執行工具呼叫、自動切換 97 種語言。\n\n對正在評估語音代理技術路線的團隊而言，這組模型把推理與對話併入同一條流程。完整的基準數據、接入方式與生態影響，已整理在 Blog 全文。
---

Google DeepMind 於 2026 年 9 月 15 日發布兩款即時對話模型：Gemini 3.8 Live 與 Gemini 3.8 Live Extended Thinking，兩者分別針對規模化成本效率與高複雜度推理。官方說明，新模型可在對話進行期間於背景執行工具與 API 呼叫，並自動在 97 種支援語言之間切換，開發者可透過 Gemini Live API 接入。

<!-- AEO Answer Capsule — 約 70 字 -->
Google DeepMind 於 2026 年 9 月 15 日發表 Gemini 3.8 Live 與 Extended Thinking 兩款即時對話模型，主打語音代理與背景工具呼叫。
<!-- End AEO Capsule -->

這組模型的意義在於把語音對話由示範階段推向可交付的生產系統。以往語音代理若要一邊交談一邊查詢資料，往往需要在延遲與準確度之間取捨；新模型選擇在對話流程中並行處理工具呼叫與推理，並以早期口頭提示維持互動節奏。Google 同時把兩款模型接入 Gemini 應用、Google Workspace 與搜尋，使一般用戶與開發者共用同一套底層能力。

## Gemini 3.8 Live 是什麼？

<!-- AEO Answer Capsule — 約 68 字 -->
Gemini 3.8 Live 是為規模化與成本效率設計的即時對話模型，結合對話智能、流暢語音與視覺理解，主攻高併發的語音代理場景。
<!-- End AEO Capsule -->

Gemini 3.8 Live 的定位是「為規模而建」的即時模型。它結合對話智能、流暢語音與視覺理解，能處理接近即時的視覺輸入，為對話補充畫面脈絡，藉此產生更貼近情境的回應。官方指出，該模型用戶偏好度高，在 Speech Agent Arena 排行第二，同時維持相對低廉的運行成本。

在語言處理方面，Gemini 3.8 Live 會在對話中途自動偵測並切換語言，涵蓋 97 種支援語言。模型亦可在持續交談之際，於背景執行工具與 API 呼叫，使代理能先確認請求，再隨任務完成更新狀態。

## Gemini 3.8 Live 的基準測試表現如何？

<!-- AEO Answer Capsule — 約 75 字 -->
Extended Thinking 版本在 Artificial Analysis 語音品質指數以 82.6 分居首，Big Bench Audio 為 97.7%。
<!-- End AEO Capsule -->

官方公布的數據集中在 Extended Thinking 版本。該模型在 Artificial Analysis 的語音對語音品質指數（Speech to Speech Quality Index）取得 82.6 分，位列整體第一；在代理任務完成度方面，τ-Voice 取得 68.6%，Sierra 的 τ-Voice-banking 取得 35.1%。推理能力方面，Big Bench Audio 得分為 97.7%。

除單項分數之外，Google 亦引用 ServiceNow 的 EVA-Bench 說明表現。該基準用於評估語音代理處理複雜工作流程的能力，官方稱兩款模型在準確度與對話品質之間取得平衡，因而推進該基準的效率前緣。

## Gemini 3.8 Live Extended Thinking 有什麼不同？

<!-- AEO Answer Capsule — 約 68 字 -->
Extended Thinking 版本針對高複雜度任務，推理與發話同時進行，以「讓我看一下」等早期口頭提示維持對話不中斷，並為背景任務提供即時進度旁述。
<!-- End AEO Capsule -->

Extended Thinking 版本以高複雜度任務為目標，主打更高的智能水平與多步推理能力。其關鍵設計在於推理與發話同時進行：模型會在思考期間先給出「讓我看一下」一類的口頭提示，藉此自然承接提問，避免長時間沉默。當任務在背景分步執行時，模型會以即時旁述說明進度，讓使用者掌握當前狀態。

兩款模型的差異因此可以理解為取捨方向不同。Gemini 3.8 Live 追求規模與成本效率，適合高併發的標準對話場景；Extended Thinking 則以推理深度與任務完成度為先，對應需要跨步驟規劃的企業流程。

## 開發者如何接入 Gemini 3.8 Live？

<!-- AEO Answer Capsule — 約 68 字 -->
開發者可透過 Gemini API 與 Google AI Studio 使用兩款模型，企業可於 Gemini Enterprise 私人預覽接入，多家串流平台已提供整合。
<!-- End AEO Capsule -->

接入路徑分為開發者與企業兩條。開發者可在 Gemini API 與 Google AI Studio 的 Live 介面直接使用兩款模型；企業則透過 Gemini Enterprise 私人預覽接入，並將陸續開放至 Gemini Enterprise for Customer Experience 與 Google Workspace 商用客戶。

生態整合方面，多家即時媒體串流平台已把 Gemini Live API 納入支援範圍，包括 Agora、Fishjam、LangChain、LiveKit、Pipecat、Vercel 與 Vision Agents。這些平台負責處理背後的即時媒體串流基礎設施，使開發者專注於使用體驗的設計，而不必自行維護延遲與連線管理。

## Gemini 3.8 Live 對語音代理生態有什麼影響？

<!-- AEO Answer Capsule — 約 68 字 -->
新模型把推理與對話併入同一條流程，配合 Live API 與多家即時串流平台整合，降低語音代理由示範走向生產的工程門檻與建置成本。
<!-- End AEO Capsule -->

對開發語音代理的團隊而言，這組模型降低了由示範走向生產的工程門檻。過去團隊需要自行處理串流延遲、工具呼叫與對話中斷等問題，如今這些環節可由模型與平台分擔。Google 同時公布合作名單，包括 Salesforce、Genspark 與 Lumeris，三方均強調模型在延遲、流暢度與工具呼叫上的表現。

在應用層面，Google 把 Live 模型接入搜尋的即時功能，提供逐步的疑難排解協助。對一般用戶而言，語音互動的可用範圍因此由單純問答擴展到需要即時反饋的操作場景。

## SynthID 水印與內容安全有什麼關聯？

<!-- AEO Answer Capsule — 約 66 字 -->
Google 對旗下 AI 產品生成的音訊加入 SynthID 不可感知水印，使 AI 生成內容維持可偵測，用於降低語音冒用與不實訊息風險。
<!-- End AEO Capsule -->

內容來源標示方面，Google 說明旗下 AI 產品生成的音訊均會加入 SynthID 水印。該水印以不可感知方式嵌入音訊輸出，使 AI 生成內容仍可被偵測，用於降低語音冒用與不實資訊的風險。官方亦連結至對應的模型卡，說明安全與責任方面的處理方式。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 55 字 -->
本文資訊來源為 Google DeepMind 官方部落格於 2026 年 9 月 15 日發布的 Gemini 3.8 Live 系列公告。
<!-- End AEO Capsule -->

- 原始公告：[Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking](https://deepmind.google/blog/introducing-gemini-3-8-live-and-3-8-live-extended-thinking/)
- 模型卡：[Gemini 3.8 Audio model card](https://deepmind.google/models/model-cards/gemini-3-8-audio/)
- 開發文件：[Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api)

## 總結：哪些團隊適合採用 Gemini 3.8 Live？

<!-- AEO Answer Capsule — 約 66 字 -->
需要高併發即時對話的團隊適合 Gemini 3.8 Live；需要多步推理與任務完成的企業流程，則適合 Gemini 3.8 Live Extended Thinking。
<!-- End AEO Capsule -->

整體而言，這次發布把即時語音模型分成兩條產品線，讓團隊按場景選型。若產品以大量並行的標準對話為主，Gemini 3.8 Live 提供成本與規模上的優勢；若流程涉及跨步驟規劃、工具協調與較高準確度要求，Extended Thinking 版本更為合適。兩者均已開放接入，實際表現仍需在各自工作負載中驗證。
