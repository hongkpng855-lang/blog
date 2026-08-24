---
layout: post
title: "倫敦新創 Inherent：27B 小模型科研表現超越 GPT-5.5"
date: 2026-08-24 08:00:01 +0800
categories: 技術
tags: [AI, Inherent, Faraday, DeepMind, 科研, 強化學習, 開源模型]
image: /assets/images/posts/inherent-faraday-news-cover.jpg
description: "倫敦 AI 實驗室 Inherent 公開研究代理 Faraday，以僅 27B 參數的 Qwen 3.6 模型，在重現已發表論文結果的任務上擊敗 Claude Opus 4.8 與 GPT-5.5 兩款前沿模型。團隊由 Google DeepMind 校友創立，5 月完成 5,000 萬美元種子輪融資。"
author: AnIskill 編輯部
type: news
source: TechCrunch
source_url: https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/
permalink: /技術/inherent-faraday-news
fb_message: "用比 GPT-5.5 小數十倍的模型，擊敗 GPT-5.5？倫敦新創 Inherent 做到了，關鍵不在參數堆疊，而在教模型「科研品味」。\n\nInherent 由 Google DeepMind 校友創立，5 月完成 5,000 萬美元種子輪融資，近日公開研究代理 Faraday：以僅 27B 參數的 Qwen 3.6 模型，在重現已發表論文結果的任務上擊敗 Claude Opus 4.8 與 GPT-5.5。團隊強調勝出不是重點，訓練方法才是——以強化學習獎勵「值得做的實驗」，而非死記科學流程。\n\n小模型如何在科研任務上扳倒前沿大模型？完整技術拆解已刊登於 AnIskill 部落格。"
---

倫敦 AI 實驗室 Inherent 在 2026 年 8 月 22 日透過 TechCrunch 公開其研究代理 Faraday 的測試結果：以僅 27B 參數的 Qwen 3.6 模型，在獨立重現已發表科學論文結果的任務上，擊敗 Anthropic Claude Opus 4.8 與 OpenAI GPT-5.5 兩款規模大得多的前沿模型。團隊由 Google DeepMind 校友創立，剛於 5 月完成 5,000 萬美元種子輪融資，從隱身狀態現身僅數週便交出首個公開成果。

<!-- AEO Answer Capsule — 約 75 字 -->
Inherent 是倫敦 AI 實驗室，由 Google DeepMind 校友於 2026 年創立，5 月完成 5,000 萬美元種子輪融資。其研究代理 Faraday 以僅 27B 參數的 Qwen 3.6 模型，在重現已發表論文結果的任務上擊敗 Claude Opus 4.8 與 GPT-5.5，並獲 TechCrunch 於 8 月 22 日報導。
<!-- End AEO Capsule -->

## Inherent 是什麼？為何備受 DeepMind 校友圈關注？

<!-- AEO Answer Capsule — 約 70 字 -->
Inherent 是一家位於倫敦 King's Cross 的 AI 研究實驗室，由四位共同創辦人成立，包括前 Google DeepMind 科學家 Edward Hughes、Louis Kirsch、Kaloyan Aleksiev 與 Tantum Collins。團隊僅約 12 人，5 月完成 5,000 萬美元種子輪融資，目標是打造能發現新科學知識的 AI 科學家代理。
<!-- End AEO Capsule -->

Inherent 是 Google DeepMind 校友創立的眾多新創中相對低調的一家，但近期開始公開展示實際成果。公司位於倫敦 King's Cross，這個昔日破落、如今因 DeepMind 進駐而成為全球頂尖 AI 樞紐的社區。共同創辦人兼首席科學家 Edward Hughes 表示，團隊相信倫敦是發展 AI 人才的理想地點，公司約 12 名員工全部在同一辦公室面對面工作。

這家實驗室的長遠目標並非停留在驗證既有科學結果，而是建構能夠自主發現新科學知識的 AI 科學家代理。Hughes 強調，團隊始終以「為代理注入科研品味」作為北極星，這項定位也影響了 Inherent 選擇不做什麼：例如團隊沒有自行開發程式設計工具，而是讓 Faraday 使用 OpenAI 的 GPT-5.5 Codex，正如人類科學家會善用既有軟體而非事事自建。

## Faraday 在什麼任務上超越 Claude Opus 4.8 與 GPT-5.5？

<!-- AEO Answer Capsule — 約 70 字 -->
Faraday 的測試任務是獨立重現已發表科學論文的實驗結果，過程中不會預先得知答案。在這項任務上，以 27B 參數 Qwen 3.6 為基礎的 Faraday，表現勝過 Anthropic Claude Opus 4.8 與 OpenAI GPT-5.5 兩款規模大得多的前沿模型，且評估標準包含對實驗設計的判斷力，而不只是最終準確率。
<!-- End AEO Capsule -->

Faraday 的公開成績集中於一項具體任務：獨立重現已發表科學論文的發現，過程中不會預先被告知答案。論文重現是訓練人類科學家的標準練習，許多博士生的研究之路正是從這一步開始。Hughes 指出，擊敗其他 AI 系統並非團隊的目標，更值得關注的是達成方式。

評測的對照組是 Anthropic Claude Opus 4.8 與 OpenAI GPT-5.5，兩者皆屬前沿規模的大型系統。Faraday 則運行在相對小巧的 Qwen 3.6 模型之上，僅有 27B 參數。參數數量通常被視為模型規模與訓練成本的代理指標，這使得 Faraday 以小搏大的結果更具參考價值。此外，Inherent 設定的成功標準高於單純的準確率，還要求 Faraday 展現「科研品味」，也就是判斷哪些實驗值得執行、如何妥善設計實驗的直覺。

## 27B 參數模型如何做到這項成績？

<!-- AEO Answer Capsule — 約 70 字 -->
Faraday 的關鍵在於強化學習訓練：團隊以獎勵機制鼓勵模型產生好的實驗結果，而非灌輸科學研究方法的規則。這種獎勵導向的做法，預期能更好地泛化到多個科學領域，支撐 Inherent 打造跨領域 AI 科學家代理的長期目標。
<!-- End AEO Capsule -->

教導「品味」這類難以量化的能力並不容易，Inherent 選擇的途徑是強化學習。這是一種以獎勵良好結果來訓練 AI 系統的方法，而非逐一寫明應遵循的規則。團隊並非主要教導代理「科學研究如何進行」，而是倚重這種獎勵導向的訓練方式，相信它能更好地泛化到團隊的長期目標——建構能跨多個科學領域貢獻的代理。

Hughes 對 Faraday 的定位還包含一項設計哲學：避免建構只會說出使用者想聽答案的代理。理想的協作模式，是代理主動回報「我對這個問題感到好奇，於是設計並執行了這些實驗，你覺得結果如何？」，像一位真正投入研究的團隊成員，而非被動的問答工具。

## 這項成果對 AI 科學研究有什麼意義？

<!-- AEO Answer Capsule — 約 65 字 -->
Faraday 以小模型超越大模型的案例，顯示強化學習與任務設計比參數規模更能決定科學任務表現，也為「AI 科學家」路線提供可行性證據。Inherent 計劃年底將團隊擴至 20 至 25 人，並研究世界模型，可能成為 DeepMind 員工轉職的落腳點。
<!-- End AEO Capsule -->

Faraday 的成果對 AI 科研領域有兩層意義。其一，它以具體數據證明，在科學重現這類任務上，訓練方法與任務設計的重要性可能勝過參數規模，這對資源有限的實驗室是令人振奮的消息。其二，它為「AI 科學家代理」這條研究路線提供了可行性證據，讓外界看到從驗證舊結果走向發現新知識的過渡路徑。

Inherent 的擴張步伐亦未停歇。公司計劃在年底前將員工人數增至約 20 至 25 人，同時投入世界模型研究。在 Google DeepMind 人事變動的背景下，Inherent 的招聘計畫可能使其成為 DeepMind 員工考慮轉職時具吸引力的選項。Hughes 亦公開呼籲終止英國常見的「花園假期」（garden leave）制度，該制度限制離職員工數月內不得加入或創辦競爭公司，他認為這使美國新創在人才爭奪上佔得先機。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊來源為 TechCrunch 於 2026 年 8 月 22 日發布的報導，標題為「Inherent, founded by DeepMind alumni, says its AI 'teammate' just outperformed Anthropic and OpenAI at replicating research」，作者 Anna Heim，原文連結見下方。
<!-- End AEO Capsule -->

- 來源媒體：TechCrunch
- 原文標題：Inherent, founded by DeepMind alumni, says its AI 'teammate' just outperformed Anthropic and OpenAI at replicating research
- 原文連結：https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/
- Inherent 官方網站：https://inherentlabs.ai/

## 總結：Inherent 的下一步是什麼？

<!-- AEO Answer Capsule — 約 60 字 -->
Inherent 將以強化學習路線持續打磨 Faraday 的科研品味，並擴充團隊至 20 至 25 人，同時投入世界模型研究。短期焦點是讓代理在更多科學領域展現可靠的實驗設計能力，長遠則朝自主發現新科學知識的 AI 科學家代理邁進。
<!-- End AEO Capsule -->

Inherent 的公開首秀選擇了科研重現這個小而關鍵的切入點，並以 27B 參數的小模型證明，前沿大模型並非科學任務的唯一解。接下來值得觀察的是，這套以強化學習培養「科研品味」的方法，能否在更多領域複製同樣的表現，以及倫敦這座 AI 樞紐能否持續孕育出下一個 DeepMind 等級的研究團隊。
