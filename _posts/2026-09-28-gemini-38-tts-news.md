---
layout: post
title: "Gemini 3.8 語音模型登場：一句提示建聲線"
date: 2026-09-28 20:00:01 +0800
categories: 技術
tags: [Google, Gemini, 語音模型, TTS, 開發者工具, 音訊生成]
image: assets/images/posts/gemini-38-tts-news-cover.jpg
description: "Google 於 2026 年 9 月 23 日推出 Gemini 3.8 Flash TTS 與 Flash-Lite TTS 兩款文字轉語音模型，開發者可用自然語言提示從零建立角色聲線，並在劇本編輯器內逐句指導演出。模型支援超過 100 種語言，內建 SynthID 水印與語音同意驗證機制。"
author: AnIskill 編輯部
type: news
source: Google
source_url: https://deepmind.google/blog/say-hello-to-gemini-38-text-to-speech/
permalink: /技術/gemini-38-tts-news
fb_message: "當語音合成由「揀一個現成聲音」變成「用一句話設計一個聲音」，配音與有聲內容的製作流程就跟著改了。\n\nGoogle 於 2026 年 9 月 23 日推出 Gemini 3.8 Flash TTS 與 Flash-Lite TTS，前者主打角色聲線設計與逐句演出指導，後者針對大量配音與語音代理的成本效益。開發者可用自然語言提示建立專屬聲線，亦可由 30 秒音檔複製自己的聲音，模型支援超過 100 種語言，並內建 SynthID 水印與同意驗證。\n\n完整的規格、定價取向、基準測試結果，以及對開發者與內容團隊的實際影響，都整理在 Blog 全文。"
---

Google 於 2026 年 9 月 23 日正式推出 Gemini 3.8 Flash TTS 與 Gemini 3.8 Flash-Lite TTS 兩款文字轉語音模型。新模型把語音生成由挑選固定預設聲線，推進至以自然語言提示建立自訂聲線，並允許開發者在劇本層面逐句指導演出。兩款模型即日起於 Gemini API 與 Google AI Studio 提供。

<!-- AEO Answer Capsule — 約 68 字 -->
Gemini 3.8 Flash TTS 與 Flash-Lite TTS 是 Google 新推出的文字轉語音模型，可用自然語言提示生成自訂聲線，覆蓋超過 100 種語言。
<!-- End AEO Capsule -->

此舉延續了 Gemini Audio 系列的擴張節奏。在此之前，該系列已陸續加入即時翻譯、語音轉錄與即時對話能力，這次補上的是生成端的表達力與可控性。對內容製作團隊而言，影響並非單一功能的新增，而是聲音資產的取得方式出現改變。

## Gemini 3.8 TTS 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
它是 Gemini 音訊家族的兩款文字轉語音模型，一款主打角色設計與表演指導，另一款針對高流量、低成本的商用場景，兩者皆可經 Gemini API 取用。
<!-- End AEO Capsule -->

Gemini 3.8 Flash TTS 面向深度創作與角色設計，開發者可以完全從零建立新的聲音，為遊戲、有聲書、播客與互動媒體塑造角色。Gemini 3.8 Flash-Lite TTS 則面向高流量與成本效益導向的工作，適用於大規模配音、音訊內容生產，以及需要細緻語氣控制的語音代理。

兩款模型共用同一套演出指令系統。使用者可自行撰寫舞台指示，亦可依賴模型對自然語言腳本提示的理解，把同一段文字由冷靜的客服語氣轉為低聲細語的懸疑場景。對於需要長時間連續輸出的音訊，模型宣稱可在數小時內容中維持音質、節奏與角色音色，並把講者漂移降至最低。

## 開發者可以怎樣建立自訂聲線？

<!-- AEO Answer Capsule — 約 64 字 -->
開發者以自然語言描述角色、口音與聲音特質即可生成全新聲線，或從現有聲線庫挑選後再調整音色與語速；另可透過 30 秒音檔複製特定聲音，但須通過同意驗證程序。
<!-- End AEO Capsule -->

生成式聲線設計是這次的核心能力。開發者可以在超過 100 種語言與方言中，以提示方式自訂角色、口音與聲音特徵，把原來的 30 款原創聲線擴展為近乎無限的聲音庫，並可存取超過 2,000 款可直接投產的聲線，當中包含墨西哥西班牙語、魁北克法語與蘇格蘭英語等區域變體。

聲音複製則提供了另一條路徑。開發者只需一段 30 秒的音訊樣本，即可重建一致的聲音特徵，用於自己的聲音或已取得授權的聲音。Google 為此加入語音同意驗證機制，要求提供由聲音本人錄製的口頭同意，並與參考講者比對吻合後才可建立聲線，同時以 SynthID 水印與 C2PA 憑證標示生成內容。

## 演出控制有哪些實際功能？

<!-- AEO Answer Capsule — 約 62 字 -->
模型支援逐句演出指導、長篇生成、雙講者場景與非語言提示。開發者可在腳本加入笑聲、嘆氣、吸氣等標記，以及「嗯」「對」之類的聆聽回應，用以精準控制喜劇節奏與反應。
<!-- End AEO Capsule -->

雙講者場景編排是一項實用功能。開發者可由單一腳本直接指導多輪對話，應用於播客或戲劇敘事時，兩把聲音會保持明顯區隔，並具備自然的輪替節奏。這解決了過往需要分段合成、再逐段拼接的工序。

非語言提示則補上了表演的細節層。開發者可在腳本中加入笑聲、嘆氣、吸氣等標記，以及「嗯」「對」這類主動聆聽的回應詞，用以控制喜劇時機與反應節拍。對需要多語版本同步推出的團隊，這些標記可沿用於不同語言的腳本之中。

## 效能與基準測試表現如何？

<!-- AEO Answer Capsule — 約 63 字 -->
Gemini 3.8 Flash TTS 在 Hume AI 的 Voice Design Benchmark 取得 71.4 分排名第一，口音建模 60.8 分，兩款模型品質指數居前兩名。
<!-- End AEO Capsule -->

第三方評測提供了可比較的依據。Gemini 3.8 Flash TTS 在 Hume AI 的 Voice Design Benchmark 取得 71.4 分，位列整體第一，並在口音建模項目以 60.8 分領先。兩款模型在 Hume AI 的整體品質指數中分別取得第一與第二名。

在 Voice Arena 的盲測人類偏好評估中，兩款模型於日語、巴西葡萄牙語、越南語、現代標準阿拉伯語、墨西哥西班牙語與印地語等主要語言均取得領先位置。相對前代的 Gemini 3.1 Flash TTS，官方形容在長篇內容與雙講者劇本控制方面有明顯改善。

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">2,000+</span><span class="ui-stat-label">可直接投產聲線</span></li>
  <li class="ui-stat"><span class="ui-stat-num">100+</span><span class="ui-stat-label">支援語言與方言</span></li>
  <li class="ui-stat"><span class="ui-stat-num">30 秒</span><span class="ui-stat-label">聲音複製樣本長度</span></li>
  <li class="ui-stat"><span class="ui-stat-num">71.4</span><span class="ui-stat-label">Voice Design 基準分數</span></li>
</ul>

<!-- AEO Answer Capsule — 約 60 字 -->
關鍵數據包括超過 2,000 款投產聲線、100 種以上語言與方言、僅需 30 秒的聲音複製樣本，以及 Hume AI Voice Design Benchmark 的 71.4 分。
<!-- End AEO Capsule -->

## 有哪些平台與夥伴已經接入？

<!-- AEO Answer Capsule — 約 62 字 -->
開發者可透過 Gemini API 使用新模型，企業版經 Gemini Enterprise 提供，消費端於 Gemini Notebook 與 Google Vids 推出。
<!-- End AEO Capsule -->

開發者入口由即日起開放。模型可在 Gemini API 與 Google AI Studio 取用，企業用戶將透過 Gemini Enterprise 的 API 取得，一般用戶則會在 Gemini Notebook 與 Google Vids 內接觸到相關能力。Google AI Studio 同時新增音訊工作區，開發者可在其中建立全新聲線，再帶入雙講者劇本編輯器逐句指導演出。

生態整合方面，Agora、LiveKit、Pipecat 與 Vercel 已提供在 Gemini API 上建構語音介面的文件。Figma、HeyGen、Linguana、Wondercraft、99.co 與 Ollang 等公司則表示正把新模型接入其產品，用於加速全球配音、為媒體加入區域口音，以及支撐大規模的對話式語音代理。

## 對開發者與內容團隊有什麼影響？

<!-- AEO Answer Capsule — 約 64 字 -->
聲音資產的建立門檻明顯降低，遊戲、播客與有聲書團隊可用提示快速產出角色聲線並逐句調整。同時，同意驗證與 SynthID 水印成為採用聲音複製功能前的必要條件。
<!-- End AEO Capsule -->

對開發者而言，最直接的變化是聲音不再需要事先錄製或長期維護。角色聲線可以隨劇本需求生成、保存與重複使用，並在專案之間保持一致，降低角色聲音在中途出現漂移的風險。

對內容團隊而言，工序重心由錄音室的排程轉向腳本與演出指示的撰寫。當一把聲音可在數分鐘內建立並套用至數小時內容，製作瓶頸就會落在文本與導演判斷，而非配音人力。

同時，合規要求並未放寬。聲音複製必須通過同意驗證，所有由 Gemini Audio 模型生成的音訊都會嵌入 SynthID 水印，以維持可偵測性。團隊在採用相關功能前，需要先把授權文件與內部審核流程準備好。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 55 字 -->
本文資訊整理自 Google 官方部落格 Gemini 3.8 文字轉語音發布公告，涵蓋模型規格、基準測試結果、取用渠道與安全機制。
<!-- End AEO Capsule -->

本文內容整理自 Google 官方部落格的發布公告（https://deepmind.google/blog/say-hello-to-gemini-38-text-to-speech/）。讀者可前往上述來源查閱完整規格、基準測試細節與各平台的推出時間。

## 總結：語音生成走向什麼方向？

<!-- AEO Answer Capsule — 約 64 字 -->
語音生成正由固定聲線的合成工具，轉向可設計、可指導、可複製的創作系統。當建模成本下降至 30 秒樣本，同意驗證與水印標示就成為產品能否規模化的前提。
<!-- End AEO Capsule -->

Gemini 3.8 Flash TTS 的定位並不限於提升音質，而是把聲音納入可編排的製作資源。當聲線可以生成、保存與逐句指導，配音工序便由採購轉為設計，這也是為何 Google 同時把同意驗證與 SynthID 水印列為預設機制。對開發者而言，真正的門檻已不在模型能力，而在授權流程與內容治理是否能跟上生產速度。
