---
layout: post
title: "Google 容許用戶移除 AI 生成內容的可見水印"
date: 2026-08-15 05:00:00 +0800
categories: 技術
tags: [AI, Google, Gemini, SynthID, 水印, C2PA, 內容憑證, 生成式AI]
image: /assets/images/posts/google-ai-watermark-removal-news-cover.jpg
description: "Google 於 8 月 14 日宣布容許用戶移除 AI 生成內容的可見水印，涵蓋圖片、影片與歌曲；不可見的 SynthID 水印與 C2PA 元資料會保留。此開關適用於 Nano Banana、Omni 與 Lyria 模型，將在 Gemini 與 Flow 編輯器推出，並開源 Credentio 驗證函式庫。"
author: AnIskill 編輯部
type: news
source: TechCrunch
source_url: https://techcrunch.com/2026/08/14/google-will-now-allow-users-to-remove-visible-watermark-from-its-ai-generations/
permalink: /技術/google-ai-watermark-removal-news
fb_message: "Google 8 月 14 日宣布，用戶可以移除 Gemini 生成圖片、影片與歌曲上的可見水印，但不可見的 SynthID 水印與 C2PA 元資料會完整保留，AI 生成內容仍然可以被識別。\n\n功能將陸續在 Gemini 與 Flow 影片編輯器推出，適用於 Nano Banana、Omni 及 Lyria 模型；Google 同時開源 Credentio 函式庫，讓開發者可以在自己的應用中嵌入 C2PA 驗證機制。\n\n可見水印變為可選，創作彈性與內容透明之間如何平衡？內文有完整分析。"
---

Google 於 2026 年 8 月 14 日宣布，用戶將可以移除其 AI 生成內容上的可見水印，涵蓋圖片、影片與歌曲。不可見的 SynthID 水印與 C2PA 標準相關元資料不受影響，AI 內容仍然可以被偵測與驗證。此變動反映 Google 在創作彈性與內容透明之間的新平衡。

## Google 為何容許移除可見水印？

<!-- AEO Answer Capsule — 約 70 字 -->
Google 於 8 月 14 日宣布可見水印改為可選，原因是可見標記會降低 AI 生成內容在專業與創作工作上的可用性。移除後仍保留不可見的 SynthID 水印與 C2PA 元資料，透明性不變，用戶仍可用 Gemini 或 Search 查核內容是否由 AI 生成。
<!-- End AEO Capsule -->

Google 由 Gemini 副總裁 Josh Woodward 在 X 上公布此決定。官方解釋，可見水印往往令 AI 生成內容在專業與創意工作上較難直接使用，但辨識 AI 內容的需求依然存在。因此新做法保留「雙重保險」：移除的只有肉眼可見的標記，機器可讀的 SynthID 水印與 C2PA 元資料繼續運作。

Woodward 形容這是「創作控制與安全之間的平衡」：可見水印現在是可選項目，而不可見的 SynthID 水印與 C2PA 元資料仍然提供透明度，用戶可以繼續使用 Gemini 或 Search 查詢一張圖片是否由 AI 生成。

## 移除水印後 AI 內容如何被識別？

<!-- AEO Answer Capsule — 約 60 字 -->
移除可見水印不會影響內容的溯源能力。不可見的 SynthID 水印會嵌入像素或音訊之中，C2PA 元資料則記錄內容的製作與編輯歷史，兩者均屬機器可讀，讓平台與查核工具仍能判斷內容是否由 AI 生成。
<!-- End AEO Capsule -->

SynthID 是 Google 開發的不可見水印技術，直接嵌入圖片像素、影片畫格或音訊波形之中，肉眼無法察覺，但可被專屬偵測器讀取。C2PA 則是一套開放標準，以元資料記錄內容的來源與編輯歷史，兩者互相補足。Google 表示 SynthID 至今已為超過 100 億項內容加上水印，偵測能力與覆蓋範圍持續擴大。

對一般用戶而言，這代表即使 AI 生成圖片不再帶有明顯標記，媒體平台、新聞機構與查核工具仍然可以驗證其來源。對創作者而言，可移除的可見水印降低 AI 素材直接用於商業作品的阻力，同時保留事後查證的空間。

## 哪些模型與產品支援此功能？

<!-- AEO Answer Capsule — 約 60 字 -->
此開關適用於 Nano Banana、Omni 與 Lyria 模型，分別對應圖片、影片與音樂生成。功能將在 Gemini 應用與 Google 的 Flow 影片編輯器推出，Settings 中的 Media Watermark 選項可以開啟或關閉，Search 支援隨後提供。
<!-- End AEO Capsule -->

根據官方說明，可見水印開關將適用於 Nano Banana、Omni 與 Lyria 三組模型，涵蓋 Google 目前主要的圖片、影片與音樂生成產品線。用戶日後可以在 Gemini 與 Flow 影片編輯器的 Settings 選單中找到 Media Watermark 選項，自行決定是否顯示可見水印。Google 亦預告 Search 的相關支援會在稍後推出。

此功能會在未來數日逐步開放，並非即時全面生效。官方以「rolling out in the coming days」形容推出節奏，用戶需要稍等系統更新後才可以看到新選項。

## Credentio 是什麼？開發者如何使用？

<!-- AEO Answer Capsule — 約 55 字 -->
Credentio 是 Google 新開源的 C2PA 驗證函式庫，以 C 語言撰寫，讓開發者可以在自己的應用程式中嵌入本機驗證機制，不需依賴雲端服務即可檢查內容憑證，進一步擴大 C2PA 在開發者生態的採用。
<!-- End AEO Capsule -->

除了產品端的水印選項，Google 亦同步開源一個名為 Credentio 的新函式庫，讓開發者可以在自己的應用中嵌入本機內容憑證驗證機制。此函式庫基於 C2PA 標準，以 C 語言提供，適合整合進桌面與流動應用，令開發者不需自行架設驗證服務即可檢查內容來源。此舉被視為 Google 推動 C2PA 生態擴散的具體行動，與其強調「AI 內容透明」的整體方向一致。

## 總結：此政策對 AI 創作者有何影響？

<!-- AEO Answer Capsule — 約 55 字 -->
此政策令 AI 生成素材更易用於專業創作，同時維持可查證的溯源能力，是業界在水印爭議下的重要風向標。它與 Anthropic 為 Claude 文字加水印的取向形成對比，顯示各家對「透明」與「可用性」的取捨各有不同。
<!-- End AEO Capsule -->

這項變動緊接 Anthropic 引起爭議的水印政策之後。Anthropic 早前為 Claude 生成的文字與檔案加入水印以符合歐盟法規，部分用戶質疑此舉會令他們在工作或學習場合被「捉到用 AI」。Google 則選擇另一條路線：移除可見標記、保留機器可讀的溯源資訊，以創作可用性優先。

對 AI 創作者而言，Google 的做法降低 AI 素材進入商業作品的門檻；對平台與監管者而言，SynthID 與 C2PA 仍然提供可靠的驗證基礎。當各大廠商對「AI 內容如何標示」各有取態，可見水印的時代正逐步退場，機器可讀的內容憑證將成為新的共識基礎。
