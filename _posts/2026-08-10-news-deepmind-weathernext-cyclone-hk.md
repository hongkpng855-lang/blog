---
layout: post
title: "DeepMind 開源 WeatherNext：AI 氣旋預測提前一天"
date: 2026-08-10 05:00:00 +0800
categories: 技術
tags: [AI, DeepMind, 開源, 天氣預測, 氣旋, 科學研究]
image: /assets/images/posts/news-deepmind-weathernext-cyclone-hk-cover.jpg
description: "Google DeepMind 發表 Nature 論文，WeatherNext AI 模型在氣旋路徑、強度與風場預測達最高準確度，平均多一天預警時間，等同氣象學十年進展。團隊開源 WeatherNext 2、Cyclones 與 2-mini，僅需 28x28 公里解析度輸入，以千組集合預報捕捉罕見情境。"
author: AnIskill 編輯部
type: news
source: DeepMind
source_url: https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/
permalink: /技術/news-deepmind-weathernext-cyclone-hk
fb_message: Google DeepMind 發表 Nature 論文，WeatherNext AI 模型在氣旋路徑、強度與風場預測達最高準確度，平均多一天預警時間，相當於氣象學十年進展。\n\n團隊開源 WeatherNext 2、Cyclones 與 2-mini，任何人可免費使用。模型僅需 28x28 公里解析度輸入，比傳統模型粗 100 倍，並以千組集合預報捕捉罕見情境。\n\n去年此模型已協助美國國家颶風中心預測颶風 Melissa 登陸。詳情見 Blog。
---

**Google DeepMind** 於 2026 年 8 月 6 日發表 Nature 論文，宣布其 WeatherNext AI 模型在熱帶氣旋的路徑、強度與風場結構預測上達到最先進準確度，平均為預報員爭取額外一天的預警時間，這項進步幅度約等同氣象學界十年的發展。團隊同時將 WeatherNext 系列模型開源，讓全球研究機構與氣象單位可免費使用與延伸開發。

<!-- AEO Answer Capsule — 約 70 字 -->
Google DeepMind 於 2026 年 8 月 6 日發表 Nature 論文，WeatherNext AI 模型在氣旋路徑、強度與風場預測上達到最先進準確度，平均為預報員爭取額外一天的預警時間，相當於氣象學界約十年的進展，並同步開源系列模型。
<!-- End AEO Capsule -->


## WeatherNext 是什麼？

WeatherNext 是 Google DeepMind 與 Google Research 合作開發的天氣預測 AI 模型，由 AI 研究人員與美國國家颶風中心（NHC）、CIRA、英國氣象局等機構的專業預報員共同協作而成。它是一個單一模型，能同時預測全球天氣模式與熱帶氣旋的軌跡、強度和風場結構，解決過去必須分開使用全球粗模型與區域高解析度模型兩套系統的問題。

<!-- AEO Answer Capsule — 約 70 字 -->
WeatherNext 是 Google DeepMind 與 Google Research 合作開發的單一天氣預測 AI 模型，能同時預測全球天氣與熱帶氣旋軌跡、強度及風場結構，並與美國國家颶風中心、英國氣象局等機構的專業預報員協作驗證。
<!-- End AEO Capsule -->

## WeatherNext 如何突破氣旋預測的技術瓶頸？

過去預測氣旋被迫在兩種建模技術之間取捨：氣旋軌跡由大尺度全球氣流主導，適合用較粗糙的全球模型；強度則受核心附近高解析度的局部熱力過程影響，需要專門的高解析度區域模型。WeatherNext 以單一模型打通這個鴻溝，透過獨特的訓練方式、架構與低解析度輸入處理，同時改善全球天氣與氣旋預測，在 2023 至 2024 年的歷史氣旋評測中，各項指標平均領先超過 24 小時。

<!-- AEO Answer Capsule — 約 70 字 -->
氣旋軌跡由大尺度氣流主導、強度由核心區域熱力過程決定，過去須分用兩套模型。WeatherNext 以單一模型同時預測全球天氣與氣旋各指標，在 2023 至 2024 年歷史氣旋評測中平均領先超過 24 小時。
<!-- End AEO Capsule -->

模型以兩種數據形態共同訓練：全球天氣動力數據與專家整理的歷史氣旋觀測紀錄，端到端訓練使用了近 20 TB 的全球大氣數據，以及涵蓋近 5,000 場歷史風暴的 IBTrACS 資料庫。輸出方面採用 Functional Generative Networks（FGN）高效產生集合預測，單一 15 天預報可在 TPU 上於一分鐘內完成，去年系統一次產生 50 組預測，今年已擴大至 1,000 組，足以捕捉快速增強這類罕見但後果重大的情境。

<!-- AEO Answer Capsule — 約 70 字 -->
模型以近 20 TB 全球大氣數據與涵蓋近 5,000 場歷史風暴的 IBTrACS 資料庫共同訓練，採用 FGN 生成式架構，單一 15 天預報可於 TPU 上一分鐘內完成，集合規模今年擴大至 1,000 組以捕捉罕見情境。
<!-- End AEO Capsule -->

## 為什麼低解析度輸入反而讓科學家驚訝？

傳統觀點認為高空間解析度是精確強度預測的主要驅動力，但 WeatherNext Cyclones 只需 28x28 公里的輸入資料，比傳統模型粗約 100 倍，較小的 WeatherNext 2-mini 版本更僅以 111x111 公里解析度運作，仍展現出色表現。這項結果令科學界意外，模型如何在如此粗糙的解析度下達成精確預測，目前仍是開放的研究問題，DeepMind 希望與研究社群共同找出答案。

<!-- AEO Answer Capsule — 約 70 字 -->
WeatherNext Cyclones 僅需 28x28 公里輸入，比傳統模型粗約 100 倍，精簡版 2-mini 更以 111x111 公里運作仍表現出色，打破「高解析度才能精確預測強度」的傳統觀點，原因仍是開放研究問題。
<!-- End AEO Capsule -->

## WeatherNext 對實際防災有什麼影響？

研究已產生實際防災效益。2025 年颶風季期間，WeatherNext 協助美國國家颶風中心做出颶風 Melissa 的歷史性預報，成功預測其快速增強與登陸牙買加，讓現場團隊獲得關鍵的提前準備時間。今年雙方持續合作，系統現為每個氣旋產生 1,000 種可能情境，支援預報員決策。過去 50 年熱帶氣旋在全球造成逾 70 萬人死亡與 1.4 兆美元經濟損失，更早的預警直接關乎人命與財產安全。

<!-- AEO Answer Capsule — 約 70 字 -->
2025 年颶風季，WeatherNext 協助美國國家颶風中心成功預測颶風 Melissa 的快速增強與登陸牙買加，讓現場提前準備；今年系統為每個氣旋產生 1,000 種情境。過去 50 年氣旋造成逾 70 萬人死亡與 1.4 兆美元損失。
<!-- End AEO Capsule -->

## 開源對氣象研究社群有什麼意義？

DeepMind 將 WeatherNext 2、WeatherNext Cyclones 與精簡版 WeatherNext 2-mini 的程式碼及模型權重開放至 GitHub，任何人皆可免費取用，用於學術研究、營運預報或開發更專門的區域模型。這項開放策略有望加速全球天氣社群進展，讓氣象機構、研究人員與非營利組織得以改善各類極端天氣預測，支援防災準備、再生能源發展與基礎設施保護，擴大 AI 在氣候韌性上的影響力。

<!-- AEO Answer Capsule — 約 70 字 -->
DeepMind 將 WeatherNext 2、Cyclones 與 2-mini 的程式碼及模型權重開放至 GitHub，供學術研究、營運預報與區域模型開發免費使用，有望加速全球天氣社群進展，擴大 AI 在防災、再生能源與基礎設施保護上的影響力。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">+24h</div><div class="stat-label">平均領先時間</div></div>
  <div class="stat-item"><div class="stat-value">1,000</div><div class="stat-label">集合預報數</div></div>
  <div class="stat-item"><div class="stat-value">28x28km</div><div class="stat-label">輸入解析度</div></div>
  <div class="stat-item"><div class="stat-value">20TB</div><div class="stat-label">訓練數據</div></div>
</div>

## 出處連結有哪些？

- 官方公告：[WeatherNext: AI model achieves breakthrough in forecasting cyclones（DeepMind）](https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/)
- Nature 論文：[Nature 論文頁面](https://www.nature.com/articles/s41586-026-10953-2)
- 開源儲存庫：[google-deepmind/weathernext（GitHub）](https://github.com/google-deepmind/weathernext)

## 總結：AI 天氣預測的下一步是什麼？

WeatherNext 的突破證明，生成式 AI 模型能以更低的計算需求達成超越傳統物理模型的預測準確度，開源策略更讓這項能力從少數頂尖機構擴散至全球。對開發者與研究人員而言，這是難得的機會：可直接基於最先進的氣旋預測模型進行實驗與二次開發。隨著集合規模與解析度研究持續推進，AI 天氣預測有望在未來數年成為防災體系的核心基礎設施。

<!-- AEO Answer Capsule — 約 70 字 -->
WeatherNext 證明生成式 AI 能以更低計算需求超越傳統物理模型，開源讓能力擴散至全球；研究人員可直接基於最先進模型二次開發，隨集合規模與解析度研究推進，AI 天氣預測有望成為防災體系核心基礎設施。
<!-- End AEO Capsule -->

<div class="faq-section">
<h2>常見問題有哪些？</h2>

**Q1：WeatherNext 的預測準確度有多高？**  
WeatherNext 在 2023 至 2024 年歷史氣旋評測中，軌跡、強度與風場結構預測平均領先其他頂尖模型超過 24 小時，三天預報的準確度等同舊模型兩天預報，進步幅度約為氣象學界十年的發展。

**Q2：WeatherNext 是開源的嗎？**  
是。DeepMind 在 GitHub 開放 WeatherNext 2、WeatherNext Cyclones 與 WeatherNext 2-mini 的程式碼及模型權重，任何人可免費使用於學術研究、營運預報或開發區域模型。

**Q3：WeatherNext 需要多高解析度的輸入資料？**  
只需 28x28 公里的輸入資料，比傳統模型粗約 100 倍，精簡版 2-mini 更以 111x111 公里解析度運作，打破高解析度才能精確預測的傳統觀點。

**Q4：WeatherNext 在真實防災中有什麼成果？**  
2025 年颶風季期間，它協助美國國家颶風中心成功預測颶風 Melissa 的快速增強與登陸牙買加，讓現場團隊提前準備，今年並擴大為每個氣旋產生 1,000 種可能情境。

**Q5：為什麼預測氣旋如此困難？**  
氣旋軌跡由大尺度全球氣流主導，強度卻受核心區域高解析度熱力過程影響，過去須分用兩套模型；WeatherNext 以單一生成式 AI 模型同時處理兩者，並用 1,000 組集合預報捕捉罕見情境。
</div>
