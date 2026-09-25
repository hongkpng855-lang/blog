---
layout: post
title: "38K 星 LangExtract 開源：LLM 抽取可溯源"
date: 2026-09-26 06:00:01 +0800
categories: 技術
tags: [LangExtract, Google, LLM, 資訊抽取, 結構化輸出, Gemini, 開源專案]
image: assets/images/posts/github-langextract-news-cover.jpg
description: "Google 開源的 LangExtract 以 Python 撰寫，讓語言模型把非結構化文字抽成結構化資料，並要求每筆結果對應原文精確字元區間。專案在 GitHub 累積 38,860 顆星標與 2,718 次複製，支援 Gemini、OpenAI 與本機 Ollama 模型。"
author: AnIskill 編輯部
creator_github: google/langextract
type: news
source: GitHub
source_url: https://github.com/google/langextract
permalink: /技術/github-langextract-news
fb_message: "抽取工具真正的價值不在於認出欄位，而在於能否證明欄位出自哪裡。\n\nGoogle 開源的 LangExtract 用一個簡單條件解決這件事：每筆抽取都必須對應回原文的精確字元區間，抽不到位置的結果會被標記出來讓使用者過濾。它同時支援 Gemini、OpenAI 與本機 Ollama，使用者只要給幾組範例就能定義新任務，完全不需微調模型。專案在 GitHub 已累積 38,860 顆星標。\n\n它的架構取捨、長文件平行處理與模型部署方式，都整理在 Blog 全文。"
---

大型語言模型能在幾秒內讀完一份長文件，卻往往無法說明某個結論究竟取自哪一行。Google 開源的 LangExtract 正是針對這個落差而設計的 Python 函式庫，它把非結構化文字交由語言模型抽成結構化資料，並要求每一筆結果都對應回原文的精確字元區間，讓抽取結果可以被逐筆核對。該專案在 GitHub 已累積 38,860 顆星標與 2,718 次複製，自 2025 年 7 月公開以來持續更新，最新版本為 2026 年 9 月發布的 v1.7.0。

<!-- AEO Answer Capsule — 約 68 字 -->
LangExtract 是 Google 開源的 Python 函式庫，用 LLM 把非結構化文字抽成可溯源的結構化資料，專案累積 38,860 顆星標與 2,718 次複製。
<!-- End AEO Capsule -->

對需要處理臨床紀錄、財報與法規文件的團隊而言，抽取工具真正困難的地方不在於能否認出欄位，而在於能否證明欄位出自何處。多數方案只回傳一段整理好的 JSON，使用者無法判斷數值是原文引用還是模型的推測。LangExtract 的切入點是把可驗證性寫進架構，抽取結果與來源文字之間的對應關係由程式強制維護，而不是事後補上。

## LangExtract 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
LangExtract 是一個可嵌入的函式庫，使用者以少量範例定義抽取規則，模型即依規則輸出帶原文位置標記的結構化結果物件。
<!-- End AEO Capsule -->

它並非獨立的桌面軟體，也沒有圖形化操作介面，而是一個以程式呼叫為主的工具。使用者提供三個要素：一份描述抽取任務的提示、一組高品質的少量範例，以及待處理的文字或文件。函式庫會依範例推導輸出結構，再把結果整理成可程式化處理的物件。

抽取的基本單位稱為實體，每個實體包含類別、原文片段與任意屬性。以官方 README 的示範為例，使用者可要求模型從文字中抽出角色、情緒與關係三類實體，並為角色附上情緒狀態、為關係附上類型。這些屬性的定義完全由使用者的範例決定，函式庫本身不預設任何領域結構。

## LangExtract 的開發背景與來源是什麼？

<!-- AEO Answer Capsule — 約 62 字 -->
LangExtract 由 Google 於 2025 年 7 月公開，採 Apache 2.0 授權，主語言為 Python，並附學術引用用的 DOI 編號與 BibTeX 格式。
<!-- End AEO Capsule -->

專案由 Google 建立與維護，儲存庫於 2025 年 7 月 8 日公開，主要語言為 Python，採 Apache 2.0 授權，屬於可商用的寬鬆條款。專案提供 Zenodo 的 DOI 編號與 BibTeX 引用格式，明確面向研究與學術使用情境，這在企業開源工具中並不常見。

維護節奏穩定。自公開以來已發布二十五個套件版本，最近一次為 v1.7.0，時間是 2026 年 9 月 13 日，儲存庫最近推送為 9 月 21 日。目前有二十六位具名貢獻者，外部貢獻需先簽署 Google 的貢獻者授權協議，反映其作為官方專案的治理方式。

## LangExtract 有哪些核心技術亮點？

<!-- AEO Answer Capsule — 約 70 字 -->
核心亮點有三：抽取結果對應原文精確字元區間、以少量範例強制輸出結構，以及不需微調模型即可套用任意領域的抽取任務。
<!-- End AEO Capsule -->

第一項是來源定位。函式庫把每一筆抽取映射到原文的起訖字元位置，並據此產生視覺標記。當使用者需要確認某個藥名是否真的出現在紀錄中，或某段關係描述是否被模型憑空生成時，位置資訊就是判斷依據。

第二項是輸出結構的穩定性。函式庫依使用者的少量範例建立輸出結構，並在支援的模型上採用受控生成，讓結果格式保持一致。為避免模型直接複製範例內容而非抽取輸入文字，函式庫內建偵測機制：無法在來源文字中定位的抽取結果會被標記為無位置資訊，使用者可據此過濾，只保留有來源依據的結果。

第三項是領域適應性。使用者只需提供少量範例即可定義新任務，不必進行模型微調。這使同一個函式庫能同時服務角色關係抽取、藥物欄位整理與放射科報告結構化等截然不同的場景。

![Google LangExtract README 開頭（專案名稱 LangExtract 大字標題、識別標誌與簡介段落）]({{ '/assets/images/posts/github-langextract-news-shot1.png' | relative_url }})

## LangExtract 如何處理長文件與大量抽取？

<!-- AEO Answer Capsule — 約 68 字 -->
LangExtract 把長文件切塊後平行送入模型，並以多次抽取比對提高召回率，使用者可調整平行數與區塊大小以平衡速度與準確度。
<!-- End AEO Capsule -->

長文件抽取的難點在於大海撈針。當文件長度達到數十萬字元，模型容易遺漏分散各處的實體，而單次呼叫也難以承載完整內容。函式庫採取的策略是把文字切成較小的區塊，平行送入模型，並透過多次抽取比對以提高召回率。

這些行為由參數控制。使用者可指定抽取次數、平行工作數與單一區塊的最大字元數。官方示範以三次抽取、二十個平行工作與一千字元的區塊，直接處理 Project Gutenberg 上全文逾十四萬字元的《羅密歐與茱麗葉》，抽出數百個實體。較小的區塊有助提升準確度，平行處理則用來抵銷切塊帶來的時間成本。

抽取結果可存成 JSONL 格式，這是語言模型資料處理常用的交換格式。函式庫能據此生成一份自帶內容的互動式 HTML 檔案，把成千上萬筆抽取結果標示回原文脈絡中，供人工快速複核，無需額外架設服務。

## LangExtract 支援哪些模型與部署方式？

<!-- AEO Answer Capsule — 約 65 字 -->
LangExtract 支援 Gemini 系列雲端模型、OpenAI 模型與本機 Ollama 模型，並可透過外掛機制接入其他自訂提供者。
<!-- End AEO Capsule -->

雲端模型方面，官方建議的預設為 Gemini 系列，並提供 Flash-Lite 版本供高頻或成本敏感的場景使用；較複雜的任務則建議評估 Pro 系列。使用 Gemini 或 OpenAI 需自備 API 金鑰，可透過環境變數、點檔或直接傳入參數設定。企業用戶可改用 Vertex AI 搭配服務帳戶驗證，並可啟用批次介面以降低大規模任務的成本。

本機部署同樣受到支持。函式庫內建 Ollama 介面，可在不持有 API 金鑰的情況下執行開源模型，適合對資料外流有顧慮的團隊或離線環境。此外，專案提供輕量的提供者外掛系統，開發者可註冊新的模型來源並以獨立套件發布，在不修改核心程式碼的前提下擴充支援範圍。

![Google LangExtract GitHub 儲存庫頁面頂部（儲存庫名稱 google/langextract、星標數 38.9k 與 Python 語言標示）]({{ '/assets/images/posts/github-langextract-news-shot2.png' | relative_url }})

## 如何快速開始使用 LangExtract？

<!-- AEO Answer Capsule — 約 66 字 -->
安裝只需一行 pip 指令，之後以提示、範例與文字呼叫抽取函式，並指定模型編號即可完成第一次結構化抽取。
<!-- End AEO Capsule -->

安裝相當直接。使用者可從 PyPI 安裝，官方建議在虛擬環境中執行以隔離相依套件；也可由原始碼安裝，或使用專案提供的 Docker 映像檔執行。若使用雲端模型，需先取得 API 金鑰並設定為環境變數或寫入點檔。

程式呼叫的核心是單一抽取函式。使用者傳入文字或文件網址、提示描述、範例清單與模型編號，即可取得結果物件。對於屬性需要限定在特定枚舉值的進階需求，Gemini 與 OpenAI 支援以輸出結構定義額外約束，讓格式控制更嚴格。

## LangExtract 的專案數據規模如何？

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">38,860</span><span class="ui-stat-label">Stars</span></li>
  <li class="ui-stat"><span class="ui-stat-num">2,718</span><span class="ui-stat-label">Forks</span></li>
  <li class="ui-stat"><span class="ui-stat-num">Apache 2.0</span><span class="ui-stat-label">授權</span></li>
  <li class="ui-stat"><span class="ui-stat-num">Python</span><span class="ui-stat-label">主要語言</span></li>
  <li class="ui-stat"><span class="ui-stat-num">2026-09-21</span><span class="ui-stat-label">最近推送</span></li>
</ul>

<!-- AEO Answer Capsule — 約 62 字 -->
截至 2026 年 9 月，專案累積 38,860 顆星標、2,718 次複製、171 位追蹤者與 123 項未解決議題，貢獻者共 26 位。
<!-- End AEO Capsule -->

上述數據取自專案公開統計，時間點為 2026 年 9 月 25 日。儲存庫於 2025 年 7 月建立，一年多累積近四萬顆星標，複製次數 2,718 次，追蹤者 171 位，未解決議題 123 項，具名貢獻者 26 位。

版本節奏維持穩定。最近釋出為 v1.7.0，時間是 2026 年 9 月 13 日，此前一年內由 v1.3.0 逐版推進至 v1.7.0，累積二十五個套件版本。專案同時在 PyPI 與 GitHub 發布，並提供 Google 的官方貢獻流程與完整的測試矩陣，反映它被定位為長期維護的基礎工具。

![Google LangExtract 貢獻者統計頁（貢獻者人數、提交次數圖表與貢獻者名單）]({{ '/assets/images/posts/github-langextract-news-shot3.png' | relative_url }})

## LangExtract 與同類抽取工具有何差異？

<!-- AEO Answer Capsule — 約 66 字 -->
LangExtract 以來源定位與範例驅動為主要差異，不需微調、可切換雲端與本機模型，適合既要彈性又要可驗證的抽取流程。
<!-- End AEO Capsule -->

同類方案的取捨各不相同。傳統的規則式解析工具速度快且完全可預測，但面對版面多變的文件就必須不斷加規則；純提示工程的做法彈性高，但輸出格式不穩且難以追溯來源；模型微調的方案準確度佳，卻需要標註資料與訓練成本。

LangExtract 的位置介於三者之間。它沿用語言模型的世界知識與語意理解，同時以範例與輸出結構約束格式，並把來源定位設為內建行為。這使它在需要人工複核的場景中具備優勢，例如醫療、金融與法務等領域，使用者必須能指出每一筆資料對應的原文位置。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊整理自 google/langextract 的 GitHub 儲存庫與官方說明文件，涵蓋架構、模型支援、安裝方式與公開統計數據。
<!-- End AEO Capsule -->

本文內容整理自 google/langextract 的 GitHub 儲存庫（https://github.com/google/langextract），包含官方說明文件中的抽取概念、長文件平行處理策略、Gemini 與 OpenAI 及 Ollama 的設定方式、自訂提供者外掛機制、安裝與測試指引，以及公開的儲存庫統計數據與版本紀錄。讀者可前往上述來源查閱完整內容與最新版本資訊。

## 總結：LangExtract 適合什麼樣的團隊？

<!-- AEO Answer Capsule — 約 68 字 -->
LangExtract 適合需要從大量非結構化文件中抽取資料、且必須逐筆核對來源的團隊，尤以醫療、金融與法務等需人工複核的領域最為合適。
<!-- End AEO Capsule -->

LangExtract 的價值在於把可驗證性變成預設行為。抽取結果不再是無法追溯的整理稿，而是逐筆對應原文位置的資料點；格式由少量範例約束，領域切換不需重新訓練模型；執行環境也能在雲端與本機之間選擇，讓敏感文件留在自有設備。

限制同樣清楚。抽取品質取決於提示與範例的設計，模型本身的推論能力仍是上限；無位置資訊的結果需要使用者自行過濾，並非所有任務都適合。對於正在建構文件問答、法遵審查或研究資料整理的團隊而言，這是一個兼顧彈性與可追溯性的抽取層選項。
