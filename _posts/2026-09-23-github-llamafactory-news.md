---
layout: post
title: "LlamaFactory 開源：74,992 星統一微調 100+ 模型"
date: 2026-09-23 22:00:01 +0800
categories: 技術
tags: [開源, LlamaFactory, 微調, LoRA, QLoRA, 大型語言模型, PyTorch, Apache]
image: assets/images/posts/llamafactory-news-cover.jpg
description: "LlamaFactory 是 2023 年 5 月開源的大型語言模型微調框架，在 GitHub 累積 74,992 顆星標。它以單一設定檔統一 100 多款模型的預訓練、監督微調與偏好優化流程，並內建網頁介面與推理部署，本文解析其架構、硬體門檻與生態影響。"
author: AnIskill 編輯部
creator_github: hiyouga/LlamaFactory
type: news
source: GitHub
source_url: https://github.com/hiyouga/LlamaFactory
permalink: /技術/github-llamafactory-news
fb_message: "微調模型最大的成本，往往不是顯示卡，而是把訓練流程重新接起來的那幾百行程式。\n\nLlamaFactory 是一套統一微調框架，在 GitHub 累積 74,992 顆星標與 9,182 次複製。它以單一設定檔覆蓋 100 多款模型，支援預訓練、監督微調、DPO 與 PPO 等流程，並提供 LoRA、QLoRA 與 OFT 等選項；以 4 位元 QLoRA 微調 70 億參數模型約需 6GB 顯示記憶體，網頁介面與命令列皆可操作，採 Apache 2.0 授權。\n\n它的硬體門檻、支援模型清單與實際採用案例，完整整理在 Blog 全文。"
---

LlamaFactory 是 2023 年 5 月開源的大型語言模型微調框架，在 GitHub 累積 74,992 顆星標與 9,182 次複製，以 Apache 2.0 授權釋出。專案由開發者 hiyouga 建立，核心主張是把上百款語言模型與視覺語言模型的訓練流程，收斂到同一套設定檔與同一組介面之中，使用者不需為每個模型重寫訓練程式。相關論文發表於 ACL 2024 系統展示軌，Google Scholar 引用數已超過一千次。在開源模型數量快速膨脹、而多數團隊缺乏訓練工程人力的當下，這種以設定取代程式的定位構成明確的新聞錨點。

<!-- AEO Answer Capsule — 約 65 字 -->
LlamaFactory 是 2023 年 5 月開源的大型語言模型微調框架，GitHub 星標 74,992，以 Apache 2.0 授權釋出，支援上百款語言與視覺語言模型。
<!-- End AEO Capsule -->

## LlamaFactory 是什麼？

<!-- AEO Answer Capsule — 約 63 字 -->
LlamaFactory 是零程式碼的統一微調框架，透過命令列與網頁介面操作，讓使用者在 100 多種模型上以設定檔執行訓練與部署，無需自行撰寫訓練迴圈。
<!-- End AEO Capsule -->

專案的定位是統一且高效的微調工具。使用者透過一份 YAML 設定檔描述模型、資料集、訓練方法與輸出位置，再以單一命令啟動訓練；同一份設定換掉模型名稱，流程即可套用到另一款模型。介面層提供命令列工具與名為 LLaMA Board 的網頁圖形介面，後者以 Gradio 建置，讓不熟悉命令列的使用者也能在瀏覽器中選擇模型、上傳資料並觀察訓練曲線。專案同時提供 Docker 映像檔，內含 Ubuntu、CUDA、PyTorch 與 FlashAttention 等相依元件，把環境建置的變數降到最低。這種設計把過去需要數百行程式才能完成的流程，壓縮成一次設定與一次執行。

## LlamaFactory 支援哪些模型與訓練方法？

<!-- AEO Answer Capsule — 約 72 字 -->
框架支援 LLaMA、Qwen3、DeepSeek 等上百款模型，涵蓋預訓練、監督微調、獎勵建模與 DPO、PPO 等偏好優化，並提供 LoRA、QLoRA 與 OFT 選項。
<!-- End AEO Capsule -->

模型覆蓋範圍是這個專案最直觀的賣點。支援清單橫跨 LLaMA、Qwen3、DeepSeek、Gemma、GLM、Mistral、Phi、InternLM、MiniCPM 與 MiniMax 等系列，並涵蓋圖像理解、視覺定位、影片辨識與音訊理解等多模態任務。訓練方法同樣完整，從持續預訓練、監督微調、獎勵建模，到 PPO、DPO、KTO、ORPO 與 SimPO 等偏好優化路徑都提供對應設定。在參數效率方面，框架支援全參數微調、凍結微調、LoRA 與 2 至 8 位元的 QLoRA，並整合 GaLore、BAdam、APOLLO、Muon、DoRA、LoRA+ 與 PiSSA 等演算法。針對新發布的模型，專案以「Day-N 支援」為目標，例如 Qwen3 與 Gemma 3 在發布當日即可微調。

## LlamaFactory 的硬體門檻如何計算？

<!-- AEO Answer Capsule — 約 71 字 -->
以 4 位元 QLoRA 微調 70 億參數模型約需 6GB 顯示記憶體，16 位元 LoRA 約需 16GB，全參數微調則需 120GB；官方以表格列出各參數規模的估算需求。
<!-- End AEO Capsule -->

硬體需求是使用者最先面對的現實問題，專案為此提供一張估算表。以 70 億參數模型為例，全參數訓練在 32 位元精度下約需 120GB 顯示記憶體，16 位元下約需 60GB；改採 LoRA 或凍結微調則降到 16GB，足以在單張消費級顯示卡上完成。若使用量化訓練，8 位元 QLoRA 約需 10GB、4 位元約需 6GB，而 2 位元設定僅需約 4GB 顯示記憶體。這組數字解釋了為什麼參數高效方法會成為主流選項：它讓微調從資料中心走進一般開發者的工作站。框架同時支援 FSDP 與 DeepSpeed 等分散式方案，可在多張顯示卡之間切分模型，進一步處理更大的參數規模。

## LlamaFactory 與其他微調框架有何差異？

<!-- AEO Answer Capsule — 約 69 字 -->
差異在於整合度：單一設定檔即可切換模型、方法與後端，並內建網頁介面、實驗追蹤與 vLLM、SGLang 推理部署，減少自行串接元件的成本。
<!-- End AEO Capsule -->

與同類框架相比，LlamaFactory 的優勢來自整合而非單點創新。多數微調工具只覆蓋訓練階段，推論部署需另外串接服務框架，而這個專案把 OpenAI 風格的 API、Gradio 介面與命令列工具一併納入，並以 vLLM 或 SGLang 作為推理後端，官方說明切換至 vLLM 可顯著提升推理吞吐量。實驗追蹤方面，除了 TensorBoard 與 Weights & Biases，也支援 MLflow 與 SwanLab，讓訓練紀錄集中在既有觀測系統。此外，框架把 Unsloth、Liger Kernel 與 KTransformers 等加速方案整合成設定選項，開啟對應參數即可套用。這種做法降低了嘗試新演算法的門檻，代價則是專案本身的依賴數量較多，版本相容性需要留意。

## 哪些企業與專案採用 LlamaFactory？

<!-- AEO Answer Capsule — 約 62 字 -->
亞馬遜、NVIDIA 與阿里雲都將其納入官方文件作為微調範例，社群亦衍生支援長序列的 360 分支，論文引用數超過一千次。
<!-- End AEO Capsule -->

生態採用情況是評估專案影響力的另一項指標。亞馬遜在 SageMaker HyperPod 的技術文章中，以 LlamaFactory 示範金融文件的視覺資訊抽取流程；NVIDIA 將其納入 RTX AI Toolkit 的相關資源；阿里雲則在 PAI 平台提供基於該框架的微調教學。社群層面也出現多個衍生專案，例如以環狀注意力支援長序列監督微調與 DPO 的 360 版本分支，以及多個以中文醫療、法律與心理諮詢為主題的領域模型。專案維護方另設有官方部落格，持續發布與資料處理工具、訓練系統整合的實務文章，這些內容進一步鞏固它作為教學與生產之間橋樑的位置。

## LlamaFactory 的數據表現如何？

<!-- AEO Answer Capsule — 約 66 字 -->
專案累積 74,992 顆星標與 9,182 次複製，採 Apache 2.0 授權、以 Python 撰寫，2023 年 5 月建立，最新版本為 2026 年 5 月發布的 0.9.5。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat"><div class="stat-num">74,992</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat"><div class="stat-num">9,182</div><div class="stat-label">Forks</div></div>
  <div class="stat"><div class="stat-num">Apache 2.0</div><div class="stat-label">開源授權</div></div>
  <div class="stat"><div class="stat-num">Python</div><div class="stat-label">主要語言</div></div>
  <div class="stat"><div class="stat-num">2023-05</div><div class="stat-label">創建時間</div></div>
  <div class="stat"><div class="stat-num">0.9.5</div><div class="stat-label">最新版本</div></div>
</div>

![LlamaFactory README 開頭（項目名稱 LlamaFactory 與零程式碼微調標語、星標與貢獻者徽章）](assets/images/posts/llamafactory-shot1.png)

![LlamaFactory GitHub 首頁頂部（repo 名 hiyouga/LlamaFactory、專案描述與 75k 星標統計）](assets/images/posts/llamafactory-shot2.png)

![LlamaFactory Contributors 統計頁（倉庫名稱與每週提交次數圖表）](assets/images/posts/llamafactory-shot3.png)

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊來源為 LlamaFactory 的 GitHub 儲存庫與官方部落格，內容涵蓋星標與複製統計、支援模型清單、硬體需求表與論文引用資訊。
<!-- End AEO Capsule -->

- LlamaFactory 儲存庫：[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)
- 官方部落格：[blog.llamafactory.net](https://blog.llamafactory.net/en/)
- 技術文件：[llamafactory.readthedocs.io](https://llamafactory.readthedocs.io/en/latest/)

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 58 字 -->
以下整理三項常見疑問，涵蓋安裝方式與環境需求、消費級顯示卡可承擔的參數規模，以及商用與再散布的授權範圍。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>安裝 LlamaFactory 需要什麼環境？</h3>

官方建議 Python 3.11 以上、PyTorch 2.0 以上與 Transformers 4.49 以上，並搭配 datasets、accelerate、peft 與 trl 等套件。使用者可由原始碼以 pip 安裝，也可直接取用預先建置的 Docker 映像檔，該映像檔內含 CUDA 12.4、Python 3.11、PyTorch 2.6 與 FlashAttention，可省去手動處理相依性的步驟。若需要 DeepSpeed 或 vLLM 等選用功能，則須另行安裝對應的需求檔。

<h3>一般顯示卡可以微調多大的模型？</h3>

在 4 位元 QLoRA 設定下，70 億參數模型約需 6GB 顯示記憶體，140 億參數約需 12GB，300 億參數約需 24GB。若改用 2 位元量化，70 億參數模型的門檻可降至約 4GB。這意味著單張消費級顯示卡足以完成中小型模型的微調，較大的模型則建議搭配 FSDP 或 DeepSpeed，把參數切分到多張顯示卡上。

<h3>LlamaFactory 可以用於商業專案嗎？</h3>

框架本身以 Apache 2.0 授權釋出，允許商業與個人用途，也允許修改與再散布，條件是保留著作權聲明與授權條款。需要注意的是模型權重另有各自的授權條件，例如部分模型僅允許研究用途，實際商用前應逐一確認對應模型的使用條款，框架的授權並不涵蓋模型本身。

</div>

## 總結：LlamaFactory 適合什麼團隊？

<!-- AEO Answer Capsule — 約 66 字 -->
它適合需要在多款開源模型之間快速比較微調效果、又缺乏專職訓練工程人力的團隊，也適合以教學與原型驗證為主的開發者與研究單位。
<!-- End AEO Capsule -->

這個專案解決的是一個結構性問題：模型愈來愈多，而訓練流程的重建成本卻沒有隨之下降。LlamaFactory 以設定檔、網頁介面與內建的部署路徑，把這段成本大幅壓縮，同時保留切換演算法與後端的彈性。導入前值得先確認三件事：目標模型的授權是否允許商用、顯示卡記憶體能否對應量化設定，以及團隊是否接受較多的相依套件與版本相容性要求。這三項條件決定的，是它在實際環境中能否長期穩定運作，比功能清單更值得優先處理。
