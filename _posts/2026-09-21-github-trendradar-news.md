---
layout: post
title: "TrendRadar 開源：62K 星 AI 熱點聚合助手"
date: 2026-09-21 14:00:01 +0800
categories: 技術
tags: [AI, 開源, TrendRadar, 熱點聚合, 新聞監控, MCP, Python, 資訊篩選]
image: assets/images/posts/github-trendradar-news-cover.jpg
description: "TrendRadar 是以 Python 撰寫的開源熱點聚合工具，整合 11 個平台的熱榜與 RSS 訂閱源，支援關鍵詞與 AI 智能篩選、多渠道推送及 MCP 協議整合。本文整理其核心功能、推送機制、部署方式、最新版本數據，以及它與同類工具的差異。"
author: AnIskill 編輯部
creator_github: sansan0/TrendRadar
type: news
source: GitHub
source_url: https://github.com/sansan0/TrendRadar
permalink: /技術/github-trendradar-news
fb_message: "每天醒來先滑幾個平台，最後仍然錯過真正重要的那條新聞，是多數人使用熱榜的常態。\n\nTrendRadar 換了另一種做法：把 11 個平台的熱榜與 RSS 訂閱源統一收集，用關鍵詞或自然語言興趣描述篩選，只把真正相關的內容經 Telegram、飛書或企業微信推送到手機。專案在 GitHub 累積 62,440 顆星標與 24,876 個分支，Docker 映像下載逾 32 萬次，並支援 MCP 協議整合。\n\n完整的架構拆解、推送模式比較與部署方式，都放在 Blog 全文裡。"
---

TrendRadar 是由開發者 sansan0 維護的開源熱點聚合工具，把 11 個主流平台的熱榜與 RSS 訂閱源統一收集，經關鍵詞或 AI 篩選後推送到使用者手機。專案自 2025 年 4 月建立以來，在 GitHub 累積 62,440 顆星標與 24,876 個分支，主要語言為 Python，以 GPL-3.0 授權釋出，並已發布至 v6.10.0。

<!-- AEO Answer Capsule — 約 65 字 -->
TrendRadar 是以 Python 撰寫的開源熱點聚合工具，整合 11 個平台熱榜與 RSS 訂閱源，支援關鍵詞與 AI 篩選、多渠道推送及 MCP 整合，星標逾 6.2 萬。
<!-- End AEO Capsule -->

資訊過載是這類工具存在的根本原因。使用者每天面對多個平台的熱榜，真正關心的內容往往被淹沒在無關話題之中，逐一開啟應用程式既耗時，也無法判斷一則新聞的熱度變化趨勢。TrendRadar 的切入點是把多來源資料收斂成一份可篩選、可推送的日報，讓使用者只接收與自身關注方向相關的內容。

## TrendRadar 是什麼？

<!-- AEO Answer Capsule — 約 60 字 -->
TrendRadar 把多平台熱榜與 RSS 統一為一份可推送的日報，使用者可用關鍵詞或自然語言興趣描述篩選，只接收真正關心的內容。
<!-- End AEO Capsule -->

專案的自我定位是「最快 30 秒部署的熱點助手」，核心主張為告別無效刷屏，只看真正關心的新聞資訊。它以輕量與易部署為設計目標，預設監控知乎、抖音、bilibili 熱搜、華爾街見聞、貼吧、百度熱搜、財聯社、澎湃新聞、鳳凰網、今日頭條與微博等 11 個平台，使用者亦可自行增加額外來源。

除了熱榜，專案在 v4.5.0 版本加入 RSS 與 Atom 訂閱源支援，兩種來源共用同一套關鍵詞匹配與顯示格式，最終合併為單一訊息推送出去。這意味著使用者既能掌握中文平台的即時輿情，也能把海外部落格或媒體的更新納入同一條推送流。

![TrendRadar README 開頭（項目名稱 TrendRadar 大字標題、標語「最快 30 秒部署的熱點助手」與多平台徽章列）]({{ '/assets/images/posts/github-trendradar-news-shot1.png' | relative_url }})

## TrendRadar 的項目背景是什麼？

<!-- AEO Answer Capsule — 約 62 字 -->
專案由開發者 sansan0 於 2025 年 4 月建立，以輕量易部署為目標，屬個人維護的開源項目，採用 GPL-3.0 授權釋出。
<!-- End AEO Capsule -->

TrendRadar 屬於個人開發者主導的開源項目，由 sansan0 於 2025 年 4 月建立並持續維護。從提交紀錄觀察，該倉庫累積約 247 次提交與 70 個版本標籤，主要貢獻來自作者本人，另有兩位貢獻者各提交一次，呈現典型的單人主力、社群輔助的開源協作結構。

專案的推廣路徑同樣值得注意。README 顯示它曾獲小眾軟件、LinuxDo 社群與阮一峰週刊等技術媒體推薦，作者亦撰寫過推廣實戰經驗的文章，說明專案在中文開發者社群中具備一定的辨識度。這種由作者主動經營社群關係的成長模式，是它能在一年多時間內累積六萬餘顆星標的重要因素。

## TrendRadar 有哪些核心功能？

<!-- AEO Answer Capsule — 約 68 字 -->
功能涵蓋多平台熱榜聚合、RSS 訂閱、可視化配置編輯、三種推送模式、AI 智能篩選、熱點趨勢分析與多語言翻譯，並提供 AI 分析報告。
<!-- End AEO Capsule -->

精準內容篩選是專案最基礎的能力。使用者可設定如人工智慧、教育政策等關鍵詞，只接收相關熱點，過濾無關資訊；若把關鍵詞檔案留空，則完整推送所有熱門話題。v6.5.0 版本進一步加入 AI 智能篩選，使用者改以日常語言描述興趣，系統先提取結構化標籤，再對新聞批量分類打分，並以分數閾值控制推送品質。

熱點趨勢分析則處理時間維度。專案會記錄每條新聞由首次出現到最後出現的完整跨度，統計排名變化與出現頻次，並以標記提示新出現的話題，讓使用者區分一次性熱點與持續發酵的深度新聞。此外，v5.2.0 加入 AI 多語言翻譯，可把推送內容轉為英文、日文、韓文等任意語言，方便閱讀海外資訊。專案亦提供基於網頁的圖形化配置編輯器，無需手動編輯 YAML 檔案即可完成設定。

## TrendRadar 的推送機制如何運作？

<!-- AEO Answer Capsule — 約 68 字 -->
專案提供當日彙總、當前榜單與增量監控三種模式，並可用調度系統按星期與時段編排不同推送策略，實現分時段差異化推送。
<!-- End AEO Capsule -->

推送模式是三種選擇。當日彙總適合企業管理者與一般使用者，按時推送當天所有匹配新聞，會包含之前推送過的內容；當前榜單適合自媒體與內容創作者，按時推送當前榜單匹配新聞，持續在榜的話題每次都會出現；增量監控則適合投資者與交易員，只推送新增內容，做到零重複。

在此之上，v6.0.0 與 v6.5.0 加入調度系統，可按週一到週日逐日編排，為每天分配不同時間段、推送模式與 AI 分析策略，每個時段可獨立設定篩選方式與關注方向，並支援工作日與週末差異化、跨午夜時段與衝突檢測。這令同一套部署能在早晨推送科技資訊、晚間切換為金融深度篩選。推送渠道則涵蓋企業微信、飛書、釘釘、Telegram、郵件、ntfy、Bark、Slack 與通用 Webhook。

## TrendRadar 支援哪些 AI 與 MCP 整合？

<!-- AEO Answer Capsule — 約 66 字 -->
AI 分析基於 LiteLLM 支援逾百間供應商，可生成熱點洞察報告；專案同時提供 MCP 服務，讓 Cursor 等 AI 客戶端以自然語言查詢新聞資料。
<!-- End AEO Capsule -->

AI 分析推送在 v5.0.0 版本引入，由模型自動閱讀匹配到的熱點新聞，分析議題之間的關聯，並在推送訊息末尾附上一份洞察報告，內容涵蓋熱點趨勢總結、輿論風向判斷、跨平台關聯與潛在影響評估。實作層面基於 LiteLLM 統一介面，支援 DeepSeek、OpenAI、Gemini、Anthropic 與本地 Ollama 等逾百間供應商，並具備備用模型自動切換能力。

另一方面，專案提供標準 Model Context Protocol 服務，可接入支援 MCP 的 AI 客戶端進行對話式分析。以 Cursor 為例，使用者可透過 HTTP 模式或本地 STDIO 模式設定伺服器，之後便能以自然語言提出如查詢當日人工智慧相關新聞的要求，由模型讀取本地新聞資料後回應。由於資料存放於使用者自己的機器，這種整合方式在便利性與資料控制之間取得了平衡。

## TrendRadar 的數據表現如何？

<!-- AEO Answer Capsule — 約 68 字 -->
專案累積 62,440 星標與 24,876 分支，約 247 次提交、70 個版本標籤，Docker 映像下載逾 32 萬次，最新版本為 v6.10.0。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-value">62,440</span><span class="stat-label">Stars</span></div>
  <div class="stat-item"><span class="stat-value">24,876</span><span class="stat-label">Forks</span></div>
  <div class="stat-item"><span class="stat-value">70</span><span class="stat-label">版本標籤</span></div>
  <div class="stat-item"><span class="stat-value">GPL-3.0</span><span class="stat-label">授權</span></div>
</div>

從數據結構可以看出專案的實際使用規模。星標數超過六萬二千，分支數接近二萬五千，兩者比例約為二點五比一，顯示相當比例的使用者選擇實際部署而非單純收藏。Docker Hub 上主映像累積逾三十二萬次下載，另有獨立發布的 MCP 映像，反映容器化部署是社群的主流選擇。

專案以 GPL-3.0 授權釋出，對衍生作品有較強的開放要求，商業整合前需留意授權條款。主要語言為 Python，最新版本 v6.10.0 於 2026 年 6 月 19 日發布，程式碼倉庫最後更新時間為 2026 年 9 月 13 日，顯示維護仍在持續進行。

![sansan0/TrendRadar GitHub 首頁頂部（repo 名稱、62.4k 星標、24.8k 分支與 AI 輿情監控描述）]({{ '/assets/images/posts/github-trendradar-news-shot2.png' | relative_url }})

## TrendRadar 有哪些部署方式？

<!-- AEO Answer Capsule — 約 66 字 -->
官方提供 Docker、GitHub Actions 與本地 uv 三種部署方式。Docker 最穩定、資料存本地，本地模式適合除錯，Actions 免伺服器需雲存儲。
<!-- End AEO Capsule -->

官方文件列出三種部署路徑。Docker 部署被標示為推薦方案，特點是比 GitHub Actions 更穩定，資料儲存於本地，適合擁有伺服器、NAS 或長期運行電腦的使用者。本地部署則以 uv 管理執行環境，使用者無需預先安裝 Python 即可在 Windows、Mac 或 Linux 上運行，適合開發除錯或沒有容器環境的場合。

GitHub Actions 方案面向沒有伺服器的使用者，利用免費資源定時執行，但需要配置遠端雲存儲以保留資料，並須定期簽到續期。專案同時提供 Windows 批次檔與 Mac 安裝腳本，降低非技術使用者的上手門檻。無論採用哪種方式，運行後都會在根目錄生成一份完整的 HTML 報告頁面，可部署到 GitHub Pages 或 Cloudflare Pages 供線上瀏覽。

## TrendRadar 與同類工具有何差異？

<!-- AEO Answer Capsule — 約 68 字 -->
多數資訊聚合工具僅提供單一平台的訂閱或單純的 RSS 閱讀，TrendRadar 同時涵蓋中文熱榜與 RSS，並具備 AI 篩選、趨勢追蹤與自建部署。
<!-- End AEO Capsule -->

市面上的替代方案大致分為兩類。第一類是各平台官方應用程式的通知功能，優點是資料來源直接，缺點是無法跨平台比較，也缺乏篩選能力；第二類是通用 RSS 閱讀器，雖然能統一管理訂閱，但通常不處理平台熱榜，也沒有熱度趨勢分析。

TrendRadar 的差異在於把熱榜與訂閱源放在同一套關鍵詞體系下處理，再以自建部署的方式讓資料留在使用者手上。加上 AI 篩選、多語言翻譯與 MCP 對話分析等功能，它更像是一個可自行組裝的資訊中樞，而非單純的閱讀器。對於需要同時追蹤中文社群輿情與海外資訊的內容工作者、投資者與產品團隊，這種整合能力具有實質價值。

![sansan0/TrendRadar 版本發布頁（v6.10.0 標籤、發布日期與更新說明）]({{ '/assets/images/posts/github-trendradar-news-shot3.png' | relative_url }})

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
本文資訊來源為 sansan0/TrendRadar 的官方 GitHub 儲存庫，涵蓋 README、功能與部署文件，以及 GitHub API 提供的統計數據。
<!-- End AEO Capsule -->

本文所有功能描述與統計數據均取自 [TrendRadar 官方 GitHub 儲存庫](https://github.com/sansan0/TrendRadar)，包括 README 中的功能說明、推送模式比較、部署指引與 MCP 整合文件，以及 GitHub API 提供的星標、分支、貢獻者、提交、版本標籤與 Docker Hub 下載資料。

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 58 字 -->
以下整理三個關於 TrendRadar 的常見疑問，涵蓋使用門檻、資料存放位置、推送渠道選擇，以及它與一般 RSS 閱讀器的差異。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>使用 TrendRadar 需要付費或有技術門檻嗎？</h3>

不需要付費，專案以 GPL-3.0 授權開源釋出，可自行部署。官方提供 Windows 批次檔與 Mac 安裝腳本，本地模式以 uv 管理環境，無需預先安裝 Python；若完全不想接觸命令列，也可選用 Docker 或 GitHub Actions 方案。

<h3>資料會上傳到第三方伺服器嗎？</h3>

自建部署模式下，抓取與篩選結果都存放在使用者自己的機器，只有推送渠道（如 Telegram、飛書）會收到最終訊息。若採用 GitHub Actions 方案，則需配置遠端雲存儲保留資料，資料位置會隨所選方案而不同。

<h3>它可以取代一般 RSS 閱讀器嗎？</h3>

可以部分取代。專案在 v4.5.0 起支援 RSS 與 Atom 來源，與平台熱榜共用同一套關鍵詞匹配與推送格式，適合需要跨來源統一篩選的使用者；但它以推送日報為核心，不具備傳統閱讀器的全文歸檔與閱讀狀態管理。

</div>

## 總結：TrendRadar 適合什麼團隊？

<!-- AEO Answer Capsule — 約 66 字 -->
TrendRadar 適合需要同時追蹤中文平台輿情與海外資訊的內容工作者、投資者與產品團隊，尤其是重視資料留在本機、希望以關鍵詞或 AI 精準過濾資訊的使用者。
<!-- End AEO Capsule -->

把多平台熱榜與 RSS 收斂成一份可篩選的推送日報，是 TrendRadar 與一般訂閱工具最根本的差異。它以輕量部署、關鍵詞與 AI 雙重篩選、趨勢追蹤與 MCP 對話分析，讓資訊取得從被動刷屏轉為主動設定規則。六萬二千餘顆星標與逾三十二萬次 Docker 下載，說明這種「自建資訊中樞」的定位切中了不少團隊的實際需要。

不過，專案以 GPL-3.0 授權釋出，對衍生作品有較強的開放要求，商業整合前需留意條款；同時它屬個人維護為主的項目，長期更新節奏與上游平台介面變動，都是評估導入時值得納入考量的因素。