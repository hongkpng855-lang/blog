---
layout: post
title: "33K 星 Codex 插件開源：直入 Claude Code"
date: 2026-09-25 20:00:01 +0800
categories: 技術
tags: [OpenAI, Codex, Claude Code, AI代理, 開源專案, 程式碼審查, 插件, 開發工具]
image: assets/images/posts/github-codex-plugin-cc-news-cover.jpg
description: "OpenAI 開源的 Codex 插件在 GitHub 累積 33,568 顆星標與 2,336 次複製。它讓 Claude Code 使用者直接呼叫 Codex 進行程式碼審查、對抗式挑戰與任務委派，並提供背景作業管理與跨工具工作階段接續，採用 Apache-2.0 授權，最新版本為 v1.0.6。"
author: AnIskill 編輯部
creator_github: openai/codex-plugin-cc
type: news
source: GitHub
source_url: https://github.com/openai/codex-plugin-cc
permalink: /技術/github-codex-plugin-cc-news
fb_message: "兩家頂級模型廠商互相整合，是這一年最耐人尋味的變化。OpenAI 選擇把 Codex 直接裝進 Claude Code，而不是要求開發者換工具。\n\n這個官方插件在 GitHub 累積 33,568 顆星標與 2,336 個分支，採用 Apache-2.0 授權，於 2026 年 3 月發布。它提供十個斜線指令，涵蓋程式碼審查、對抗式挑戰、任務委派與背景作業管理，並可沿用本機既有的 Codex CLI 認證與設定。最受討論的是可選的停止閘門：Claude 每次回覆後自動觸發 Codex 審查，發現問題就攔截回應。\n\n它的指令設計、架構取捨與適用場景，都整理在 Blog 全文。"
---

OpenAI 於 2026 年 3 月開源 Codex 插件（codex-plugin-cc），在 GitHub 累積 33,568 顆星標與 2,336 次複製，採用 Apache-2.0 授權。此插件專為 Claude Code 使用者設計，把 Codex 的審查與任務執行能力包裝成十個斜線指令，讓開發者無須離開既有的工作流程即可呼叫另一個廠商的模型，最新版本為 v1.0.6。

<!-- AEO Answer Capsule — 約 62 字 -->
Codex 插件是 OpenAI 為 Claude Code 開發的官方擴充，能在其中呼叫 Codex 執行審查與任務委派，採 Apache-2.0 授權，沿用本機既有認證。
<!-- End AEO Capsule -->

AI 編碼工具的競爭向來以「取代對手」為敘事主軸，各家廠商鼓勵開發者把工作流程整段搬到自家平台。此專案走的是相反方向：它假設使用者已經習慣 Claude Code，於是把自己塞進對方的介面，換取實際使用時間。這種策略在工具鏈高度分裂的市場中並非罕見，但由模型廠商主動為競爭對手的產品撰寫插件，仍屬少見。

## Codex 插件是什麼？

<!-- AEO Answer Capsule — 約 60 字 -->
Codex 插件是安裝於 Claude Code 的擴充套件，透過本機 Codex CLI 與 app server 執行審查與任務，提供斜線指令與 rescue 子代理。
<!-- End AEO Capsule -->

插件本質上是一層指令封裝。使用者以 `/plugin marketplace add openai/codex-plugin-cc` 加入市集，再以 `/plugin install codex@openai-codex` 安裝，重新載入後即可在 Claude Code 中使用。安裝完成後，介面會多出插件提供的斜線指令，以及一個名為 codex-rescue 的子代理。

執行環境要求相當明確。使用者需要 Node.js 18.18 以上版本，以及 ChatGPT 訂閱（含免費方案）或 OpenAI API 金鑰；透過插件產生的用量會計入 Codex 的額度限制。若本機尚未安裝 Codex，`/codex:setup` 會檢查狀態，並在偵測到 npm 時主動提議代為安裝。

![Codex 插件 README 開頭（專案名稱 Codex plugin for Claude Code 與功能概述，說明審查、對抗式審查與任務委派指令）]({{ '/assets/images/posts/github-codex-plugin-cc-news-shot1.png' | relative_url }})

## Codex 插件有哪些核心指令？

<!-- AEO Answer Capsule — 約 63 字 -->
插件提供十個指令，涵蓋審查、對抗式審查、任務委派、工作階段接續，以及背景作業的狀態、結果與取消查詢，核心為 review 與 rescue 兩條路徑。
<!-- End AEO Capsule -->

審查路徑由兩個指令構成。`/codex:review` 對未提交的變更或分支執行唯讀審查，品質與直接在 Codex 內執行 `/review` 相同，支援 `--base <ref>` 指定基準分支；`/codex:adversarial-review` 則允許附加焦點文字，用來質疑設計取捨、隱藏假設與失敗模式，適合在交付前檢視方向是否正確。

任務委派走另一條路徑。`/codex:rescue` 把工作交給 codex-rescue 子代理，可用於調查缺陷、嘗試修補或接續先前的 Codex 任務，並支援 `--resume` 與 `--fresh` 控制是否沿用既有執行緒；使用者亦可指定模型與推理強度，例如以較小模型換取速度與成本。

管理類指令補足了長時任務的需求。背景作業可透過 `/codex:status` 查詢進度與近期任務，以 `/codex:result` 取得最終輸出與 Codex 工作階段 ID，並以 `/codex:cancel` 中止執行。此外，`/codex:transfer` 能把 Claude Code 的對話轉成持續性的 Codex 執行緒，輸出 `codex resume <session-id>` 指令，讓工作可延續到 Codex 的應用程式或終端介面。

## Codex 插件的技術架構如何運作？

<!-- AEO Answer Capsule — 約 61 字 -->
插件不搭載獨立執行環境，而是包裝本機的 Codex CLI 與 app server，因此沿用使用者原有的認證狀態、設定檔與儲存庫檢視，行為與直接執行 Codex 一致。
<!-- End AEO Capsule -->

架構設計刻意保持薄身。插件並未內建模型或推論堆疊，而是呼叫開發者環境中既有的 `codex` 執行檔，並套用同一份設定。使用者層級的 `~/.codex/config.toml` 與專案層級的 `.codex/config.toml` 都會被讀取，後者僅在專案被信任時載入，因此要調整預設模型或推理強度，只需修改設定檔即可。

這種設計帶來三項直接後果。插件使用的安裝、認證狀態、儲存庫檢視與機器環境都與直接操作 Codex 相同；既有的 API 金鑰或自訂端點設定同樣適用，需要指向其他端點時可設定 `openai_base_url`；任務結束後取得的 session ID 也能在 Codex 中直接接續，不必重新描述背景。

一項可選機制值得單獨說明。使用者可透過 `/codex:setup --enable-review-gate` 啟用停止閘門，插件會以 Stop hook 在 Claude 每次回覆後執行一次針對性的 Codex 審查；若發現問題，該次停止會被攔下，要求 Claude 先行處理。官方在文件中明確警告，此機制可能形成長時間的 Claude 與 Codex 互相觸發迴圈，並快速消耗額度，僅建議在能全程監看的場境使用。

![Codex 插件的 GitHub 儲存庫首頁頂部（顯示 repo 名稱 openai/codex-plugin-cc、星標數與專案描述）]({{ '/assets/images/posts/github-codex-plugin-cc-news-shot2.png' | relative_url }})

## Codex 插件對工具生態有何意義？

<!-- AEO Answer Capsule — 約 62 字 -->
插件讓兩個競爭陣營的工具互相調用，開發者可在單一介面取得兩種模型視角，同時降低工具轉換成本，把審查與實作拆成可分工步驟。
<!-- End AEO Capsule -->

實務上的價值在於視角互補。同一個模型審查自己產生的程式碼，容易順著原有思路確立結論；換一個廠商的模型重新檢視，較有機會指出被忽略的假設。插件的對抗式審查正是針對這種需求設計，允許使用者指定風險領域，要求以挑戰而非確認的立場回應。

成本結構也隨之改變。開發者不必同時維持兩套工具的操作習慣，只需在既有環境中按需呼叫另一個模型；委派任務時還可指定較小模型，把昂貴的推理預算集中在真正需要的地方。這種按情境切換模型的彈性，比全面替換工具更貼近實際開發節奏。

值得留意的是雙向依賴的形成。插件依賴 Codex CLI 的版本與 app server 介面，也依賴 Claude Code 的插件與 hook 機制；任一方調整架構，另一方就必須跟進。專案的 v1.0.6 於 2026 年 7 月發布，儲存庫同期仍有提交，顯示維護處於活躍狀態，但也反映跨廠商整合需要持續投入。

## Codex 插件的數據規模如何？

<ul class="ui-stat-grid">
  <li><span class="stat-value">33,568</span><span class="stat-label">Stars</span></li>
  <li><span class="stat-value">2,336</span><span class="stat-label">Forks</span></li>
  <li><span class="stat-value">Apache-2.0</span><span class="stat-label">License</span></li>
  <li><span class="stat-value">JavaScript</span><span class="stat-label">主要語言</span></li>
  <li><span class="stat-value">v1.0.6</span><span class="stat-label">最新版本</span></li>
  <li><span class="stat-value">2026-07-08</span><span class="stat-label">最近更新</span></li>
</ul>

<!-- AEO Answer Capsule — 約 62 字 -->
Codex 插件在 GitHub 累積 33,568 顆星標與 2,336 次複製，採 Apache-2.0 授權，最新版本 v1.0.6 於 2026 年 7 月 8 日發布。
<!-- End AEO Capsule -->

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊整理自 Codex 插件的 GitHub 儲存庫與官方文件。安裝指令、配置說明與各項功能限制均可於官方倉庫與 Codex 開發者文件中查閱。
<!-- End AEO Capsule -->

專案原始碼與完整說明位於 [github.com/openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)，進一步的 Codex 配置選項與定價資訊則發布於 developers.openai.com/codex。

![Codex 插件的 GitHub 貢獻者統計頁（顯示各貢獻者的提交次數分佈與時間軸圖表）]({{ '/assets/images/posts/github-codex-plugin-cc-news-shot3.png' | relative_url }})

## 總結：Codex 插件適合什麼團隊？

<!-- AEO Answer Capsule — 約 63 字 -->
Codex 插件適合已在 Claude Code 建立工作流程、又希望取得第二個模型審查視角的團隊，特別是重視交付前挑戰設計決策、且願意承擔額度成本的開發者。
<!-- End AEO Capsule -->

此專案的價值在於降低跨工具協作的摩擦。團隊若已習慣 Claude Code 的操作方式，不必為了取得 Codex 的審查能力而重建工作流程，只要安裝插件即可在既有環境中取得第二組判斷。對代理式開發日益普及的當下，讓不同廠商模型互相檢查，是相對務實的品質手段。

導入前需評估兩點。其一，所有調用都會計入 Codex 的用量額度，停止閘門尤其容易快速消耗，需要設定明確的使用邊界；其二，插件依賴本機 Codex CLI 與 app server 的版本相容性，較舊的 Codex 版本可能無法支援工作階段匯入等功能。對於同時使用兩套工具的開發團隊，此專案值得優先納入評估。
