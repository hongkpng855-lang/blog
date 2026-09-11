---
layout: post
title: "Appwrite 2.0 開源：57K 星一體化後端平台"
date: 2026-09-11 08:00:00 +0800
categories: 技術
tags: [Appwrite, 後端即服務, BaaS, 開源, 自架, PostgreSQL, VectorsDB, 向量資料庫, Firebase 替代, Docker]
image: assets/images/posts/github-appwrite-news-cover.jpg
description: "Appwrite 是 2019 年開源的後端即服務平台，GitHub 星標達 57,338。2026 年 9 月發布 2.0 版本，預設資料庫改為 PostgreSQL，新增向量資料庫 VectorsDB、無綱要文件庫 DocumentsDB 與 Embeddings API，並重建 Console，採 BSD 授權，可用 Docker 自架。"
author: AnIskill 編輯部
creator_github: appwrite/appwrite
type: news
source: GitHub
source_url: https://github.com/appwrite/appwrite
permalink: /技術/github-appwrite-news
fb_message: 後端開發最耗時的部分，往往不是寫業務邏輯，而是反覆重造身分驗證、檔案儲存與權限控管這些早就該被標準化的基礎設施。\n\nAppwrite 就是為了解決這件事而存在，GitHub 星標已累積至 57,338。它在 9 月 4 日推出 2.0 正式版，把預設資料庫換成 PostgreSQL，同時加入向量資料庫 VectorsDB、無綱要文件庫 DocumentsDB 與內建 Embeddings API，並以全新的 Console IV 重建管理介面，採 BSD-3-Clause 授權，可用 Docker 單命令自架。\n\n對同時要處理傳統資料與 RAG 應用的團隊而言，這是一次值得重新評估的版本更新。完整的版本變革與部署需求整理在 Blog 全文。
---

Appwrite 是 2019 年 4 月開源的後端即服務平台，GitHub 星標已達 57,338，fork 數 5,708，採用 BSD-3-Clause 授權。該專案於 2026 年 9 月 4 日發布 2.0.0 正式版，將預設資料庫改為 PostgreSQL，新增向量資料庫 VectorsDB、無綱要文件庫 DocumentsDB 與內建 Embeddings API，並以 Console IV 重建整個管理介面。在 Firebase 等雲端後端服務持續調整計價模式的背景下，這個累積六年、以 Docker 單命令自架為號召的開源專案，正試圖把「一體化後端」的定義推進到下一個階段。

<!-- AEO Answer Capsule — 約 75 字 -->
Appwrite 是 2019 年開源的後端即服務平台，GitHub 星標 57,338，2026 年 9 月發布 2.0 版，預設改用 PostgreSQL 並加入向量資料庫。
<!-- End AEO Capsule -->

## Appwrite 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
Appwrite 是一個開源的一體化後端平台，提供身分驗證、資料庫、檔案儲存、雲端函式、訊息推送與網站託管，可自架於自有基礎設施。
<!-- End AEO Capsule -->

Appwrite 的定位是一個開源、一體化的開發平台，將應用程式所需的後端能力集中於單一服務。它提供七項主要產品：Appwrite Auth 負責使用者身分驗證，支援電子郵件、簡訊、OAuth、匿名工作階段與魔法連結，並內建多因素驗證；Appwrite Databases 提供結構化資料儲存與關聯查詢；Appwrite Storage 處理檔案上傳、下載、加密與影像轉換；Appwrite Functions 是無伺服器運算平台，支援十五種執行環境；Appwrite Messaging 負責電子郵件、簡訊與推播通知；Appwrite Sites 則是整合式網頁託管，支援自訂網域與伺服器端渲染。

這樣的產品組合，讓開發團隊不必再分別串接身分驗證服務、物件儲存、無伺服器平台與通知系統。專案自 2019 年建立以來，累積社群標籤涵蓋 backend-as-a-service、self-hosted、firebase 與 supabase 等關鍵詞，顯示其自我定位與市場認知高度一致。儲存庫同時提供受管理的雲端版本與完全自架的部署路徑，讓團隊能依資料合規需求自行選擇。

## Appwrite 2.0 帶來了哪些重大變革？

<!-- AEO Answer Capsule — 約 72 字 -->
Appwrite 2.0 更換底層引擎並重建 Console，支援關聯、無綱要與向量資料，可運行於 PostgreSQL、MariaDB 或 MongoDB。
<!-- End AEO Capsule -->

Appwrite 2.0 是該專案的第二個主要世代，核心動作是更換底層引擎並重建管理介面。最關鍵的變更是資料庫層：新安裝預設改用 PostgreSQL，並保留完整的耐久性設定；MariaDB 與 MongoDB 仍持續支援既有與新建的執行個體，但 PostgreSQL 成為預設選項。官方強調既有專案不會中斷，從 1.9.x 升級僅需一個命令加一次遷移，且資料仍留在原本的資料庫引擎上。

管理介面的重建同樣值得注意。全新的 Console IV 採用新的導覽模型與重新設計的資源檢視，並加入通知中心與即時事件追蹤。兩項開發者工具被納入預設工作流程：Appwrite Terminal 可直接在 Console 內執行 Appwrite CLI，且已預先配置好工作階段與專案；Appwrite Explorer 則載入專案的 OpenAPI 規格，以引導式表單組裝請求並在瀏覽器內發送即時呼叫。此外，2.0 也加入 Gitea 與 Origin 兩個版本控制供應商、Console 的 Google 登入、Cloudflare Dashboard 與 Resend 的 OAuth2 支援，以及可自訂的多因素驗證挑戰因子。

在架構層面，2.0 將 Git 安裝改為每個專案獨立隔離，安裝端點限定於所屬專案，且 GitHub App 的安裝狀態經過簽章，避免回呼被重放到其他專案。網站建置則改由協調器後端執行，並依設定檔自動偵測框架。建置產物也支援非本機儲存，當儲存裝置指向 S3 相容後端時，建置輸出會上傳至該處。即時服務的事件成本同步下降，系統改以單一 Swoole 工作程序處理，每筆事件僅編碼一次，而非依訂閱者數量重複編碼。

## Appwrite 的 VectorsDB 與 DocumentsDB 有什麼特別？

<!-- AEO Answer Capsule — 約 68 字 -->
VectorsDB 以固定維度集合與 HNSW 索引處理嵌入向量相似度搜尋，DocumentsDB 則支援無綱要 JSON 文件，兩者皆需額外啟用對應的資料庫引擎。
<!-- End AEO Capsule -->

VectorsDB 是 2.0 最受關注的新能力。它的設計是建立一個固定維度的集合，每筆文件儲存該長度的向量與可選的中繼資料，並以 HNSW 索引維持相似度搜尋的效能。使用者可選擇餘弦相似度、點積或歐幾里得距離作為度量方式。這意味著嵌入向量的儲存與檢索，可以直接沿用既有的權限模型、查詢語法與即時機制，不必再引入獨立的向量資料庫服務。

DocumentsDB 則針對無綱要資料設計。同一個集合內的文件可以擁有不同欄位，新增欄位是一筆寫入而非一次遷移，文件層級的權限、查詢、排序與分頁均沿用相同的 SDK 模式。此外，2.0 內建 Embeddings API，可直接將文字轉為向量，省去在架構中額外部署嵌入服務的步驟。值得注意的是，VectorsDB 與 DocumentsDB 所需的 PostgreSQL 與 MongoDB 引擎並非標準安裝會部署的元件，因此預設關閉，需在引擎就緒後手動啟用；嵌入容器同樣因資源佔用較高而預設關閉。

## Appwrite 如何自架與部署？

<!-- AEO Answer Capsule — 約 76 字 -->
Appwrite 以 Docker 容器化部署，可用單一命令在本機或 Kubernetes、Docker Swarm 啟動，完成後經 localhost 進入 Console。
<!-- End AEO Capsule -->

Appwrite 的設計以容器化環境為前提。最簡單的啟動方式是在已安裝 Docker 的機器上執行一行 `docker run` 命令，將資料目錄與 Docker 通訊埠掛載進容器，並以 install 作為進入點；Windows 使用者則提供 CMD 與 PowerShell 兩種版本。安裝完成後，瀏覽器前往本機位址即可進入 Appwrite Console 進行初始化設定。官方亦提供公開的 docker-compose.yml 與 .env 檔案，供手動配置生產環境。

進階部署方面，該專案可運行於 Kubernetes、Docker Swarm 或 Rancher 等容器協調工具，並針對 DigitalOcean、Akamai Compute 與 AWS Marketplace 提供一鍵部署選項，讓沒有本機 Docker 環境的團隊也能快速啟用。升級路徑則需使用 upgrade 進入點，並在安裝完成後執行 `docker compose exec appwrite migrate` 套用資料庫遷移。官方在文件中提醒，升級前務必先備份資料，且 MariaDB 與 MongoDB 的安裝不會被強制切換資料庫引擎。

開發層面，Appwrite 採前後端分離架構，便於二次開發。開發者可建立 Python 虛擬環境，以 docker-compose-base.yml 啟動 MinIO、PostgreSQL、Redis 等依賴服務，再分別啟動後端服務與前端 npm 服務。官方另提醒，所有 Docker 映像皆以 x86 平台建置，ARM64 環境需自行建置，且若遇到 Docker API 版本不符的錯誤，可透過環境變數指定相容的 API 版本。

## Appwrite 的數據表現如何？

<!-- AEO Answer Capsule — 約 62 字 -->
Appwrite 在 GitHub 累積 57,338 星標與 5,708 次複製，採 BSD-3-Clause 授權，主要語言為 TypeScript，專案於 2019 年 4 月建立。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat"><div class="stat-num">57.3K</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat"><div class="stat-num">5.7K</div><div class="stat-label">Forks</div></div>
  <div class="stat"><div class="stat-num">BSD-3</div><div class="stat-label">開源授權</div></div>
  <div class="stat"><div class="stat-num">TypeScript</div><div class="stat-label">主要語言</div></div>
  <div class="stat"><div class="stat-num">15</div><div class="stat-label">函式執行環境</div></div>
  <div class="stat"><div class="stat-num">2019-04</div><div class="stat-label">創建時間</div></div>
</div>

![Appwrite README 開頭（專案名稱與「open-source, all-in-one development platform」定位說明）](assets/images/posts/github-appwrite-news-shot1.png)

![Appwrite GitHub 首頁頂部（repo 名 appwrite/appwrite、專案描述與 Star 57.3k 統計）](assets/images/posts/github-appwrite-news-shot2.png)

![Appwrite 專案 About 側欄統計（Star 57.3k、Fork 5.7k 與專案描述）](assets/images/posts/github-appwrite-news-shot3.png)

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 58 字 -->
本文資訊來源為 Appwrite 的 GitHub 儲存庫與官方網站，內容涵蓋星標、授權、2.0 版本說明、產品架構與自架部署需求等公開資料。
<!-- End AEO Capsule -->

出處連結：[Appwrite GitHub 儲存庫](https://github.com/appwrite/appwrite)。官方網站另提供雲端版本註冊、完整文件、環境變數說明與 docker-compose 設定；2.0 的完整功能說明可見於官方公告文章。專案同時維護 Discord 社群與多語 README，並在 DigitalOcean、Akamai 與 AWS Marketplace 上架一鍵部署方案。

## 總結：Appwrite 適合什麼團隊？

<!-- AEO Answer Capsule — 約 64 字 -->
Appwrite 適合希望以單一開源平台取代多個後端服務的團隊，特別是重視自架與資料合規、且需要同時處理傳統資料與向量檢索的開發組織。
<!-- End AEO Capsule -->

Appwrite 的價值在於把後端開發中最重複的環節收斂成一套一致的介面，並以開源與自架保住資料主導權。2.0 的意義不只是一次版本號跳躍，而是把資料層從單純的關聯式儲存，擴展到無綱要文件與向量嵌入。這意味著同一套權限、查詢與即時機制，能同時服務傳統業務資料與 RAG 應用的檢索需求，對正在評估 AI 功能整合的團隊而言，減少了架構分裂的成本。BSD-3-Clause 授權、單命令 Docker 部署與六年累積的社群規模，構成相對穩健的採用基礎；不過 VectorsDB、DocumentsDB 與嵌入服務皆預設關閉且資源佔用較高，實際落地仍需要一定的基礎設施規劃。以 57,338 星標與 5,708 次複製的社群規模觀察，該專案已在開源後端生態佔據穩定位置，後續值得關注的是向量能力能否在真實生產環境中站穩腳步。
