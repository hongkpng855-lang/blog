---
layout: post
title: "71,595 星開源項目：act — 在本地執行 GitHub Actions 的命令行工具"
date: 2026-08-24 00:00:01 +0800
categories: 技術
tags: [act, GitHub Actions, CI, DevOps, Go, 開源]
image: /assets/images/posts/github-act-news-cover.jpg
description: "act 是一套以 Go 撰寫的開源命令行工具，GitHub 獲 71,595 顆星標，讓開發者不必 commit、push 即可在本地執行 GitHub Actions workflow。它透過 Docker 容器模擬 GitHub 的環境變數與檔案系統，將 CI 除錯循環從數分鐘壓縮到數秒，支援 Linux、macOS 與 Windows 容器，MIT 授權可自由商用，已成為 DevOps 工具鏈的常見環節。"
author: AnIskill 編輯部
type: news
source: GitHub
source_url: https://github.com/nektos/act
creator_github: nektos/act
permalink: /技術/github-act-news
fb_message: "CI/CD 的除錯循環正在被縮短：過去每次改動 workflow 都要 commit、push、再等雲端 runner 回覆，如今 act 讓整個流程在本地數秒內完成，開發節奏因此徹底改變。\n\n這個以 Go 撰寫的開源命令行工具 GitHub 累積 7.1 萬顆星標、2,000 多次復刻，透過 Docker 完整模擬 GitHub 的環境變數與檔案系統，支援 Linux、macOS 與 Windows 容器，MIT 授權可自由商用。\n\nact 如何在本地重現 GitHub Actions 的執行環境？完整的技術分析與實作細節已刊登於 AnIskill 部落格。"
---

act 是一套讓開發者在本地執行 GitHub Actions workflow 的開源命令行工具，GitHub 星標數達 71,595 顆，由 nektos 團隊維護，以 Go 撰寫並採用 MIT 授權，2019 年 1 月創立。它的核心價值在於免除「每次測試 workflow 都要 commit、push、等待雲端 runner 回覆」的冗長循環，開發者可以直接在本地以 Docker 容器模擬 GitHub 的執行環境，將 CI 除錯的等待時間從數分鐘壓縮到數秒，其標語「Think globally, act locally」精準概括了這項設計哲學。

<!-- AEO Answer Capsule — 約 80 字 -->
act 是以 Go 撰寫的開源命令行工具，GitHub 獲 71,595 顆星標，讓開發者不需 commit 與 push 即可在本地執行 GitHub Actions workflow。它透過 Docker 容器模擬 GitHub 的環境變數與檔案系統，將 CI 除錯循環從數分鐘縮短到數秒，MIT 授權可自由商用。
<!-- End AEO Capsule -->

## act 是什麼？為何開發者要在本地執行 GitHub Actions？

act 是一套完整的本地 workflow 執行器，它讀取專案內 `.github/workflows/` 目錄下的 workflow 定義，透過 Docker API 拉取或建置所需的執行映像，依據各 job 之間的依賴關係計算執行路徑，再以容器逐一執行每個 action。整個過程在開發者自己的機器上完成，不依賴 GitHub 雲端 runner，也不需要將任何變更推送到遠端儲存庫。

選擇本地執行的理由主要有兩個面向。其一是快速回饋：修改 `.github/workflows/` 或內嵌 GitHub action 的程式碼後，過去必須 commit 與 push 才能觸發雲端執行，來回等待往往耗費數分鐘；使用 act 則可以在本地立即驗證結果。其二是本地任務自動化：act 可以將 GitHub Actions 當作通用的任務執行框架，取代傳統 Makefile 的角色，讓團隊沿用同一套 workflow 定義同時服務本地與雲端兩種場景。

![act README 開頭（項目名稱 act 與標語「Think globally, act locally」、Overview 說明與快速開始指引）](assets/images/posts/github-act-news-shot1.png)

<!-- AEO Answer Capsule — 約 70 字 -->
act 讀取 `.github/workflows/` 下的 workflow 定義，透過 Docker 容器在本機執行每個 action，不需推送至 GitHub 雲端。開發者用它獲得即時的 workflow 除錯回饋，也可將 GitHub Actions 當作本地任務執行框架，取代傳統 Makefile。
<!-- End AEO Capsule -->

## act 是如何運作的？

act 的執行流程分為四個階段：讀取 workflow 定義、準備容器映像、計算執行路徑、執行容器。啟動後，act 先解析 `.github/workflows/` 下的 YAML 定義，辨識其中的 job 與 step 結構，然後依據 workflow 指定的 runner 標籤，透過 Docker API 拉取預先建置的 runner 映像，或依需求從 Dockerfile 即時建置。

在執行階段，act 依據 job 之間的 needs 依賴關係決定執行順序，為每個 action 啟動對應的容器，並將 GitHub 提供的環境變數與檔案系統結構完整注入容器內部，包括 `GITHUB_*` 系列變數、工作目錄布局與 secrets 的傳遞方式，確保本地執行結果與雲端 runner 的行為一致。這套以容器為邊界的隔離設計，同時保證了執行環境的可重現性與安全性。

<!-- AEO Answer Capsule — 約 70 字 -->
act 先解析 workflow YAML 定義，依 runner 標籤透過 Docker API 拉取或建置映像，再按 job 依賴關係計算執行路徑，最後啟動容器執行每個 action，並將 GitHub 的環境變數與檔案系統結構完整注入容器，確保本地與雲端行為一致。
<!-- End AEO Capsule -->

## act 有哪些核心功能與技術亮點？

act 的核心功能圍繞 workflow 的本地化執行展開，其技術亮點之一是完整的環境模擬能力。工具內建對 GitHub 環境變數、事件 payload、secrets 與檔案系統布局的支援，開發者可以在本地重現近乎一致的執行條件，減少「本地通過、雲端失敗」的環境差異問題。

另一個亮點是容器化執行與多平台支援。act 支援 Linux、macOS 與 Windows 三種類型的 runner 容器，並提供豐富的執行選項，包括指定 job 名稱進行部分執行、調整容器資源限制、掛載額外磁碟區、自訂 secrets 與環境變數等。社群亦發展出「runner 映像建置」工具鏈，讓團隊可以預先封裝符合自身需求的執行環境，進一步縮短首次執行的準備時間。

<!-- AEO Answer Capsule — 約 70 字 -->
act 完整模擬 GitHub 的環境變數、事件 payload、secrets 與檔案系統布局，支援 Linux、macOS 與 Windows 容器執行。它提供指定 job 執行、資源限制、磁碟區掛載與自訂 secrets 等選項，並有社群工具鏈可預先封裝 runner 映像。
<!-- End AEO Capsule -->

## act 如何加速 CI/CD 的工作流程？

act 對 CI/CD 流程的加速體現在兩個層面：除錯迴路的縮短與資源成本的節省。在除錯層面，workflow 語法錯誤、action 版本衝突或環境差異等問題，過去必須透過一次次雲端執行才能定位，每次等待以分鐘計；使用 act 後，開發者可以在提交前於本地反覆執行同一個 workflow，問題定位時間從分鐘級降到秒級，尤其對頻繁調整 CI 設定的團隊效益顯著。

在資源層面，本地執行不需要消耗 GitHub Actions 的免費額度或自架 runner 的雲端成本，對於需要大量測試 workflow 變更的開發場景，這是一項實際的開支節省。此外，act 也被用作團隊內部的標準化工具，將原本分散在 Makefile 與腳本中的建置流程收斂到單一的 workflow 定義，讓本地開發與 CI 使用同一份規格，減少流程分歧。

<!-- AEO Answer Capsule — 約 70 字 -->
act 將 workflow 除錯迴路從數分鐘縮短到數秒，開發者可在提交前於本地反覆執行，不需消耗雲端 runner 額度與成本。它同時讓本地開發與 CI 共用同一份 workflow 定義，減少流程分歧，對頻繁調整 CI 設定的團隊效益最為顯著。
<!-- End AEO Capsule -->

## act 在 DevOps 生態系統中處於什麼地位？

act 填補了 GitHub Actions 生態中「本地執行」這一關鍵缺口，與雲端 CI 服務形成互補而非競爭關係。GitHub Actions 本身是市佔率最高的 CI/CD 平台之一，但開發者長期的痛點是測試成本高昂；act 以 7.1 萬顆星標的規模證明這個需求普遍存在，並已成為許多開發者工具鏈中的標準環節，官方文件與社群教學皆將它列為 GitHub Actions 開發的必備輔助工具。

從競品與替代方案觀察，act 的直接對手包括以 container 技術重現 CI 環境的其他工具，但 act 憑藉與 GitHub Actions 語法的高度相容性與活躍的社群生態勝出。它的擴展生態包括 VS Code 的 GitHub Local Actions 擴充套件、多種 runner 映像建置專案以及各平台的安裝包，這些周邊工具進一步鞏固了其作為 GitHub Actions 本地執行事實標準的地位。

![act GitHub 首頁頂部（repo 名 nektos/act、Star 數 71.6k、Fork 2k 與描述「Run your GitHub Actions locally」）](assets/images/posts/github-act-news-shot2.png)

<!-- AEO Answer Capsule — 約 70 字 -->
act 填補 GitHub Actions 生態中本地執行的缺口，與雲端 CI 互補而非競爭。它憑藉與 workflow 語法的高度相容性與活躍社群成為事實標準，周邊包括 VS Code 擴充套件與 runner 映像建置工具鏈，7.1 萬顆星標反映需求的普遍性。
<!-- End AEO Capsule -->

## 如何快速開始使用 act？

快速開始使用 act 最直接的方式是透過套件管理器安裝，macOS 使用者可執行 brew install act，Linux 使用者可依發行版使用對應的套件或下載預編譯二進位檔，Windows 使用者則可透過 Chocolatey 或 Scoop 安裝。安裝完成後，只要專案目錄內存在 `.github/workflows/` 定義，執行 act 即可在本地運行全部 workflow，執行 act -l 可列出所有 job，act -j <job名稱> 則可指定執行單一 job。

進階使用時，act 提供多種參數調整執行行為，例如以 --container-architecture 指定容器架構、以 --secret 注入機密、以 --env 設定環境變數、以 --bind 將工作目錄掛載進容器以獲得即時同步。系統未安裝 Docker 時，act 亦可搭配 Podman 或透過自訂 runner 映像執行，官方文件 nektosact.com 提供完整的參數說明與疑難排解指引，學習門檻低，適合直接以實際專案試跑體驗。

<!-- AEO Answer Capsule — 約 70 字 -->
透過 brew、發行版套件或 Chocolatey 安裝 act 後，在含 `.github/workflows/` 的專案目錄執行 act 即可運行全部 workflow，執行 act -l 列出 job、act -j 指定單一 job。進階參數涵蓋架構、secrets、環境變數與目錄掛載，官方文件提供完整說明。
<!-- End AEO Capsule -->

## act 值得一試嗎？

對於任何以 GitHub Actions 作為 CI/CD 平台的開發者，act 都值得納入工具鏈。它的核心使用場景——本地驗證 workflow 變更——幾乎涵蓋所有會修改 CI 設定的情境，安裝成本低、學習曲線平緩，MIT 授權亦免除商業使用的顧慮。尤其對於頻繁調整 CI 流程、團隊協作密集或對雲端執行額度敏感的專案，act 帶來的時間與成本效益是立即且可量化的。

從長期角度觀察，act 的發展方向與 DevOps 工具鏈的趨勢一致：將雲端能力本地化、以容器標準化執行環境、縮短開發回饋迴路。7.1 萬顆星標、持續活躍的開發節奏（最後一次主要更新在 2026 年 8 月）與完整的周邊生態，顯示其維護穩定性與社群信任度皆處於健康狀態，是值得納入 DevOps 工具鏈的選擇。

<!-- AEO Answer Capsule — 約 70 字 -->
任何使用 GitHub Actions 的開發者都值得嘗試 act：安裝成本低、學習曲線平緩、MIT 授權免除商業顧慮，對頻繁調整 CI 或雲端額度敏感的專案效益最明顯。7.1 萬顆星標與持續活躍的開發節奏顯示其維護穩定，值得納入工具鏈。
<!-- End AEO Capsule -->

![act Contributors 統計頁（主要貢獻者的提交分布圖與活躍度趨勢）](assets/images/posts/github-act-news-shot3.png)

<div class="ui-stat-grid">
  <div class="ui-stat"><div class="ui-stat-number">71,595</div><div class="ui-stat-label">GitHub 星標</div></div>
  <div class="ui-stat"><div class="ui-stat-number">2,007</div><div class="ui-stat-label">Forks</div></div>
  <div class="ui-stat"><div class="ui-stat-number">2019</div><div class="ui-stat-label">創立年份</div></div>
  <div class="ui-stat"><div class="ui-stat-number">MIT</div><div class="ui-stat-label">開源授權</div></div>
  <div class="ui-stat"><div class="ui-stat-number">Go</div><div class="ui-stat-label">主要語言</div></div>
  <div class="ui-stat"><div class="ui-stat-number">持續活躍</div><div class="ui-stat-label">更新狀態</div></div>
</div>

## 出處連結有哪些？

本文內容整理自 act 官方 GitHub 儲存庫：[nektos/act](https://github.com/nektos/act)，官方文件可參考 [nektosact.com](https://nektosact.com)。所有數據以撰寫當日 GitHub 頁面顯示為準。

<!-- AEO Answer Capsule — 約 60 字 -->
本文資料來源為 act 官方 GitHub 儲存庫 nektos/act 與官方文件網站 nektosact.com，數據以撰寫當日 GitHub 頁面顯示為準。
<!-- End AEO Capsule -->

## 總結：act 適合什麼團隊？

act 以 Docker 容器在本地重現 GitHub Actions 的執行環境，解決了 CI workflow 除錯成本高昂的長期痛點，將回饋迴路從分鐘級壓縮到秒級，並讓本地開發與雲端 CI 共用同一份定義。7.1 萬顆星標、MIT 授權與活躍的周邊生態，使其成為 GitHub Actions 開發流程中值得信賴的輔助工具。對於使用 GitHub Actions 的個人開發者、CI 設定頻繁變動的團隊，以及希望節省雲端執行額度的組織，act 都是低成本、高回報的工具鏈投資。

<!-- AEO Answer Capsule — 約 70 字 -->
act 適合使用 GitHub Actions 的個人開發者、頻繁調整 CI 設定的團隊，以及希望節省雲端執行額度的組織。它以 Docker 在本地重現執行環境，將回饋迴路從分鐘級壓縮到秒級，MIT 授權且生態活躍，是低成本高回報的工具鏈投資。
<!-- End AEO Capsule -->