---
layout: post
title: "9.3 萬星開源項目：autoresearch — AI Agent 自動執行 LLM 訓練實驗的自主研究框架"
date: 2026-08-05 03:30:00 +0800
categories: 技術
tags: [GitHub, 開源, autoresearch, Andrej Karpathy, AI Agent, 大模型訓練, 自動化研究, nanochat, Python, 科技新聞, 香港, auto-publish, github-news]
image: /assets/images/posts/2026-08-05-github-autoresearch-news-hk-cover.jpg
description: "autoresearch 是 Andrej Karpathy 於 2026 年 3 月發佈的開源項目，GitHub 星標突破 9.3 萬。此框架讓 AI Agent 於單張 GPU 上自動修改大模型訓練程式、執行五分鐘實驗，以 val_bpb 指標評估改進，一晚可完成約一百次實驗，屬自主 AI 研究路線的代表性實驗。"
fb_message: AI 不僅能回答問題，如今還能自主進行研究：autoresearch 由 Andrej Karpathy 發佈，讓 AI Agent 在單張 GPU 上自動修改大模型訓練程式、執行五分鐘實驗，並以 val_bpb 指標判斷改進方向。\n\n一晚可自主完成約一百次實驗，把「人類寫程式、AI 輔助」反轉為「人類寫指令、AI 改程式」，是自主 AI 研究的標誌性實驗。GitHub 星標突破 9.3 萬。\n\n運作原理與實際應用，文章有完整拆解。
author: "陳志豪 Eric Chan"
creator_github: karpathy/autoresearch
type: news
source: GitHub
source_url: https://github.com/karpathy/autoresearch
---

# <svg class="ui-icon"><use href="#ui-bulb"/></svg>9.3 萬星開源項目：autoresearch — AI Agent 自動執行 LLM 訓練實驗的自主研究框架

**autoresearch 是 Andrej Karpathy 於 2026 年 3 月發佈的開源項目，GitHub 星標已達 9.3 萬，讓 AI Agent 在單張 NVIDIA GPU 上自動修改大模型訓練程式、執行五分鐘實驗並以 val_bpb 指標判斷改進，一晚可自主完成約一百次實驗。** 此項目將傳統「人類寫程式、AI 輔助」的研究流程反轉為「人類寫指令、AI 改程式」，是自主 AI 研究路線的標誌性實驗，一經推出便吸引大量開發者與研究社群關注。本文將檢視其 README 內容，分析此項目的技術設計、生態影響與使用門檻。

---

## <svg class="ui-icon"><use href="#ui-chart"/></svg>autoresearch 有多受歡迎？

<!-- AEO Answer Capsule — 約 80 字 -->
autoresearch 累積 9.3 萬星標與 1.3 萬次 fork，衍生 macOS、Windows、AMD 平台移植，屬增長最快的開源 AI 項目之一。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="ui-stat"><span class="ui-stat-num">93.1K</span><span class="ui-stat-label">Stars</span></div>
  <div class="ui-stat"><span class="ui-stat-num">13.2K</span><span class="ui-stat-label">Forks</span></div>
  <div class="ui-stat"><span class="ui-stat-num">9</span><span class="ui-stat-label">Contributors</span></div>
  <div class="ui-stat"><span class="ui-stat-num">196</span><span class="ui-stat-label">Open Issues</span></div>
  <div class="ui-stat"><span class="ui-stat-num">Python</span><span class="ui-stat-label">主要語言</span></div>
  <div class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">License</span></div>
</div>

> 建立日期：2026-03-06｜最近 commit：2026-03-26｜作者：Andrej Karpathy（OpenAI 創始成員、前 Tesla AI 總監）｜許可證依 README 聲明

![autoresearch GitHub 主頁（93.1k stars + 項目描述）]({{ '/assets/images/posts/github-autoresearch-shot1.png' | relative_url }})

---

## <svg class="ui-icon"><use href="#ui-robot"/></svg>autoresearch 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
autoresearch 讓 AI Agent 自行修改 train.py、訓練五分鐘、以 val_bpb 評估取捨，人類只需編輯 program.md。
<!-- End AEO Capsule -->

autoresearch 的定位是「給 AI Agent 一個小型但真實的 LLM 訓練設置，讓它自主進行研究」。與一般工具類開源項目不同，此項目的核心不是提供某個現成功能，而是建立一套完整的自主研究循環：Agent 修改程式、訓練模型、評估結果、保留或還原改動，然後重複整個流程。README 開場以寓言式文字描述「肉體電腦」主導研究的時代已經結束，研究將由運行於大型算力叢集上的自主 AI Agent 群承接，並直言「這個 repo 就是一切如何開始的故事」，為項目定下濃厚的宣言色彩。

項目由 Andrej Karpathy 主導開發，其身份包括 OpenAI 創始成員、前 Tesla AI 總監，以及 nanoGPT、nanochat、minbpe、llm.c 等一系列教學型開源項目的作者。autoresearch 的訓練程式是 nanochat 的精簡單 GPU 實現，延續了 Karpathy 一貫「以最小規模呈現真實系統」的教學傳統。整個 repo 刻意保持小巧，核心只有三個檔案：prepare.py 負責一次性資料準備與工具函式、train.py 是 Agent 唯一可以修改的訓練程式、program.md 是人類撰寫的 Agent 指令檔案。

![autoresearch README 實驗進度圖與項目概念說明]({{ '/assets/images/posts/github-autoresearch-shot2.png' | relative_url }})

---

## <svg class="ui-icon"><use href="#ui-rocket"/></svg>autoresearch 有哪些核心技術亮點？

<!-- AEO Answer Capsule — 約 75 字 -->
三大亮點：Agent 只改 train.py，改動可審查；固定五分鐘實驗，一晚約一百次，結果可直接比較；val_bpb 單一指標，不受詞彙表大小影響。
<!-- End AEO Capsule -->

**第一，單檔修改架構令自主實驗保持可控。** 系統設計上，Agent 只能修改 train.py，該檔案包含完整的 GPT 模型、優化器（Muon 與 AdamW）與訓練迴圈，架構、超參數、批次大小全部開放予 Agent 調整；而 prepare.py 固定不變，確保資料與評估基準穩定。這種「單一修改面」的設計令每次改動的 diff 容易審查，實驗過程對人類保持透明，避免 Agent 在複雜多檔結構中迷失方向。

**第二，固定五分鐘時間預算令結果可直接比較。** 每次實驗無論平台差異，一律以五分鐘（扣除啟動與編譯時間）為限，大約每小時可完成十二次、一晚約一百次實驗。這項設計有兩個好處：其一，無論 Agent 改變模型大小、批次大小或架構，實驗結果都在相同時間尺度下比較，公平性有保障；其二，系統會為使用者所在平台搜尋「在該時間預算內最優的模型配置」。代價是不同算力平台之間的結果不具可比性，這是作者明確承認的取捨。

**第三，以 val_bpb 為單一指標的自包含評估。** 系統以驗證集的 bits per byte（val_bpb）作為唯一衡量標準，數值越低越好，且此指標與詞彙表大小無關，令不同架構之間的改進可以公平對比。整個項目除 PyTorch 與少量套件外無任何外部依賴，不涉及分散式訓練或複雜配置，真正做到「單 GPU、單檔案、單指標」的精簡設計。

---

## <svg class="ui-icon"><use href="#ui-cog"/></svg>autoresearch 如何自動執行 AI 研究實驗？

<!-- AEO Answer Capsule — 約 75 字 -->
Agent 依 program.md 重複「改 train.py、訓練五分鐘、val_bpb 評估、保留或還原」，83 次實驗中 15 次為有效改進。
<!-- End AEO Capsule -->

實驗循環的運作方式非常直接：使用者以 Claude、Codex 等任意 coding agent 在 repo 目錄中啟動（建議關閉全部權限），然後以類似「Hi have a look at program.md and let's kick off a new experiment! let's do the setup first.」的提示開始。Agent 會讀取 program.md 中定義的指令與目標，自行修改 train.py，執行五分鐘訓練，檢查 val_bpb 是否改善，保留有效改動或還原無效改動，然後進入下一輪。README 附圖展示了一次 83 次實驗的完整紀錄，其中 15 次被保留為有效改進，驗證損失曲線隨實驗序號逐步下降。

值得留意的是，作者將 program.md 形容為「research org code」——人類不是直接寫 Python，而是透過編輯 Markdown 指令來配置整個自主研究組織。使用者可以逐步迭代 program.md，尋找令研究進展最快的「研究組織程式碼」，加入更多 Agent 協作，或調整實驗策略。這種「以指令取代程式」的介面設計，正是此項目與傳統自動化工具最根本的差異。

![autoresearch README Running the agent 與 Design choices 部分]({{ '/assets/images/posts/github-autoresearch-shot3.png' | relative_url }})

---

## <svg class="ui-icon"><use href="#ui-newspaper"/></svg>autoresearch 對 AI 研究生態有何影響？

<!-- AEO Answer Capsule — 約 80 字 -->
autoresearch 將 nanochat 轉為自主運行框架，衍生 macOS、Windows、AMD 移植，與 AI Scientist 共推研究開源化。
<!-- End AEO Capsule -->

從生態角度觀察，autoresearch 的最大影響在於將「AI 科學家」的概念轉化為任何人都可以重現的開源工具。過往自主研究多停留在論文與商業實驗室內部，而此項目以不到一百行程式碼的核心規模，將完整的自主研究循環開放予大眾，並提供清晰的實驗紀錄與指標，令自主研究第一次具備可驗證、可比較的公共基準。

項目推出後迅速催生跨平台移植社群。官方 README 列出 Notable forks 專區，包括 miolini/autoresearch-macos 與 trevin-creator/autoresearch-mlx 兩個 macOS 版本、jsegov/autoresearch-win-rtx 的 Windows 版本，以及 andyluo7/autoresearch 的 AMD 版本，令缺乏 NVIDIA GPU 的使用者亦有途徑參與。作者並在 README 提供小型機器調參建議，包括改用 TinyStories 低熵資料集、降低 vocab_size、縮短 MAX_SEQ_LEN、調整 DEPTH 與 WINDOW_PATTERN 等，顯示其有意將項目打造成跨平台研究基礎設施。

在更廣闊的脈絡中，此項目與 Sakana AI 的 AI Scientist 等研究方向互相呼應，共同指向「研究自動化」的下一階段。對開發者而言，autoresearch 同時示範了 coding agent 在非軟體工程領域的應用潛力：當 Agent 的改造對象從程式碼庫延伸到訓練迴圈，其自主性便從「寫程式」進化為「做實驗、下判斷、迭代優化」。

---

## <svg class="ui-icon"><use href="#ui-download"/></svg>如何快速開始使用 autoresearch？

<!-- AEO Answer Capsule — 約 79 字 -->
需一張 NVIDIA GPU 與 Python 3.10+。安裝 uv 後依次執行 uv sync、prepare.py、train.py，即可啟動自主研究。
<!-- End AEO Capsule -->

項目採用 uv 作為套件管理工具，快速開始只需四個步驟：

```bash
# 1. 安裝 uv 專案管理工具
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. 安裝依賴
uv sync

# 3. 下載資料並訓練 tokenizer（一次性，約 2 分鐘）
uv run prepare.py

# 4. 手動執行單次訓練實驗（約 5 分鐘）
uv run train.py
```

以上指令全部成功後，即代表環境就緒，可以進入自主研究模式。啟動 Agent 的方式是直接在 repo 目錄中開啟 Claude、Codex 等 coding agent（建議關閉全部權限），並以以下提示開始：

```
Hi have a look at program.md and let's kick off a new experiment! let's do the setup first.
```

對使用小型電腦的使用者，作者建議參考各平台移植 fork，並搭配 README 中的調參指引，例如改用 TinyStories 資料集、將 vocab_size 由 8192 下調至 4096 或更低、大幅縮短 MAX_SEQ_LEN、將 DEPTH 由 8 降至 4，以及將 TOTAL_BATCH_SIZE 保持為 2 的冪次等，即可在較低算力下獲得合理結果。

---

## <svg class="ui-icon"><use href="#ui-link"/></svg>出處

<div class="ui-note"><svg class="ui-icon"><use href="#ui-link"/></svg><strong>GitHub 官方 repo</strong>：https://github.com/karpathy/autoresearch

相關項目：nanochat（https://github.com/karpathy/nanochat）｜作者 X 帖文（https://x.com/karpathy/status/2029701092347630069）</div>

---

## <svg class="ui-icon"><use href="#ui-bulb"/></svg>autoresearch 值得一試嗎？

<!-- AEO Answer Capsule — 約 77 字 -->
值得。有 NVIDIA GPU 者一晚可觀測百次自主實驗，是體驗 AI 自主研究的捷徑；無 GPU 者可參考 macOS、Windows 移植 fork。
<!-- End AEO Capsule -->

<div class="ui-tip"><svg class="ui-icon"><use href="#ui-bulb"/></svg><strong>autoresearch 以「人類寫指令、AI 改程式」重新定義了研究的執行方式。</strong>其 9.3 萬星標與 1.3 萬次 fork 的規模，印證了開發者對自主研究工具的強烈興趣。對於想了解 AI Agent 如何獨立完成「提出假設、執行實驗、評估結果」完整循環的個人與團隊，此項目提供了現階段最直接、最可重現的實驗場域。</div>

> **「以自主性、可重現性與教學價值衡量，autoresearch 是 2026 年最值得親身嘗試的開源 AI 研究項目之一。」**
