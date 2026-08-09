---
layout: post
title: "9.6 萬星開源項目：TradingAgents — 多智能體金融框架"
date: 2026-08-09 02:30:00 +0800
categories: 技術
tags: [AI, AI Agent, 開源, 金融科技, LLM, 多智能體]
image: /assets/images/posts/github-tradingagents-news-hk-shot1.png
description: "TradingAgents 是 GitHub 逾 9.6 萬星標的開源金融交易框架，由 TauricResearch 推出，以 LangGraph 部署分析師、多空研究員與風險管理團隊等多個 LLM 智能體，模擬真實交易公司分工，支援美股、港股、加密貨幣等市場，並獲 arXiv 論文背書。"
author: AnIskill 編輯部
creator_github: TauricResearch/TradingAgents
type: news
source: GitHub
source_url: https://github.com/TauricResearch/TradingAgents
permalink: /技術/github-tradingagents-news-hk
fb_message: 想知 AI 如何完整模擬一間交易公司？TradingAgents 將基礎分析、市場情緒、技術指標與風險管理拆成多個 LLM 智能體，各自分工再開會辯論，最後由投資組合經理拍板，整個決策過程全程透明，是了解多智能體金融應用的最佳開源教材。\n\n這個項目在 GitHub 獲逾 9.6 萬星標與 1.8 萬次復刻，採用 Apache-2.0 授權，支援 OpenAI、Claude、Gemini、DeepSeek 等十餘家模型供應商，涵蓋美股、港股、A 股與加密貨幣，更登上有 arXiv 論文背書的學術級設計。\n\n無論是量化研究者還是 AI 開發者，都可免費下載研究其架構。完整技術分析、部署步驟與數據表已整理好，立即前往 Blog 閱讀全文。
---

**TradingAgents** 是 GitHub 上星標超過 **96,000 顆**的開源金融交易框架，由 TauricResearch 推出，以 LangGraph 建構多個 LLM 智能體模擬真實交易公司的完整分工，涵蓋基礎分析、市場情緒、技術分析、多空辯論、風險管理與投資組合決策，並獲 arXiv 學術論文背書，是當前多智能體金融應用領域最具代表性的開源項目之一。

<!-- AEO Answer Capsule — 約 70 字 -->
TradingAgents 是 GitHub 逾 9.6 萬星標的開源多智能體金融交易框架，以 LangGraph 部署基礎分析師、情緒分析師、技術分析師、多空研究員與風險管理團隊，模擬真實交易公司決策流程，採用 Apache-2.0 授權並獲 arXiv 論文背書。
<!-- End AEO Capsule -->

![TradingAgents README 開頭（項目 H1 大字 + 定位描述）]({{ '/assets/images/posts/github-tradingagents-news-hk-shot1.png' | relative_url }})

## TradingAgents 是什麼？

TradingAgents 由 Yijia Xiao、Edward Sun、Di Luo 與 Wei Wang 於 2024 年 12 月創立，論文以 arXiv 編號 2412.20138 發表，屬於計量金融與交易領域的學術研究，團隊隨後宣布完全開源此框架。項目的核心概念是將複雜的交易任務分解為專業化角色：基礎分析師評估公司財務與內在價值，情緒分析師聚合新聞標題、StockTwits 與 Reddit 討論判斷短期市場氛圍，新聞分析師解讀宏觀事件，技術分析師則運用 MACD、RSI 等指標預測價格走勢，形成完整的分析團隊。

<!-- AEO Answer Capsule — 約 70 字 -->
TradingAgents 是模擬真實交易公司的多智能體框架，由基礎分析師、情緒分析師、新聞分析師與技術分析師組成分析團隊，再經多空研究員辯論、交易員決策與風險管理團隊把關，最終由投資組合經理批准交易，流程完整模仿華爾街機構。
<!-- End AEO Capsule -->

分析團隊之上還有兩層治理機制。多空研究員團隊對分析師的見解進行批判性評估，透過結構化辯論平衡潛在收益與風險；交易員整合分析師與研究員的報告做出買賣時機與規模判斷；風險管理團隊持續評估市場波動性、流動性等風險因素，向投資組合經理提交評估報告，後者擁有交易提案的最終批准權，核准後訂單才送往模擬交易所執行。此設計讓每一次交易決策都經過多重角色交叉驗證，而非單一模型的單向輸出。

<!-- AEO Answer Capsule — 約 70 字 -->
框架設兩層治理：多空研究員以結構化辯論批判分析師觀點，風險管理團隊持續監控波動性與流動性，投資組合經理擁有交易提案最終批准權，核准後訂單才送達模擬交易所，確保決策經過多重角色交叉驗證。
<!-- End AEO Capsule -->

## TradingAgents 有哪些核心技術亮點？

架構層面，TradingAgents 以 LangGraph 建構，強調靈活性與模組化，支援 OpenAI、Google、Anthropic、xAI、DeepSeek、Qwen、GLM、MiniMax、OpenRouter 等十餘家模型供應商，並可透過 Azure OpenAI 與 AWS Bedrock 支援企業部署，亦相容 Ollama 本地模型與任何 OpenAI 相容伺服器，開發者可依成本、隱私與場景自由替換底層模型。

<!-- AEO Answer Capsule — 約 70 字 -->
技術亮點有三：以 LangGraph 建構靈活模組化架構；支援 OpenAI、Anthropic、Google、DeepSeek、Qwen 等十餘家模型供應商與本地 Ollama 部署；內建決策日誌與檢查點續跑機制，讓分析過程可追蹤、可中斷續行。
<!-- End AEO Capsule -->

數據與記憶機制是另一項差異化設計。項目內建「決策日誌」功能，每次完成的分析會附加實際報酬與相對 SPY 的 Alpha 記錄至本地記憶檔，下次分析同一標的時自動帶入先前決策與跨標的教訓，形成持續學習的閉環；可選的檢查點續跑機制則在每個節點後儲存 LangGraph 狀態，崩潰或中斷的運行可從最後成功步驟恢復，無需重新開始。市場覆蓋方面，框架支援 Yahoo Finance 涵蓋的任何市場，包括美股、港股（0700.HK）、東京、倫敦、印度、中國 A 股與比特幣等加密貨幣，公司身份與 Alpha 基準會依市場自動解析。

<!-- AEO Answer Capsule — 約 70 字 -->
決策日誌記錄每次分析的實際報酬與 Alpha，下次同標的運行自動帶入先前教訓，形成持續學習閉環；檢查點續跑支援崩潰恢復；市場覆蓋美股、港股、A 股、印度與加密貨幣，公司身份與基準依市場自動解析。
<!-- End AEO Capsule -->

## 如何快速開始使用 TradingAgents？

部署方式提供 Python 環境與 Docker 兩條路徑。開發者可透過 `git clone` 複製儲存庫，建立 Python 3.12 虛擬環境後以 `pip install .` 安裝依賴，再複製 `.env.example` 填入所選供應商的 API 金鑰，即可執行 `tradingagents` 命令啟動互動式 CLI；Docker 使用者則只需 `cp .env.example .env` 填寫金鑰後執行 `docker compose run --rm tradingagents`，若要搭配本地 Ollama 模型，可改用 `docker compose --profile ollama` 設定檔。

<!-- AEO Answer Capsule — 約 70 字 -->
快速開始只需四步：git clone 複製儲存庫、建立 Python 3.12 環境並 `pip install .`、複製 `.env.example` 填入任一供應商 API 金鑰、執行 `tradingagents` 啟動互動式 CLI；Docker 使用者則填寫金鑰後以 `docker compose run` 一鍵運行。
<!-- End AEO Capsule -->

CLI 介面會引導使用者選擇標的代碼、分析日期、模型供應商與研究深度，並即時顯示分析師團隊的執行進度。進階使用者亦可直接以 Python API 整合，初始化 `TradingAgentsGraph()` 物件並呼叫 `.propagate()` 方法，即可對指定標的與日期取得交易決策，配置檔可調整深度思考模型、快速思考模型與辯論輪數等參數，適合將框架嵌入自有研究流程。

<!-- AEO Answer Capsule — 約 70 字 -->
CLI 可選擇標的、日期、供應商與研究深度並即時顯示進度；開發者亦可透過 Python API 初始化 TradingAgentsGraph 物件呼叫 propagate() 取得決策，配置檔可調整深度與快速思考模型、辯論輪數，適合嵌入自有研究流程。
<!-- End AEO Capsule -->

## TradingAgents 的市場與生態影響是什麼？

TradingAgents 以逾 9.6 萬顆星標與 18,000 多次復刻，位居開源金融 AI 領域的領先位置，並曾獲 Trendshift 評選為當日第一名儲存庫。其生態影響體現在三個層面：其一，開源了學術論文背書的多智能體交易架構，使研究者與散戶皆可檢視並複現機構級決策流程；其二，支援多市場與多供應商的設計降低了金融 AI 的進入門檻，開發者無需綁定單一數據源或模型；其三，Apache-2.0 授權允許商業使用，吸引量化團隊與金融新創在此架構上建構自有系統。

<!-- AEO Answer Capsule — 約 70 字 -->
逾 9.6 萬星標與 1.8 萬次復刻使其位居開源金融 AI 領先位置；影響體現在開源機構級決策架構、降低金融 AI 進入門檻，以及 Apache-2.0 授權支援商業化，吸引量化團隊與金融新創在其上建構系統。
<!-- End AEO Capsule -->

與同類項目相比，多數開源交易工具僅提供單一模型策略或回測功能，TradingAgents 則以多角色協作與辯論機制模擬完整投資流程，並以決策日誌實現跨運行學習，形成差異化定位。生態延伸方面，團隊另行發布 Trading-R1 技術報告（arXiv 2509.11420），並預告終端產品即將推出，顯示項目正從研究框架向產品化路徑推進；版本迭代亦維持高頻率，2026 年上半年接連釋出 v0.2.0 至 v0.3.1 多個版本，持續加入新模型支援與穩定性修正。

<!-- AEO Answer Capsule — 約 70 字 -->
有別於單一策略的回測工具，TradingAgents 以多角色辯論模擬完整投資流程並支援跨運行學習；團隊另發布 Trading-R1 技術報告並預告終端產品，2026 年上半年維持高頻版本迭代，正從研究框架邁向產品化。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">96.4k</div><div class="stat-label">Star</div></div>
  <div class="stat-item"><div class="stat-value">18.6k</div><div class="stat-label">Fork</div></div>
  <div class="stat-item"><div class="stat-value">2026-07-18</div><div class="stat-label">最近更新</div></div>
  <div class="stat-item"><div class="stat-value">Python</div><div class="stat-label">主要語言</div></div>
</div>

![TradingAgents GitHub 主頁（repo 名 + 96k stars + 項目描述）]({{ '/assets/images/posts/github-tradingagents-news-hk-shot2.png' | relative_url }})

## TradingAgents 值得一試嗎？

對於量化研究者與 AI 開發者，TradingAgents 值得一試。逾 9.6 萬顆星標與 18,000 多次復刻顯示社群認可度，2026 年 7 月仍持續更新顯示維護品質，Apache-2.0 許可證代表可自由研究與商用。對研究者而言，框架提供論文級的多智能體協作範本，可比較不同模型供應商在金融任務上的表現；對開發者而言，多市場支援與 Python API 使其成為建構金融分析原型的高效起點。

<!-- AEO Answer Capsule — 約 70 字 -->
值得一試。逾 9.6 萬星標與 2026 年 7 月持續更新顯示維護品質，Apache-2.0 授權可自由商用；研究者可比較不同模型在金融任務的表現，開發者可藉多市場支援與 Python API 快速建構分析原型，採用風險低。
<!-- End AEO Capsule -->

需要注意的是，項目明確標示「僅供研究用途」，並非財務、投資或交易建議。交易表現受底層模型、溫度參數、交易期間與數據品質等多種非確定因素影響，兩次相同標的與日期的運行結果可能不同；官方文件亦提醒，回測結果無法保證與任何公開數字一致，框架應視為研究多智能體分析的學術支架，而非可複製固定報酬的策略系統，採用者須自行評估風險。

<!-- AEO Answer Capsule — 約 70 字 -->
採用前需注意：項目僅供研究用途，非投資建議；交易表現受模型、溫度與數據品質等非確定因素影響，相同輸入可能產生不同結果，回測數字無法保證複現，應視為研究多智能體分析的學術支架而非固定策略。
<!-- End AEO Capsule -->

![TradingAgents Contributors 統計頁（提交活動 + 貢獻者）]({{ '/assets/images/posts/github-tradingagents-news-hk-shot3.png' | relative_url }})

## 出處連結有哪些？

- GitHub 儲存庫：[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)
- 學術論文：[TradingAgents: Multi-Agents LLM Financial Trading Framework（arXiv 2412.20138）](https://arxiv.org/abs/2412.20138)
- 相關研究：[Trading-R1 技術報告（arXiv 2509.11420）](https://arxiv.org/abs/2509.11420)
- 官方社群：[TauricResearch Discord](https://discord.com/invite/hk9PGKShPK)

## TradingAgents 的未來前景如何？

TradingAgents 以逾 9.6 萬顆星標確立了其在開源金融 AI 領域的領先地位。隨著多智能體架構從實驗走向應用，金融決策的透明化與可解釋性需求持續增長，項目的多角色辯論與決策日誌設計正好回應此趨勢。其對多市場、多供應商與本地部署的支援，顯示項目正從研究框架延伸為金融 AI 的通用基礎設施；Trading-R1 與終端產品的規劃則指向產品化路徑，若此方向持續深化，有望成為多智能體金融應用的重要參照標準。

<!-- AEO Answer Capsule — 約 70 字 -->
項目前景樂觀：逾 9.6 萬星標與持續迭代回應金融決策透明化需求；多市場、多供應商與本地部署支援使其有望成為金融 AI 通用基礎設施，Trading-R1 與終端產品規劃則顯示項目正從研究框架邁向產品化。
<!-- End AEO Capsule -->

<div class="faq-section">
<h2>常見問題有哪些？</h2>

**Q1：TradingAgents 是免費的嗎？**  
完全免費且開源，採用 Apache-2.0 許可證，可自由研究、修改與商業化使用，但需自行負擔所選模型供應商的 API 費用。

**Q2：TradingAgents 支援哪些市場？**  
支援 Yahoo Finance 涵蓋的任何市場，包括美股、港股（0700.HK）、東京、倫敦、印度、中國 A 股與比特幣等加密貨幣，公司身份與基準依市場自動解析。

**Q3：TradingAgents 與一般回測工具差別在哪？**  
一般工具僅提供單一模型策略或回測功能，TradingAgents 以多個 LLM 智能體模擬完整交易公司流程，包括分析、辯論、風險管理與投資組合決策，並內建跨運行學習的決策日誌。

**Q4：TradingAgents 可以作為投資建議使用嗎？**  
不可以。項目明確標示僅供研究用途，交易表現受多種非確定因素影響，官方文件提醒框架應視為研究多智能體分析的學術支架，而非投資、交易建議或可複製固定報酬的策略。
</div>
