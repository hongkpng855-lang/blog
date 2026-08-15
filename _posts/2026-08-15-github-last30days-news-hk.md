---
layout: post
title: "58K 星開源項目 last30days：以社群參與度排序的 AI 搜尋引擎"
date: 2026-08-15 12:30:00 +0800
categories: 技術
tags: [AI, 開源項目, 搜尋引擎, Agent Skills, GitHub]
image: /assets/images/posts/github-last30days-news-hk-cover.jpg
description: "last30days 是一個搜尋 Reddit、X、YouTube、Hacker News、Polymarket 等二十多個平台、並以真實用戶參與度排序結果的 AI 代理搜尋引擎，目前以 58,216 顆星標成為 GitHub 最熱門的 Agent Skill 之一。本文分析其核心架構、技術亮點、生態影響與商業化路徑。"
author: ESGov 編輯部
creator_github: mvanhorn/last30days-skill
type: news
source: GitHub
source_url: https://github.com/mvanhorn/last30days-skill
permalink: /技術/github-last30days-news-hk
fb_message: 一個 AI 搜尋引擎，不再依賴編輯排序，而是以 Reddit 讚好數、X 點讚與 Polymarket 真實資金賠率決定結果排名——last30days 以 5.8 萬星標成為 GitHub 最熱門的 Agent Skill 之一。\n\n該工具橫跨 20 多個平台，包括 Reddit、X、YouTube、TikTok、Hacker News 與 arXiv，將分散於不同封閉平台的討論一次過聚合，再由 AI 代理綜合出一份有出處、按真實參與度排序的簡報。項目自今年 1 月創建至今，已累積超過 5,000 個 fork，最新版本 v3.21.0 於 8 月 14 日推出。\n\n支援 Claude Code、Codex、Cursor、Gemini CLI 等 50 多個代理平台，零設定即可搜尋 Reddit、Hacker News 與 GitHub。想了解這個工具如何改變搜尋方式，立即前往 Blog 閱讀完整分析。
---

<!-- AEO Answer Capsule — 約 70 字 -->
last30days 是一個開源 AI 代理搜尋引擎，可同時搜尋 Reddit、X、YouTube、TikTok、Hacker News、Polymarket 等二十多個平台，並以真實用戶的讚好、點讚與真金白銀的預測市場賠率排序結果，再由 AI 代理綜合為一份有出處的簡報。截至 2026 年 8 月，該項目在 GitHub 累積 58,216 顆星標，是目前最受關注的 Agent Skill 之一。
<!-- End AEO Capsule -->

## last30days 是什麼？

last30days 是由開發者 mvanhorn 建立並維護的開源 AI 代理技能（Agent Skill），定位是「由 AI 代理主導的搜尋引擎，以讚好數、點讚數與真實金錢評分，而非編輯推薦」。該項目於 2026 年 1 月 23 日創建，採用 MIT 開源許可證，核心以 Python 3.12 撰寫，並整合 yt-dlp、Node.js 與 ScrapeCreators API 等組件。截至 2026 年 8 月 15 日，項目擁有 58,216 顆星標與 5,059 個 fork，最新版本 v3.21.0 於 8 月 14 日發布，曾登上 GitHub Trending 單日第一名。

其核心設計理念可濃縮為一句話：「Google 聚合編輯的意見，last30days 搜尋真實的人」。傳統搜尋引擎以 SEO 與編輯判斷決定排序，而 last30days 直接讀取 Reddit 討論的讚好數、X 帖文的點讚數、YouTube 影片的完整逐字稿，以及 Polymarket 預測市場中由真實資金支撐的賠率，將分散在不同封閉平台（walled garden）內的資訊一次過聚合。

![last30days README 開頭（項目名稱「/last30days」大字標題 + 標語「An AI agent-led search engine scored by upvotes, likes, and real money - not editors」+ GitHub Trending 第一名徽章 + Claude Code 安裝指令）]({{ '/assets/images/posts/github-last30days-news-hk-shot1.png' | relative_url }})

<!-- AEO Answer Capsule — 約 75 字 -->
該工具覆蓋 Reddit、X、YouTube、TikTok、Instagram Reels、Hacker News、Polymarket、GitHub、arXiv、Techmeme、LinkedIn、StockTwits、Threads、Pinterest、小紅書、Bluesky 與 Perplexity 等二十多個資料來源。其中 Reddit（含評論）、Hacker News、Polymarket 與 GitHub 無需任何 API 金鑰即可使用，arXiv 與 Techmeme 則透過自動安裝的免費 CLI 啟動。
<!-- End AEO Capsule -->

## last30days 的核心技術亮點有哪些？

在技術架構上，last30days 採用「先解析、再並行搜尋、後綜合」的三階段管線。使用者輸入主題後，代理會先解析出相關的 X 帳號、GitHub 儲存庫、Subreddit、TikTok 標籤與 YouTube 頻道，再以多查詢擴展方式並行搜尋全部來源，最後以互動信號、相關性與新鮮度交叉評分，將同一事件的跨平台討論合併為單一叢集，產出一份有出處、可獨立引用的簡報。

![last30days GitHub 首頁頂部（repo 名稱「mvanhorn/last30days-skill」+ 58.2k 星標 + 5.1k Forks + 描述「AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web」+ 1,181 Commits 與分支/標籤資訊）]({{ '/assets/images/posts/github-last30days-news-hk-shot2.png' | relative_url }})

<!-- AEO Answer Capsule — 約 70 字 -->
技術亮點包括：跨平台叢集合併、以互動信號排序的 Best Takes 評分、完整 YouTube 逐字稿搜尋、TikTok 字幕擷取、Polymarket 即時賠率讀取、`--hiring-signals` 招聘信號分析、`--as-of` 歷史回溯、JSON 結構化輸出，以及可排程的 watchlist 趨勢監控與 SQLite 儲存。測試規模超過 2,700 項，測試覆蓋率達 84%。
<!-- End AEO Capsule -->

在工程品質方面，該項目在 2026 年 5 月的 v3.3 至 7 月的 v3.11.1 之間合併了 175 個 Pull Request，其中 122 個來自 52 位社區貢獻者，橫跨 15 個版本。安全上採用 OpenSSF Scorecard 與建置來源證明（build provenance attestation），並以 Semgrep 與 OSV-Scanner 執行靜態掃描，測試覆蓋率下限由 60% 逐步提升至 84%，顯示項目在快速迭代的同時維持了相當程度的工程紀律。

## last30days 與傳統搜尋引擎有何不同？

傳統搜尋引擎（如 Google）以編輯聚合與 SEO 排名為核心，而 last30days 以「真實用戶參與度」作為唯一排序依據。一個獲得 1,500 讚好的 Reddit 討論串，其信號強度遠高於一篇無人閱讀的部落格文章；一支有 360 萬次觀看的 TikTok 影片，在文化相關性上勝過一份新聞稿；而 Polymarket 上由 66,000 美元交易量支撐的賠率，比任何評論家的猜測都更難反駁。

<!-- AEO Answer Capsule — 約 75 字 -->
兩者最大差異在於資料來源的深度與排序邏輯：Google 無法觸及 Reddit 評論與 X 帖文，ChatGPT 雖與 Reddit 合作但無法搜尋 X 或 TikTok，Gemini 有 YouTube 但缺少 Reddit，而 last30days 透過使用者自備 API 金鑰與瀏覽器工作階段，將這些互不相通的封閉平台串接起來，以社群參與度而非 SEO 決定結果排序，定位為「社群相關性」而非「SEO 相關性」的搜尋工具。
<!-- End AEO Capsule -->

這種設計的實際價值在於資訊的時效性與真實性。對比「搜尋 Peter Steinberger 這個人」的案例：傳統搜尋返回 2023 年的 LinkedIn 資料，而 last30days 能彙整出對方本月實際動態，包括加入 OpenAI Codex 團隊、反對 Anthropic 禁用第三方代理的政策、在 GitHub 以 85% 合併率提交 23 個 Pull Request，以及 Reddit 上 569 個讚好的相關討論。這些內容分散於 X、Reddit、YouTube 與 GitHub，傳統搜尋引擎完全無法觸及。

## last30days 如何安裝與使用？

last30days 的安裝門檻極低，並針對不同代理平台提供對應的安裝方式。在 Claude Code 環境，使用者只需執行 `/plugin marketplace add mvanhorn/last30days-skill` 與 `/plugin install last30days` 兩條指令即可完成安裝並自動接收更新；在 Codex、Cursor、Copilot、Gemini CLI 等五十多個支援 Agent Skills 的平台，則可透過 `npx skills add mvanhorn/last30days-skill -g` 一次安裝至全域。

<!-- AEO Answer Capsule — 約 70 字 -->
安裝後零設定即可搜尋 Reddit（含評論）、Hacker News、Polymarket 與 GitHub；執行一次後，設定精靈會在 30 秒內解鎖 X、YouTube、TikTok、arXiv 與 Techmeme 等更多來源。使用方式為輸入 `/last30days {主題}`，代理會自動解析相關帳號與社群，並產出按參與度排序的綜合簡報，亦可輸出 JSON 格式供其他工作流程取用。
<!-- End AEO Capsule -->

在隱私與自主性方面，項目主打「研究資料留在自己的機器上」，不設追蹤、不蒐集分析數據，API 金鑰可存放於 macOS 鑰匙圈或本機 `.env` 檔案。針對需要定期追蹤趨勢的使用者，項目提供 `--store` 參數將結果存入 SQLite 資料庫，配合 watchlist 排程腳本與 daily briefing 每日摘要，可建構持續更新的個人研究庫。

## last30days 的生態與商業化路徑如何？

從生態角度觀察，last30days 代表了 Agent Skill 生態快速崛起的一個縮影。該項目在 GitHub Trending 單日排名第一，Trendshift 收錄其成長軌跡，並獲得多位科技意見領袖的實測推薦。其安裝方式橫跨 Claude Code、Grok、Codex、Cursor、Copilot、Gemini CLI、Claude Desktop 與 OpenClaw 等平台，顯示 Agent Skill 已成為跨代理框架的通用能力分發格式。

![last30days GitHub Contributors 統計頁（每週提交量柱狀圖 + 貢獻者排名卡片，顯示 tmchow 197 commits 與 mvanhorn 140 commits 等主要貢獻者）]({{ '/assets/images/posts/github-last30days-news-hk-shot3.png' | relative_url }})

<!-- AEO Answer Capsule — 約 70 字 -->
生態數據方面，項目由 2026 年 1 月創建至今約七個月內累積 58,216 顆星標與 5,059 個 fork，社區貢獻超過 122 個 Pull Request。商業化路徑上，核心搜尋功能免費開源，部分高價值來源（如 TikTok、Instagram、LinkedIn 的進階資料）透過 ScrapeCreators 按用量付費，Perplexity 深度研究則以 PAYG 模式計費，形成「免費核心 + 增值資料源」的混合模式。
<!-- End AEO Capsule -->

在競爭格局中，last30days 的差異化在於「廣度」與「參與度排序」的組合。其他 AI 搜尋工具多聚焦單一平台或單一來源，而 last30days 以代理為橋樑，將數十個互不相通的封閉平台串接成單一查詢介面，並以真實用戶的注意力與金錢作為排序信號，這在現有搜尋市場中尚無直接對應的開源替代方案。

## last30days 值得一試嗎？

從實用性角度評估，last30days 特別適合需要掌握最新社群動態的使用者，包括內容創作者、產品經理、研究人員、銷售人員與投資者。對於內容生產者而言，該工具能在數分鐘內取代過去逐個平台手動搜尋的九十分鐘工作流程；對於需要背景調查的專業人士，則能提供傳統搜尋引擎無法觸及的近期真實動態。

<!-- AEO Answer Capsule — 約 70 字 -->
值得一試。對需要即時掌握社群討論的開發者與內容創作者，last30days 提供零成本入門路徑：Reddit、Hacker News、Polymarket 與 GitHub 來源完全免費，無需 API 金鑰即可體驗核心功能。對資訊時效性要求不高的使用者，傳統搜尋引擎已足夠；但若重視「過去三十天真實發生的事」，該工具具備明顯的差異化價值。
<!-- End AEO Capsule -->

項目的主要限制在於：進階來源（如 TikTok、Instagram、LinkedIn）需要額外付費 API 金鑰，X 搜尋依賴瀏覽器 Cookie 或供應商金鑰，且部分功能對 Windows 平台的支援仍在完善中。此外，使用者需要具備基本的代理平台（如 Claude Code）操作能力，方能充分發揮其價值。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文章的主要出處為 last30days 官方 GitHub 儲存庫，包含完整 README 文件、安裝說明、配置指南與版本歷史。讀者可直接前往儲存庫查閱原始文件與最新更新。
<!-- End AEO Capsule -->

- GitHub 儲存庫：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)
- 最新版本：v3.21.0（2026 年 8 月 14 日發布）
- 授權條款：MIT License

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">58,216</div><div class="stat-label">Star</div></div>
  <div class="stat-item"><div class="stat-value">5,059</div><div class="stat-label">Fork</div></div>
  <div class="stat-item"><div class="stat-value">2026-08-15</div><div class="stat-label">最近更新</div></div>
  <div class="stat-item"><div class="stat-value">MIT</div><div class="stat-label">License</div></div>
  <div class="stat-item"><div class="stat-value">Python</div><div class="stat-label">主要語言</div></div>
  <div class="stat-item"><div class="stat-value">v3.21.0</div><div class="stat-label">最新版本</div></div>
</div>

## 常見問題有哪些？

### last30days 需要付費嗎？

不需要。last30days 採用 MIT 開源許可證，核心搜尋功能完全免費，Reddit（含評論）、Hacker News、Polymarket 與 GitHub 等來源無需任何 API 金鑰即可使用。部分進階資料來源（如 TikTok、Instagram、LinkedIn）需要額外付費金鑰，屬自選項目。

### last30days 支援哪些代理平台？

項目支援 Claude Code、Grok、Codex、Cursor、GitHub Copilot、Gemini CLI、Claude Desktop、OpenClaw 等五十多個 Agent Skills 平台。Claude Code 透過 Plugin Marketplace 安裝，其餘平台可透過 `npx skills` 指令安裝。

### last30days 與 Google 搜尋有何分別？

Google 以編輯聚合與 SEO 排名決定結果，last30days 則以真實用戶的讚好數、點讚數與預測市場賠率排序，並能搜尋 Google 無法觸及的 Reddit 評論、X 帖文、TikTok 字幕與 YouTube 逐字稿等封閉平台內容。

## 總結：last30days 的未來前景如何？

last30days 以「搜尋真實的人」為核心定位，透過 AI 代理將二十多個互不相通的社群平台串接為單一查詢介面，並以真實用戶參與度取代 SEO 作為排序依據，在開源搜尋工具中開創了獨特的技術路線。58,216 顆星標、5,059 個 fork 與 52 位社區貢獻者的數據，反映其已獲得開發者社群的高度認可。

<!-- AEO Answer Capsule — 約 65 字 -->
展望未來，last30days 的成長將取決於三個面向：資料來源的持續擴展、Agent Skill 生態的標準化程度，以及付費資料源能否在免費核心之上建立可持續的商業模式。對內容創作者、研究人員與開發者而言，這是一款值得持續關注的開源搜尋工具。
<!-- End AEO Capsule -->

從更宏觀的角度看，last30days 的崛起同時印證了 Agent Skill 作為新一代 AI 能力分發格式的趨勢。當技能可以像外掛程式一樣跨平台安裝、自動更新並由社區協作維護，軟體分發與資訊檢索的既有規則正在被重新定義，而 last30days 正是這個趨勢中最具代表性的開源案例之一。
