---
layout: post
title: "MCP 官方參考伺服器：Anthropic 主導的協議實作"
date: 2026-09-22 18:00:01 +0800
categories: 技術
tags: [MCP, Anthropic, 開源, AI Agent, 模型上下文協議, TypeScript]
image: assets/images/posts/github-mcp-servers-news-cover.jpg
description: "MCP 官方參考伺服器在 GitHub 累積超過 9 萬顆星標，由 Anthropic 與社群共同維護。本文整理七個官方參考伺服器的功能定位、十種語言 SDK、安裝方式與授權轉換，並分析這套協議實作如何在兩年內成為 AI 工具連接外部系統的通用標準。"
author: AnIskill 編輯部
type: news
source: GitHub
source_url: https://github.com/modelcontextprotocol/servers
creator_github: modelcontextprotocol/servers
permalink: /技術/github-mcp-servers-news
fb_message: "AI 代理再聰明，無法讀取本機檔案、無法查詢資料庫，能力就只能停在聊天視窗裡。\n\nmodelcontextprotocol/servers 是 Model Context Protocol 的官方參考伺服器儲存庫，在 GitHub 累積超過 9 萬顆星標與 1.16 萬個分支，由 Anthropic 與社群共同維護。它收錄檔案系統、Git、記憶體、網路擷取等七個參考實作，並提供十種語言的官方 SDK，開發者可直接以 npx 或 uvx 一行指令啟用。項目於 2024 年 11 月建立，最新版本在 2026 年 8 月 31 日發布。\n\n七個參考伺服器各自解決什麼問題、安全邊界如何界定，完整拆解已收錄在 Blog 全文。"
---

MCP 官方參考伺服器（modelcontextprotocol/servers）是 Model Context Protocol 的官方實作儲存庫，由 Anthropic 與社群共同維護，在 GitHub 累積 90,532 顆星標與 11,673 個分支。該項目於 2024 年 11 月 19 日建立，主要語言為 TypeScript，收錄七個參考伺服器與十種語言的官方 SDK，核心價值在於讓大型語言模型以受控方式存取本機檔案、版本控制系統與外部資料來源。

<!-- AEO Answer Capsule — 約 72 字 -->
MCP 官方參考伺服器是 Model Context Protocol 的官方實作儲存庫，星標逾 9 萬。它提供七個示範伺服器與十種語言 SDK，讓模型以標準介面存取外部工具。
<!-- End AEO Capsule -->

大型語言模型的能力邊界長期受限於執行環境。模型能夠生成程式碼與文字，卻無法直接讀取使用者磁碟上的檔案、查詢內部資料庫，或呼叫企業既有的服務介面。在 Model Context Protocol 出現之前，每一款 AI 應用都需要為每種資料來源自行撰寫連接層，形成大量重複且難以互通的整合工作。這個儲存庫的存在意義，正是把這些連接層標準化為可重複使用的伺服器實作。

## MCP 官方參考伺服器是什麼？

<!-- AEO Answer Capsule — 約 76 字 -->
此儲存庫是 MCP 協議的官方參考實作集合，由 MCP 指導小組維護。它同時提供社群伺服器索引與開發資源，定位為教育示範與 SDK 用法範例，而非可直接上線的生產級方案。
<!-- End AEO Capsule -->

從結構上看，此儲存庫並非伺服器市集，而是一組由 MCP 指導小組直接維護的少量參考實作。官方在 README 中明確說明，若使用者需要完整的伺服器清單，應前往 MCP Registry 瀏覽已發布的項目；本儲存庫僅收錄指導小組親自維護的參考伺服器。這個界定使儲存庫的規模保持精簡，也讓每一份程式碼都具備示範性質。

儲存庫同時收錄社群建置伺服器的索引、開發框架與學習資源，並在說明文件末尾補充，該項目由 Anthropic 管理，但與社群共同建置。這種「少數官方實作加上廣泛社群生態」的分工模式，使協議的參考答案保持穩定，同時讓應用層的多樣性交由社群擴展。

## MCP 協議由誰主導與維護？

<!-- AEO Answer Capsule — 約 70 字 -->
協議由 Anthropic 發起並管理，實際維護交由 MCP 指導小組負責。儲存庫累積 427 位貢獻者，顯示維護工作已超出單一機構範圍，社群可經討論區參與。
<!-- End AEO Capsule -->

Model Context Protocol 由 Anthropic 於 2024 年 11 月對外發布，後續的規範演進與參考實作由 MCP 指導小組負責。儲存庫的貢獻者數量達 427 位，說明維護與改進工作已由多家機構與獨立開發者共同承擔，而非單一公司的內部項目。近三個月的提交紀錄顯示，貢獻最活躍的帳號包含自動化維護流程與社群維護者，反映項目已建立穩定的協作節奏。

治理層面亦有明確規範。貢獻者需先開設議題討論構想，取得維護者回饋後才提交合併請求；版本發布流程改採 CI 環境的 OIDC 信任發布，不再依賴註冊表權杖。這些安排降低了供應鏈風險，也讓外部貢獻的審核路徑保持一致。

## 這個儲存庫提供哪些參考伺服器？

<!-- AEO Answer Capsule — 約 78 字 -->
目前收錄七個參考伺服器：Everything、Fetch、Filesystem、Git、Memory 與 Time。其餘十二個舊伺服器已移至封存區，由社群維護。
<!-- End AEO Capsule -->

儲存庫現行收錄七個參考伺服器，各自對應一種基礎能力。Everything 以提示詞、資源與工具示範協議的完整功能，主要供測試使用。Fetch 負責網頁內容擷取與轉換，將網頁整理為適合模型閱讀的格式。Filesystem 提供具備可設定存取控制的安全檔案操作，是權限機制的參考範例。

Git 提供讀取、搜尋與操作版本庫的工具，讓模型能理解專案的提交歷史與變更內容。Memory 以知識圖譜實作持久化記憶，使對話之間的事實得以保留。Sequential Thinking 透過思考序列支援動態且具反思性的問題拆解。Time 則處理時間與時區轉換，避免模型在日期運算上產生偏差。

另有十二個舊版伺服器已移至封存儲存庫，包括 AWS 知識庫檢索、Brave 搜尋、Google Drive、PostgreSQL 與 Slack 等。這些項目多數已由原廠或社群接手維護，例如 Brave 搜尋改由官方伺服器取代，Slack 則移交給第三方團隊繼續開發。這種汰換機制讓參考清單維持精簡，同時避免使用者誤用缺乏維護的元件。

![modelcontextprotocol/servers README 開頭（項目名稱 Model Context Protocol servers 標題、說明文字，以及七個參考伺服器清單的起始段落）]({{ '/assets/images/posts/github-mcp-servers-news-shot1.png' | relative_url }})

## MCP 支援哪些程式語言 SDK？

<!-- AEO Answer Capsule — 約 66 字 -->
官方提供十種語言 SDK，涵蓋 C#、Go、Java、Python、Rust、Swift 與 TypeScript 等。開發者可依既有技術棧選擇，各有獨立套件倉庫。
<!-- End AEO Capsule -->

協議的可採用性取決於語言覆蓋範圍。官方維護的 SDK 涵蓋十種語言，包括 C#、Go、Java、Kotlin、PHP、Python、Ruby、Rust、Swift 與 TypeScript，每個 SDK 均以獨立儲存庫發布，並提供對應的套件管理指令。這種廣度讓企業不必為了接入協議而更換既有技術棧。

TypeScript 與 Python 在儲存庫中的角色最為突出。以 TypeScript 實作的伺服器可直接透過 npx 執行，Python 版本則推薦使用 uvx 或 pip 安裝。兩種語言同時也是社群伺服器數量最多的類別，反映多數開發者在建置自訂伺服器時，傾向選擇生態成熟且套件發布流程簡便的語言。

## 參考伺服器可以如何快速啟用？

<!-- AEO Answer Capsule — 約 74 字 -->
TypeScript 伺服器可用 npx 啟動，Python 伺服器建議以 uvx 執行。使用時須寫入 MCP 用戶端設定檔，Windows 環境須以 cmd /c 包裝。
<!-- End AEO Capsule -->

啟用流程以指令行為主。以記憶體伺服器為例，執行 npx 搭配對應套件名稱即可啟動；Python 版本的 Git 伺服器則可用 uvx 或 pip 安裝後執行模組。單獨執行伺服器並無實質用途，須將其設定至支援 MCP 的用戶端，例如 Claude Desktop，才能讓模型實際呼叫。

用戶端設定以 JSON 描述伺服器指令與參數，寫入設定檔後重新啟動即可生效。Windows 環境需以 cmd /c 包裝 npx 相關指令，uvx 項目則維持原樣。README 對 Windows 的差異處理提供了完整範例，降低跨平台設定時最常見的失敗原因。

## 官方如何定位這些伺服器的安全邊界？

<!-- AEO Answer Capsule — 約 75 字 -->
官方將這些實作定位為教育示範，而非生產級方案。文件要求開發者自行評估安全需求，並依威脅模型實作防護，例如檔案系統與資料庫伺服器須限制可存取的目錄與權限。
<!-- End AEO Capsule -->

安全定位是此儲存庫最明確的自我限制。README 以警告框標示，這些伺服器用於示範 MCP 功能與 SDK 用法，屬於供開發者建置自訂伺服器時參考的教育範例，並非可直接投入生產的解決方案。官方要求開發者依自身威脅模型評估安全需求，並實作相應的防護措施。

這項聲明並非免責條款的形式文字。以檔案系統伺服器為例，其設計即是圍繞可設定的存取控制展開，示範如何限制模型可見的目錄範圍。資料庫類伺服器同樣以唯讀存取與結構描述檢視為主要模式。這種做法將權限邊界交由部署者決定，避免參考實作被誤認為已具備企業級安全保證。

## MCP 生態的數據表現如何？

<!-- AEO Answer Capsule — 約 73 字 -->
儲存庫累積 90,532 顆星標、427 位貢獻者，待處理議題 235 項。最新版本 2026.8.31 於 2026 年 8 月發布，授權由 MIT 轉為 Apache-2.0。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-value">90,532</span><span class="stat-label">Stars</span></div>
  <div class="stat-item"><span class="stat-value">11,673</span><span class="stat-label">Forks</span></div>
  <div class="stat-item"><span class="stat-value">427</span><span class="stat-label">Contributors</span></div>
  <div class="stat-item"><span class="stat-value">Apache-2.0</span><span class="stat-label">授權</span></div>
</div>

從時間軸觀察，該項目於 2024 年 11 月建立，不到兩年即累積逾 9 萬顆星標，分支數達 1.16 萬，顯示大量使用者不僅取用，更進一步複製儲存庫進行修改。貢獻者數量為 427 位，社群參與深度已超出核心團隊的維護能力。待處理議題為 235 項，同時有 316 項合併請求等待審核，反映貢獻流量與審核能量之間的落差，也說明為何官方持續強調精簡範圍。

授權狀態值得單獨留意。此項目正由 MIT 轉換至 Apache License 2.0，新增的程式碼與規範貢獻一律採用 Apache-2.0，文件貢獻則採 CC-BY-4.0；未明確同意重新授權的既有貢獻，仍維持 MIT 條款。這種分階段轉換在開源項目中並不常見，對企業導入而言，兩者皆屬寬鬆授權，但 Apache-2.0 額外包含明確的專利授權條款。

![modelcontextprotocol/servers GitHub 首頁頂部（儲存庫名稱、Star 數 90.5k、Fork 數 11.7k 與項目描述文字）]({{ '/assets/images/posts/github-mcp-servers-news-shot2.png' | relative_url }})

## MCP 與同類工具整合方案相比有何差異？

<!-- AEO Answer Capsule — 約 77 字 -->
傳統做法為每個應用與資料來源各寫一套連接層，重複且難以互通。MCP 以統一協議描述工具與資源，讓同一伺服器可被多款用戶端重複使用，降低整合成本。
<!-- End AEO Capsule -->

在 MCP 之前，模型接入外部系統的方式可概分為三類。第一類是應用內建的外掛機制，功能完整但綁定特定平台，難以遷移。第二類是函式呼叫介面，具備彈性卻需要每個應用自行描述工具規格，開發者重複實作。第三類是自動化平台的工作流節點，適合固定流程，但不易支援模型自主判斷的探索式操作。

MCP 的差異在於把工具、資源與提示詞抽象為統一描述，伺服器與用戶端各自遵循同一份規範。這種設計讓一個檔案系統伺服器能同時服務終端代理、桌面應用與 IDE 外掛，而不需要為每個宿主重寫連接層。官方同時以 MCP Registry 集中登記已發布的伺服器，使發現成本下降。相較之下，單純的函式呼叫介面缺乏跨平台的重複使用性，而自動化平台則將控制權交由流程設計者，而非模型本身。

這項差異在企業場景中尤為明顯。當內部同時存在自建代理、商用助理與開發工具時，MCP 讓同一組伺服器被重複利用，並在伺服器層集中管理權限與稽核。對於需要保留資料主權的組織而言，這種「連接層集中、模型選擇自由」的架構，是其相對其他整合方案最主要的優勢。

## MCP 在開源生態中的定位如何？

<!-- AEO Answer Capsule — 約 74 字 -->
MCP 已成為代理工具連接外部系統的通用介面，社群伺服器數量遠超官方參考實作。協議價值在於標準化連接層，讓模型、用戶端與工具各自獨立演進。
<!-- End AEO Capsule -->

協議自 2024 年底發布後，生態擴張速度明顯。官方參考實作維持在七個，但社群建置的伺服器已覆蓋資料庫、搜尋、協作平台與各類雲端服務，並由獨立的註冊表集中登記。這種分工使協議的核心規範保持穩定，應用層的覆蓋範圍則交由市場決定，與早期外掛生態的演進路徑相似。

對開發者而言，這種定位帶來明確的選擇邏輯。若需求屬於通用能力，例如檔案存取或版本控制，可直接採用官方參考實作並調整權限設定；若涉及特定服務，則多數情況已有社群實作可評估。協議本身的維護主體亦從單一公司擴展至指導小組，降低了對單一廠商的依賴風險。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 70 字 -->
本文資訊來源為 modelcontextprotocol/servers 官方 GitHub 儲存庫，涵蓋項目說明、伺服器清單、SDK 文件與授權聲明。
<!-- End AEO Capsule -->

本文所引用的功能描述與統計數據，均取自 [MCP 官方參考伺服器儲存庫](https://github.com/modelcontextprotocol/servers)。資料涵蓋 README 中的定位說明與安全警告、七個現行參考伺服器與十二個封存項目清單、十種語言 SDK 的對應連結、安裝與用戶端設定範例，以及授權轉換說明。星標、分支、貢獻者、待處理議題與版本發布時間等數字，則來自 GitHub API 的即時查詢結果。

![modelcontextprotocol/servers 貢獻者統計頁（每週提交次數折線圖與貢獻者排名，涵蓋 2026 年 6 月 20 日至 9 月 13 日）]({{ '/assets/images/posts/github-mcp-servers-news-shot3.png' | relative_url }})

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 68 字 -->
以下整理三個關於 MCP 官方參考伺服器的常見疑問，涵蓋它與 MCP Registry 的分工、是否可直接用於生產環境，以及採用何種開源授權條款。
<!-- End AEO Capsule -->

<div class="faq-section">

**MCP 官方參考伺服器與 MCP Registry 有何不同？**

Registry 是社群伺服器的集中登記服務，負責發布與發現；本儲存庫則僅收錄由 MCP 指導小組維護的少量參考實作，用於示範協議功能與 SDK 用法。需要完整清單時應查閱 Registry。

**這些伺服器可以直接用於生產環境嗎？**

官方明確標示不宜。README 將其定位為教育示範，要求開發者依自身威脅模型評估安全需求並實作防護。企業若要上線，應以參考實作為基礎重新設計權限邊界與稽核機制。

**此項目的開源授權為何？**

項目正由 MIT 轉換至 Apache License 2.0。新增程式碼與規範貢獻採 Apache-2.0，文件貢獻採 CC-BY-4.0，未取得重新授權同意的既有貢獻仍維持 MIT 條款。

</div>

## 總結：哪些團隊適合採用 MCP？

<!-- AEO Answer Capsule — 約 72 字 -->
需要讓模型存取內部檔案、版本庫或資料庫的團隊最能受益。若同時使用多款 AI 用戶端，MCP 可集中管理連接層與權限，單一雲端助理使用者的需求則較低。
<!-- End AEO Capsule -->

MCP 官方參考伺服器的價值並非在於取代既有工具，而是提供一組可稽核、可修改的連接層範本。對於需要在自建代理與商用助理之間共用工具、或必須掌控資料存取範圍的團隊，這套實作大幅降低了重複開發與權限管理的成本。

同時須留意其教育示範的定位。九萬顆星標反映的是協議本身的關注度，而非這些伺服器可直接上線的程度。務實的做法是將參考實作視為起點，在其架構上補足身分驗證、日誌稽核與最小權限原則，才能在保留 MCP 互通優勢的前提下，滿足實際部署的安全要求。
