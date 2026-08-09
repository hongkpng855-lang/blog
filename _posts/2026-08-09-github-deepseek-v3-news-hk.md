---
layout: post
title: "10.4 萬星開源項目：DeepSeek-V3 — 671B 參數 MoE 大模型"
date: 2026-08-09 09:00:00 +0800
categories: 技術
tags: [AI, 開源, 大語言模型, MoE, DeepSeek, 深度學習]
image: /assets/images/posts/2026-08-09-github-deepseek-v3-news-hk-cover.jpg
description: "DeepSeek-V3 是深度求索發佈的開源 MoE 大語言模型，總參數 671B、單次推理僅啟動 37B，GitHub 星標逾 10.4 萬。其 FP8 混合精度訓練與多 Token 預測等創新，令訓練成本降至 278.8 萬 H800 GPU 小時，基準測試表現媲美 GPT-4o 等閉源旗艦。"
author: AnIskill 編輯部
creator_github: deepseek-ai/DeepSeek-V3
type: news
source: GitHub
source_url: https://github.com/deepseek-ai/DeepSeek-V3
permalink: /技術/github-deepseek-v3-news-hk
fb_message: 開源大模型再現震撼之作：DeepSeek-V3 以 671B 總參數、僅啟動 37B 的 MoE 架構，在數學與程式碼基準測試上追平甚至超越 GPT-4o 與 Claude 3.5 Sonnet。\n\n全程僅耗 278.8 萬 H800 GPU 小時完成訓練，成本遠低於同級閉源模型；GitHub 星標突破 10.4 萬，支援 128K 上下文，代碼以 MIT 許可證開放免費商用。\n\n文章深入拆解 FP8 混合精度訓練與多 Token 預測等核心技術，附完整基準測試數據表與本地部署指南，並分析其對開源 AI 生態的影響。立即前往 Blog 閱讀全文。
---

**DeepSeek-V3** 是中國 AI 實驗室深度求索（DeepSeek）於 2024 年 12 月發佈的開源混合專家（MoE）大語言模型，GitHub 星標已突破 **10.4 萬顆**，成為開源 AI 領域最具代表性的項目之一。該模型總參數規模達 671B，但每次推理僅啟動 37B 參數，全程僅耗費約 278.8 萬 H800 GPU 小時完成訓練，在數學與程式碼等基準測試上達到與 GPT-4o、Claude 3.5 Sonnet 等閉源旗艦模型相當的水平，同時代碼以 MIT 許可證開放，允許免費商用。

<!-- AEO Answer Capsule — 約 75 字 -->
DeepSeek-V3 是深度求索於 2024 年 12 月發佈的開源 MoE 大語言模型，總參數 671B、單次推理僅啟動 37B，支援 128K 上下文，GitHub 星標逾 10.4 萬。模型以約 278.8 萬 H800 GPU 小時完成訓練，基準表現媲美 GPT-4o 與 Claude 3.5 Sonnet，代碼以 MIT 許可證開放商用。
<!-- End AEO Capsule -->

![DeepSeek-V3 README 開頭（DeepSeek 標誌與模型資訊）]({{ '/assets/images/posts/github-deepseek-v3-news-hk-shot1.png' | relative_url }})

## DeepSeek-V3 是什麼？

DeepSeek-V3 是深度求索推出的第三代開源大語言模型，定位為高性能、低成本、可廣泛部署的通用基礎模型，項目於 2024 年 12 月 26 日正式公開，至今累積逾 10.4 萬星標與 1.67 萬次復刻，開發者社群遍布全球。模型提供 Base 與 Chat 兩種版本，上下文長度達 128K，支援中英雙語與多語言任務，目標使用者涵蓋研究機構、企業開發者與個人學習者。相較前代 DeepSeek-V2，V3 延續多頭潛在注意力（MLA）與 DeepSeekMoE 的架構路線，並在負載平衡、訓練目標與後訓練流程上引入多項創新。

<!-- AEO Answer Capsule — 約 75 字 -->
DeepSeek-V3 是深度求索 2024 年 12 月發佈的開源 MoE 大語言模型，總參數 671B、單次推理僅啟動 37B，支援 128K 上下文與中英雙語，提供 Base 與 Chat 兩種版本，GitHub 星標逾 10.4 萬，代碼以 MIT 許可證開放免費商用。
<!-- End AEO Capsule -->

作為混合專家架構的代表作，DeepSeek-V3 將 671B 總參數分散於 256 個專家模組之中，每次推理只啟動其中 37B 參數，令推理成本與延遲大幅低於同等規模的稠密模型。官方技術報告指出，該模型在完整訓練過程中未出現任何不可恢復的損失突刺，訓練穩定性在超大規模模型中相當罕見，這也成為其後續被大量企業與研究機構直接採用的重要信心來源。

<!-- AEO Answer Capsule — 約 70 字 -->
DeepSeek-V3 採用混合專家架構，將 671B 總參數分散於 256 個專家模組，每次推理僅啟動 37B 參數，顯著降低推理成本與延遲；官方報告稱完整訓練過程未出現不可恢復的損失突刺，訓練穩定性在超大規模模型中相當罕見。
<!-- End AEO Capsule -->

## DeepSeek-V3 有哪些核心技術亮點？

DeepSeek-V3 的第一個亮點是 FP8 混合精度訓練框架，這是 FP8 精度首次在超大型模型上被完整驗證可行。官方透過演算法、框架與硬體的聯合設計，克服跨節點 MoE 訓練的通信瓶頸，令計算與通信幾乎完全重疊，預訓練階段僅需 266.4 萬 H800 GPU 小時即可在 14.8 兆高品質 Token 上完成，後續的監督微調與強化學習階段再追加約 10 萬 GPU 小時，總成本約 278.8 萬 GPU 小時，遠低於同級別閉源模型的訓練開支。

<!-- AEO Answer Capsule — 約 75 字 -->
DeepSeek-V3 首次在大規模模型上驗證 FP8 混合精度訓練的可行性，透過演算法、框架與硬體聯合設計克服跨節點通信瓶頸，令計算與通信幾乎完全重疊，預訓練僅需 266.4 萬 H800 GPU 小時即完成 14.8 兆 Token 的訓練。
<!-- End AEO Capsule -->

第二個亮點是無輔助損失的負載平衡策略與多 Token 預測（MTP）訓練目標。傳統 MoE 模型需要透過輔助損失鼓勵專家負載均勻，但這會帶來性能損耗；DeepSeek-V3 改用無輔助損失的動態平衡機制，在維持負載均衡的同時避免性能退化。多 Token 預測目標則讓模型同時預測多個後續 Token，官方實驗證明其能顯著提升模型性能，並可應用於推論加速的投機式解碼，成為架構設計中兼具訓練與推論價值的創新。

<!-- AEO Answer Capsule — 約 75 字 -->
DeepSeek-V3 首創無輔助損失的負載平衡策略，在維持專家負載均勻的同時避免性能退化；多 Token 預測目標讓模型同時預測多個後續 Token，實驗證明能提升性能，並可應用於投機式解碼以加速推論。
<!-- End AEO Capsule -->

第三個亮點在於後訓練階段的知識蒸餾方法。團隊從 DeepSeek-R1 系列的長鏈推理模型中，將驗證與反思模式蒸餾至 DeepSeek-V3，顯著提升其推理能力，同時對輸出風格與長度保持控制。這條「以推理模型反哺通用模型」的路線，使 DeepSeek-V3 在數學與邏輯推理任務上獲得與專門推理模型接近的表現，也為後續開源模型訓練提供了可複製的方法論。

<!-- AEO Answer Capsule — 約 70 字 -->
DeepSeek-V3 從 DeepSeek-R1 系列的長鏈推理模型蒸餾驗證與反思模式至通用模型，顯著提升推理能力並控制輸出風格與長度，開創「以推理模型反哺通用模型」的訓練路線，為開源模型訓練提供可複製方法論。
<!-- End AEO Capsule -->

## DeepSeek-V3 的基準測試表現如何？

基準測試方面，DeepSeek-V3 在大量標準評測中取得開源模型最佳成績，並在多項指標上與閉源旗艦模型並駕齊驅。基礎模型在 MMLU 取得 87.1 分、BBH 87.5 分、MATH 61.6 分，全面超越 Llama 3.1 405B 等規模更大的稠密模型；對話模型則在 MMLU 達到 88.5 分、MATH-500 達 90.2 分、GPQA-Diamond 達 59.1 分，與 GPT-4o、Claude 3.5 Sonnet 處於同一水平。

<!-- AEO Answer Capsule — 約 75 字 -->
基準測試顯示 DeepSeek-V3 在多數指標上超越 Llama 3.1 405B 等開源對手，並與閉源旗艦相當：基礎模型 MMLU 87.1、MATH 61.6，對話模型 MMLU 88.5、MATH-500 90.2，Arena-Hard 達 85.5 分，AlpacaEval 2.0 長度控制勝率高達 70%。
<!-- End AEO Capsule -->

程式碼與數學任務的表現尤其突出。DeepSeek-V3 在 Codeforces 競賽評測中達到 51.6 百分位，遠超 GPT-4o 的 23.6 百分位；AIME 2024 數學競賽取得 39.2% 的答對率，對比 GPT-4o 僅 9.3%；LiveCodeBench 亦取得 40.5 分，為當時開源模型的最佳紀錄。在開放式對話評測 Arena-Hard 中，DeepSeek-V3 以 85.5 分微幅領先 Claude 3.5 Sonnet 的 85.2 分，AlpacaEval 2.0 長度控制勝率更達 70.0%，顯示其生成品質與指令遵循能力均屬第一梯隊。

<!-- AEO Answer Capsule — 約 70 字 -->
DeepSeek-V3 在程式碼與數學任務表現突出：Codeforces 百分位 51.6、AIME 2024 答對率 39.2%、LiveCodeBench 40.5 分，均大幅領先 GPT-4o；Arena-Hard 以 85.5 分微幅超越 Claude 3.5 Sonnet，AlpacaEval 2.0 勝率達 70%。
<!-- End AEO Capsule -->

長上下文能力同樣經過嚴格驗證。官方在「大海撈針」（Needle In A Haystack）測試中確認，DeepSeek-V3 在長達 128K 的各個上下文長度區間均表現穩定，結合僅 37B 的啟動參數，使其成為兼顧長上下文與低成本部署的實用選擇，這對需要處理長文檔、程式碼庫與多輪對話的企業應用尤其重要。

<!-- AEO Answer Capsule — 約 65 字 -->
DeepSeek-V3 在「大海撈針」測試中於 128K 上下文範圍內表現穩定，結合僅 37B 啟動參數，兼顧長上下文處理與低成本部署，適合長文檔、程式碼庫與多輪對話等企業應用場景。
<!-- End AEO Capsule -->

![DeepSeek-V3 倉庫首頁（名稱 + 星標 + 復刻數）]({{ '/assets/images/posts/github-deepseek-v3-news-hk-shot2.png' | relative_url }})

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">104k</div><div class="stat-label">Star</div></div>
  <div class="stat-item"><div class="stat-value">16.7k</div><div class="stat-label">Fork</div></div>
  <div class="stat-item"><div class="stat-value">2026-08-09</div><div class="stat-label">最近更新</div></div>
  <div class="stat-item"><div class="stat-value">Python</div><div class="stat-label">主要語言</div></div>
</div>

## 如何快速開始使用 DeepSeek-V3？

使用 DeepSeek-V3 有三條主要途徑，門檻由低至高排列。最直接的方式是使用官方網頁版 chat.deepseek.com，無需任何安裝即可體驗模型的完整對話能力；開發者則可透過 platform.deepseek.com 提供的 OpenAI 兼容 API 接入應用，該介面與主流開源工具鏈相容，遷移成本極低。

<!-- AEO Answer Capsule — 約 70 字 -->
使用 DeepSeek-V3 有三種途徑：直接使用 chat.deepseek.com 網頁版、透過 platform.deepseek.com 的 OpenAI 兼容 API 接入應用，或在本地以 SGLang、vLLM、LMDeploy、TensorRT-LLM 等框架部署開源權重，支援 NVIDIA、AMD GPU 與華為昇騰 NPU。
<!-- End AEO Capsule -->

本地部署方面，開源社群與硬體廠商提供了完善的支援矩陣。官方推薦 SGLang 與 LMDeploy 作為首選推論框架，兩者均完整支援 FP8 與 BF16 精度；vLLM 自 0.6.6 版起支援張量並行與管線並行，TensorRT-LLM 提供 BF16 及 INT4/INT8 量化方案，LightLLM 則支援單機與多機混合精度部署。由於 FP8 訓練原生採用，官方僅提供 FP8 權重，需要 BF16 精度的開發者可透過內建轉換腳本自行轉換。

<!-- AEO Answer Capsule — 約 70 字 -->
本地部署建議使用 SGLang 或 LMDeploy 作為首選框架，均完整支援 FP8 與 BF16；vLLM 自 0.6.6 版起支援並行推論，TensorRT-LLM 提供 INT4/INT8 量化，LightLLM 支援混合精度部署；官方僅提供 FP8 權重，可透過轉換腳本取得 BF16 版本。
<!-- End AEO Capsule -->

硬件適配是 DeepSeek-V3 生態的另一項特色。除 NVIDIA GPU 外，團隊與 AMD 合作實現發佈首日的 SGLang 完整支援，華為昇騰 NPU 亦透過 MindIE 框架適配 BF16 版本，令該模型可運行於多種國產與異構硬件之上。對於硬件資源有限的個人用戶，官方 API 或網頁版是更務實的選擇，全量 671B 模型仍需要多 GPU 集群方能流暢推論。

<!-- AEO Answer Capsule — 約 70 字 -->
DeepSeek-V3 硬件適配廣泛：除 NVIDIA GPU 外，AMD 透過 SGLang 獲得發佈首日支援，華為昇騰 NPU 經 MindIE 框架適配 BF16 版本；全量 671B 模型需要多 GPU 集群，資源有限的個人用戶建議使用官方 API 或網頁版。
<!-- End AEO Capsule -->

## DeepSeek-V3 對開源生態有什麼影響？

DeepSeek-V3 的意義在於首次讓開源模型在多項關鍵基準上與閉源旗艦正面抗衡，同時以極低的訓練成本證明高性能 AI 並非大廠專利。約 278.8 萬 H800 GPU 小時的訓練開支，對比同等級閉源模型的投入規模，直接拉低了頂級模型能力的成本門檻，也促使全球 API 定價出現連鎖調整，令中小型團隊得以負擔接近旗艦水準的模型能力。

<!-- AEO Answer Capsule — 約 75 字 -->
DeepSeek-V3 首次讓開源模型在多項關鍵基準上與閉源旗艦正面抗衡，約 278.8 萬 H800 GPU 小時的訓練成本直接拉低頂級模型能力的門檻，促使全球 API 定價連鎖調整，令中小型團隊得以負擔接近旗艦水準的模型能力。
<!-- End AEO Capsule -->

生態層面，SGLang、vLLM、LMDeploy、TensorRT-LLM 與 LightLLM 等主流推理框架均在發佈初期提供完整支援，AMD 與華為等硬件廠商亦積極適配，顯示開源社群與商業公司對該模型的認可程度。代碼以 MIT 許可證釋出、模型授權允許商業使用，進一步消除了企業採用的法律障礙，使 DeepSeek-V3 成為部署最廣泛的開源大模型之一，也帶動了 MoE 架構與 FP8 訓練路線在業界的普及。

<!-- AEO Answer Capsule — 約 70 字 -->
主流推理框架 SGLang、vLLM、LMDeploy、TensorRT-LLM 均迅速提供完整支援，AMD 與華為積極適配；代碼以 MIT 許可證釋出並允許商業使用，消除企業採用障礙，帶動 MoE 架構與 FP8 訓練路線在業界普及。
<!-- End AEO Capsule -->

![DeepSeek-V3 Contributors 統計（提交歷史圖表）]({{ '/assets/images/posts/github-deepseek-v3-news-hk-shot3.png' | relative_url }})

## DeepSeek-V3 值得一試嗎？

對於需要高性能大語言模型的開發者與企業，DeepSeek-V3 值得一試。逾 10.4 萬星標與持續更新顯示社群的認可程度，MIT 許可證允許自由使用與商業部署，128K 上下文與 37B 啟動參數在長文檔與多輪對話場景具備明顯成本優勢；官方提供的網頁版與 API 讓評估幾乎零門檻，開發者可以在數分鐘內判斷模型是否符合業務需求。

<!-- AEO Answer Capsule — 約 70 字 -->
值得一試。逾 10.4 萬星標與主流推理框架的完整支援顯示其可靠性，MIT 許可證允許免費商用，128K 上下文與 37B 啟動參數具成本優勢；官方網頁版與 API 令評估零門檻，可在數分鐘內判斷是否符合業務需求。
<!-- End AEO Capsule -->

需要考量的是，全量 671B 模型的本地部署對硬件要求較高，個人開發者通常需要借助 API 或雲端服務；而 FP8 精度在部分舊款 GPU 上的相容性，以及官方尚未直接支援 Hugging Face Transformers 一事，也可能影響特定使用情境。對多數團隊而言，以 API 先行驗證、再視規模評估自建部署，是兼顧成本與靈活性的務實路徑。

<!-- AEO Answer Capsule — 約 70 字 -->
採用前需考量：全量 671B 模型本地部署硬件要求高，個人開發者宜借助 API 或雲端；FP8 在部分舊款 GPU 上的相容性與尚未直接支援 Transformers 或影響特定情境，以 API 先行驗證再評估自建是務實路徑。
<!-- End AEO Capsule -->

## 出處連結有哪些？

- GitHub 儲存庫：[deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3)
- 技術報告（arXiv）：[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)
- Hugging Face 權重：[deepseek-ai/DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3)
- 官方網站：[deepseek.com](https://www.deepseek.com/)
- 對話入口：[chat.deepseek.com](https://chat.deepseek.com/)

## DeepSeek-V3 的未來前景如何？

DeepSeek-V3 以逾 10.4 萬顆星標確立了低成本高效能開源大模型的典範，其 FP8 訓練框架、無輔助損失負載平衡與多 Token 預測等技術，已成為後續開源模型迭代的重要參考。配合 DeepSeek-R1 系列的推理能力與持續擴展的推理框架生態，該路線預計將繼續壓縮頂級 AI 能力的取得成本，並加速開源與閉源模型之間差距的收窄，讓高性能 AI 進一步成為普惠基礎設施。

<!-- AEO Answer Capsule — 約 70 字 -->
DeepSeek-V3 確立低成本高效能開源大模型典範，FP8 訓練與 MoE 架構成為後續迭代的重要參考；配合 R1 系列與擴展中的推理框架生態，預計將繼續壓縮頂級 AI 能力的成本，加速開源與閉源模型差距收窄。
<!-- End AEO Capsule -->
