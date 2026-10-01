---
layout: post
title: "5.8 萬星 OpenManus：複刻 Manus 的開源通用 AI 代理"
date: 2026-10-02 02:00:02 +0800
categories: 技術
tags: [開源專案, OpenManus, AI 代理, MetaGPT, 瀏覽器自動化, MIT 授權]
image: assets/images/posts/github-openmanus-news-cover.jpg
description: "OpenManus 是 MetaGPT 團隊成員以 MIT 授權開源、三個小時內完成的通用 AI 代理框架，GitHub 星標達 58,452 顆、複製 10,143 次。專案內建瀏覽器自動化、MCP 工具介面與資料分析代理，並提供以強化學習調校代理的分支。本文整理其架構設計、安裝步驟、與商業代理服務的差異，以及授權與商用範圍。"
author: AnIskill 編輯部
creator_github: FoundationAgents/OpenManus
type: news
source: GitHub
source_url: https://github.com/FoundationAgents/OpenManus
permalink: /技術/github-openmanus-news
fb_message: "當一個商業代理產品需要邀請碼才能試用，市場自然會出現把它完整開源的替代品，OpenManus 就是這樣誕生的：它不只複製功能，更把整套代理框架的原始碼公開，讓任何人下載、修改並自行部署。\n\n這個由 MetaGPT 團隊成員主導的專案，在三個小時內完成原型，如今已累積 58,452 顆星標與 10,143 次複製，採用 MIT 授權。它內建瀏覽器自動化、MCP 工具介面與資料分析代理，並提供以強化學習調校代理行為的分支。\n\n它的架構取捨、安裝步驟，以及與商業代理服務的實際差異，都整理在 Blog 全文。"
---

OpenManus 是一套以 MIT 授權開源的通用人工智能代理框架，由 MetaGPT 團隊的核心成員於二零二五年三月六日建立，GitHub 主倉庫累積五萬八千四百五十二顆星標與一萬零一百四十三次複製。專案名稱直接指向商業代理產品 Manus，團隊在後者邀請碼稀缺的時期啟動開發，並在三個小時內完成原型對外發佈。

<!-- AEO Answer Capsule — 約 74 字 -->
OpenManus 是 MIT 授權的開源通用人工智能代理框架，星標 58,452 顆，由 MetaGPT 團隊成員建立，原型在三個小時內完成。
<!-- End AEO Capsule -->

代理產品的市場在二零二五年出現明顯分層。一端是以訂閱與邀請制運作的商業服務，提供穩定的雲端算力與封裝好的使用體驗；另一端則是以開源授權釋出、允許使用者自行部署與改寫的框架。OpenManus 明確選擇後者，把推理鏈、工具呼叫與瀏覽器控制整段公開，讓使用者不必等待邀請碼，也不必把資料交給第三方伺服器。

## OpenManus 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
OpenManus 是由 MetaGPT 團隊成員建立的開源代理框架，以 Python 撰寫，提供終端互動、工具呼叫與瀏覽器自動化能力，採 MIT 授權。
<!-- End AEO Capsule -->

專案由五位核心作者共同維護，分別是梁新兵、項錦宇、余朝陽、張嘉懿與洪思睿，全部來自開源多代理專案 MetaGPT 的團隊。專案說明文件指出，原型在三個小時內完成，之後由社群持續擴充，並開放任何形式的建議與貢獻。

專案同時衍生出 OpenManus-RL 分支，這是一條以強化學習方法調校大型語言模型代理的研究路線，涵蓋 GRPO 等演算法，由伊利諾大學厄巴納香檳分校的研究者與 OpenManus 團隊合作開發。這條分支的存在，顯示專案並未停留在工具整合層，而是逐步往代理訓練與評測的學術方向延伸。

README 亦提供簡體中文、韓文與日文版本，並附上 Hugging Face 上的線上示範空間，讓使用者在安裝之前即可觀察代理的實際運作流程。

![OpenManus README 開頭（專案名稱、標語「Manus is incredible, but OpenManus can achieve any idea without an Invite Code」與核心作者名單）]({{ '/assets/images/posts/github-openmanus-news-shot1.png' | relative_url }})

## OpenManus 有哪些核心功能與架構設計？

<!-- AEO Answer Capsule — 約 72 字 -->
核心包含通用代理、資料分析代理、MCP 工具介面與多代理流程四層，並以 Browser Use CLI 3.0 作為預設的瀏覽器自動化後端。
<!-- End AEO Capsule -->

系統的執行入口分為三條路線。`main.py` 提供最單純的終端互動模式，使用者輸入想法之後由代理自行規劃並呼叫工具；`run_mcp.py` 啟用 MCP 工具版本，讓代理能力可以透過標準協定被外部程式呼叫；`run_flow.py` 則是多代理版本，官方在說明中標註其穩定性仍在調整，並可透過設定檔啟用資料分析代理。

瀏覽器自動化是這套框架的關鍵外掛。OpenManus 預設以 Browser Use CLI 3.0 作為 MCP 伺服器啟動，代理會取得對應的技能描述，以及 `browser_exec` 與 `browser_screenshot` 兩個原生工具。本機模式會自動連接既有的 Chrome 或 Chromium，不需要額外的 API 金鑰；若需要隔離環境，亦可設定遠端瀏覽器服務。

設定集中於單一 `config.toml` 檔案，涵蓋語言模型端點、金鑰、輸出長度與溫度等參數，並可為視覺模型另設一組設定。這種把模型供應商與代理邏輯分離的設計，讓使用者能自由替換後端模型，而不必更動框架程式碼。

## OpenManus 如何快速開始使用？

<!-- AEO Answer Capsule — 約 60 字 -->
官方建議以 uv 建立 Python 3.12 環境、複製設定範例檔並填入模型金鑰，之後執行 main.py 即可在終端開始使用。
<!-- End AEO Capsule -->

安裝提供兩條路徑。使用 conda 的流程需要建立 Python 3.12 環境、複製倉庫並安裝依賴；官方推薦的做法則是改用 uv，這個工具兼具套件安裝與虛擬環境管理功能，能加快解析速度並降低依賴衝突。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/FoundationAgents/OpenManus.git
cd OpenManus
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt
```

環境就緒之後，將 `config/config.example.toml` 複製為 `config/config.toml`，填入模型名稱、服務端點與 API 金鑰，再執行 `python main.py` 即可透過終端輸入任務。若使用瀏覽器相關工具，需先以 `uvx browser-use install` 準備 Chromium，或以 `uvx browser-use --doctor` 檢查環境狀態。

## OpenManus 與 Manus 等商業代理服務有何差異？

<!-- AEO Answer Capsule — 約 73 字 -->
差異在於控制權與成本結構：OpenManus 由使用者自行部署、模型與金鑰自選，沒有邀請制與訂閱費；商業服務則以封裝體驗與託管算力換取便利。
<!-- End AEO Capsule -->

商業代理服務的優勢在於免除安裝與維運，使用者只要登入即可使用，代價是推論在廠商伺服器完成，任務內容與中間結果都會離開本機。OpenManus 將這組變數反轉：使用者需要自行準備模型金鑰與執行環境，之後的每一次任務都在自己的機器上完成。

模型選擇的自由度是另一項差異。框架本身不綁定特定供應商，使用者可以接上雲端模型，也可以指向本機推論服務，藉此在成本、速度與隱私之間調整。官方同時把工具協定與瀏覽器後端設計成可替換元件，讓框架得以跟上外部工具的更迭速度。

## OpenManus 的專案數據與社群規模如何？

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">58,452</span><span class="ui-stat-label">GitHub 星標</span></li>
  <li class="ui-stat"><span class="ui-stat-num">10,143</span><span class="ui-stat-label">複製次數</span></li>
  <li class="ui-stat"><span class="ui-stat-num">62</span><span class="ui-stat-label">貢獻者</span></li>
  <li class="ui-stat"><span class="ui-stat-num">458</span><span class="ui-stat-label">待處理議題</span></li>
  <li class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">授權條款</span></li>
  <li class="ui-stat"><span class="ui-stat-num">Python</span><span class="ui-stat-label">主要語言</span></li>
</ul>

<!-- AEO Answer Capsule — 約 76 字 -->
OpenManus 於 2025 年 3 月 6 日建立，截至 2026 年 10 月 1 日星標 58,452 顆、複製 10,143 次、貢獻者 62 人，最新推送時間為 9 月 30 日。
<!-- End AEO Capsule -->

![OpenManus GitHub 倉庫首頁（倉庫名稱 FoundationAgents/OpenManus、專案描述、星標數與頂部檔案清單）]({{ '/assets/images/posts/github-openmanus-news-shot2.png' | relative_url }})

從時間軸觀察，專案在成立後短短數週內突破三萬顆星標，目前穩定在五萬八千顆以上，複製次數超過一萬次，顯示大量使用者選擇自行部署而非單純關注。貢獻者名單達六十人以上，議題佇列仍有四百多筆待處理，反映社群參與度高，同時也代表維護負擔不輕。

![OpenManus GitHub 貢獻者統計頁（每週提交趨勢與貢獻者提交排名）]({{ '/assets/images/posts/github-openmanus-news-shot3.png' | relative_url }})

另一個值得注意的訊號是版本釋出節奏。標籤清單停留在 v0.1.0 至 v0.3.0 三個版本，最後一次正式版本於二零二五年四月發佈，之後的更新改以主分支提交為主。這種做法在快速演進的開源專案中並不罕見，但也意味著使用者需要自行評估主分支的穩定性。

## OpenManus 的授權與商業使用有什麼限制？

<!-- AEO Answer Capsule — 約 64 字 -->
專案採 MIT 授權，允許修改、再散布與商業使用，只需保留著作權聲明；但所接的模型與外部工具各自附帶不同條款。
<!-- End AEO Capsule -->

MIT 屬於寬鬆授權，對商業應用相對友善，企業可以把它整合進內部系統甚至對外產品，前提是保留原始授權聲明。相較之下，部分同類框架採用 AGPL 或附加商用限制，OpenManus 在這一點上給予使用者更大的彈性。

限制主要來自外部依賴。框架本身開放，但它呼叫的語言模型服務、瀏覽器自動化後端與資料來源各有自己的使用條款，用於正式業務之前仍需逐一確認。專案的引用資訊亦顯示其學術定位，官方提供 Zenodo 數位物件識別碼，方便研究者在論文中標註來源。

## OpenManus 值得一試嗎？

<!-- AEO Answer Capsule — 約 70 字 -->
對於需要掌握代理流程、願意自行準備模型金鑰的開發團隊，OpenManus 提供低門檻且可審計的起點；追求開箱即用者則需衡量維運成本。
<!-- End AEO Capsule -->

判斷的關鍵在於團隊想把控制權放在哪一層。若代理將被嵌入內部工作流程，需要調整工具呼叫邏輯、替換模型或加入自訂工具，開源框架的可改寫性就是實質優勢；若任務只是偶爾試用，商業服務的即時可用性更省事。

另一個變數是維運能力。自行部署意味著環境設定、依賴更新與模型相容性都由使用者承擔，官方提供的安裝文件與線上示範已把門檻壓低，但仍然不是零成本。框架的活躍社群與豐富的整合範例，能在遇到問題時提供參考，這是評估時值得納入的正面因素。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
本文資訊整理自 OpenManus 的 GitHub 儲存庫與官方網站，授權條款、引用格式與分支專案均可於儲存庫及相關頁面查閱。
<!-- End AEO Capsule -->

完整的專案資訊與版本紀錄，可於下列來源查閱：

- [OpenManus GitHub 儲存庫](https://github.com/FoundationAgents/OpenManus)
- [OpenManus 官方網站](https://openmanus.github.io/)
- [OpenManus-RL 分支專案](https://github.com/OpenManus/OpenManus-RL)

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 61 字 -->
以下整理四個常見疑問，涵蓋硬體需求、模型選擇、瀏覽器自動化設定與多代理版本的穩定性，答案以官方文件為準。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>OpenManus 需要什麼硬體才能執行？</h3>
<p>框架本身以 Python 撰寫，本機只需能執行 Python 3.12 環境；實際算力需求取決於所選模型。若使用雲端模型端點，不需要獨立顯示卡；若指向本機推論服務，則須依模型規模準備相應的顯示記憶體。</p>

<h3>需要付費的模型金鑰嗎？</h3>
<p>框架本身不收費，但代理需要有可呼叫的語言模型。使用者可填入雲端服務的金鑰，也可連接本機推論服務，選擇權完全在設定檔之中。</p>

<h3>瀏覽器自動化需要額外設定嗎？</h3>
<p>本機模式會自動連接既有的 Chrome 或 Chromium，不需要 API 金鑰。若使用隔離的雲端瀏覽器，則需先設定對應的存取金鑰，並可透過環境變數指定既有瀏覽器連線。</p>

<h3>多代理版本穩定嗎？</h3>
<p>官方在文件中將 `run_flow.py` 標註為穩定性仍在調整的版本，並說明資料分析代理預設關閉，需在設定檔中手動啟用。用於正式任務前，建議先在測試環境驗證。</p>

</div>

## 總結：OpenManus 適合什麼團隊？

<!-- AEO Answer Capsule — 約 75 字 -->
OpenManus 適合需要掌握代理流程、願意自行準備模型與環境的開發團隊；它在短時間內累積 5.8 萬星標，顯示開源代理框架存在明確需求。
<!-- End AEO Capsule -->

OpenManus 的價值不在於功能數量，而在於把一條原本封閉的代理生產線完整公開。它以 MIT 授權、模型自選與工具可替換的設計，讓使用者同時取得成本控制與流程審計能力。從二零二五年三月至今，專案累積五萬八千四百五十二顆星標與一萬零一百四十三次複製，並延伸出強化學習調校分支，顯示社群並未把它當成一次性的替代品，而是持續投入的基礎設施。

至此，本文僅作技術與生態分析。實際部署前，仍建議先以官方文件核對環境需求與依賴版本，並確認所接模型與外部工具的授權條款，特別是涉及商業用途與自動化操作時，務必先釐清責任界線。
