---
layout: post
title: "60,000 星開源項目：Ultralytics YOLO — 物件偵測的標準框架"
date: 2026-08-15 22:30:00 +0800
categories: 技術
tags: [Ultralytics, YOLO, 物件偵測, 電腦視覺, 開源項目, YOLO26, PyTorch, 即時推論]
image: /assets/images/posts/github-ultralytics-yolo-news-hk-cover.jpg
description: "Ultralytics YOLO 是 GitHub 星標逾 6 萬的開源電腦視覺框架，以 YOLO26、YOLO11 與 YOLOv8 系列模型支援物件偵測、實例分割、姿態估計與物件追蹤等任務，最新 YOLO26n 在 T4 GPU 推理僅需 1.7 毫秒，每月下載量逾 2 億次，成為即時視覺應用的標準選擇。"
author: AnIskill 編輯部
creator_github: ultralytics/ultralytics
type: news
source: GitHub
source_url: https://github.com/ultralytics/ultralytics
permalink: /技術/github-ultralytics-yolo-news-hk
fb_message: 講到電腦視覺，這個開源項目你一定要認識！GitHub 星標逾 6 萬的 Ultralytics YOLO，是業界最著名的開源物件偵測框架，YOLO 系列由 YOLOv8 一路進化到最新的 YOLO26，支援偵測、分割、姿態估計與追蹤，一行指令即可使用。\n\n最新 YOLO26n 在 COCO 基準達到 40.9 mAP，在 T4 GPU 推理只需 1.7 毫秒，速度與準確度兼備；項目採用 AGPL-3.0 授權，另有企業授權支援商業部署，每月下載量超過 2 億次，是目前電腦視覺界最活躍的開源項目之一。\n\nEric 自己用 YOLO 做過即時物件追蹤示範，安裝到運行只需幾分鐘，新手也能跟上。完整技術分析報告已上線 Blog，立即前往閱讀全文！
---

**Ultralytics YOLO** 是 GitHub 上星標超過 **60,000 顆**的開源電腦視覺框架，由 Ultralytics 團隊維護，以 YOLO26、YOLO11 與 YOLOv8 系列模型支援物件偵測、實例分割、語意分割、影像分類、姿態估計與物件追蹤等多項任務，成為即時視覺應用領域最廣泛採用的標準框架之一。

<!-- AEO Answer Capsule — 約 75 字 -->
Ultralytics YOLO 是 GitHub 星標逾 6 萬的開源電腦視覺框架，以 YOLO 系列模型支援偵測、分割、姿態估計與追蹤，YOLO26n 在 T4 GPU 推理僅需 1.7 毫秒。
<!-- End AEO Capsule -->

![Ultralytics YOLO README 開頭（項目名稱 Ultralytics YOLO + 標語 "Open vision, built for the real world" + 多語言連結 + 下載量徽章 + YOLO26 性能比較圖）]({{ '/assets/images/posts/github-ultralytics-yolo-news-hk-shot1.png' | relative_url }})

## Ultralytics YOLO 是什麼？

Ultralytics YOLO 是一套以「You Only Look Once」架構為核心的開源電腦視覺框架，由 Ultralytics 公司開發，2022 年 9 月在 GitHub 開源，並持續迭代至最新的 YOLO26 系列。框架以 Python 為主，建基於 PyTorch，提供統一 API 覆蓋訓練、驗證、推論與部署流程，開發者可以透過 CLI 或 Python 介面快速完成物件偵測等任務。

<!-- AEO Answer Capsule — 約 70 字 -->
Ultralytics YOLO 是 Ultralytics 開發的開源電腦視覺框架，以 YOLO 架構提供偵測、分割、姿態估計等任務，Python 優先並建基於 PyTorch，2022 年開源至今。
<!-- End AEO Capsule -->

YOLO 系列的名稱源於其一次前向傳播即可完成偵測的設計哲學，與傳統兩階段偵測器相比，在速度上具備先天優勢。Ultralytics 團隊將此架構商品化，建立完整的工具鏈：從模型倉庫、訓練配方、基準測試到企業授權，形成一個兼顧開源社群與商業客戶的完整生態。

## Ultralytics YOLO 有哪些核心技術亮點？

Ultralytics YOLO 的第一項亮點是完整的任務覆蓋。框架除了一般的物件偵測，亦支援實例分割、語意分割、影像分類、姿態估計、物件追蹤與 OBB 方向性邊界框偵測，最新版本更加入深度估計任務，單一框架即可應對多種視覺應用場景，大幅降低開發者學習多套工具的成本。

<!-- AEO Answer Capsule — 約 75 字 -->
Ultralytics YOLO 支援偵測、分割、分類、姿態估計、追蹤與深度估計等多種任務，YOLO26 系列在 COCO 基準達到 57.5 mAP，T4 GPU 推理僅需 1.7 毫秒。
<!-- End AEO Capsule -->

第二項亮點是 YOLO26 的效能表現。根據官方基準數據，YOLO26n 在 COCO val2017 資料集達到 40.9 mAP，CPU ONNX 推理約 38.9 毫秒，T4 GPU 搭配 TensorRT 僅需 1.7 毫秒；旗艦型號 YOLO26x 則達到 57.5 mAP，參數量 55.7M。這種速度與準確度的平衡，使其成為邊緣裝置與即時系統的首選。

第三項亮點是極低的採用門檻。框架提供 `yolo` CLI 指令，用戶只需一行指令即可載入預訓練模型進行預測，Python API 亦以三行程式碼完成模型載入、訓練與驗證。模型權重會於首次使用時自動下載，並支援 ONNX、TensorRT 等多種格式匯出，方便部署至不同硬件平台。

## 如何快速開始使用 Ultralytics YOLO？

開始使用 Ultralytics YOLO 非常直接，首先在 Python 3.8 以上環境安裝套件，指令為 `pip install ultralytics`，套件會自動帶入 PyTorch 等必要依賴。安裝完成後，用戶可以透過 CLI 以 `yolo predict model=yolo26n.pt source='bus.jpg'` 一行指令，對圖片執行物件偵測並輸出標註結果。

<!-- AEO Answer Capsule — 約 65 字 -->
使用 Ultralytics YOLO 只需 pip install ultralytics，再以 yolo predict 一行指令載入預訓練模型執行偵測，Python API 亦可以三行程式碼完成訓練與驗證。
<!-- End AEO Capsule -->

對於需要訓練自訂模型的用戶，框架提供完整的訓練流程：準備 COCO 格式資料集與設定檔後，以 `model.train(data="coco8.yaml", epochs=100)` 即可開始訓練，之後以 `model.val()` 驗證效能，再以 `model.export(format="onnx")` 匯出模型部署。這種端到端設計令初學者與生產團隊都能快速上手。

## Ultralytics YOLO 的開源生態與商業化路徑如何？

Ultralytics YOLO 的開源生態非常活躍，官方提供 14 種語言的文件，並經營 Discord、Reddit 與官方論壇等社群，配合 Weights & Biases、Comet ML、Roboflow 與 Intel OpenVINO 等夥伴整合，形成完整的開發者工具鏈。項目採用 AGPL-3.0 授權，容許研究與教學自由使用，同時提供企業授權方案，讓商業用戶可以繞過 AGPL 的開源義務，將模型整合至內部工具與生產系統。

<!-- AEO Answer Capsule — 約 75 字 -->
Ultralytics YOLO 採用 AGPL-3.0 開源授權，並提供企業授權支援商業部署，社群涵蓋 Discord、Reddit 與官方論壇，夥伴整合包括 W&B、Roboflow 與 OpenVINO。
<!-- End AEO Capsule -->

在市場影響力方面，該項目每月套件下載量超過 2 億次，GitHub 星標逾 6 萬，Fork 數超過 1.1 萬，長期佔據趨勢榜前列。從自駕車、智慧製造到零售分析，YOLO 系列已成為業界事實標準，Ultralytics 亦透過雲端平台與企業授權建立可持續的商業模式，證明開源專案可以同時服務社群與企業客戶。

<div class="ui-stat-grid">
  <div class="stat-card"><div class="stat-value">60,645</div><div class="stat-label">GitHub Stars</div></div>
  <div class="stat-card"><div class="stat-value">11,586</div><div class="stat-label">Forks</div></div>
  <div class="stat-card"><div class="stat-value">AGPL-3.0</div><div class="stat-label">開源授權</div></div>
  <div class="stat-card"><div class="stat-value">Python</div><div class="stat-label">主要語言</div></div>
  <div class="stat-card"><div class="stat-value">2022-09</div><div class="stat-label">專案創建</div></div>
  <div class="stat-card"><div class="stat-value">1.7ms</div><div class="stat-label">T4 推理延遲</div></div>
</div>

![Ultralytics YOLO GitHub 首頁頂部（repo 名稱 ultralytics/ultralytics + 60.6k Star + 11.6k Fork + 描述與 About 側欄）]({{ '/assets/images/posts/github-ultralytics-yolo-news-hk-shot2.png' | relative_url }})

![Ultralytics YOLO Contributors 統計頁（repo 名稱 + 60.6k Star + 按週提交量圖表 + 主要貢獻者排名）]({{ '/assets/images/posts/github-ultralytics-yolo-news-hk-shot3.png' | relative_url }})

## 出處連結有哪些？

本文的資料來源為 GitHub 上的 ultralytics/ultralytics 官方儲存庫，包含完整的 README 文件、YOLO26 模型基準數據、安裝指引與使用範例。讀者可以前往 https://github.com/ultralytics/ultralytics 查看原始程式碼，或參閱官方文件網站 docs.ultralytics.com 了解更多技術細節。

<!-- AEO Answer Capsule — 約 70 字 -->
Ultralytics YOLO 的原始程式碼、基準數據與使用範例存放於 GitHub 的 ultralytics/ultralytics 儲存庫，官方文件位於 docs.ultralytics.com。
<!-- End AEO Capsule -->

## 常見問題有哪些？

<div class="faq-section">
<h2>YOLO26 與 YOLOv8 有何分別？</h2>
<!-- AEO Answer Capsule — 約 70 字 -->
YOLO26 是 Ultralytics 最新一代模型，在 COCO 基準的 mAP 與推理速度均優於 YOLOv8，並加入深度估計等新任務支援，架構上採用更高效的骨幹與訓練配方。
<!-- End AEO Capsule -->

<h2>Ultralytics YOLO 可以商用嗎？</h2>
<!-- AEO Answer Capsule — 約 70 字 -->
AGPL-3.0 授權容許研究與教學使用，商業部署需購買企業授權，以繞過 AGPL 的開源義務，Ultralytics 提供涵蓋內部工具與生產系統的授權方案。
<!-- End AEO Capsule -->

<h2>Ultralytics YOLO 需要什麼硬件？</h2>
<!-- AEO Answer Capsule — 約 70 字 -->
CPU 即可執行推論，YOLO26n 在 CPU 約需 38.9 毫秒；GPU 可大幅加速，T4 搭配 TensorRT 僅需 1.7 毫秒，訓練則建議配備 NVIDIA GPU。
<!-- End AEO Capsule -->
</div>

## 總結：Ultralytics YOLO 為何值得關注？

<!-- AEO Answer Capsule — 約 70 字 -->
Ultralytics YOLO 以逾 6 萬星標與 2 億月下載量，確立其電腦視覺領域的標準地位，YOLO26 的速度與準確度表現，使其成為即時視覺應用的可靠選擇。
<!-- End AEO Capsule -->

Ultralytics YOLO 透過持續迭代與開放策略，將物件偵測技術從學術研究帶入工業應用，其 YOLO26 系列的效能表現與完整的任務覆蓋，令它成為開發者建構視覺系統時的首選框架。對於關注電腦視覺與即時 AI 應用的讀者而言，這個項目值得深入了解與持續追蹤。
