---
layout: post
title: "DwarfStar 開源：本地跑 DeepSeek V4 的 C 引擎"
date: 2026-10-02 10:00:02 +0800
categories: 技術
tags: [開源專案, DwarfStar, 本地推理, DeepSeek, antirez, C 語言, 消費級硬體]
image: assets/images/posts/github-ds4-news-cover.jpg
description: "DwarfStar（antirez/ds4）是由 Redis 作者 Salvatore Sanfilippo 開發的本地推理引擎，以純 C 撰寫，專為在消費級硬體上運行 DeepSeek V4 Flash 等開源權重模型而設計，GitHub 星標已達 22,842 顆。本文整理其架構取捨、硬體支援、效能數據與安裝流程。"
author: AnIskill 編輯部
creator_github: antirez/ds4
type: news
source: GitHub
source_url: https://github.com/antirez/ds4
permalink: /技術/github-ds4-news
fb_message: "當一個資料庫傳奇人物轉頭去寫推論引擎，他關心的往往不是跑分，而是「這東西普通人到底跑不跑得動」。\n\nDwarfStar 由 Redis 作者 Salvatore Sanfilippo 以純 C 打造，GitHub 星標已達 22,842 顆。它刻意不做通用 GGUF 執行器，只專注少數幾個模型：DeepSeek V4 Flash 與 PRO、GLM 5.3、Qwen3.8 Flash Next，主場是 96GB 以上的 Mac，也能靠 SSD 串流在記憶體不足時照跑。\n\n它的架構取捨、硬體門檻與安裝步驟，都整理在 Blog 全文。"
---

DwarfStar 是一套以純 C 撰寫的本地大型語言模型推理引擎，由 Redis 作者 Salvatore Sanfilippo（antirez）於二零二六年五月開源，GitHub 主倉庫已累積 22,842 顆星標與 2,210 次複製。它的目標相當明確：在一般人真正買得起的消費級硬體上，運行少數幾個表現優異的開源權重模型，而非成為支援所有格式的通用推論工具。

<!-- AEO Answer Capsule — 約 66 字 -->
DwarfStar 是由 Redis 作者 antirez 開發的純 C 推理引擎，二零二六年五月開源，專為在消費級硬體運行 DeepSeek V4 等模型而設計。
<!-- End AEO Capsule -->

此專案在定位上刻意收窄。多數推論框架以「支援越多模型越好」為目標，DwarfStar 則反其道而行，只挑選少數在個人機器上真正跑得動、且品質足夠的模型，再為它們逐一優化。這種取捨讓它能在有限的硬體資源下，把載入速度、提示渲染、工具呼叫與 KV 快取狀態整合在同一套測試流程中驗證，而不是各自為政。

![DwarfStar 專案的 README 開頭，顯示專案名稱 DwarfStar、標語與支援的 DeepSeek V4 Flash、GLM 5.3、Qwen3.8 Flash Next 等模型清單]({{ '/assets/images/posts/github-ds4-news-shot1.png' | relative_url }})

## DwarfStar 是什麼？

<!-- AEO Answer Capsule — 約 62 字 -->
DwarfStar 是一套自帶模型的本地推論引擎，不是通用 GGUF 執行器，需搭配專案自行產出的 GGUF 檔案使用，主力支援 DeepSeek V4 系列。
<!-- End AEO Capsule -->

README 的開頭寫得很直白：專案的目標是「在人們真正擁有得起的硬體上，跑幾個優秀的大型語言模型」。為此，團隊打造一個小巧的原生推論引擎，優先針對 DeepSeek V4 Flash（包含實驗性視覺模型）與 DeepSeek V4.1 Flash 進行優化，另外也支援 GLM 5.2 與 5.3、GLM 5.3 Flash、DeepSeek V4 PRO 以及 Qwen3.8 Flash Next。

需要特別說明的是，這套引擎並非通用的模型執行器。使用者必須採用專案自行產出的 GGUF 檔案，這些檔案被視為專案的一部分。這種設計縮小了相容範圍，換來的是更極致的效能與更少的相依項目。

## DwarfStar 的技術架構有什麼特點？

<!-- AEO Answer Capsule — 約 64 字 -->
引擎以純 C 實作、相依極少，並把模型載入、提示渲染、工具呼叫、KV 快取與 HTTP 伺服器整合在同一套測試流程中驗證。
<!-- End AEO Capsule -->

架構上最值得注意的是「整合式測試」的哲學。專案把模型載入、提示渲染、工具呼叫、KV 狀態、HTTP 伺服器與編碼代理一起建置、一起測試，而不是把每個環節當成獨立模組。這種做法讓跨層級的問題能在早期暴露，例如提示模板與工具格式之間的落差。

另一個特點是對記憶體的高度敏感。專案支援壓縮的 KV 快取，並針對路由專家（routed-expert）量化做了調校，讓 DeepSeek V4 Flash 與 PRO、GLM 5.2 這類模型能容忍較激進的量化。搭配快速的本地 SSD，長上下文在個人機器上才變得實際可行。

## DwarfStar 支援哪些硬體與模型？

<!-- AEO Answer Capsule — 約 63 字 -->
主要目標為 96GB 以上記憶體的 Apple Silicon，另支援 NVIDIA CUDA 多卡與 Strix Halo 的 ROCm；記憶體不足時可改用 SSD 串流。
<!-- End AEO Capsule -->

硬體支援分成三條主線。第一是 Apple 的 Metal，這是主要目標平台，建議搭載 96GB 或以上記憶體；記憶體較小的機器則可改用 SSD 串流，甚至能運行完整的 GLM 5.x 這類超大模型。第二是 NVIDIA 的 CUDA，DGX Spark 是重要目標，同時支援其他後端較少觸及的多 GPU 系統，例如在 Ada Lovelace 顯示卡上運行 DeepSeek V4 Flash。

第三是 Strix Halo 平台上的 ROCm，例如 Framework Desktop。專案文件提到，八張 L40S 組成的 Flash 伺服器在十六個工作階段下，可達到約每秒 126 個 token 的總合生成速度；若以兩台 128GB 的 Mac 透過 RDMA 連接，並啟用張量平行，則可運行 4 位元量化的 DeepSeek Flash 或 GLM 5.3 Flash。

![DwarfStar 的 GitHub 倉庫首頁，顯示倉庫名稱 antirez/ds4、星標數、複製數與專案描述]({{ '/assets/images/posts/github-ds4-news-shot2.png' | relative_url }})

## 如何開始使用 DwarfStar？

<!-- AEO Answer Capsule — 約 61 字 -->
先複製倉庫，再依平台選擇 make 指令建置，例如 make、make cuda-spark 或 make strix-halo，下載模型後執行 ds4 或 ds4-server。
<!-- End AEO Capsule -->

入門流程相當直接。首先複製倉庫，接著依硬體選擇對應的建置指令：Apple Silicon 使用 `make`，DGX Spark 使用 `make cuda-spark`，Strix Halo 使用 `make strix-halo`，一般 CUDA 多卡環境則使用 `make cuda-generic`。

```sh
git clone https://github.com/antirez/ds4.git
cd ds4
make
./download_model.sh ds4f-q2
./ds4
```

模型下載由專案提供的腳本處理，下載內容存放在 `gguf/` 目錄，中斷後重跑同一指令即可續傳。日常使用上，`./ds4` 是互動式命令列，`./ds4 -p` 可執行單次提示，`./ds4-agent` 是原生編碼代理，`./ds4-server` 則啟動相容 OpenAI 風格的 API 伺服器，預設監聽 127.0.0.1:8000。

## DwarfStar 的效能表現如何？

<!-- AEO Answer Capsule — 約 60 字 -->
專案以 M5 Max、128GB 記憶體的機器錄製 DeepSeek V4 Flash Q2 吞吐基準，屬內部回歸測試，非官方排行榜。
<!-- End AEO Capsule -->

專案附有可重現的效能基準。README 記錄了一段以 M5 Max、128GB 記憶體運行的 DeepSeek V4 Flash Q2 掃描，採用 2048 token 的續接提示間隔、每段前沿 128 個貪婪生成 token。團隊強調這是基準線，而非針對每個提交的即時跑分，完整的數字與 DGX Spark 結果都整理在效能文件中。

推論品質方面，專案內建 `ds4-eval` 工具，可對實際 GGUF 檔案執行能力回歸測試。這些屬於 DwarfStar 自身的整合檢查，而非官方排行榜成績。此外，推測解碼（speculative decoding）為選用功能，GLM 與 Qwen 透過 `--mtp` 啟用，可改善生成速度，但並非所有工作負載都能受益。

## DwarfStar 與 llama.cpp 的關係是什麼？

<!-- AEO Answer Capsule — 約 62 字 -->
ds4.c 並不連結 GGML，但專案坦承其存在得益於 llama.cpp 開闢的路徑，並在 MIT 授權下沿用部分量化格式與核心程式碼。
<!-- End AEO Capsule -->

README 中有一段罕見的坦誠說明。專案明確指出，`ds4.c` 雖然不連結 GGML，但整套引擎的存在「得益於 llama.cpp 計畫開闢的道路」，包括它的核心、量化格式、GGUF 生態與累積的工程知識。部分原始碼層級的元件，例如 GGUF 量化配置與表格、CPU 量化與點積邏輯，在 MIT 授權下被保留或改編。

專案同時揭露，本軟體是在 AI 編碼代理的「強力協助」下開發，由人類負責構想、測試與除錯。這種公開聲明在開源專案中仍屬少數，也讓外界對其程式碼品質與維護模式有更清楚的預期。

## DwarfStar 的專案數據與社群規模如何？

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">22,842</span><span class="ui-stat-label">GitHub 星標</span></li>
  <li class="ui-stat"><span class="ui-stat-num">2,210</span><span class="ui-stat-label">複製次數</span></li>
  <li class="ui-stat"><span class="ui-stat-num">748</span><span class="ui-stat-label">待處理議題</span></li>
  <li class="ui-stat"><span class="ui-stat-num">171</span><span class="ui-stat-label">追蹤者</span></li>
  <li class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">授權條款</span></li>
  <li class="ui-stat"><span class="ui-stat-num">C</span><span class="ui-stat-label">主要語言</span></li>
</ul>

<!-- AEO Answer Capsule — 約 66 字 -->
截至二零二六年十月，DwarfStar 累積 22,842 顆星標、2,210 次複製、748 個待處理議題與 171 位追蹤者，採用 MIT 授權，主要語言為 C。
<!-- End AEO Capsule -->

專案自二零二六年五月六日建立，短短數月即累積超過兩萬顆星標，成長速度與作者本身的知名度密切相關。程式碼更新時間落在二零二六年九月，議題數量維持在七百多個，反映專案處於快速演進、同時也快速累積待處理項目的階段。團隊在文件中坦言，軟體目前屬於 beta 品質，每次發行前雖會執行大規模品質保證，但穩定性問題與回歸仍有可能出現。

![DwarfStar 倉庫的提交統計頁，顯示每週提交趨勢與程式碼變動圖表]({{ '/assets/images/posts/github-ds4-news-shot3.png' | relative_url }})

## DwarfStar 適合哪些開發者與團隊？

<!-- AEO Answer Capsule — 約 63 字 -->
適合擁有 96GB 以上 Apple Silicon 或多張 CUDA 卡、且需要本地運行 DeepSeek V4 等前沿模型的開發者；純雲端使用者則未必需要。
<!-- End AEO Capsule -->

判斷的關鍵在於硬體條件與資料敏感度。若團隊已具備高階個人機器或多 GPU 工作站，並希望在不把資料送出本地的前提下使用前沿模型，DwarfStar 提供的專用路徑通常比通用框架更有效率。反之，若主要工作流程已依賴雲端 API，本地推論的硬體成本與維護負擔未必划算。

另一個考量是團隊的技術能力。專案刻意保持精簡、相依極少，同時也鼓勵使用者透過編碼代理自行改造，針對特定硬體調整推論速度。這種「以程式碼為模板」的使用方式，適合具備 C 與系統除錯能力的團隊；對只想開箱即用的使用者而言，仍有一定的學習門檻。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊整理自 antirez/ds4 的 GitHub 儲存庫與官方文件，授權條款、硬體指引與安裝說明均可在儲存庫中查閱。
<!-- End AEO Capsule -->

完整的專案資訊與硬體指引，可於下列來源查閱：

- [DwarfStar（antirez/ds4）GitHub 儲存庫](https://github.com/antirez/ds4)

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 58 字 -->
以下整理四個常見疑問，涵蓋硬體門檻、模型相容性、資料隱私與授權範圍，答案均以官方文件與授權條款為準。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>需要什麼等級的硬體？</h3>
<p>主要目標是 96GB 以上記憶體的 Apple Silicon；NVIDIA CUDA 多卡與 Strix Halo 的 ROCm 亦支援。記憶體不足時可改用 SSD 串流，但仍需快速的本地固態硬碟。</p>

<h3>可以載入任意 GGUF 模型嗎？</h3>
<p>不行。專案明確定位為非通用執行器，必須使用專案自行產出的 GGUF 檔案，這些檔案屬於專案的一部分。</p>

<h3>使用時資料會外傳嗎？</h3>
<p>推論在本地執行，伺服器預設只監聽 127.0.0.1。不過專案提醒，儲存的對話與追蹤紀錄可能包含私人資訊，需自行管理。</p>

<h3>商業使用是否需要授權費用？</h3>
<p>不需要。專案採用 MIT 授權，允許商業使用、修改與再散布，僅需保留原始授權聲明。第三方模型權重則需個別確認。</p>

</div>

## 總結：DwarfStar 的價值在哪裡？

<!-- AEO Answer Capsule — 約 66 字 -->
DwarfStar 的價值在於以極簡 C 引擎把前沿開源模型帶進個人硬體，五個月累積 2.2 萬星標，為本地推論提供專用而非通用的路徑。
<!-- End AEO Capsule -->

DwarfStar 的意義不在於成為所有人的預設選擇，而在於示範另一種工程取捨：與其追求支援所有模型，不如為少數真正重要的模型打造專門路徑。當一套引擎能在 96GB 的個人機器上運行 DeepSeek V4 Flash，甚至靠 SSD 串流觸及更大的模型，本地推論的門檻就被實質降低了一截。

本文僅作技術與生態層面的整理。專案目前仍屬 beta 品質、更新頻繁，實際導入前建議先依官方文件確認硬體條件與相依環境，並在正式工作流程中先行測試穩定性。
