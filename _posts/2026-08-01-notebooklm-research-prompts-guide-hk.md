---
layout: post
title: "AI 文獻回顧指南：NotebookLM 8 個 Prompt 快速消化研究庫"
date: 2026-08-01 15:00:00 +0800
categories: 技術
tags: [NotebookLM, Gemini, AI 研究, 文獻回顧, Prompt, 學術, 人工智能, 科技教學, 香港, auto-publish, notebooklm]
image: /assets/images/posts/2026-08-01-notebooklm-research-cover.jpg
description: "寫論文、做研究，最頭痕就係文獻回顧：幾十篇 PDF 堆埋成座山，睇完都唔知睇咗啲咩。NotebookLM 將成個研究庫變成你嘅 AI 研究助理，8 個實戰 Prompt 幫你由文獻回顧、研究缺口、證據壓力測試到引用審計一氣呵成。由 IT 顧問親身實測，教你真正用盡 AI 做研究。"
author: "Sun ny"
---

# AI 文獻回顧指南：NotebookLM 8 個 Prompt 快速消化研究庫
> **「文獻回顧」四個字，係每個研究人嘅惡夢。**
>
> 幾十篇 PDF 下載咗、分類咗、然後…就冇然後。睇完 Abstract 已經攰，邊有心機逐篇逐篇做筆記？

我試過一次最誇張：為咗一個研究題目，download 咗成 40 幾篇論文，最後 deadline 前兩日先逼自己「速讀」— 結果寫出嚟嘅文獻回顧自己都唔敢睇返。

直到我認真用咗 **Google NotebookLM**（而家叫 Gemini Notebook）— 成個 workflow 唔同晒。**呢篇文我唔係教你理論，係直接俾你 8 個實戰 Prompt**，全部我親身試過、執過，照用就得。

---

## 首先：點解係 NotebookLM，而唔係普通 ChatGPT？

好多人問我：「AI 做研究，用 ChatGPT 咪得？」— 係得，但係有個致命問題：**佢會作嘢**（Hallucination）。你叫佢「總結呢篇文」，佢可能寫得好靚，但引述咗一篇根本唔存在嘅研究。

NotebookLM 唔同：
- **Grounded（有根有據）**：佢淨係答你上傳咗嘅 sources，唔會自己作資料出嚟
- **逐句有 Citation**：每個 claim 都有來源連結，㩒入去就睇到原文邊一段
- **支援長文件**：成篇論文 PDF 直接丟入去，佢幫你掘深層技術細節

簡單講：**佢係「研究助理」，唔係「作嘢機器」**。前提係你要識得叫佢做嘢 — 以下 8 個 Prompt 就係叫你做嘢嘅「咒語」。

---

## <svg class="ui-icon"><use href="#ui-robot"/></svg>8 個實戰 Prompt（照用就得）

> <svg class="ui-icon"><use href="#ui-newspaper"/></svg>**8 個 Prompts 一眼睇晒**（3D 筆記風格總結圖，我自己整嘅 ）：

![NotebookLM 8 個 Prompts（上半場 1-4）]({{ '/assets/images/posts/2026-08-01-notebooklm-prompts-1.png' | relative_url }})

### 1⃣ 零基礎文獻回顧生成器（Zero-Shot Literature Review）

**幾時用**：研究起步，乜都未睇，想快速知道個領域而家去到邊。

**Prompt（自己執過版）**：
> 分析我 notebook 入面所有已選取的來源，就著 [你的研究主題] 生成一份完整嘅文獻回顧。輸出請按以下結構：
> - 領域背景同目前整體狀態
> - 現有文獻嘅主要缺口同爭議
> - 唔同研究方法/觀點嘅主要優勢（用清單列出）
> - 關鍵發現同研究方法細節
> - 主要挑戰同未來研究方向

**實戰貼士**：出嚟之後，**第一件事唔係改文，係㩒啲 citation 去核實** — 睇下每個 claim 係咪真係嚟自你啲 sources。呢個動作會令你份文獻回顧可信度升一倍。

### 2⃣ 多來源論文摘要機（Multi-Source Summarizer）

**幾時用**：成堆 PDF 冇時間逐篇睇，想快速知道每篇講乜。

> 逐一檢視呢個 notebook 入面嘅每一份文件（包括長篇 PDF 同論文），為每份來源提供獨立摘要，內容要涵蓋：核心研究主題、使用嘅研究方法、關鍵結論。特別留意要從長篇文件嘅深處提取重要技術細節，唔好淨係睇 Abstract。

**實戰貼士**：呢個係我使用率最高嘅一個。重點係「**逐份獨立摘要**」— 唔好叫佢「綜合」，綜合咗就分唔到邊篇講乜。出嚟嘅摘要可以直接貼入你嘅筆記軟件做索引。

### 3⃣ 跨來源研究缺口偵測器（Gap & Opportunity Finder）

**幾時用**：文獻睇得七七八八，準備寫「研究缺口」嗰段，但唔知自己嘅研究有咩位可以企。

> 比較我 workspace 入面所有已上載嘅來源。辨識出：尚未被解答嘅問題、重複出現嘅方法學弱點、過時嘅假設、以及證據仍然有限嘅範疇。最後根據呢啲文章嘅具體例子，推薦 3 個最有前途嘅研究方向俾我。

**實戰貼士**：**「Research Gap」唔係你「覺得」有就係有，要 citation 支持**。呢個 Prompt 出嚟嘅缺口全部有原文依據，寫論文嗰陣你可以直接引用 — 審稿人最憎嗰啲「無中生有」嘅 gap statement。

### 4⃣ 概念拆解導師（Interactive Concept Breakdown）

**幾時用**：睇到一段好艱深嘅嘢，睇咗三次都唔明。

> 化身成一位專業導師。我而家 focus 喺呢段摘錄：[貼上你唔明嘅原文]。請用日常用語同貼地嘅比喻，將呢個概念拆解成簡單講法。最後解釋返呢個重點同我 notebook 入面其他文獻嘅整體發現有咩關連。

**實戰貼士**：呢個係「理解」層面嘅神器。重點係要佢**解釋同其他文獻嘅關連** — 咁你先會由「睇得明一段」升級到「睇得明成個領域點串連」。比喻記住抄低，寫論文 intro 嗰陣用返嚟解釋俾讀者聽，超好用。

### 5⃣ 證據壓力測試（Evidence Stress-Test）

> <svg class="ui-icon"><use href="#ui-newspaper"/></svg>**下半場 5-8**：

![NotebookLM 8 個 Prompts（下半場 5-8）]({{ '/assets/images/posts/2026-08-01-notebooklm-prompts-2.png' | relative_url }})

**幾時用**：你覺得自己嘅結論好穩陣？咁就要試下撼佢。

> 檢視我 workspace 所有來源嘅主要結論，然後由多個唔同角度挑戰佢哋：入面有咩隱藏假設？有咩邏輯漏洞？有咩證據係缺失嘅？最後將正反兩邊整合，得出一個經過壓力測試、有證據基礎嘅結論。

**實戰貼士**：**呢個係我最推薦研究生用嘅一個**。寫論文最怕嘅係 reviewer 一句「Your conclusion is not well-supported」— 用呢個 Prompt 提前自己撼自己，撼完執返靚，好過俾人撼完先嚟改。文科理科一樣啱用。

### 6⃣ 引用來源審計（Citation & Source Audit）

**幾時用**：要 check 自己啲 sources 邊啲信得過、邊啲係充數。

> 評估我 notebook 入面每一份來源嘅可信度同方法學嚴謹度，由最強到最弱排名，考慮因素包括證據嚴謹度同潛在偏見。對於每一個主要主張，標示出支持佢嘅原文段落；特別標記任何**主要靠背景引用（background citations）而唔係直接數據**支撐嘅主張。

**實戰貼士**：留意最後嗰句 — 「靠背景引用而唔係直接數據」嘅 claims 係文獻回顧入面最容易呃到人嘅嘢。**一篇文引用 50 次唔代表佢可信**，要睇佢啲關鍵 claim 係咪有自己嘅數據支持。出嚟嘅排名直接決定你邊啲 sources 要重點讀。

### 7⃣ Podcast 簡報腳本（Audio Briefing Script）

**幾時用**：要將研究講俾非專業人士聽（導師、屋企人、甚至係你自己用 Audio Overview 快速重溫）。

> 將我上載嘅文獻入面嘅核心辯論同主要 takeaways 整合成一份非技術性摘要。用清晰、對談式嘅語氣，集中對比唔同研究觀點嘅分別，將複雜科學簡化到一般大眾都聽得明。

**實戰貼士**：**NotebookLM 有個 Audio Overview 功能**，可以自動生成「兩個人傾偈」嘅 podcast 版摘要 — 通勤嗰陣聽，比自己睇快好多。而呢個 Prompt 就係教你控制佢「傾乜」— 冇 prompt 嘅 Audio Overview 會亂噏，有咗呢個佢會跟住你嘅框架講。

### 8⃣ 執行摘要 + 閱讀路線圖（Executive Research Brief）

**幾時用**：成個研究項目收尾，或者交報告前，將成個 workspace 濃縮做一頁紙。

> 將我成個研究 workspace 轉成一份結構化嘅執行摘要，包括：
> - 執行摘要（Executive Summary）
> - 核心概念同關鍵指標
> - 各方共識 vs 分歧
> - 實際應用場景
> - 建議嘅深入閱讀順序
> 請排版清晰，等我可以直接儲存到 NotebookLM 嘅筆記面板。

**實戰貼士**：最後嗰項「**優先閱讀順序**」好有用 — 如果你仲有 20 篇文未睇，跟住佢個次序讀，保證你先睇最重要嗰啲。deadline 前救命用。

---

## <svg class="ui-icon"><use href="#ui-download"/></svg>完整實戰 Workflow（由零開始）

跟住呢個次序做，成個研究流程會順好多：

1. **建立 Notebook** → 將所有 PDF/文獻丟入去（免費版每個 Notebook 有來源限制，Plan 好先上傳）
2. **Prompt 2**：逐份摘要 → 快速掌握每篇講乜
3. **Prompt 1**：生成文獻回顧初稿 → 知道個領域全貌
4. **Prompt 3**：搵研究缺口 → 定位自己嘅研究位置
5. **Prompt 6**：來源審計 → 知道邊啲文可信、邊啲要小心
6. **Prompt 5**：壓力測試自己嘅結論 → 提前執漏
7. **寫文嗰陣**：用 Prompt 4 理解深奧概念、用 Prompt 8 整理執行摘要
8. **交貨前**：用 Prompt 7 整返個 Audio Overview 快速重溫（順便 check 自己係咪真係明）

---

## <svg class="ui-icon"><use href="#ui-alert"/></svg>5 個常見錯誤（我親身踩過）

1. **唔㩒 Citation** — 淨係信 AI 總結，冇㩒入去原文核實。**AI 出嚟嘅嘢只係索引，唔係真理**。
2. **Sources 唔篩就丟入去** — 乜鬼都上傳，連啲 SEO 農場文章都入埋。**上傳前自己先篩一輪**，質素唔好嘅 source 會污染晒所有輸出。
3. **叫 AI「綜合」晒所有文** — 綜合完你根本分唔到邊篇講乜。**要獨立摘要就用獨立摘要**，要綜合先綜合。
4. **當佢係 Google** — 問啲 sources 入面冇嘅嘢，佢答唔到就開始「作」。**記得：問題一定要建基於你上傳嘅文獻**。
5. **直接交 AI 寫嘅嘢** — 學術誠信問題，唔使我解釋。**AI 係幫你消化同理解，唔係幫你代筆**。

---

## <svg class="ui-icon"><use href="#ui-question"/></svg>FAQ

**Q1：NotebookLM 免費嗎？**
免費版每個 Notebook 有 sources 數量限制（約 50 個來源），對大部分研究項目夠用。要更多容量/更高級功能就要 Google AI Pro / Plus 訂閱。我自己用免費版做咗成個研究項目都冇逼住要升級。

**Q2：支援中文文獻嗎？**
支援。NotebookLM 支援多語言，中文 PDF 一樣可以上傳同分析。不過英文學術文獻嘅處理質素始終係最成熟，如果兩邊都有，建議英文為主、中文輔助。

**Q3：同 ChatGPT / Claude 有咩分別？**
最大分別就係 **Grounded + Citation**。ChatGPT 係「乜都識啲」嘅百科全書，NotebookLM 係「淨係識你啲文獻」嘅專屬助理。做研究嚟講，後者嘅「唔識就話你知」反而係優點 — 佢唔會用一堆聽落好真但係假嘅引用呃你。

**Q4：做 Qualitative Research（質性研究）都用得著？**
用得著。訪談稿、田野筆記全部可以上傳，Prompt 5（壓力測試）同 Prompt 6（來源審計）對質性研究嘅資料分析一樣有用。唔好諗到佢淨係 for 理科。

**Q5：幾多篇文先值得用？**
三篇以上就值得。三篇以下自己睇仲快過 setup。

---

## <svg class="ui-icon"><use href="#ui-bulb"/></svg>總結

文獻回顧嘅痛苦，唔係因為你唔勤力，係因為你冇工具。**NotebookLM 將「睇 50 篇文」變成「問 8 條問題」** — 唔係叫你偷懶，係叫你將時間用喺真正重要嘅嘢：思考、質疑、同埋寫出你自己嘅觀點。

試下用第一個 Prompt 開始，你就會明我講乜。

> **「試過先講」** — 我唔會推介自己未用過嘅嘢。呢 8 個 Prompt 全部實測過，攞去用，唔使多謝我，記得㩒 Citation 就得 
