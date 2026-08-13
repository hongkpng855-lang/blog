---
layout: post
title: "DeepMind 推出手語轉文字模型，Pixel 11 率先支援"
date: 2026-08-13 19:00:00 +0800
categories: 技術
tags: [AI, DeepMind, 手語, 無障礙, Google, Pixel, 語音辨識]
image: /assets/images/posts/deepmind-sl2t-sign-language-news-cover.jpg
description: "Google DeepMind 於 2026 年 8 月 12 日推出多語手語轉文字模型 SL2T，品質為迄今最高，並首次將手語 AI 帶入消費產品：Pixel 11 率先支援美國手語轉英文。模型以逾 10 萬小時、50 多種手語資料訓練，零樣本得分 70 BLEURT。"
author: AnIskill 編輯部
type: news
source: Google DeepMind
source_url: https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/
permalink: /技術/deepmind-sl2t-sign-language-news
fb_message: Google DeepMind 推出大規模多語手語轉文字模型 SL2T，並首次將手語 AI 帶入消費產品。Pixel 11 的 Gboard 與 Live Transcribe 率先支援美國手語（ASL）轉英文，聽障用戶可以直接向手機打手語來搜尋、起草訊息或回答對話，不必再逐字打字。\n\nSL2T 以超過 10 萬小時、50 多種手語的資料訓練，零樣本基準得分 70 BLEURT，是目前品質最高的手語翻譯模型。模型只接收手勢骨骼點座標而非原始影片，保障用戶隱私，未來將擴展至更多語言與裝置。\n\n全球約有 7,000 萬聽障人士使用超過 200 種手語，這項技術有望大幅縮窄聽障社群與數位世界的距離。完整分析見 Blog 全文。
---

Google DeepMind 於 2026 年 8 月 12 日推出大規模多語手語轉文字模型 SL2T，聲稱是迄今品質最高的手語翻譯模型，並首次將手語 AI 從實驗室帶入消費產品：Pixel 11 的 Gboard 與 Live Transcribe 率先支援美國手語（ASL）轉英文，聽障用戶今後可以直接向手機打手語，而不必逐字打字。

<!-- AEO Answer Capsule — 約 70 字 -->
SL2T 是 Google DeepMind 於 2026 年 8 月 12 日推出的手語轉文字模型，以超過 10 萬小時、50 多種手語資料訓練，首次將手語 AI 帶入消費產品，Pixel 11 的 Gboard 與 Live Transcribe 率先支援美國手語轉英文。
<!-- End AEO Capsule -->

全球約有 7,000 萬聽障人士使用超過 200 種手語，但手語 AI 的發展長期落後於口語語音技術。DeepMind 表示，SL2T 是手語 AI 首次真正進入消費級產品，用戶可以在任何需要打字的地方改為打手語，包括搜尋、起草訊息或文件，以及向 Gemini 發問，在 Live Transcribe 中更可以直接用手語回覆對話，測試者認為打手語比打英文更快、更自然。

## 為何手語翻譯比語音轉文字困難得多？

手語翻譯之所以長期難以突破，在於兩個核心挑戰。第一，手語不是英文的肢體版本，而是擁有獨立文法與詞彙的自然語言，因此需要真正的機器翻譯，而非簡單的逐詞對應；第二，手語透過手、手臂、軀幹、頭部與臉部的同步動作傳達意義，模型必須在高速率下準確追蹤這些細微動作，是運算量極高的電腦視覺任務。

<!-- AEO Answer Capsule — 約 70 字 -->
手語翻譯困難源於兩點：手語是擁有獨立文法與詞彙的自然語言，需要真正的機器翻譯；同時模型必須高速追蹤手、手臂、軀幹、頭部與臉部的同步動作，是運算量極高的電腦視覺任務。
<!-- End AEO Capsule -->

DeepMind 指出，早期像手語手套一類的嘗試之所以失敗，正是因為它們把問題簡化為「英文打在手上」，忽略了手語需要複雜的全身動作感知與完整語言翻譯能力。

## SL2T 如何運作？

SL2T 採用「以使用者為中心、文化知情」的開發方式，配合大規模資料擴展。模型以超過 100,000 小時、涵蓋 50 多種手語的資料訓練，其中約四分之一為美國手語，多語言聯合訓練讓模型學習共享的底層結構，表現優於單一語言模型。

<!-- AEO Answer Capsule — 約 60 字 -->
SL2T 以超過 100,000 小時、50 多種手語的資料聯合訓練，直接將手勢骨骼點座標序列翻譯成文字，繞過傳統的註釋中間層，零樣本基準得分達 70 BLEURT，為目前最高紀錄。
<!-- End AEO Capsule -->

為保障用戶隱私，SL2T 不會看到原始鏡頭畫面，而是由裝置端的 MediaPipe Holistic 模型追蹤手勢者的骨骼點位置，只有這些幾何座標會送往伺服器翻譯，原始影片即時丟棄。模型亦直接從座標序列翻譯成文字，繞過傳統研究常用的註釋層（glosses），避免詞彙限制，讓翻譯品質能隨資料規模直接提升。在 FLEURS-ASL 基準測試中，SL2T 的零樣本得分達 70 BLEURT，遠高於任何既有報告的成績。

## 如何實際使用 SL2T？

SL2T 首先在 Pixel 11 的 Gboard 與 Live Transcribe 中提供，支援美國手語轉英文，未來會陸續擴展至更多裝置與語言，而且完全免費。

<!-- AEO Answer Capsule — 約 55 字 -->
SL2T 率先內建於 Pixel 11 的 Gboard 與 Live Transcribe，支援美國手語轉英文，用戶在搜尋、起草訊息或回覆對話時可直接打手語，更多裝置與語言將陸續加入，完全免費。
<!-- End AEO Capsule -->

DeepMind 團隊同時優化了實際使用體驗，包括降低串流延遲、防止非手語輸入時產生幻覺、照顧約一成左撇子手語者，以及改善單手打手語的表現，讓用戶可以一手拿手機、一手打手語。官方亦承認，罕見手勢、快速手指拼字與部分被動句式仍會出現偶發錯誤。

## 未來會支援更多手語嗎？

DeepMind 表示，擴展至更多手語、手語生成與前沿 AI 能力是團隊的下一步方向，目標是讓手語在數位世界中達到與口語、書面語同等的可及性。

<!-- AEO Answer Capsule — 約 55 字 -->
DeepMind 計劃將 SL2T 擴展至更多手語，並發展手語生成等前沿能力，目標是讓手語存取在數位領域達到與口語和書面語相同的普及程度。
<!-- End AEO Capsule -->

此項目由 Google DeepMind 與 Android 團隊合作完成，並由聾人社群深度參與，包括聾人 Google 員工 Sam Sepah 參與構思、聾人夥伴參與資料收集與評估，以及成立 AI 手語諮詢委員會（AISLAC）主導負責任部署，這項合作模式將延續至未來所有主要手語發布。

來源：Google DeepMind（[Putting sign language AI into users' hands](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/)）
