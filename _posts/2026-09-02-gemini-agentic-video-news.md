---
layout: post
title: "Gemini 推出 Agentic Video：長影片理解成本大減"
date: 2026-09-02 14:00:01 +0800
categories: 技術
tags: [AI, Gemini, Google DeepMind, 影片理解, API, LLM]
image: assets/images/posts/gemini-agentic-video-news-cover.jpg
description: "Google DeepMind 推出 Agentic Video 影片理解功能，讓 Gemini 3.7 Flash 等模型以更少 token 分析長影片，支援次秒級時刻檢索、異常偵測與動作計數，開發者可透過 Gemini API 設定 processing 參數啟用，費用沿用標準 token 定價。"
author: AnIskill 編輯部
type: news
source: Google DeepMind
source_url: https://deepmind.google/blog/introducing-agentic-video-in-gemini/
permalink: /技術/gemini-agentic-video-news
fb_message: 長影片分析一直是 AI 應用的高成本痛點，Google DeepMind 這次直接從 API 層面解決。\n\nGemini 3.7 Flash 啟用 Agentic Video 後，能在長達數小時的影片中精準找出關鍵時刻，token 消耗大幅下降，LongVideoBench 基準顯示準確度同步提升；功能沿用標準 token 定價，不另收費。\n\n開發者只要在 API 設定將 processing 設為 agentic 即可啟用，完整教學與程式範例已整理在 Blog。
---

Google DeepMind 在 2026 年 9 月 1 日宣佈推出 Agentic Video 影片理解功能，讓旗下 Gemini 模型以顯著較低的 token 成本分析長影片。此功能目前支援 Gemini 3.7 Flash、3.6 Flash 與 3.5 Flash-Lite，透過 Gemini API 與 Google AI Studio 即可使用，開發者只需在設定中將 processing 參數設為 agentic。本文整理此功能的運作方式、支援任務與對開發者的實際影響。

## Agentic Video 是什麼？

<!-- AEO Answer Capsule — 約 75 字 -->
Agentic Video 讓 Gemini 以較低 token 成本分析長影片，設定 processing 為 agentic 即啟用，支援時刻檢索與異常偵測任務。
<!-- End AEO Capsule -->

Agentic Video 的核心概念，是讓模型不再以固定幀率被動掃描整段影片，而是針對查詢內容主動決定「何時看、看哪一段、看多仔細」。官方描述此功能可將影片理解從高成本的批次處理，轉變為更接近人類觀看方式的動態分析。對開發者而言，這項能力直接反映在 API 請求的 token 消耗上，長影片分析的經濟門檻因此大幅下降。

## 它能在長影片中完成哪些任務？

<!-- AEO Answer Capsule — 約 65 字 -->
它能定位次秒級畫面變化、在多小時影片中搜尋特定片段、偵測異常行為，並統計重複動作與物件數量，傳統逐幀分析難以兼顧成本與準確度。
<!-- End AEO Capsule -->

官方列出的能力包括四類。第一是次秒級時刻檢索，可精準找出以每秒一幀分析時容易遺漏的畫面狀態變更與剪接邊界，適合自動化影片剪輯。第二是長影片針海撈針式搜尋，能在跨越數小時的影片中回答複雜查詢，而不消耗數百萬 token。第三是異常偵測，系統會以較高幀率重新取樣感興趣的時間區段，檢查快速動作與細微視覺瑕疵。第四是動作與物件計數，可準確追蹤重複的肢體動作及不同物件在一段時間內的出現。

## 支援哪些模型？如何啟用？

<!-- AEO Answer Capsule — 約 70 字 -->
支援 Gemini 3.7 Flash、3.6 Flash、3.5 Flash-Lite，在 API 設定 processing 為 agentic 即啟用，收費沿用標準 token 定價。
<!-- End AEO Capsule -->

Agentic Video 目前開放於 Gemini API、Google AI Studio 與 Gemini Enterprise Agent Platform，覆蓋 Gemini 3.7 Flash、3.6 Flash 與 3.5 Flash-Lite 三個模型。啟用方式非常簡單，開發者只需在 API 設定的影片輸入中將 processing 欄位設為 agentic，官方同時提供完整的開發者指南。Google 也計劃把這項效率與品質提升帶入 Gemini 應用程式，未來數月內將逐步開放給所有使用 Flash 與 Flash-Lite 模型的用戶，並應用於 YouTube 的 Ask YouTube 功能。

## 對開發者有什麼影響？

<!-- AEO Answer Capsule — 約 65 字 -->
開發者無需自建影片摘要管線，能以更少 token 完成長影片問答與分析，官方也計畫將功能帶入 Gemini 應用程式與 YouTube 問答功能。
<!-- End AEO Capsule -->

對開發者來說，這項功能最直接的價值在於成本結構的改變。官方在 LongVideoBench 長影片理解基準上的對比顯示，啟用 Agentic Video 後 token 消耗大幅減少，同時準確度提升；動態幀率機制讓模型能準確計算快速動作，例如透過以不同幀率重複掃描影片來計算快速移動的次數。早期參與測試的合作夥伴回報了強勁的測試表現，意味著這項能力已具備實際生產環境的可用性。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 55 字 -->
本文資訊來源為 Google DeepMind 官方部落格於 2026 年 9 月 1 日發佈的 Agentic Video 介紹文章，原始連結見下方。
<!-- End AEO Capsule -->

- [Introducing agentic video understanding with Gemini](https://deepmind.google/blog/introducing-agentic-video-in-gemini/)

## 總結：這個功能適合什麼場景？

<!-- AEO Answer Capsule — 約 70 字 -->
Agentic Video 讓長影片理解從高成本批次處理轉為日常可用能力，適合需要影片檢索、內容審查與自動剪輯的開發團隊，標準 API 定價降低採用門檻。
<!-- End AEO Capsule -->

Agentic Video 的出現，將影片分析的主流模式從「整段影片固定抽幀」推進到「依查詢動態取樣」，對影片檢索、內容審查、運動分析與自動剪輯等應用有直接幫助。對預算有限的開發團隊而言，標準 token 定價加上顯著的 token 節省，使得處理長時間影片的服務更具可行性。隨著 Gemini 應用程式與 YouTube 陸續整合此能力，一般使用者也可望在未來數月內感受到長影片問答體驗的改善。