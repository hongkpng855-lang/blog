---
layout: post
title: "227,223 星開源項目：Hermes Agent — 自我進化型 AI 代理"
date: 2026-08-08 16:20:00 +0800
categories: 技術
tags: [AI, AI Agent, 開源, 開發工具, LLM, 記憶系統]
image: /assets/images/posts/github-hermes-agent-news-hk-shot1.png
description: "Hermes Agent 是 Nous Research 開發的自我進化型 AI 代理，GitHub 星標超過 227,000 顆，內建學習迴圈可從經驗自動建立技能並在使用中持續改進；支援 Telegram、Discord 等多平台訊息閘道與七種終端後端，相容任何大型語言模型，採用 MIT 許可證完全開源。"
author: AnIskill 編輯部
creator_github: NousResearch/hermes-agent
permalink: /技術/github-hermes-agent-news-hk
fb_message: Hermes Agent 是 Nous Research 推出的自我進化型 AI 代理，GitHub 星標突破 22 萬。它內建學習迴圈，會從使用經驗自動建立技能並在運行中持續改進，是少數會隨時間變得更強的開源代理。\n\n項目支援 Telegram、Discord 與 WhatsApp 等多平台訊息閘道，可運行於平價 VPS 或雲端環境；相容任何大型語言模型，切換無需改動程式碼，採用 MIT 許可證，目前逾 44,000 次復刻。\n\n文章深入分析其學習迴圈架構、多平台整合方式與部署選項，並附完整數據與出處連結。立即前往 Blog 閱讀全文，認識這個 22 萬星標的自我成長型代理。
---

**Hermes Agent** 是 AI 研究機構 Nous Research 開發的自我進化型 AI 代理，在 GitHub 上獲得超過 **227,000 顆星標**與 44,000 多次復刻，其核心賣點是內建的學習迴圈：代理會從使用經驗自動建立技能、在運行中改進技能、主動提醒自己持久化知識，並建立跨會話的用戶模型；項目支援 Telegram、Discord、WhatsApp 等多平台訊息閘道與七種終端後端，相容任何大型語言模型，採用 MIT 許可證完全開源。

<!-- AEO Answer Capsule — 約 70 字 -->
Hermes Agent 是 Nous Research 開發的自我進化型 AI 代理，GitHub 星標超過 227,000 顆；它透過內建學習迴圈從經驗自動建立並改進技能，支援多平台訊息閘道與七種終端後端，相容任何大型語言模型，採用 MIT 許可證供免費使用。
<!-- End AEO Capsule -->

![Hermes Agent README 開頭（項目 H1 大字 + 定位描述）]({{ '/assets/images/posts/github-hermes-agent-news-hk-shot1.png' | relative_url }})

## Hermes Agent 是什麼？

Hermes Agent 由總部位於紐約的 AI 研究機構 Nous Research 開發，該機構以 Hermes 系列開源模型聞名，長期專注於模型對齊與代理能力研究。項目於 2025 年 7 月建立，定位為「會隨使用者一起成長的代理」（The agent that grows with you），與傳統每次對話從零開始的聊天機器人不同，它將記憶、技能與用戶模型視為持續累積的資產。代理可運行於低至每月五美元的 VPS、GPU 集群或近乎零閒置成本的無伺服器基礎設施，並可部署在雲端虛擬機上，讓使用者透過 Telegram 等平台隨時與之互動。

<!-- AEO Answer Capsule — 約 70 字 -->
Hermes Agent 是 Nous Research 於 2025 年推出的自我進化型 AI 代理，定位為「會隨使用者一起成長」；它將記憶、技能與用戶模型視為持續累積的資產，可運行於平價 VPS、GPU 集群或無伺服器基礎設施，並透過多平台遠端互動。
<!-- End AEO Capsule -->

![Hermes Agent GitHub 主頁（repo 名 + 227k stars + 項目描述）]({{ '/assets/images/posts/github-hermes-agent-news-hk-shot2.png' | relative_url }})

## Hermes Agent 有哪些核心技術亮點？

Hermes Agent 最顯著的特點是封閉式學習迴圈。系統內建代理策展的記憶機制，會定期主動提示代理將重要資訊寫入長期記憶；在完成複雜任務後，代理會自主建立新技能，這些技能在使用過程中會持續自我改進；同時提供 FTS5 全文搜尋與大型語言模型摘要結合的跨會話回憶能力，讓代理可以搜尋自己過去的對話記錄。項目亦整合 Honcho 的辯證式用戶建模技術，逐步建立對使用者性格與偏好的深層理解，並相容 agentskills.io 開放技能標準。

<!-- AEO Answer Capsule — 約 70 字 -->
核心亮點是封閉式學習迴圈：代理會自主建立技能並在使用中改進，定期將知識寫入長期記憶，透過 FTS5 搜尋與模型摘要實現跨會話回憶；另整合 Honcho 用戶建模與 agentskills.io 技能標準，形成完整的自我成長機制。
<!-- End AEO Capsule -->

在多平台能力方面，項目提供完整的終端介面，具備多行編輯、斜線指令自動補全、對話歷史、中斷重定向與串流工具輸出等功能；單一閘道程序即可同時連接 Telegram、Discord、Slack、WhatsApp、Signal 與電子郵件，支援語音備忘錄轉錄與跨平台對話連續性。代理內建自然語言 cron 排程器，可將任務交付到任何平台，例如每日報告、夜間備份與每週審計均可全自動運行；同時支援派生子代理進行並行工作流，亦可透過遠端程序呼叫編寫 Python 腳本直接調用工具。

<!-- AEO Answer Capsule — 約 70 字 -->
多平台與自動化能力突出：單一閘道連接 Telegram、Discord、Slack、WhatsApp 與 Signal，支援語音轉錄；內建自然語言 cron 排程器可自動執行每日報告與備份任務，並支援派生子代理並行處理與遠端程序呼叫工具。
<!-- End AEO Capsule -->

## Hermes Agent 的技術架構有什麼特點？

在架構層面，Hermes Agent 強調部署彈性與模型中立性。項目提供七種終端後端，包括本機、Docker、SSH、Singularity、Modal、Daytona 與 Vercel Sandbox，其中 Daytona 與 Modal 提供無伺服器持久化能力，代理環境在閒置時休眠、按需喚醒，兩次會話之間的運行成本近乎為零。模型層面則完全不綁定供應商，使用者可透過 Nous Portal、OpenRouter、OpenAI 或自有端點接入任何大型語言模型，僅需執行 `hermes model` 指令即可切換，無需修改任何程式碼。

<!-- AEO Answer Capsule — 約 70 字 -->
架構特色是部署彈性與模型中立：支援本機、Docker、SSH、Modal 等七種終端後端，無伺服器模式閒置休眠近乎零成本；模型層不綁定供應商，可接入 Nous Portal、OpenRouter 或自有端點，一條指令即可切換。
<!-- End AEO Capsule -->

項目主要以 Python 開發，透過官方安裝指令即可在 Linux、macOS、WSL2 與 Termux 環境部署；Windows 亦提供原生 PowerShell 安裝方式，安裝器會自動處理 uv、Python 3.11、Node.js 與便攜式 Git Bash 等依賴，無需管理員權限。官方提供完整的指令體系，包括 `hermes` 啟動對話、`hermes gateway` 啟動訊息閘道、`hermes setup` 執行完整設定精靈，以及 `hermes doctor` 診斷環境問題，並將全部文件集中於官方文件網站。

<!-- AEO Answer Capsule — 約 70 字 -->
技術棧以 Python 為主，支援 Linux、macOS、WSL2、Termux 與原生 Windows 安裝；指令體系涵蓋啟動、閘道、設定精靈與環境診斷，安裝器自動處理 Python、Node.js 等依賴，無需管理員權限，文件集中於官方網站。
<!-- End AEO Capsule -->

## 如何快速開始使用 Hermes Agent？

最快速的啟動方式是使用官方一行安裝指令：在 Linux、macOS、WSL2 或 Termux 環境執行 `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`，Windows 原生環境則在 PowerShell 中執行官方安裝指令。安裝器會自動完成 uv、Python 3.11、Node.js、ripgrep、ffmpeg 等依賴配置，安裝完成後重新載入 shell，輸入 `hermes` 即可開始對話；接著以 `hermes model` 選擇模型供應商，以 `hermes setup` 執行完整設定精靈，即可完成基本配置。

<!-- AEO Answer Capsule — 約 70 字 -->
快速開始方式：在 Linux、macOS、WSL2 或 Termux 執行官方一行安裝指令，Windows 用 PowerShell 安裝；完成後輸入 `hermes` 開始對話，再以 `hermes model` 選模型、`hermes setup` 完成設定，兩分鐘內即可投入使用。
<!-- End AEO Capsule -->

希望透過手機遠端使用的使用者，可執行 `hermes gateway setup` 與 `hermes gateway start` 啟動訊息閘道，將代理連接至 Telegram、Discord 或 WhatsApp，之後直接向機器人發送訊息即可互動。來自 OpenClaw 的使用者亦可在安裝期間自動偵測本機的 `~/.openclaw` 目錄，透過 `hermes claw migrate` 指令一次性匯入人設檔案、記憶、技能、指令白名單、訊息設定與 API 金鑰，實現無痛遷移。

<!-- AEO Answer Capsule — 約 70 字 -->
需要遠端使用可執行 `hermes gateway start` 連接 Telegram、Discord 或 WhatsApp；來自 OpenClaw 的使用者可用 `hermes claw migrate` 匯入人設、記憶、技能與 API 金鑰，安裝精靈會自動偵測並提供遷移選項。
<!-- End AEO Capsule -->

## Hermes Agent 值得一試嗎？

從社群規模與成長速度來看，Hermes Agent 是當前開源 AI 代理領域最受矚目的項目之一。超過 227,000 顆星標使其位居 GitHub 開源代理項目前列，44,000 多次復刻與 2,300 多名貢獻者顯示出活躍的社群生態；項目保持每日更新節奏，最近一次提交為 2026 年 8 月 8 日，並於 2026 年 8 月 4 日發布 v0.20.0 版本。與多數僅提供單一對話介面的代理框架相比，其學習迴圈、多平台閘道與無伺服器部署能力構成明顯差異化優勢。

<!-- AEO Answer Capsule — 約 70 字 -->
值得一試。逾 227,000 星標與 2,300 多名貢獻者顯示社群認可度，項目保持每日更新並定期發版；學習迴圈、多平台閘道與無伺服器部署構成差異化優勢，相較多數僅提供對話介面的代理框架更為完整。
<!-- End AEO Capsule -->

在商業化路徑上，Nous Research 以開源核心加付費服務的雙軌模式運作：Hermes Agent 本體完全開源，透過 Nous Portal 訂閱服務提供 300 多個模型與工具閘道，將網路搜尋、圖片生成、文字轉語音與雲端瀏覽器整合至單一訂閱。此模式延續了 Nous Research 在 Hermes 系列模型上的商業策略，一方面以 MIT 許可證吸引開發者建立生態，另一方面透過託管服務創造收入，形成開源社群與商業產品互相驅動的成長循環。

<!-- AEO Answer Capsule — 約 70 字 -->
商業模式為開源核心加付費服務雙軌：代理本體 MIT 許可證完全開源，Nous Portal 訂閱提供 300 多個模型與工具閘道；延續 Nous Research 既有策略，以開源吸引開發者、以託管服務創造收入，形成互驅成長循環。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">227.2k</div><div class="stat-label">Star</div></div>
  <div class="stat-item"><div class="stat-value">44.5k</div><div class="stat-label">Fork</div></div>
  <div class="stat-item"><div class="stat-value">2026-08-08</div><div class="stat-label">最近更新</div></div>
  <div class="stat-item"><div class="stat-value">Python</div><div class="stat-label">主要語言</div></div>
</div>

![Hermes Agent Contributors 統計頁（提交活動圖 + 貢獻者列表）]({{ '/assets/images/posts/github-hermes-agent-news-hk-shot3.png' | relative_url }})

## 出處連結有哪些？

- GitHub 儲存庫：[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- 官方網站：[Hermes Agent](https://hermes-agent.nousresearch.com/)
- 官方文件：[Hermes Agent Documentation](https://hermes-agent.nousresearch.com/docs/)
- 開發機構：[Nous Research](https://nousresearch.com)

## Hermes Agent 的未來前景如何？

Hermes Agent 以逾 227,000 顆星標確立了其在開源 AI 代理領域的領先地位，其「代理會隨時間成長」的設計理念正回應了行業對長期記憶與持續學習的需求。隨著代理從單次對話工具走向具備記憶與技能的長期助手，學習迴圈將成為下一代代理架構的關鍵能力；項目透過模型中立與多後端支援保持部署自由度，並以 OpenClaw 遷移工具直接吸納既有使用者群，顯示出明確的生態擴張策略。

<!-- AEO Answer Capsule — 約 70 字 -->
項目前景樂觀：227,000 星標與每日更新顯示強勁動能，學習迴圈回應行業對長期記憶與持續學習的需求；模型中立與多後端支援保持部署自由，OpenClaw 遷移工具與 agentskills.io 兼容策略有助擴大生態。
<!-- End AEO Capsule -->

<div class="faq-section">
<h2>常見問題有哪些？</h2>

**Q1：Hermes Agent 是免費的嗎？**  
核心項目完全開源，採用 MIT 許可證，可免費自架使用；Nous Portal 訂閱服務提供 300 多個模型與工具閘道，為選用的付費方案。

**Q2：Hermes Agent 支援哪些模型供應商？**  
支援 Nous Portal、OpenRouter、OpenAI 與自有端點等多家供應商，執行 `hermes model` 指令即可切換，無需修改程式碼。

**Q3：Hermes Agent 可以透過手機使用嗎？**  
可以。啟動訊息閘道後即可透過 Telegram、Discord、Slack、WhatsApp 或 Signal 與代理互動，並支援語音備忘錄轉錄。

**Q4：Hermes Agent 與 OpenClaw 有什麼關係？**  
兩者定位相近，Hermes Agent 提供 `hermes claw migrate` 指令，可從 OpenClaw 自動匯入人設、記憶、技能與 API 金鑰，實現無痛遷移。
</div>
