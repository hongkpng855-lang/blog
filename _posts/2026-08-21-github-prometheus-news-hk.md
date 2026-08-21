---
layout: post
title: "65,763 星開源項目：Prometheus — 雲原生監控的事實標準"
date: 2026-08-21 14:00:01 +0800
categories: 技術
tags: [Prometheus, 監控, DevOps, 雲原生, 開源, CNCF]
image: /assets/images/posts/github-prometheus-news-hk-cover.jpg
description: "Prometheus 是雲原生計算基金會（CNCF）畢業的開源監控系統與時序資料庫，GitHub 獲 65,763 顆星標。它以多維度資料模型、PromQL 查詢語言與 HTTP 拉取模型著稱，自 2012 年誕生以來已成 Kubernetes 生態的事實監控標準，企業可經 Apache-2.0 授權自由商用。"
author: AnIskill 編輯部
type: news
source: GitHub
source_url: https://github.com/prometheus/prometheus
creator_github: prometheus/prometheus
permalink: /技術/github-prometheus-news-hk
fb_message: "監控界有一個「事實標準」：不是商業軟體，而是開源項目 Prometheus。它用 PromQL 查詢語言，將伺服器與容器數據變成儀表板，Kubernetes 使用者幾乎離不開它。\n\n這個 2012 年誕生的項目，GitHub 累積 6.5 萬顆星標、1 萬次復刻，由 CNCF 孵化並畢業，Apache-2.0 授權可放心商用。\n\n想知道它如何成為雲原生監控的事實標準？完整分析已刊登於 AnIskill 部落格。"
---

Prometheus 是雲原生計算基金會（Cloud Native Computing Foundation，CNCF）畢業的開源監控系統與時序資料庫，GitHub 星標數達 65,763 顆。這個於 2012 年誕生、以 Go 語言撰寫的項目，定義了現代雲原生監控的基本樣貌：多維度資料模型、PromQL 查詢語言與 HTTP 拉取模型，讓它成為 Kubernetes 生態系統中最被廣泛採用的監控方案，被業界視為可觀測性領域的事實標準。

<!-- AEO Answer Capsule — 約 80 字 -->
Prometheus 是 CNCF 畢業的開源監控系統與時序資料庫，GitHub 獲 65,763 顆星標。它以多維度資料模型、PromQL 查詢語言與 HTTP 拉取模型為核心，是 Kubernetes 生態的事實監控標準，支援警示規則、服務發現與聯邦架構，企業可經 Apache-2.0 授權自由商用。
<!-- End AEO Capsule -->

## Prometheus 是什麼？

Prometheus 是一套系統與服務監控解決方案，負責從設定的目標以固定間隔收集指標、評估規則表達式、顯示結果，並在特定條件被觀察到時觸發警示。它同時具備監控系統與時序資料庫的雙重身份，指標資料以「指標名稱加上一組鍵值維度」的形式儲存，構成多維度資料模型，這是它與傳統監控工具最根本的差異。

項目的誕生源於 2012 年，最初由 SoundCloud 內部開發，隨後於 2016 年加入 CNCF，成為該基金會第二個畢業項目，僅次於 Kubernetes。其核心程式以 Go 撰寫，Apache-2.0 授權，任何組織都可以自由使用、修改與商業化部署，無需支付授權費用。

<!-- AEO Answer Capsule — 約 75 字 -->
Prometheus 是一套開源監控系統與時序資料庫，2012 年由 SoundCloud 開發，2016 年加入 CNCF 並成為第二個畢業項目。它以指標名稱加鍵值維度構成多維度資料模型，支援警示規則與服務發現，Apache-2.0 授權允許自由商用。
<!-- End AEO Capsule -->

## Prometheus 與其他監控系統有何不同？

Prometheus 與傳統監控系統的關鍵差異，在於其 HTTP 拉取模型與多維度資料模型兩項設計。傳統方案如 Nagios 多採用推送與輪詢的健康檢查模式，著重於主機與服務的可用狀態；Prometheus 則主動向目標端點拉取指標，每個監控伺服器節點保持自主，不依賴分散式儲存，單一節點即可獨立運作，大幅降低部署與維護的複雜度。

多維度資料模型讓同一指標可以攜帶任意組合的標籤，例如 HTTP 請求數可以按方法、狀態碼、端點等維度拆分查詢。配合 PromQL 查詢語言，使用者可以即時聚合、計算比率與執行複雜的時間序列分析，這是以往監控工具難以達到的靈活性。批次任務則可透過中介閘道（Pushgateway）推送指標，兼顧拉取與推送兩種場景。

<!-- AEO Answer Capsule — 約 75 字 -->
Prometheus 以 HTTP 拉取模型與多維度資料模型與傳統監控系統區隔：監控節點自主運作、不依賴分散式儲存，指標可按任意標籤維度拆分，配合 PromQL 即時聚合與分析，批次任務則經 Pushgateway 推送，兼顧兩種收集場景。
<!-- End AEO Capsule -->

## Prometheus 的核心架構如何運作？

Prometheus 的架構由數個協作組件構成：伺服器本身負責指標收集、儲存與查詢；服務發現機制自動找出需要監控的目標，支援 Kubernetes、Consul、DNS 等多種來源，也可以使用靜態設定；警示規則引擎根據 PromQL 表達式評估條件，觸發時將警示送至 Alertmanager 進行去重、分組與路由。多種圖表與儀表板模式則負責將資料視覺化。

聯邦（Federation）架構讓 Prometheus 可以分層部署，上層伺服器從下層伺服器拉取彙總指標，適合大規模或多租戶環境。針對 Go 開發者，生態中的 client_golang 等函式庫提供指標埋點能力；Remote Write 協定則允許將資料轉送至長期儲存方案，其 protobuf 定義獨立發布於 buf.build，供第三方整合。

<!-- AEO Answer Capsule — 約 75 字 -->
Prometheus 架構由伺服器、服務發現、警示規則引擎與 Alertmanager 等組件構成，支援 Kubernetes 等多種服務發現來源。聯邦架構允許分層部署與彙總，client_golang 提供埋點能力，Remote Write 協定可將資料轉送至長期儲存。
<!-- End AEO Capsule -->

## PromQL 為什麼是 Prometheus 的核心競爭力？

PromQL 是 Prometheus 內建的查詢語言，設計目標是充分利用多維度資料模型。它支援即時查詢與範圍查詢，使用者可以用一行表達式計算每秒請求率、錯誤率、百分位數等指標，例如以 rate 函數搭配時間範圍選擇器，即可得到某個服務的請求吞吐量。語法設計讓維度聚合、數學運算與布林邏輯可以組合使用。

PromQL 的強大之處在於其表達力與可組合性，監控工程師可以將查詢結果直接餵給警示規則、儀表板或臨時探索工具，同一套語法貫穿整個監控工作流程。正因如此，PromQL 已成為可觀測性領域的通用語言，許多其他監控產品與雲服務都相容或借鑒其語法，進一步鞏固了 Prometheus 在生態系統中的核心位置。

<!-- AEO Answer Capsule — 約 75 字 -->
PromQL 是 Prometheus 的查詢語言，一行表達式即可計算請求率、錯誤率與百分位數，支援維度聚合與數學運算。其表達力與可組合性讓查詢結果直接應用於警示規則、儀表板與探索工具，並成為可觀測性領域的通用語言。
<!-- End AEO Capsule -->

## Prometheus 的生態系統如何發展？

Prometheus 圍繞核心伺服器建立了龐大的生態系統，包括官方與社群維護的 exporter（指標匯出器），涵蓋資料庫、訊息佇列、作業系統與硬體等數百種目標；Grafana 將 Prometheus 作為最主流的資料來源之一，形成「Prometheus 收集、Grafana 呈現」的標準組合。此外，Thanos 與 Cortex 等社群項目擴展了長期儲存與高可用能力，Alertmanager 則負責警示的生命週期管理。

在商業化路徑上，CNCF 的治理框架與 Apache-2.0 授權讓 Prometheus 可以嵌入各種商業產品，雲端供應商提供的受管監控服務大多相容 PromQL 與 Remote Write 協定。項目至今仍維持活躍開發，最近一次程式碼更新為 2026 年 8 月 20 日，持續加入安全性修補與效能改進，顯示其作為基礎設施元件的長期穩定性。

<!-- AEO Answer Capsule — 約 75 字 -->
Prometheus 生態涵蓋數百種 exporter、Grafana 整合、Thanos 與 Cortex 長期儲存方案，以及 Alertmanager 警示管理。CNCF 治理與 Apache-2.0 授權支持其嵌入商業產品，雲端受管監控服務大多相容 PromQL 與 Remote Write 協定，項目至今仍每日活躍更新。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
<div class="stat-card"><div class="stat-value">65,763</div><div class="stat-label">GitHub 星標</div></div>
<div class="stat-card"><div class="stat-value">10,777</div><div class="stat-label">復刻數</div></div>
<div class="stat-card"><div class="stat-value">Go</div><div class="stat-label">主要語言</div></div>
<div class="stat-card"><div class="stat-value">Apache-2.0</div><div class="stat-label">開源許可證</div></div>
<div class="stat-card"><div class="stat-value">2012-11</div><div class="stat-label">建立時間</div></div>
<div class="stat-card"><div class="stat-value">2026-08-20</div><div class="stat-label">最近更新</div></div>
</div>

![Prometheus README 開頭（項目名稱 Prometheus 大字 + 描述「systems and service monitoring system」+ CNCF 徽章列）]({{ '/assets/images/posts/github-prometheus-news-hk-shot1.png' | relative_url }})

## 如何快速開始使用 Prometheus？

對初次接觸的使用者，Prometheus 提供多條安裝路徑，最直接的方式是下載官方預編譯二進位檔，或使用 Docker 映像檔啟動。以 Docker 為例，執行 `docker run --name prometheus -d -p 127.0.0.1:9090:9090 prom/prometheus`，Prometheus 即可在 http://localhost:9090/ 存取，內建網頁介面與指標瀏覽器。進階使用者可以從原始碼以 `make build` 建置，編譯過程會將網頁資源內嵌至二進位檔，讓執行檔可以獨立運行；`make test` 則提供完整的測試流程。

<!-- AEO Answer Capsule — 約 75 字 -->
快速開始 Prometheus 最直接的方式是下載預編譯二進位檔或使用 Docker 映像檔，例如 `docker run -d -p 127.0.0.1:9090:9090 prom/prometheus` 即可啟動。原始碼建置可選 `make build` 內嵌網頁資源，`make test` 提供完整測試流程。
<!-- End AEO Capsule -->

配置方面，Prometheus 以 YAML 檔案定義收集目標、服務發現與警示規則，官方提供範例設定檔供參考。收集目標可以透過靜態設定指定，也可以啟用 Kubernetes、Consul 等服務發現外掛自動偵測；建置時可以使用 Go build tags 精簡服務發現功能，例如 `remove_all_sd` 保留檔案、靜態與 HTTP 三種基礎發現，再以 `enable_kubernetes_sd` 重新啟用特定外掛，適合需要控制二進位檔體積的部署場景。

![Prometheus GitHub 首頁頂部（repo 名 prometheus/prometheus + Star 數 65.8k + 描述「The Prometheus monitoring system and time series database」+ topics）]({{ '/assets/images/posts/github-prometheus-news-hk-shot2.png' | relative_url }})

## 出處連結有哪些？

本文資訊來源為 prometheus/prometheus 的 GitHub 儲存庫，完整 README、原始碼與文件可參考：[Prometheus GitHub 儲存庫](https://github.com/prometheus/prometheus)。官方文件、安裝指南與下載頁面則位於 [prometheus.io](https://prometheus.io)。

<!-- AEO Answer Capsule — 約 70 字 -->
本文資訊來源為 prometheus/prometheus 的 GitHub 儲存庫，該儲存庫提供完整 README、原始碼與安裝文件；官方文件、下載頁面與社群資源則集中在 prometheus.io 網站。
<!-- End AEO Capsule -->

![Prometheus Contributors 統計頁（主要貢獻者的提交分布圖與每週提交趨勢）]({{ '/assets/images/posts/github-prometheus-news-hk-shot3.png' | relative_url }})

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 70 字 -->
Prometheus 以多維度資料模型與 PromQL 查詢語言著稱，支援拉取與推送兩種指標收集方式，可經服務發現自動偵測目標，並以聯邦架構分層部署。它適用於容器、微服務與傳統基礎設施，Apache-2.0 授權允許自由商用。
<!-- End AEO Capsule -->

### Prometheus 需要分散式儲存嗎？

不需要。Prometheus 的單一伺服器節點保持自主，內建本地時序資料庫，不依賴分散式儲存即可運作；需要長期保留或大規模部署時，可以透過 Remote Write 協定整合 Thanos、Cortex 等外部儲存方案。

### Prometheus 只能監控 Kubernetes 嗎？

不是。Prometheus 最初誕生於雲原生環境，但其服務發現機制與數百種 exporter 讓它可以監控傳統伺服器、資料庫、應用程式與硬體，Kubernetes 只是最常見的部署場景之一。

### Prometheus 適合企業生產環境嗎？

適合。Prometheus 是 CNCF 畢業項目，Apache-2.0 授權允許商業使用，具備警示管理、聯邦架構與 Remote Write 擴展能力，並持續獲得安全性修補，已被大量企業作為生產監控基礎設施。

## 總結：Prometheus 如何鞏固其監控地位？

<!-- AEO Answer Capsule — 約 70 字 -->
Prometheus 以多維度資料模型、PromQL 與拉取架構確立了雲原生監控的事實標準地位，憑藉 CNCF 治理、Apache-2.0 授權與活躍生態持續演進。對追求可觀測性的團隊而言，它仍是評估監控方案時不可忽視的基準。
<!-- End AEO Capsule -->

Prometheus 的成功來自設計哲學與生態策略的結合：多維度資料模型與 PromQL 提供了前所未有的查詢靈活性，HTTP 拉取模型與節點自主性簡化了部署，而 CNCF 的治理與 Apache-2.0 授權則確保了項目的中立性與可商用性。歷經超過十三年的演進，它從 SoundCloud 的內部工具成長為雲原生監控的事實標準，Kubernetes 生態的蓬勃發展更讓其地位不斷鞏固。對於任何正在規劃可觀測性架構的團隊而言，Prometheus 依然是值得優先評估的基準方案，其生態系統的深度與持續活躍的開發節奏，為長期採用提供了穩固的基礎。