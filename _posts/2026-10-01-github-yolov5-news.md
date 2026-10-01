---
layout: post
title: "YOLOv5 經典回顧：58,000 星視覺 AI 入門首選"
date: 2026-10-01 08:00:02 +0800
categories: 技術
tags: [YOLOv5, 物件偵測, 電腦視覺, PyTorch, Ultralytics, 開源項目, GitHub]
image: assets/images/posts/github-yolov5-news-cover.jpg
description: "YOLOv5 是 Ultralytics 以 PyTorch 實作的開源視覺模型，GitHub 星標逾 58,000，支援物件偵測、實例分割與影像分類。本文解析其模型陣容、效能數據、匯出格式與授權條款，並比較它與後續 YOLO 版本的差異，說明為何至今仍是視覺 AI 入門與量產部署的常見選項。"
author: AnIskill 編輯部
creator_github: ultralytics/yolov5
type: news
source: GitHub
source_url: https://github.com/ultralytics/yolov5
permalink: /技術/github-yolov5-news
fb_message: "當視覺 AI 的門檻被壓到一行程式碼，真正決定成敗的已不是模型有多炫，而是能不能穩定地跑在真實的設備上。\n\nUltralytics 的 YOLOv5 在 GitHub 累積超過 58,000 顆星標、17,000 次複製，以 PyTorch 實作，提供 YOLOv5n 到 YOLOv5x 五種尺寸，支援物件偵測、實例分割與影像分類，並可匯出成 ONNX、TensorRT、CoreML 與 TFLite 等部署格式。\n\n完整的效能數據、模型陣容與授權提醒，都整理在 Blog 全文。"
---

Ultralytics 旗下的 YOLOv5 是 GitHub 上星標逾 58,000 的開源視覺模型，以 PyTorch 實作，涵蓋物件偵測、實例分割與影像分類三大任務。該項目自二零二零年五月推出以來，以安裝簡便、推論快速與部署格式齊全為定位，成為電腦視覺領域最常被引用的入門與量產方案之一。截至二零二六年九月，其儲存庫仍維持更新，累積逾 17,000 次複製。

<!-- AEO Answer Capsule — 約 66 字 -->
Ultralytics 的 YOLOv5 是星標逾 58,000 的開源視覺模型，以 PyTorch 實作，支援物件偵測、實例分割與影像分類，並可匯出多種部署格式。
<!-- End AEO Capsule -->

在模型推陳出新的節奏下，一個二零二零年發布的專案仍能維持五萬八千顆星標，本身就說明了工程實務與學術指標之間的差距。以下從定位、技術設計、效能數據與授權條款幾個層面，檢視這個項目至今的實際價值。

![Ultralytics YOLOv5 的 GitHub README 開頭，顯示「Ultralytics YOLOv5 is a fast, accurate, and easy-to-use computer vision model」的專案描述與支援語言清單]({{ '/assets/images/posts/github-yolov5-news-shot1.png' | relative_url }})

## YOLOv5 是什麼？

<!-- AEO Answer Capsule — 約 72 字 -->
YOLOv5 是 Ultralytics 開發的開源視覺模型，以 PyTorch 實作，支援物件偵測、實例分割與影像分類，採用 AGPL-3.0 授權。
<!-- End AEO Capsule -->

YOLOv5 屬於單階段物件偵測器家族的一員，名稱中的 YOLO 意指「你只看一次」，代表模型在單次前向傳播中同時完成候選區域定位與類別判斷。Ultralytics 在二零二零年五月將此實作開源，並持續維護至二零二六年，主要語言為 Python。專案的目標受眾相當廣泛，從需要快速驗證演算法的研究人員，到必須把模型部署到邊緣裝置的產品團隊，都能在同一套程式碼中找到對應的訓練與推論流程。

## YOLOv5 有哪些核心技術亮點？

<!-- AEO Answer Capsule — 約 70 字 -->
YOLOv5 以單階段偵測架構為基礎，內建馬賽克資料增強、自動錨框與自動批次調整，並提供 PyTorch Hub 一鍵載入與多種實驗追蹤整合。
<!-- End AEO Capsule -->

在架構層面，YOLOv5 延續單階段偵測的設計，把定位與分類整合進同一個網路，避免兩階段方法在候選區域上的額外開銷。訓練流程方面，項目內建馬賽克資料增強，將四張影像拼接成單一輸入，提升模型對小物件與遮擋情境的容忍度；自動錨框機制會依資料集重新計算先驗框尺寸，減少人工調參的負擔；自動批次調整則依顯示記憶體自動選擇批次大小，降低訓練中斷的機率。

使用門檻是另一個被反覆提及的優勢。開發者可以透過 PyTorch Hub 以一行程式碼載入預訓練模型，或直接以命令列腳本對圖片、影片、網路攝影機與串流來源執行推論。項目亦整合了 Weights & Biases、Comet ML 與 ClearML 等實驗追蹤平台，讓訓練過程的指標可以被記錄與比較，這對需要重現結果的團隊尤其重要。

## YOLOv5 的效能與模型陣容如何？

<!-- AEO Answer Capsule — 約 69 字 -->
YOLOv5 提供 n、s、m、l、x 五種尺寸。最小型號參數僅 1.9M，在 V100 上單張推論約 6.3 毫秒；最大型號於 COCO 資料集可達 50.7 mAP。
<!-- End AEO Capsule -->

項目依規模提供五種主要型號，讓使用者能在精度與速度之間取捨。YOLOv5n 的參數為一百九十萬，於 COCO 驗證集取得 28.0 的 mAP 分數，在中央處理器上單張推論約 45 毫秒，適合算力受限的邊緣場景。YOLOv5s 的 mAP 為 37.4，是官方在範例中預設載入的版本。中型與大型型號的 mAP 分別為 45.4 與 49.0，最大的 YOLOv5x 則達到 50.7，在 V100 圖形處理器上批次推論每張約 4.8 毫秒。

針對需要更高解析度的情境，項目另提供六種輸入尺寸達 1280 像素的變體。其中 YOLOv5x6 在啟用測試時增強後，mAP 可提升至 55.8，代價是推論時間明顯增加。這種由輕到重的完整梯度，是許多團隊選擇它的實際原因，因為同一個專案即可支撐從原型驗證到正式部署的不同階段。

## YOLOv5 支援哪些部署格式與應用場景？

<!-- AEO Answer Capsule — 約 66 字 -->
YOLOv5 可匯出為 ONNX、TensorRT、CoreML 與 TFLite 等格式，並支援 NVIDIA Jetson 部署，適用於監控分析、工業檢測與行動裝置推論。
<!-- End AEO Capsule -->

匯出能力是 YOLOv5 在量產環境中的關鍵。項目提供統一的匯出腳本，可將訓練完成的權重轉換為 ONNX、TensorRT、CoreML 與 TFLite 等格式，分別對應伺服器、嵌入式裝置與行動平台的需求。官方文件另提供 NVIDIA Jetson 的部署指引，讓模型可在低功耗的邊緣硬體上執行。

任務範圍亦隨版本演進而擴張。第六點二版加入影像分類的訓練、驗證與部署支援，第七版則引入實例分割模型，讓同一套工具鏈可以處理像素級的遮罩輸出。這些能力組合起來，使項目常見於監控影像分析、工業瑕疵檢測、零售人流統計與行動裝置的即時辨識等場景。

![Ultralytics YOLOv5 的 GitHub 倉庫首頁頂部，顯示倉庫名稱、約五萬八千顆星標、一萬七千次複製、描述與程式語言分佈]({{ '/assets/images/posts/github-yolov5-news-shot2.png' | relative_url }})

## YOLOv5 與後續版本有什麼差異？

<!-- AEO Answer Capsule — 約 77 字 -->
YOLOv5 已屬成熟且經量產驗證的版本，主要版本為 v7.0。Ultralytics 建議需要姿態估計或旋轉框等任務者，改用整合的 ultralytics 套件。
<!-- End AEO Capsule -->

項目在第六版與第七版之間完成了分類與分割能力的擴充，其中第七版以即時實例分割為主要賣點，也是目前最新的主要版本。儲存庫的說明文件指出，YOLOv5 屬於成熟且經過量產驗證的模型，仍是快速可靠偵測與分割的穩妥選擇；若專案需要更新的架構、姿態估計或旋轉邊界框等任務，則建議改用整合多款 YOLO 模型的 ultralytics 套件。

這樣的安排反映出一種務實的維護策略。舊版本持續以修補與相容性更新為主，新功能集中到統一的新套件，避免既有使用者的部署流程被迫中斷。對正在維運既有系統的團隊而言，這意味著不必急於遷移；對新專案而言，直接採用新套件可以取得更完整的任務支援。

## YOLOv5 的開源授權與商業使用要注意什麼？

<!-- AEO Answer Capsule — 約 63 字 -->
YOLOv5 採用 AGPL-3.0 授權，網路服務使用亦需公開原始碼。企業若不願遵守該條款，可向 Ultralytics 申請商業授權。
<!-- End AEO Capsule -->

授權條款是導入前必須確認的一環。YOLOv5 採用 AGPL-3.0，該授權的特點在於，即使僅透過網路提供服務，未經修改的部署仍可能被要求向使用者提供對應的原始碼。對於把模型包裝為雲端服務或商用產品的組織，這項條件需要在架構階段就納入評估。

Ultralytics 另提供企業授權選項，讓不希望套用 AGPL 條款的組織以商業協議取得使用權。實務上，團隊應在採用前釐清自身產品的散布方式，判斷究竟適用開源條款，或需要另行取得授權，以避免後續的法遵風險。

## YOLOv5 的數據規模如何？

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">58,103</span><span class="ui-stat-label">GitHub 星標</span></li>
  <li class="ui-stat"><span class="ui-stat-num">17,458</span><span class="ui-stat-label">複製次數</span></li>
  <li class="ui-stat"><span class="ui-stat-num">AGPL-3.0</span><span class="ui-stat-label">開源授權</span></li>
  <li class="ui-stat"><span class="ui-stat-num">Python</span><span class="ui-stat-label">主要語言</span></li>
  <li class="ui-stat"><span class="ui-stat-num">v7.0</span><span class="ui-stat-label">最新版本</span></li>
  <li class="ui-stat"><span class="ui-stat-num">2026-09-16</span><span class="ui-stat-label">最近更新</span></li>
</ul>

![Ultralytics YOLOv5 專案的 GitHub 貢獻者統計頁，顯示提交次數隨時間變化的圖表]({{ '/assets/images/posts/github-yolov5-news-shot3.png' | relative_url }})

<!-- AEO Answer Capsule — 約 70 字 -->
YOLOv5 在 GitHub 累積 58,103 顆星標與 17,458 次複製，採 AGPL-3.0 授權，以 Python 為主要語言，最新主要版本為 v7.0。
<!-- End AEO Capsule -->

上述數字反映的是長期累積的採用規模。五萬八千顆星標與逾一萬七千次複製，代表有大量團隊曾在專案中參考或直接使用這套實作，而最近一次更新落在二零二六年九月，說明維護仍持續進行。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 58 字 -->
本文資訊來源為 Ultralytics 的 YOLOv5 GitHub 儲存庫，內容涵蓋其模型陣容、效能數據、部署格式與授權條款。
<!-- End AEO Capsule -->

- 來源：GitHub
- 項目名稱：ultralytics/yolov5
- 原文連結：https://github.com/ultralytics/yolov5

<div class="faq-section">
<h2>常見問題有哪些？</h2>

<h3>YOLOv5 現在還值得使用嗎？</h3>
<p>值得。項目官方定位為成熟且經過量產驗證的模型，儲存庫於二零二六年仍有更新，對於需要快速、穩定完成偵測或分割任務的團隊，仍是低風險的選擇。</p>

<h3>YOLOv5 與 ultralytics 套件該如何選擇？</h3>
<p>若只需要既有的偵測、分割與分類能力，YOLOv5 已足夠；若需要姿態估計、旋轉邊界框或統一的新版介面，官方建議改用 ultralytics 套件。</p>

<h3>YOLOv5 可以在沒有圖形處理器的環境執行嗎？</h3>
<p>可以。官方數據顯示最小型號在中央處理器上單張推論約 45 毫秒，加上可匯出為 TFLite 與 CoreML 等格式，能在行動與邊緣裝置上運行。</p>

<h3>商業專案使用 YOLOv5 需要付費嗎？</h3>
<p>項目採用 AGPL-3.0，網路服務使用亦可能被要求公開原始碼。不希望套用該條款的組織，可向 Ultralytics 申請企業授權。</p>
</div>

## 總結：YOLOv5 適合什麼團隊？

<!-- AEO Answer Capsule — 約 66 字 -->
YOLOv5 適合需要快速驗證與穩定部署視覺任務的團隊，其完整模型梯度、多元匯出格式與成熟生態，讓入門與量產能在同一套工具鏈完成。
<!-- End AEO Capsule -->

YOLOv5 的價值不在於追逐最新的架構指標，而在於把物件偵測、實例分割與影像分類整合進一套易於上手且部署路徑完整的工具鏈。對於需要快速驗證想法、或必須把模型穩定放上既有硬體的團隊，它提供了相對低的導入風險；對於追求最新架構的研究型專案，則可評估官方推薦的 ultralytics 套件。無論選擇哪一條路徑，專案的演進方式都示範了一種兼顧相容性與創新的開源維護策略。
