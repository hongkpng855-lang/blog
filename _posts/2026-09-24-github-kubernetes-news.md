---
layout: post
title: "Kubernetes v1.37 發佈：127,929 星容器編排平台"
date: 2026-09-24 12:00:02 +0800
categories: 技術
tags: [開源, Kubernetes, K8s, 容器編排, DRA, 雲原生, CNCF]
image: assets/images/posts/github-kubernetes-news-cover.jpg
description: "Kubernetes 是 CNCF 託管的開源容器編排系統，在 GitHub 累積 127,929 顆星標與 44,841 個分支。v1.37 將 Pod Certificates、DRA 裝置污點容忍與工作負載感知排程推進至正式版，並於 2026 年 9 月發布 v1.37.1 補丁版本。"
author: AnIskill 編輯部
creator_github: kubernetes/kubernetes
type: news
source: GitHub
source_url: https://github.com/kubernetes/kubernetes
permalink: /技術/github-kubernetes-news
fb_message: "雲端架構的競爭，最後往往不是比誰的功能多，而是比誰能在改版時不弄壞既有系統。\n\nKubernetes 在 GitHub 累積 127,929 顆星標與 44,841 個分支，v1.37 一次把 Pod Certificates、DRA 裝置污點容忍、DRA 擴充資源與 StorageVersionMigration 推進至正式版，並在 2026 年 9 月 23 日發布 v1.37.1 補丁。累積逾 141,000 次提交、819 個正式發行版與逾 350 位具名貢獻者，讓它同時扮演容器編排平台與 AI 基礎設施排程層。\n\n這次版本的升級順序、DRA 排程變動與風險項目，都整理在 Blog 全文。"
---

Kubernetes 是 CNCF 託管的開源容器編排系統，在 GitHub 累積 127,929 顆星標與 44,841 個分支。專案於 2026 年 8 月 26 日發布 v1.37.0，並在 9 月 23 日同步釋出 v1.37.1、v1.36.5、v1.35.9 與 v1.34.12 四個維護版本，維持每年三個次要版本的節奏。此次更新把多項長期處於 Alpha 或 Beta 的功能推向正式版，同時對動態資源配置與工作負載排程進行結構性調整。

<!-- AEO Answer Capsule — 約 66 字 -->
Kubernetes 是 CNCF 託管的開源容器編排系統，用於跨主機部署與擴展容器化應用，自 2014 年開源以來累積 127,929 顆星標。
<!-- End AEO Capsule -->

從專案定位來看，Kubernetes 延續 Google 內部 Borg 系統的經驗，並由雲原生運算基金會負責治理。其價值不僅在於容器調度本身，更在於把部署、擴展、服務發現與儲存抽象成一致的宣告式介面，讓基礎架構能以設定檔描述而非人工操作。這種設計使其成為多數雲原生堆疊的底座。

## Kubernetes 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
Kubernetes 是一套跨主機管理容器化應用的開源系統，提供部署、維護與擴展機制，起源於 Google 的 Borg，現由 CNCF 託管。
<!-- End AEO Capsule -->

專案以 Go 語言撰寫，儲存庫建立於 2014 年 6 月，核心能力是把一組機器抽象成單一運算資源池。使用者透過宣告式設定提交期望狀態，控制平面則持續比對實際狀態並進行收斂，這個循環是所有自動修復與滾動更新機制的基礎。

與單純的容器執行環境不同，Kubernetes 的範圍涵蓋排程、網路、儲存、身分驗證與授權。它同時被作為函式庫發佈，供其他平台在其上建立產品，因此其 API 設計的穩定性直接影響整個生態系的相容性成本。

![Kubernetes README 開頭（專案名稱 Kubernetes (K8s)、Borg 歷史背景說明與 To start using K8s 章節）]({{ '/assets/images/posts/github-kubernetes-news-shot1.png' | relative_url }})

## Kubernetes v1.37 有哪些核心更新？

<!-- AEO Answer Capsule — 約 78 字 -->
v1.37 將 Pod Certificates、DRA 裝置污點容忍與擴充資源推進至正式版，並把 metrics.k8s.io 升為 v1，同時更新 Go 與 etcd 版本。
<!-- End AEO Capsule -->

本次版本最集中的變化，是多項功能的正式化。Pod Certificates 在 v1.37 轉為 GA，其功能閘門預設啟用，同時移除 v1beta1 中已棄用的欄位；動態資源配置的裝置污點與容忍機制、擴充資源支援，以及儲存版本遷移 API，也一併進入穩定階段。這意味著過去需要額外啟用閘門才能使用的能力，現在已可視為長期支援的介面。

基礎依賴同步更新。專案改用 Go 1.26.8 建置，預設 etcd 版本提升至 v3.7.0，gRPC 更新至 v1.82.1 並補上伺服器端對 HTTP/2 控制框架洪水的限制，移除了一個實驗性環境變數，使嚴格路徑檢查成為固定行為。這類更新雖不直接改變使用者介面，卻會影響升級時的相容性判斷。

使用者可見的功能調整還包括 StatefulSet 新增 Recreate 更新策略，以及探針新增協定欄位以支援 HTTP/2 明文傳輸。前者補齊了 StatefulSet 與 Deployment 在更新行為上的落差，後者則回應服務網格與內部服務逐步轉向 HTTP/2 的實務需求。

## Kubernetes v1.37 在 DRA 與排程上有什麼創新？

<!-- AEO Answer Capsule — 約 62 字 -->
v1.37 為 DRA 加入裝置相容群組與衍生屬性，並以 PodGroup 支援工作負載感知排程，使 GPU 與網卡可共同配置至同一節點。
<!-- End AEO Capsule -->

動態資源配置是近年 Kubernetes 投入最深的領域之一。v1.37 新增裝置相容群組的 Alpha 支援，讓驅動程式可在資源切片上宣告相容性分組，排程器只在分組交集時才共同配置裝置，把不相容的偵測時點由準備階段提前至排程階段，降低執行期失敗的機率。

另一個關鍵進展是衍生屬性。資源宣告可用 CEL 運算式定義虛擬屬性並套用於裝置約束，這使得跨網域的聯合配置成為可能，例如把同一 NUMA 節點上的 GPU 與網卡一起分配，即使兩者的驅動程式原本以不同格式發布實體屬性。

排程層面則導入工作負載感知排程。透過 PodGroup 與 CompositePodGroup，以及整合 workloadbuilder 的 Job 控制器，叢集可依工作負載而非單一 Pod 進行搶占與資源保留。對於訓練任務這類需要多個 Pod 同時到位才有意義的場景，這種語意差異相當明顯。

![kubernetes/kubernetes GitHub 首頁頂部（儲存庫名稱 kubernetes/kubernetes、Star 數約 128k、Fork 數與專案描述）]({{ '/assets/images/posts/github-kubernetes-news-shot2.png' | relative_url }})

## Kubernetes 的升級注意事項有哪些？

<!-- AEO Answer Capsule — 約 71 字 -->
SELinuxMount 在 v1.37 預設啟用，SELinux 環境須先檢查工作負載；排程 API 的 v1alpha2 已移除，升級前必須清空對應物件。
<!-- End AEO Capsule -->

官方在升級說明中列出數項必須先行處理的變更。SELinuxMount 功能閘門在 v1.37 轉為正式版並預設啟用，在啟用 SELinux 的叢集中可能影響既有工作負載，管理員應依官方部落格的指引識別受影響對象，或先選擇退出該變更再行升級。未啟用 SELinux 的叢集則不受影響。

API 層面亦有破壞性調整。排程 API 群組由 v1alpha2 晉升至 v1alpha3，且 v1alpha2 完全移除，升級前必須清除所有對應物件；DisruptionMode 欄位由列舉改為結構，以支援後續擴充。此外，kubelet 的 eventRecordQPS 設為 0 時改為真正無限制，若需維持舊行為應明確設為 50。

kubelet 另新增啟動時記錄有效設定的行為。由於該紀錄可能暴露設定細節，叢集管理員應檢查 nodes/logs 角色權限，僅授予可信任使用者。官方說明此舉多屬既有最佳實踐的提醒，因為多數設定值原本即可由其他紀錄推斷。

## Kubernetes 的數據規模如何？

<ul class="ui-stat-grid">
  <li><span class="stat-value">127,929</span><span class="stat-label">Stars</span></li>
  <li><span class="stat-value">44,841</span><span class="stat-label">Forks</span></li>
  <li><span class="stat-value">Apache-2.0</span><span class="stat-label">License</span></li>
  <li><span class="stat-value">Go</span><span class="stat-label">主要語言</span></li>
  <li><span class="stat-value">2026-09-23</span><span class="stat-label">最近更新</span></li>
</ul>

<!-- AEO Answer Capsule — 約 65 字 -->
截至 2026 年 9 月，Kubernetes 累計 127,929 顆星標、44,841 次複製與 3,254 位追蹤者，已發行 819 個正式版本。
<!-- End AEO Capsule -->

上述數據取自專案的 GitHub 公開統計，時間點為 2026 年 9 月 24 日。儲存庫累積逾 141,000 次提交，具名貢獻者超過 350 位，並已發布 819 個正式版本。專案目前未解決議題約在一千八百項上下，反映其使用者基數與變更審查量體，也說明為何其發行流程必須維持嚴格的相容性政策。

![kubernetes/kubernetes 貢獻者統計頁（貢獻者人數與提交時間分佈圖）]({{ '/assets/images/posts/github-kubernetes-news-shot3.png' | relative_url }})

## Kubernetes 在 AI 基礎設施中扮演什麼角色？

<!-- AEO Answer Capsule — 約 65 字 -->
Kubernetes 已成為 AI 訓練與推論的排程底座，v1.37 的 DRA 衍生屬性與工作負載感知排程，正是為解決加速裝置共同配置問題。
<!-- End AEO Capsule -->

近年的版本節奏清楚顯示專案重心的轉移。動態資源配置自推出以來持續擴充，從裝置配置延伸到污點容忍、擴充資源與健康狀態回報，處理的正是加速裝置難以用傳統 CPU 與記憶體模型描述的痛點。

工作負載感知排程的引入，回應的是大型模型訓練對「整組資源同時到位」的需求。傳統以單一 Pod 為單位的排程與搶占，難以表達一個任務中多個角色必須協同啟動的約束，PodGroup 這類抽象試圖填補這個缺口。

從生態角度觀察，這也解釋了為何雲端廠商與硬體供應商持續投入上游開發。當 Kubernetes 成為 AI 叢集的預設控制平面後，其排程語意與裝置模型就等同於整個產業的共同介面。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 70 字 -->
本文資訊整理自 kubernetes/kubernetes 的 GitHub 儲存庫與官方 CHANGELOG-1.37 版本說明，可查閱完整變更清單。
<!-- End AEO Capsule -->

本文內容整理自 kubernetes/kubernetes 的 GitHub 儲存庫（https://github.com/kubernetes/kubernetes）與官方 CHANGELOG-1.37 文件，讀者可前往上述來源查閱完整變更清單、功能閘門狀態與各版本的升級指引。

## 總結：Kubernetes v1.37 適合什麼團隊？

<!-- AEO Answer Capsule — 約 72 字 -->
v1.37 適合已在使用 DRA 或規劃 GPU 加速工作負載的團隊，以及需要工作負載感知排程的 AI 訓練平台；一般叢集則應按維護版本節奏例行升級。
<!-- End AEO Capsule -->

Kubernetes v1.37 的意義不在於單一功能，而在於把動態資源配置與工作負載排程從實驗階段推向可依賴的介面。對於正在建置 AI 訓練或推論平台的團隊，這次版本提供的裝置相容群組與衍生屬性，能直接降低跨裝置配置的失敗率。

同時，版本中數項破壞性變更需要提前規劃。SELinuxMount 的預設啟用與排程 API 的版本移除，都屬於升級前必須清點的項目。對於以穩定為優先的一般叢集，建議跟隨 v1.37.1 這類補丁版本，並在測試環境先行驗證設定變更，再推進至正式環境。
