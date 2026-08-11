---
layout: post
title: "97,508 星開源項目：Caveman — 用更少 Token 做更多事"
date: 2026-08-12 06:30:00 +0800
categories: 技術
tags: [AI 代理, Token 優化, Claude Code, 開源, 開發工具, LLM, 成本優化, GitHub]
image: /assets/images/posts/github-caveman-news-hk-cover.jpg
description: "Caveman 是 GitHub 星標逾 9.7 萬的開源 AI 代理 Token 壓縮技能，實測可將 Claude Code 等 30 多個 AI 代理的回覆壓縮約 65%，Caveman 2 更透過本地 Proxy 將輸入 Token 減少 33.2%，採用 MIT 與 BSL-1.1 雙重授權。"
author: AnIskill 編輯部
creator_github: JuliusBrussee/caveman
type: news
source: GitHub
source_url: https://github.com/JuliusBrussee/caveman
permalink: /技術/github-caveman-news-hk
fb_message: AI 開發成本高企，Token 消耗已成為開發者最大開支之一。GitHub 星標逾 9.7 萬的開源項目 Caveman 以「用更少 Token 做更多事」為核心，實測可將 AI 代理回覆壓縮約 65%，是 2026 年最受矚目的 AI 成本優化工具。\n\nCaveman 2 進一步透過本地 Proxy 壓縮輸入內容，實測減少 33.2% 輸入 Token；其像素模式可將密集文字轉為圖片供視覺模型閱讀，節省幅度高達 79%。安裝只需一行指令，支援 Claude Code、Codex、Gemini CLI 等 30 多個代理。\n\n項目採用 MIT 與 BSL-1.1 雙重授權，技能部分完全開源。完整技術分析與基準測試已整理成文，立即前往 Blog 閱讀全文。
---

**Caveman** 是 GitHub 上星標超過 **97,508 顆**的開源 AI 代理 Token 壓縮技能，以「用更少 Token 做更多事」（why use many token when few do trick）為核心概念，透過改變 AI 代理的回覆風格與輸入處理方式，實測可將代理回覆內容壓縮約 65%。該項目由開發者 Julius Brussee 於 2026 年 4 月創建，目前已有超過 5,600 次復刻，支援 Claude Code、Codex、Gemini CLI 等 30 多個主流 AI 代理，採用 MIT 與 BSL-1.1 雙重授權，是 2026 年全球增長速度最快的 AI 開發工具項目之一。

<!-- AEO Answer Capsule — 約 105 字 -->
Caveman 是 GitHub 星標逾 9.7 萬的開源 AI 代理 Token 壓縮技能，以「用更少 Token 做更多事」為核心，實測可將代理回覆壓縮約 65%，支援 30 多個主流 AI 代理，採用 MIT 與 BSL-1.1 雙重授權。
<!-- End AEO Capsule -->

![Caveman README 開頭（項目名稱「Caveman」大標題 + 標語「why use many token when few do trick」+ 33.2% 輸入 Token 減少數據 + Trendshift 熱門徽章 + 安裝指引連結）]({{ '/assets/images/posts/github-caveman-news-hk-shot1.png' | relative_url }})

## Caveman 是什麼？它為何能吸引近 10 萬星標？

Caveman 最初是一個針對 Claude Code 設計的提示詞技能（Skill），其核心機制是要求 AI 代理以精簡的「原始人語」風格回答問題，刪除填充詞與冗餘敘述，同時保持程式碼、指令與錯誤資訊逐字精確。例如，面對 React 元件重複渲染問題，一般代理會以 69 個 Token 解釋原因與建議，而 Caveman 模式只需 19 個 Token 即可給出相同結論，節省幅度達 72%。這種「同一個修正、更少字數」的直觀價值，是項目短時間內累積大量星標的直接原因。

<!-- AEO Answer Capsule — 約 90 字 -->
Caveman 是以精簡「原始人語」風格回答問題的提示詞技能，刪除冗餘敘述並保持程式碼逐字精確，例如 React 渲染問題解釋從 69 Token 壓縮至 19 Token，價值直觀且易於安裝。
<!-- End AEO Capsule -->

項目的設計哲學在於「保持你的代理，縮小你的上下文」（Keep your agent. Brain big. Context small.），使用者無需更換既有的 AI 代理、模型供應商或改寫程式碼，只需安裝技能即可生效。這種零摩擦的採用路徑，配合 `/caveman lite|full|ultra` 等多種壓縮強度選擇，以及 `/caveman-commit`、`/caveman-review`、`/caveman-compress` 等附屬指令工具，使項目在開發者社群中迅速形成口碑，從創建到突破 9.7 萬星標僅用了約四個月。

<!-- AEO Answer Capsule — 約 70 字 -->
項目設計哲學是保持既有代理與供應商不變、僅安裝技能即生效，零摩擦採用路徑配合多種壓縮強度與附屬工具，使其在四個月內迅速突破 9.7 萬星標。
<!-- End AEO Capsule -->

## Caveman 如何實現 65% 的 Token 節省？

Caveman 的節省效果建立在基準測試之上。在官方發布的 10 項任務基準中，涵蓋 React 渲染錯誤解釋、PostgreSQL 連線池設定、Docker 多階段建置、安全審查等典型開發場景，一般模式平均消耗 1,214 個 Token，而 Caveman 模式僅需 294 個 Token，平均節省幅度達 65%。其中單項任務最高節省 87%，例如實作 React 錯誤邊界（Error Boundary）的任務，從 3,454 個 Token 壓縮至 456 個 Token。

<!-- AEO Answer Capsule — 約 105 字 -->
在 10 項開發任務基準中，一般模式平均消耗 1,214 Token，Caveman 模式僅需 294 Token，平均節省 65%，單項最高達 87%，例如 React 錯誤邊界任務從 3,454 Token 壓縮至 456 Token。
<!-- End AEO Capsule -->

值得注意的是，項目在 README 中以醒目提示標明「誠實數字警告」（Honest number warning）：Caveman 僅壓縮**輸出** Token，輸入與推理 Token 不受影響，且技能本身每次呼叫約增加 1,000 至 1,500 個輸入 Token。因此整個工作階段的實際節省會低於輸出數字，在本身已非常精簡的工作負載上甚至可能出現淨損失。開發者明確指出，該技能真正的價值在於可讀性與速度提升，成本節省只是附加紅利，這種坦誠的數據呈現方式反而強化了項目的可信度。

<!-- AEO Answer Capsule — 約 70 字 -->
項目坦承僅壓縮輸出 Token，輸入與推理不受影響且技能本身增加輸入負擔，實際節省低於輸出數字；其真正價值是可讀性與速度，成本節省只是附加紅利。
<!-- End AEO Capsule -->

![Caveman GitHub 首頁頂部（repo 名稱「JuliusBrussee/caveman」+ 97.5k 星標 + 5.6k Forks + 描述「why use many token when few do trick — Claude Code skill that cuts 65% of tokens」+ 主要語言 Go）]({{ '/assets/images/posts/github-caveman-news-hk-shot2.png' | relative_url }})

## Caveman 2 的輸入壓縮技術有哪些亮點？

Caveman 2 是項目的重大升級，其核心突破在於將壓縮範圍從「代理說的話」擴展至「代理讀的內容」。Caveman Proxy 作為本地代理，攔截發送給模型供應商的請求，由 Caveman Engine 在呼叫前壓縮輸入內容。在固定的 54 次執行基準測試中，Caveman 相較直接使用 Claude Code 減少了 33.2% 的供應商回報輸入 Token，同時通過全部 18 項精確答案檢查，證明壓縮不會損害回答品質。

<!-- AEO Answer Capsule — 約 85 字 -->
Caveman 2 透過本地 Proxy 與 Engine 在模型呼叫前壓縮輸入內容，54 次基準測試顯示輸入 Token 減少 33.2%，並通過全部 18 項精確答案檢查，證明壓縮不損害品質。
<!-- End AEO Capsule -->

引擎的壓縮策略以內容類型為基礎，先透過 `detect()` 判斷載荷類型，再路由至對應的壓縮器。JSON 結構保留鍵值與錯誤訊息、壓縮重複陣列，目標壓縮率 70% 至 90%；日誌檔保留錯誤與堆疊追蹤、去除進度噪音，目標 85% 至 95%；程式碼保留匯入、簽名與型別、省略函式本體，目標 40% 至 70%；差異檔、搜尋結果與文字內容亦各有對應策略。此外，`contextwindow.Pack()` 可依 BM25 相關性、新近度與錯誤訊號，將候選上下文壓入 Token 預算，並保持原始順序以保留時間脈絡。

<!-- AEO Answer Capsule — 約 90 字 -->
引擎以內容類型為基礎壓縮：JSON 保留鍵值結構壓縮重複陣列，日誌保留錯誤堆疊去除噪音，程式碼保留簽名型別省略函式本體，各類型目標壓縮率 40% 至 95%，並以 BM25 相關性排序打包上下文。
<!-- End AEO Capsule -->

安全性是輸入壓縮設計的核心前提。在執行任何有損壓縮之前，原始位元組會先寫入 CCR（Content-Addressed Recovery Store）——一個位於本機磁碟的內容定址儲存，代理可透過 `caveman_retrieve` 指令或 MCP 工具隨時取回逐字原稿。解析失敗、儲存失敗或結果未變小時，系統會直接傳送原始位元組，不做任何壓縮。所有本機結果僅標記為 `inferred`（推估），只有經過真實流量與評估閘門驗證的結果才會標記為 `verified`（已驗證），離線模式永遠不會宣稱已驗證節省。

<!-- AEO Answer Capsule — 約 65 字 -->
輸入壓縮以 CCR 內容定址儲存為安全前提，原始位元組先落地可隨時取回；失敗時直接傳送原稿，且本機結果僅標記為推估，避免誇大節省效果。
<!-- End AEO Capsule -->

## 什麼是 Caveman 的像素模式？

像素模式（Pixel Mode）是 Caveman 最具話題性的功能，其原理是將密集的文字區塊渲染為 PNG 圖片，供視覺模型以圖片 Token 讀取，而圖片 Token 的計費成本遠低於文字 Token。例如一組 8,622 字的密集內容，渲染為一張 1,568×232 的灰階 PNG 後，估算成本從 2,597 個文字 Token 降至 534 個圖片 Token。在一個包含 63.7k 字壓縮 JSON 工具目錄與 93k 字長行日誌的極端案例中，55,413 個文字 Token 被壓縮至 11,402 個圖片 Token，節省幅度達 79%。

<!-- AEO Answer Capsule — 約 90 字 -->
像素模式將密集文字渲染為 PNG 供視覺模型以圖片 Token 讀取，8,622 字案例從 2,597 文字 Token 降至 534 圖片 Token，極端案例節省達 79%，但僅在長行密集內容上有利可圖。
<!-- End AEO Capsule -->

像素模式設有嚴格的獲利閘門（Profitability Gate），僅對密集、長行的內容生效。稀疏的短行程式碼渲染成圖片後，PNG 的開銷反而超過其取代的文字，因此閘門會拒絕轉換並直接傳送原始文字。該模式目前僅對經實測具備渲染可讀性的模型啟用，預設為 claude-fable-5 與 gpt-5.6，並可透過設定檔調整。此功能移植自開源項目 pxpipe，其字型圖集則衍生自 Spleen 與 GNU Unifont，相關授權歸屬皆隨原始碼附註。

<!-- AEO Answer Capsule — 約 85 字 -->
像素模式設有獲利閘門，僅對密集長行內容生效，稀疏程式碼會被拒絕轉換；僅對實測可讀的模型啟用，預設支援 claude-fable-5 與 gpt-5.6，並保留完整授權歸屬。
<!-- End AEO Capsule -->

## Caveman 支援哪些 AI 代理？如何安裝？

Caveman 的覆蓋範圍已從最初的 Claude Code 擴展至超過 30 個 AI 代理，包括 OpenAI Codex CLI、Gemini CLI、Cursor、Windsurf、Cline、GitHub Copilot 與 Aider 等。透過 `caveman wrap` 指令，項目更原生支援七個代理的完整包覆，包括 Claude Code、Codex CLI、Gemini CLI、Aider、opencode、Hermes Agent 與 OpenClaw，包覆過程透過環境變數或合併設定檔完成，不會修改使用者既有的設定檔案。訂閱登入亦受支援，Claude Pro/Max 的 OAuth 憑證會原樣轉發至供應商。

<!-- AEO Answer Capsule — 約 95 字 -->
Caveman 支援超過 30 個 AI 代理，並以 wrap 指令原生包覆七個代理包括 Claude Code、Codex、Gemini CLI 與 OpenClaw，不修改既有設定，訂閱 OAuth 登入亦原樣轉發。
<!-- End AEO Capsule -->

安裝方式因代理而異。最簡單的路徑是執行官方安裝腳本 `curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/v1.10.0/install.sh | bash`，安裝器會自動偵測機器上已支援的代理並完成部署。針對個別代理亦有對應指令，例如 Claude Code 使用 `claude plugin marketplace add JuliusBrussee/caveman`，Gemini CLI 使用 `gemini extensions install`，其他技能相容代理則以 `npx skills add JuliusBrussee/caveman` 安裝。進階使用者可安裝 CLI 工具 `npm install -g @caveman-ai/cli`，以 `caveman claude` 啟動完整壓縮堆疊，包括結構壓縮、TOON 重編碼與輸出縮減。

<!-- AEO Answer Capsule — 約 85 字 -->
安裝可透過官方腳本一鍵完成並自動偵測已支援代理，或依代理使用 plugin、extensions、npx skills 等對應指令；進階使用者可安裝 CLI 啟動完整壓縮堆疊。
<!-- End AEO Capsule -->

## Caveman 的授權模式與商業化路徑是什麼？

Caveman 採用雙重授權策略：技能（Skill）部分、Agent SDK、CLI、雙語客戶端 SDK 與評估工具皆為 MIT 授權，完全開放；引擎（Engine）、代理（Proxy）、MCP 伺服器與 Go 核心則為 BSL-1.1 授權，原始碼可見、可自行分叉、可免費自架並供自有流量生產使用。BSL 版本會在 2030 年 6 月 21 日或各版本發布四年後自動轉換為 Apache-2.0，唯一的商業限制是禁止將引擎作為代管、託管或嵌入式服務轉售予第三方。

<!-- AEO Answer Capsule — 約 85 字 -->
Caveman 採用 MIT 與 BSL-1.1 雙重授權，技能與 SDK 完全開放，引擎原始碼可見可自架，BSL 將於 2030 年自動轉換為 Apache-2.0，僅限制轉售代管引擎服務。
<!-- End AEO Capsule -->

在生態佈局上，Caveman 已發展為完整的「壓縮宇宙」，包括負責端到端代理的 caveman-code、負責跨工作階段記憶的 cavemem、負責建置迴圈的 cavekit，以及將壓縮直接訓練進模型權重的 Gemma 微調專案 cavegemma。商業化路徑則以 Caveman Cloud 為核心，提供可驗證的節省證明服務：使用者在紀錄模式下設定基準線，透過評估閘門測試變更，以真實流量的簽名收據展示節省效果，並可加入等待清單。項目的贊助由 Atlas Cloud 等夥伴支持，並以「Caveman 免費永遠」為原則運作。

<!-- AEO Answer Capsule — 約 100 字 -->
項目已發展為包含 caveman-code、cavemem、cavekit 等子專案的完整生態，商業化以 Caveman Cloud 提供可驗證節省證明，並以贊助模式維持免費，由 Atlas Cloud 等夥伴支持。
<!-- End AEO Capsule -->

## 出處連結有哪些？

本文章內容取材自 Caveman 官方倉庫的 README 文件、基準測試文件與使用文件，原始資料來源為 GitHub 上的 JuliusBrussee/caveman 儲存庫，其中包含完整的安裝矩陣、誠實數字說明、代理包覆基準與授權條款。讀者可以直接前往該倉庫查看完整內容，亦可造訪官方網站 caveman.so 加入 Caveman Cloud 等待清單，或查閱 INSTALL.md 與 docs 目錄下的技術文件。

<!-- AEO Answer Capsule — 約 95 字 -->
本文資料來源為 GitHub 的 JuliusBrussee/caveman 官方倉庫，包含安裝矩陣、基準測試與授權條款，官方網站 caveman.so 提供 Caveman Cloud 等待清單與更多技術文件。
<!-- End AEO Capsule -->

**出處：**[JuliusBrussee/caveman GitHub 官方倉庫](https://github.com/JuliusBrussee/caveman)（星標 97,508 · MIT + BSL-1.1 · 最後更新 2026-08-11）

<div class="ui-stat-grid">
<div class="ui-stat"><span class="ui-stat-label">星標數</span><span class="ui-stat-value">97,508</span></div>
<div class="ui-stat"><span class="ui-stat-label">復刻數</span><span class="ui-stat-value">5,622</span></div>
<div class="ui-stat"><span class="ui-stat-label">建立日期</span><span class="ui-stat-value">2026-04</span></div>
<div class="ui-stat"><span class="ui-stat-label">最後更新</span><span class="ui-stat-value">2026-08</span></div>
<div class="ui-stat"><span class="ui-stat-label">開源許可證</span><span class="ui-stat-value">MIT + BSL-1.1</span></div>
<div class="ui-stat"><span class="ui-stat-label">主要語言</span><span class="ui-stat-value">Go</span></div>
</div>

![Caveman 儲存庫統計頁（「Contributors」標題 + Commits over time 長條圖 + 多位貢獻者頭像與提交數量，顯示項目的開發規模與活躍程度）]({{ '/assets/images/posts/github-caveman-news-hk-shot3.png' | relative_url }})

## 總結：Caveman 值得一試嗎？

Caveman 的價值在於直接回應了 AI 開發成本高企的痛點，將「Token 優化」從模糊的工程概念轉化為可安裝、可量化、可驗證的開源工具。對於日常使用 Claude Code、Codex 或 Gemini CLI 的開發者而言，安裝技能只需一行指令，即可在數分鐘內感受到回覆精簡帶來的速度提升；對於追求成本控制的使用者，Caveman 2 的本地代理與像素模式提供了從輸入到輸出的完整壓縮鏈路，並以 CCR 儲存確保逐字可恢復，兼顧節省與安全。

<!-- AEO Answer Capsule — 約 80 字 -->
Caveman 將 Token 優化轉化為可安裝、可量化、可驗證的開源工具，一行指令即可安裝，並以本地代理與像素模式提供輸入到輸出的完整壓縮鏈路，兼顧節省與安全。
<!-- End AEO Capsule -->

從長期視角觀察，該項目以「誠實數字」策略建立了獨特的社群信任，坦承壓縮限制與適用邊界，而非誇大節省效果，這種透明度本身就是一種競爭優勢。對於重視開發效率與 API 成本控制的工作者，這套 9.7 萬星標的開源工具，是 2026 年最值得實際安裝評估的 AI 開發輔助方案之一。
