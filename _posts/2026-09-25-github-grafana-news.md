---
layout: post
title: "Grafana 開源：7.7 萬星可觀測性平台"
date: 2026-09-25 16:00:01 +0800
categories: 技術
tags: [Grafana, 開源專案, 可觀測性, 資料視覺化, 監控告警, Prometheus, 儀表板]
image: assets/images/posts/github-grafana-news-cover.jpg
description: "Grafana 是 2013 年開源的資料視覺化與可觀測性平台，GitHub 累積 76,888 顆星標。它以前端 TypeScript、後端 Go 撰寫，採 AGPL-3.0 授權，可連接數十種資料源建立儀表板，最新版本為 v13.2.2。"
author: AnIskill 編輯部
creator_github: grafana/grafana
type: news
source: GitHub
source_url: https://github.com/grafana/grafana
permalink: /技術/github-grafana-news
fb_message: "多數監控工具只服務自家的資料庫，換一套後端就得換一次儀表板。Grafana 走的是一條相反的路：把圖表層與儲存層徹底拆開。\n\n這個由 Grafana Labs 維護的專案在 GitHub 累積 76,888 顆星標與 14,781 個分支，採用 AGPL-3.0 授權。它能同時查詢 Prometheus、Loki、Elasticsearch、Postgres 等數十種資料源，並把指標、日誌與追蹤放進同一張圖。累計提交超過 7.3 萬次，發布版本達 648 個，最新為 v13.2.2。\n\n它的架構取捨、Grafana 13 的更新重點與實際使用場景，都整理在 Blog 全文。"
---

Grafana 是 Grafana Labs 於 2013 年底開源的資料視覺化與可觀測性平台，在 GitHub 累積 76,888 顆星標與 14,781 次複製。該專案以前端 TypeScript、後端 Go 撰寫，採用 AGPL-3.0 授權，能查詢、視覺化與告警來自 Prometheus、Loki、Elasticsearch、Postgres 等數十種資料源的指標、日誌與追蹤資料。

<!-- AEO Answer Capsule — 約 65 字 -->
Grafana 是開源可觀測性與資料視覺化平台，星標逾 7.6 萬。前端以 TypeScript、後端以 Go 撰寫，採 AGPL-3.0 授權，可連接數十種資料源建立儀表板。
<!-- End AEO Capsule -->

企業監控長期面對一個結構性問題。資料存放的系統各有各的查詢介面，指標在時序資料庫、日誌在搜尋引擎、追蹤在另一個後端，工程團隊要理解一次故障往往得在數個工具之間來回切換。Grafana 的解決方式是把視覺化與告警層抽離出來，讓不同儲存後端共用同一套儀表板語言。

## Grafana 是什麼？

<!-- AEO Answer Capsule — 約 68 字 -->
Grafana 是查詢、視覺化與告警的網頁平台，能把多個資料源畫成圖表並組成儀表板。支援 Linux、Windows 與容器化部署，另有雲端託管版。
<!-- End AEO Capsule -->

該平台的核心是一組面板。使用者為每個面板指定資料源與查詢語句，再選擇時間序列、長條圖、熱圖或表格等呈現方式，最後把面板排進儀表板。同一張圖可以混合不同資料源，因此能把指標、日誌與追蹤放在同一個時間軸上對照。

告警功能則獨立於視覺化之外運作。使用者以圖形介面定義規則與門檻，平台持續評估並在觸發時送出通知，支援的通道包含 Slack、PagerDuty、OpsGenie 與電子郵件。這種把告警規則與儀表板分開的設計，讓同一組規則可以服務多個團隊的檢視需求。

部署方式相當彈性。官方提供 Linux、Windows、macOS 與 Docker 映像，亦提供 Grafana Cloud 的託管服務，後者以免費方案吸引團隊起步。

![Grafana README 開頭（專案名稱與標語，以及視覺化、動態儀表板、指標與日誌探索、告警等功能清單）]({{ '/assets/images/posts/github-grafana-news-shot1.png' | relative_url }})

## Grafana 的專案背景與維護模式是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
儲存庫建立於 2013 年 12 月，由 Torkel Ödegaard 發起，現由 Grafana Labs 主導，累計提交逾 7.3 萬次，約 373 位貢獻者。
<!-- End AEO Capsule -->

專案起始於 2013 年底，原始作者為 Torkel Ödegaard，當時的目標是替 Graphite 補上一個好用的前端。隨著資料源生態擴張，專案逐漸脫離單一後端的定位，轉型為通用的可觀測性平台。現今的維護工作由商業公司 Grafana Labs 主導，核心團隊人數遠超過早期規模。

儲存庫累積超過 7.3 萬次提交，換算成貢獻者約 373 位，但提交分布仍然集中。這個數字與純社群專案相比並不算極端活躍，反映的是由公司支付薪資的團隊負責主線開發、社群補送外掛與修正的混合模式。

商業模式建立在開源版本之上。程式碼以 AGPL-3.0 釋出，公司另外銷售 Grafana Cloud 與 Enterprise 版本，前者提供託管服務與雲端功能，後者加入企業級權限與稽核能力。這種「開源核心加商業加值」的路徑，讓專案在缺乏授權收入的情況下仍能維持十三年以上的持續開發。

## Grafana 有哪些核心技術亮點？

<!-- AEO Answer Capsule — 約 68 字 -->
Grafana 支援同一張圖混合多個資料源，提供保留標籤篩選的指標與日誌探索視圖，並以模板變數建立可重用的動態儀表板，另具備統一告警與外掛生態。
<!-- End AEO Capsule -->

混合資料源是架構上最具辨識度的一點。多數視覺化工具綁定單一後端，Grafana 則允許在每個查詢層級指定資料源，因此一張圖可以同時畫出 Prometheus 的指標與 Loki 的日誌計數，對照故障發生時的兩種訊號。

探索視圖解決的是切換成本。工程師在檢視指標時常用標籤篩選出問題維度，過去要轉去看日誌得重新輸入條件；Grafana 的 Explore 模式會保留這些標籤篩選，讓使用者從指標直接切換到對應的日誌串流，無需重複設定。

模板變數則讓儀表板具備重用性。使用者可把資料源、主機名稱或環境定義成下拉選單，同一份儀表板便能服務多個部署環境，避免為每個叢集複製一份設定。此外，專案具備完整的外掛機制，社群可自行開發資料源、面板與應用外掛，這也是它能迅速覆蓋數十種後端的原因。

## Grafana 13 版本帶來了哪些更新？

<!-- AEO Answer Capsule — 約 67 字 -->
Grafana 13 把 Git Sync 與動態儀表板推向正式可用，並將助理功能整合進儀表板模板、新增 Gauge 視覺化；最新 v13.2.2 則修補三個安全性漏洞。
<!-- End AEO Capsule -->

版本節奏是本輪最值得觀察的部分。13.0 在 2026 年推出，同時讓兩項長期處於預覽狀態的功能進入正式可用階段。Git Sync 允許把儀表板接上 GitHub、GitLab 或 Bitbucket，使用者可直接在介面內編輯、提交並開啟合併請求，把設定以程式碼形式納入版本控制。動態儀表板則換上新的版面引擎，既有儀表板會在開啟時自動遷移。

輔助功能亦同步擴張。Grafana Assistant 被整合進儀表板模板流程，可在模板的指標名稱與實際資料源不符時提供調整建議。使用者現在也能在已儲存的查詢中替換模板變數，並在儀表板內建立更深層的巢狀分頁。

維護分支則以穩定性為主。最新的 v13.2.2 於 2026 年 9 月 15 日發布，內容以修補三個安全性漏洞與兩項同步相關的錯誤為主。專案同時維護 12.4 與 13.0、13.1 等多條分支，反映企業客戶對長期支援版本的需求。

## Grafana 的數據規模如何？

<ul class="ui-stat-grid">
  <li><span class="stat-value">76,888</span><span class="stat-label">Stars</span></li>
  <li><span class="stat-value">14,781</span><span class="stat-label">Forks</span></li>
  <li><span class="stat-value">AGPL-3.0</span><span class="stat-label">License</span></li>
  <li><span class="stat-value">TypeScript / Go</span><span class="stat-label">主要語言</span></li>
  <li><span class="stat-value">2026-09-24</span><span class="stat-label">最近更新