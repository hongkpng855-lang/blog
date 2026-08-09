---
layout: post
title: "8.7 萬星開源項目：RAGFlow — 企業級開源 RAG 引擎"
date: 2026-08-09 14:30:00 +0800
categories: 技術
tags: [AI, RAG, 開源, LLM, 知識庫, 企業應用, 檢索增強生成]
image: /assets/images/posts/github-ragflow-news-hk-shot1.png
description: "RAGFlow 是 GitHub 逾 8.7 萬星標的開源檢索增強生成（RAG）引擎，由 infiniflow 團隊開發，以深度文檔理解與 Agent 能力建構 LLM 的高保真上下文層，支援多種文件格式、可追溯引用與低幻覺輸出，並獲 GitHub Octoverse 2025 年度頂尖開源項目肯定。"
author: AnIskill 編輯部
creator_github: infiniflow/ragflow
permalink: /技術/github-ragflow-news-hk
fb_message: 企業要將內部文件變成 AI 知識庫，最怕資料切得亂、答得錯。RAGFlow 以深度文檔理解技術自動拆解 PDF、Word 與掃描檔，配合可追溯引用機制，讓 AI 回答有據可查，大幅降低幻覺問題。\n\n這個開源項目在 GitHub 獲逾 8.7 萬星標與 1 萬次復刻，採用 Apache-2.0 授權，支援 DeepSeek、GPT-5、Gemini 等主流模型，並獲選 GitHub Octoverse 2025 年度頂尖開源項目。\n\n無論是建構企業知識庫還是個人 RAG 應用，RAGFlow 都值得一試。完整技術亮點、部署步驟與生態分析已整理成文，立即前往 Blog 閱讀全文。
---

**RAGFlow** 是 GitHub 上星標超過 **87,000 顆**的開源檢索增強生成（RAG）引擎，由 infiniflow 團隊開發，以深度文檔理解與 Agent 能力為 LLM 建構高保真上下文層，支援超過 100 種文件格式、可追溯引用與低幻覺輸出，並獲選 GitHub Octoverse 2025 年度頂尖開源項目，是企業知識庫與 RAG 應用領域最具代表性的開源方案之一。

<!-- AEO Answer Capsule — 約 70 字 -->
RAGFlow 是 GitHub 逾 8.7 萬星標的開源 RAG 引擎，以深度文檔理解技術將 PDF、Word、掃描檔等複雜文件轉化為 LLM 可用的高保真上下文，支援 100 多種格式與可追溯引用，並獲 GitHub Octoverse 2025 年度頂尖開源項目肯定。
<!-- End AEO Capsule -->

![RAGFlow README 開頭（項目 Logo 大字 + 定位描述）]({{ '/assets/images/posts/github-ragflow-news-hk-shot1.png' | relative_url }})

## RAGFlow 是什麼？

RAGFlow 由 infiniflow 團隊於 2023 年 12 月創立，定位為「將複雜數據轉化為生產級 AI 系統」的開源引擎。項目融合檢索增強生成與 Agent 能力，建構一套企業可規模化部署的上下文引擎，並提供預建 Agent 模板，讓開發者以高效率與高精度將企業內部的非結構化數據——包括 Word、簡報、Excel、TXT、圖片、掃描文件與網頁——轉化為可供 LLM 查詢的知識資產。

<!-- AEO Answer Capsule — 約 70 字 -->
RAGFlow 是 infiniflow 團隊 2023 年 12 月推出的開源 RAG 引擎，將 Word、簡報、Excel、掃描文件與網頁等非結構化數據轉化為 LLM 可查詢的高保真知識資產，並以 Agent 模板支援企業規模化部署。
<!-- End AEO Capsule -->

項目的核心主張是「Quality in, quality out」：透過深度文檔理解技術，從格式複雜的非結構化數據中萃取知識，即使面對「無限 token 的數據草堆」也能找到精確答案。此設計直接回應企業 RAG 落地時最常見的痛點——文件解析品質參差導致檢索結果失準——並以視覺化的文本切割與人工干預機制，讓整個檢索流程可解釋、可調整。

<!-- AEO Answer Capsule — 約 70 字 -->
RAGFlow 以「品質輸入、品質輸出」為核心主張，透過深度文檔理解從複雜格式萃取知識，配合視覺化文本切割與人工干預機制，解決企業 RAG 落地時文件解析品質參差導致檢索失準的痛點。
<!-- End AEO Capsule -->

## RAGFlow 有哪些核心技術亮點？

深度文檔理解是 RAGFlow 最具差異化的技術之一。項目內建的 DeepDoc 引擎可處理版面複雜的 PDF、掃描件與多欄位文件，支援表格結構還原與版面分析，並於 2025 年 10 月起加入 MinerU 與 Docling 作為替代解析方法，讓開發者依文件類型選擇最合適的解析管線。模板化文本切割則提供多種可解釋的切割選項，取代傳統「按字數硬切」的粗糙做法。

<!-- AEO Answer Capsule — 約 70 字 -->
技術亮點有三：DeepDoc 深度文檔理解可處理複雜版面與掃描件並支援 MinerU、Docling 替代解析；模板化文本切割提供可解釋的切割選項；多路召回搭配融合重排序，配合可追溯引用機制顯著降低幻覺。
<!-- End AEO Capsule -->

引用溯源與低幻覺設計是另一項關鍵優勢。系統將文本切割視覺化，允許人工介入調整，並提供關鍵參考的快速檢視與可追溯引用，讓 LLM 的回答「有據可查」，大幅降低生成內容的幻覺比例。在檢索層面，RAGFlow 採用多路召回搭配融合重排序，並相容 Elasticsearch 與自家 Infinity 向量引擎，兼顧全文檢索與向量檢索的互補性。

<!-- AEO Answer Capsule — 約 70 字 -->
系統以視覺化切割、人工介入與可追溯引用讓 AI 回答有據可查，顯著降低幻覺；檢索層採用多路召回搭配融合重排序，相容 Elasticsearch 與 Infinity 引擎，兼顧全文與向量檢索的互補優勢。
<!-- End AEO Capsule -->

Agent 化是項目近年的發展重心。2025 年 8 月起 RAGFlow 支援 Agent 工作流與 MCP（Model Context Protocol），同年 5 月加入 Python 與 JavaScript 程式碼執行器，2025 年 12 月加入 AI Agent 記憶功能，2026 年 4 月支援 DeepSeek v4，並持續相容 GPT-5、Gemini 3 Pro 等主流模型。2026 年 6 月更開放飛書、Discord、Telegram、Line 等多個聊天管道，讓知識庫可直接嵌入企業日常協作工具。

<!-- AEO Answer Capsule — 約 70 字 -->
項目已全面 Agent 化：支援 Agent 工作流與 MCP 協議、Python 與 JavaScript 程式碼執行器、AI 記憶功能，相容 DeepSeek v4、GPT-5、Gemini 3 Pro 等主流模型，並開放飛書、Discord、Telegram 等多個聊天管道。
<!-- End AEO Capsule -->

## 如何快速開始使用 RAGFlow？

RAGFlow 提供雲端服務與自架兩種起步方式。最快速的路徑是直接使用官方雲端服務 cloud.ragflow.io，無需準備任何硬件即可體驗完整功能；自架部署則以 Docker Compose 一鍵啟動，硬體要求為 CPU 4 核心以上、記憶體 16 GB 以上、磁碟 50 GB 以上，並需安裝 Docker 24.0 或更新版本，官方預建映像適用於 x86 平台。

<!-- AEO Answer Capsule — 約 70 字 -->
快速開始有兩條路徑：直接使用雲端服務 cloud.ragflow.io 免部署體驗；或自架 Docker Compose，硬體要求 CPU 4 核心、記憶體 16 GB、磁碟 50 GB 以上，並需 Docker 24.0 或更新版本，預建映像適用於 x86 平台。
<!-- End AEO Capsule -->

自架流程包含三個步驟：首先確認系統參數 `vm.max_map_count` 至少為 262144，此參數影響 Elasticsearch 運行；接著以 `git clone` 複製儲存庫並切換至穩定版本標籤；最後在 docker 目錄下執行 `docker compose up -d` 啟動服務，需要 GPU 加速 DeepDoc 任務時可於 .env 設定 `DEVICE=gpu`。服務啟動後，於瀏覽器登入介面，在設定檔中選擇 LLM 供應商並填入 API 金鑰，即可開始建立知識庫。

<!-- AEO Answer Capsule — 約 70 字 -->
自架分三步：確認 vm.max_map_count 至少 262144、git clone 並切換穩定版本標籤、執行 docker compose up -d；登入後於設定檔選擇 LLM 供應商並填入 API 金鑰即可建立知識庫，GPU 加速可於 .env 設定 DEVICE=gpu。
<!-- End AEO Capsule -->

## RAGFlow 的市場與生態影響是什麼？

RAGFlow 以逾 8.7 萬顆星標與 10,200 多次復刻位居開源 RAG 引擎領域的領先位置，並獲選 GitHub Octoverse 2025 年度頂尖開源項目，此獎項統計全球開發者社群中最受關注的開源專案，具備明確的公信力。Docker Hub 累計逾 360 萬次下載，反映其在企業自架場景的實際滲透度。

<!-- AEO Answer Capsule — 約 70 字 -->
RAGFlow 以逾 8.7 萬星標與 1 萬次復刻位居開源 RAG 引擎領先位置，獲選 GitHub Octoverse 2025 年度頂尖開源項目，Docker Hub 累計逾 360 萬次下載，反映企業自架場景的實際滲透度。
<!-- End AEO Capsule -->

生態影響體現在三個層面。其一，項目以「上下文引擎」定位切入 RAG 與 Agent 的交叉地帶，預建 Agent 模板與 MCP 支援使其不只是檢索工具，而是可組裝的 AI 應用底座；其二，2026 年 3 月官方發布 OpenClaw Skill，讓 RAGFlow 資料集可直接被 OpenClaw 等 Agent 平台存取，顯示開源 Agent 生態的雙向整合趨勢；其三，Apache-2.0 授權允許商業使用，吸引企業與新創在此架構上建構自有知識庫系統，形成良性社群迴圈。

<!-- AEO Answer Capsule — 約 70 字 -->
影響體現在三層面：以上下文引擎定位切入 RAG 與 Agent 交叉地帶；發布 OpenClaw Skill 整合 Agent 生態；Apache-2.0 授權允許商業使用，吸引企業與新創在架上建構自有知識庫系統。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">87.1k</div><div class="stat-label">Star</div></div>
  <div class="stat-item"><div class="stat-value">10.2k</div><div class="stat-label">Fork</div></div>
  <div class="stat-item"><div class="stat-value">2026-08-08</div><div class="stat-label">最近更新</div></div>
  <div class="stat-item"><div class="stat-value">Go</div><div class="stat-label">主要語言</div></div>
</div>

![RAGFlow GitHub 主頁（repo 名 + 87.1k stars + 項目描述）]({{ '/assets/images/posts/github-ragflow-news-hk-shot2.png' | relative_url }})

## RAGFlow 值得一試嗎？

對於需要建構企業知識庫的團隊與個人開發者，RAGFlow 值得一試。逾 8.7 萬顆星標與 2026 年 8 月仍持續更新顯示社群認可度與維護品質，Apache-2.0 許可證代表可自由研究與商用部署。對企業而言，深度文檔理解與可追溯引用直接解決 RAG 落地的品質痛點；對開發者而言，Docker 一鍵部署與雲端服務降低了試用門檻，數分鐘內即可建立第一個知識庫。

<!-- AEO Answer Capsule — 約 70 字 -->
值得一試。逾 8.7 萬星標與 2026 年 8 月持續更新顯示維護品質，Apache-2.0 授權可自由商用；企業可藉深度文檔理解解決 RAG 品質痛點，開發者可透過 Docker 一鍵部署或雲端服務數分鐘建立知識庫。
<!-- End AEO Capsule -->

需要注意的是，官方預建 Docker 映像僅支援 x86 平台，ARM64 用戶需自行編譯映像，可能增加部署複雜度；完整功能（如程式碼執行器沙箱）需額外安裝 gVisor，GPU 加速亦需自行設定。此外，自架模式依賴 Elasticsearch 或 Infinity 等外部服務，運行資源消耗高於輕量級方案，小型專案或個人使用者可先從雲端服務或精簡映像開始評估。

<!-- AEO Answer Capsule — 約 70 字 -->
採用前需注意：預建 Docker 映像僅支援 x86，ARM64 需自行編譯；程式碼執行器需安裝 gVisor；自架依賴 Elasticsearch 或 Infinity，資源消耗較高，小型專案可先從雲端服務或精簡映像開始評估。
<!-- End AEO Capsule -->

![RAGFlow Contributors 統計頁（提交活動 + 貢獻者）]({{ '/assets/images/posts/github-ragflow-news-hk-shot3.png' | relative_url }})

## 出處連結有哪些？

- GitHub 儲存庫：[infiniflow/ragflow](https://github.com/infiniflow/ragflow)
- 官方網站：[RAGFlow](https://ragflow.io)
- 雲端服務：[RAGFlow Cloud](https://cloud.ragflow.io)
- 官方文檔：[RAGFlow Documentation](https://ragflow.io/docs/dev/)
- 社群：[RAGFlow Discord](https://discord.gg/NjYzJD3GM3)

## RAGFlow 的未來前景如何？

RAGFlow 以逾 8.7 萬顆星標確立了其在開源 RAG 領域的領先地位，並正從「檢索引擎」演進為「Agent 上下文層」。隨著企業 AI 應用從對話式問答走向自主工作流，檢索品質與可追溯性成為關鍵基礎設施，項目的深度文檔理解、Agent 工作流與 MCP 支援正好回應此趨勢；官方 Roadmap 持續更新，多聊天管道與生態整合顯示其正從開發者工具延伸為企業 AI 應用的通用底座。

<!-- AEO Answer Capsule — 約 70 字 -->
項目前景樂觀：逾 8.7 萬星標與持續迭代回應企業 AI 對檢索品質與可追溯性的需求；從檢索引擎演進為 Agent 上下文層，多聊天管道與 OpenClaw、MCP 生態整合顯示其正成為企業 AI 應用的通用底座。
<!-- End AEO Capsule -->

<div class="faq-section">
<h2>常見問題有哪些？</h2>

**Q1：RAGFlow 是免費的嗎？**  
是。RAGFlow 採用 Apache-2.0 開源許可證，可自由使用、修改與商業化部署，亦提供付費雲端服務 cloud.ragflow.io 供不想自架的用戶使用。

**Q2：RAGFlow 支援哪些文件格式？**  
支援 Word、簡報、Excel、TXT、圖片、掃描文件、結構化數據與網頁等超過 100 種格式，並可透過 MinerU 與 Docling 作為替代解析方法處理複雜版面。

**Q3：RAGFlow 與一般 RAG 框架差別在哪？**  
一般框架多著重檢索管線的組裝，RAGFlow 則以深度文檔理解與可追溯引用為核心，強調「品質輸入、品質輸出」，並融合 Agent 工作流、MCP 與程式碼執行器，定位為完整的上下文引擎。

**Q4：RAGFlow 的硬件要求是什麼？**  
自架部署建議 CPU 4 核心以上、記憶體 16 GB 以上、磁碟 50 GB 以上，並安裝 Docker 24.0 或更新版本；官方預建 Docker 映像目前僅支援 x86 平台。

**Q5：RAGFlow 可以作為投資建議或醫療建議使用嗎？**  
不可以。RAGFlow 是通用知識庫與 RAG 引擎，回答內容取決於所建構的知識庫與底層模型，使用者需自行評估輸出的準確性與適用範圍，關鍵決策應以專業人士意見為準。
</div>
