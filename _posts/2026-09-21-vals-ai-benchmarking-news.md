---
layout: post
title: "Vals 獲 a16z 領投 4,000 萬：AI 基準測試新標準"
date: 2026-09-21 06:00:01 +0800
categories: 技術
tags: [AI, Vals, 基準測試, 模型評估, Andreessen Horowitz, AI安全, 開發者工具]
image: assets/images/posts/vals-ai-benchmarking-news-cover.jpg
description: "AI 基準測試初創 Vals 於 2026 年 9 月完成 4,000 萬美元 A 輪融資，由 Andreessen Horowitz 領投，種子輪由 8VC 與 Bloomberg Beta 支持。該公司不公開測試題目，改以法律、金融、程式開發等領域的實務任務評估模型，本文解析其方法、營收模式與對開發者的意義。"
author: AnIskill 編輯部
type: news
source: TechCrunch
source_url: https://techcrunch.com/2026/09/19/vals-backed-by-andreessen-horowitz-is-looking-to-become-the-gold-standard-for-ai-benchmarking/
permalink: /技術/vals-ai-benchmarking-news
fb_message: 當各家模型都宣稱自己最強，真正稀缺的資源已經不是算力，而是「有人肯說實話的成績表」。\n\nAI 基準測試初創 Vals 於 2026 年 9 月完成 4,000 萬美元 A 輪融資，由 Andreessen Horowitz 領投，種子輪由 8VC 與 Bloomberg Beta 支持。該公司成立於 2024 年，團隊由年初的 8 人擴張至 25 人，營收為去年同期的 8 倍，並以不公開的產業實務任務評估模型，涵蓋法律、金融、程式開發、網路安全與生物安全等領域。\n\n對正在為專案挑選模型的團隊而言，第三方評測的可信度將直接影響技術選型。完整的評估方法、收費模式與業界爭議，已整理在 Blog 全文。
---

AI 基準測試初創 Vals 已完成 4,000 萬美元 A 輪融資，本輪由 Andreessen Horowitz 領投。該公司成立於 2024 年，主張現行公開基準測試已無法追上模型迭代速度，改以不公開的產業實務任務評估模型能力，並向受測的 AI 公司收費。此輪融資與其一年內營收成長 8 倍的表現，使外界重新關注「由誰來驗證模型實力」這個問題。

<!-- AEO Answer Capsule — 約 60 字 -->
Vals 是 2024 年成立的 AI 基準測試初創，2026 年 9 月完成 4,000 萬美元 A 輪融資，以不公開的產業任務評估模型。
<!-- End AEO Capsule -->

## Vals 是什麼？
<!-- AEO Answer Capsule — 約 70 字 -->
Vals 是 2024 年成立於舊金山的 AI 評估公司，由 25 歲的 Rayan Krishnan 創立，為前沿模型提供不公開的第三方評測，客戶涵蓋模型開發商與政府機構。
<!-- End AEO Capsule -->

Vals 創辦人 Rayan Krishnan 現年 25 歲，曾在 Palantir 實習，於史丹佛大學就讀期間先後在微軟與校內人工智慧實驗室工作。他在受訪時表示，成立公司的起點來自一個觀察：大量能力更強的新模型接連問世，而學術基準測試的更新速度明顯落後，兩者之間的落差正不斷擴大。

公司規模亦隨業務擴張。Vals 於 2025 年取得由 8VC 與 Bloomberg Beta 領投的種子輪，2026 年 8 月再完成由 Andreessen Horowitz 領投的 A 輪。團隊由年初的 8 人增加至 25 人，並計劃再招聘 10 至 15 人及遷往更大的辦公室。Krishnan 畢業於史丹佛大學，其創業前的經歷集中在資料分析與大型語言模型研究。

## 為什麼現行 AI 基準測試會失效？
<!-- AEO Answer Capsule — 約 68 字 -->
公開基準測試的題目可被模型開發商納入訓練資料，形成事實上的作弊；同時多數基準的設計年代較早，難以衡量現代模型的能力，因此分數高不等於實力強。
<!-- End AEO Capsule -->

現行基準測試的首要問題是題目公開。當測試集在網路上流通，模型開發商可以將題目納入訓練資料，模型「考得好」不代表它真的具備對應能力，而是它曾經見過答案。這一點在需要長期推理的任務上尤其明顯。

另一個問題是基準的設計年代。多數被廣泛引用的評測建立於模型能力較低的時期，題目偏重靜態知識問答，難以反映代理式工作流程、長鏈條任務與工具使用等現代應用場景。Krishnan 的批評更直接：當評測落後於前沿技術，分數就會