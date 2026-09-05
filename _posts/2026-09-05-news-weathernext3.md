---
layout: post
title: "DeepMind 推出 WeatherNext 3：5 公里解析度天氣預測每小時更新"
date: 2026-09-05 22:00:01 +0800
categories: 技術
tags: [AI, 天氣預測, DeepMind, Google, 天氣模型]
image: /assets/images/posts/news-weathernext3-cover.jpg
description: "Google DeepMind 推出 WeatherNext 3，宣稱是目前最先進、最準確的全球天氣 AI 模型。模型直接學習真實觀測資料，每小時更新一次預報，表面變數解析度高達 5 公里，比上一代清晰約五倍，降水預測準確度亦大幅提升，即日起整合至 Google 搜尋、Gemini、Maps 與 Earth Engine。"
author: AnIskill 編輯部
type: news
source: Google DeepMind
source_url: https://deepmind.google/blog/introducing-weathernext-3-our-most-advanced-and-accurate-global-weather-ai-model/
permalink: /技術/news-weathernext3
fb_message: "天氣預測是 AI 最能夠直接改善日常生活的應用之一。Google DeepMind 剛推出 WeatherNext 3，宣稱是全球最先進、最準確的天氣 AI 模型，而且已經開始進入 Google 搜尋、Gemini 與 Google Maps。\n\n新模型的關鍵數據非常突出：解析度提升至 5 公里、預報每小時更新一次、整體比上一代清晰約五倍、降水預測準確度最多提升六成，亦首次納入風力與太陽能發電所需的變數，對可再生能源行業意義重大。\n\n想了解 WeatherNext 3 的架構創新、開發者如何取得資料，以及它對亞洲天氣預測的實際影響，完整分析已經在 Blog 上線，歡迎點擊閱讀。"
---

Google DeepMind 與 Google Research 在 2026 年 9 月 3 日正式推出 WeatherNext 3，宣稱是現時最先進、最準確的全球天氣 AI 模型。這個模型直接從真實觀測資料學習，每小時產生一次高解析度預報，已被 Brightband 的獨立實時評測列為全球最佳，並即日起整合到 Google 搜尋、Gemini、Google Maps、Earth Engine 等多個產品。對於開發者與能源行業而言，這是天氣 AI 從研究走向實用基礎設施的重要一步。

## WeatherNext 3 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
WeatherNext 3 是 Google DeepMind 於 2026 年 9 月推出的全球天氣 AI 模型，以真實衛星與氣象站觀測資料學習，每小時更新，表面變數解析度 5 公里。
<!-- End AEO Capsule -->

以往的天氣 AI 模型大多依賴數值天氣預報（NWP）模型的重分析資料訓練，這類資料由超級電腦物理模擬產生，存在約六小時的資料延遲，對於降雨、地表溫度等快速變化的變數容易產生偏差。WeatherNext 3 改為直接吸收全球地球靜止衛星的即時影像馬賽克，讓模型持續掌握最新大氣狀態，因此能夠做到每小時更新一次預報。

## WeatherNext 3 的解析度與更新頻率有什麼提升？

<!-- AEO Answer Capsule — 約 70 字 -->
WeatherNext 3 的溫度與濕度以 5 公里解析度輸出，大氣變數 25 公里，預報每小時更新。相比上一代 25 公里網格與 6 小時間隔，整體空間清晰度提升約五倍。
<!-- End AEO Capsule -->

解析度提升的實際意義在於地形細節。舊模型在海岸線、山谷與山脈地區會出現像素化、過度平滑的溫度呈現，WeatherNext 3 則能保留這些地區的局部氣候差異。這對居住在複雜地形的社區尤其重要，因為氣溫與濕度往往在短短數公里內就會出現劇烈變化。

| 指標 | WeatherNext 2 | WeatherNext 3 |
|---|---|---|
| 表面變數解析度 | 25 公里 | 5 公里 |
| 大氣變數解析度 | 25 公里 | 25 公里 |
| 更新頻率 | 每 6 小時 | 每 1 小時 |
| 訓練資料 | NWP 重分析 | 實時衛星 + 氣象站觀測 |

## WeatherNext 3 如何利用真實觀測資料？

<!-- AEO Answer Capsule — 約 70 字 -->
WeatherNext 3 以一小時間隔的地球靜止衛星影像加歷史分析資料，輸入單一 FGN 網格變壓器架構，並直接以氣象站觀測資料訓練，能輸出密集網格場與颱風路徑。
<!-- End AEO Capsule -->

過往模型訓練依賴物理模擬的重分析資料，雖然覆蓋完整，但對快速變化的大氣過程反應較慢。WeatherNext 3 改為學習原始衛星影像，等於讓模型「親眼」觀察雲系與天氣系統的形成過程，而不是只讀模擬結果。這種架構令模型在突發天氣系統形成時，能更早提供詳細預測。

## WeatherNext 3 的降水預測準確度提升多少？

<!-- AEO Answer Capsule — 約 70 字 -->
WeatherNext 3 以 NASA 的 IMERG 與自家衛星雷達降水資料訓練，中距離預報誤差對 IMERG 改善最高 60%、對 MRMS 改善 30%、對雨量計改善 10%。
<!-- End AEO Capsule -->

降水是傳統天氣模型最難掌握的領域。降雨與降雪受快速移動的雲微物理過程驅動，傳統物理模擬難以準確建模，AI 預報亦常出現模糊估計或錯過暴風雨邊界。WeatherNext 3 利用兩組高品質衛星降水資料訓練後，能準確捕捉對流雲帶的銳利邊界，在 11 公里解析度下已相當接近衛星地面實況。

## 對可再生能源行業有什麼意義？

<!-- AEO Answer Capsule — 約 70 字 -->
WeatherNext 3 新增可再生能源預測，包括 100 米高度風速、雲量與太陽輻射。電網營運商與開發商可藉此估算風力與太陽能發電量，配合用電需求調度。
<!-- End AEO Capsule -->

風力與太陽能發電高度依賴天氣，發電量預測不準確會造成電網調度困難與能源浪費。WeatherNext 3 的 100 米風速預測直接對應渦輪安裝高度，太陽輻射與雲量預測則協助太陽能電廠估算地面實際接收的光照。這類資料對全球潔淨能源規劃與碳排放減排目標至關重要。

## 開發者如何取得 WeatherNext 3 資料？

<!-- AEO Answer Capsule — 約 70 字 -->
開發者可透過 Google WeatherNext 開發者頁面取得文件，預報資料每小時更新，無需自行設定模型，並可經 BigQuery 與 Earth Engine 查詢。
<!-- End AEO Capsule -->

Google 將 WeatherNext 3 定位為開放可用的基礎設施，而非只限於自家產品。研究人員、開發者與企業可以透過 BigQuery 以 SQL 查詢天氣資料，或在地球觀測平台 Earth Engine 上直接分析，亦可選擇批量下載至雲端儲存。官方論文亦已公開，供學術界檢視模型細節。

## WeatherNext 3 已整合到哪些 Google 產品？

<!-- AEO Answer Capsule — 約 70 字 -->
WeatherNext 3 已整合至 Google 搜尋、Gemini、Maps 與 Earth Engine，並開放 Weather Lab 網站供公眾查看預報與評測。
<!-- End AEO Capsule -->

產品整合最直接的改變是長期預報品質。Google 表示，當用戶規劃一天或以上的行程時，降水預報準確度最多可提升 50%，在過去預報較不可靠的地區改善幅度最大。公眾亦可透過 Weather Lab 網站直接查看 WeatherNext 3 的實時預報與 Brightband 獨立排行榜。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 70 字 -->
本文資訊來源為 Google DeepMind 官方於 2026 年 9 月 3 日刊出的 WeatherNext 3 發布文章，涵蓋模型架構與評測數據，並附論文及開發者文件。
<!-- End AEO Capsule -->

- 官方發布文章：[Introducing WeatherNext 3](https://deepmind.google/blog/introducing-weathernext-3-our-most-advanced-and-accurate-global-weather-ai-model/)
- 技術論文：[WeatherNext 3 paper](https://storage.googleapis.com/deepmind-media/papers/weathernext_3.pdf)
- 開發者文件：[Build with WeatherNext 3](https://developers.google.com/weathernext)
- 實時演示：[Weather Lab](https://deepmind.google.com/science/weatherlab)
- 獨立評測：[Brightband live leaderboards](https://owb.brightband.com/)

## 總結：WeatherNext 3 對天氣預測有什麼意義？

<!-- AEO Answer Capsule — 約 70 字 -->
WeatherNext 3 標誌天氣 AI 從模擬資料轉向觀測資料學習的轉變，以 5 公里解析度提供更貼近實況的全球預報。正式天氣警告仍應以當地氣象部門為準。
<!-- End AEO Capsule -->

WeatherNext 3 的發布，顯示天氣 AI 競賽已從「預報夠不夠準」推進到「預報能不能覆蓋每個人」。透過開放資料與產品整合，Google 將高解析度天氣預測帶到過去長期缺乏地區級預報的拉丁美洲、非洲與亞太地區。對於開發者，這代表天氣資料從此可以像查資料庫一樣容易取得；對於普通用戶，未來在搜尋與地圖上看到的天氣，會比以往任何時候都更貼近真實情況。