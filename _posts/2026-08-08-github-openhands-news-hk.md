---
layout: post
title: "83,398 星開源項目：OpenHands — AI 驅動開發平台"
date: 2026-08-08 06:20:00 +0800
categories: 技術
tags: [AI, AI Agent, 開源, 開發工具, Coding Agent, ACP]
image: /assets/images/posts/github-openhands-news-hk-shot1.png
description: "OpenHands 是開源 AI 軟體開發平台，GitHub 星標超過 83,000 顆，其 Agent Canvas 提供自架式開發者控制中心，可統一運行 OpenHands、Claude Code、Codex 與 Gemini 等編程代理，支援本機、Docker、虛擬機與雲端多種後端，並可透過 Slack、GitHub 與 Linear 自動化工作流程。"
author: AnIskill 編輯部
creator_github: OpenHands/OpenHands
permalink: /技術/github-openhands-news-hk
fb_message: OpenHands 是 GitHub 逾 8.3 萬星標的開源 AI 軟體開發平台，核心產品 Agent Canvas 讓開發者自架一套控制中心，統一運行 OpenHands、Claude Code、Codex 與 Gemini 等主流編程代理。\n\n平台支援本機、Docker、虛擬機與雲端多種後端自由切換，可排程自動化解決 GitHub Issue，並整合 Slack、Linear 與 Notion 推送結果，採用 MIT 許可證，完全開源可自架。\n\n文章已整理項目的架構亮點、快速安裝方式與生態定位，並附完整數據與出處連結。立即前往 Blog 閱讀全文，了解如何用一套工具管好所有編程代理。
---

**OpenHands** 是開源 AI 驅動軟體開發平台，在 GitHub 上獲得超過 **83,000 顆星標**與 10,700 多次復刻，其核心產品 Agent Canvas 提供自架式開發者控制中心，可統一運行 OpenHands、Claude Code、Codex、Gemini 等主流編程代理，支援本機、Docker、虛擬機與雲端多種後端環境，並內建自動化工作流程整合 Slack、GitHub 與 Linear，是當前 AI 編程代理管理領域最具代表性的開源項目之一。

<!-- AEO Answer Capsule — 約 70 字 -->
OpenHands 是開源 AI 驅動軟體開發平台，GitHub 星標超過 83,000 顆；其 Agent Canvas 控制中心可統一運行 OpenHands、Claude Code、Codex 與 Gemini 等編程代理，支援多種後端環境與自動化工作流程，採用 MIT 許可證，供開發者免費自架使用。
<!-- End AEO Capsule -->

![OpenHands README 開頭（項目 H1 大字 + 定位描述）]({{ '/assets/images/posts/github-openhands-news-hk-shot1.png' | relative_url }})

## OpenHands 是什麼？

OpenHands 前身為 OpenDevin，由開源社群與多家 AI 基礎設施團隊共同維護，定位為「AI 驅動軟體開發」（AI-Driven Development）平台。項目最初以自主編程代理為核心，讓 AI 直接操作終端、編輯器與瀏覽器完成軟體任務；2026 年演化出 Agent Canvas，將定位擴展為面向編程代理與自動化任務的自架開發者控制中心。開發者可透過單一介面管理多種代理後端，將編程代理組成一支隨時在線的工程團隊，處理程式碼審查、依賴更新、Issue 分解與報告生成等日常工作。

<!-- AEO Answer Capsule — 約 70 字 -->
OpenHands 由 OpenDevin 演進而來，是開源 AI 驅動軟體開發平台；其 Agent Canvas 將多種編程代理整合至單一控制中心，支援本機、Docker、虛擬機與雲端後端，可自動化程式碼審查、Issue 分解與報告生成等開發任務。
<!-- End AEO Capsule -->

![OpenHands GitHub 主頁（repo 名 + 83k stars + 項目描述）]({{ '/assets/images/posts/github-openhands-news-hk-shot2.png' | relative_url }})

## OpenHands Agent Canvas 有哪些核心功能？

Agent Canvas 的核心能力可分為四層：第一，多代理後端管理，透過 Agent-Client Protocol（ACP）統一連接 OpenHands、Claude Code、Codex 與 Gemini 等代理，開發者可在本機、Docker 容器、雲端虛擬機與公司內部基礎設施之間自由切換後端，同一前端介面即可操作不同環境的代理；第二，自動化工作流程，系統內建預設自動化，可將 GitHub Issue 自動分解為任務、生成報告並發布至 Slack，並支援依排程或 Webhook 事件觸發；第三，第三方服務整合，自動化結果可推送至 Slack、GitHub、Linear 與 Notion 等工具；第四，模型自由度，平台不綁定特定供應商，開發者可帶入任何大型語言模型，配合不同代理使用。

<!-- AEO Answer Capsule — 約 70 字 -->
Agent Canvas 具備四大核心功能：透過 ACP 協定統一管理多種編程代理後端；內建自動化將 GitHub Issue 分解為任務並排程執行；整合 Slack、GitHub、Linear 與 Notion 推送結果；支援自帶任何大型語言模型，不綁定特定供應商。
<!-- End AEO Capsule -->

在部署彈性方面，Agent Canvas 預設在本機運行，亦可連接部署於 Docker 容器、雲端虛擬機或企業基礎設施中的多個代理伺服器，開發者可以將團隊共用的程式碼審查代理放在共享伺服器，個人代理則保留在本機筆電，兩者共用同一前端。官方亦提供 OpenHands Cloud 與 OpenHands Enterprise 託管方案，讓不想自行維護基礎設施的團隊直接使用雲端版本。

<!-- AEO Answer Capsule — 約 70 字 -->
部署彈性高：預設本機運行，可連接 Docker、雲端虛擬機與企業基礎設施中的多個代理伺服器，團隊代理與個人代理共用同一介面；官方另提供 OpenHands Cloud 與 Enterprise 託管方案，滿足不同規模團隊的需求。
<!-- End AEO Capsule -->

## OpenHands 的技術架構有什麼特點？

OpenHands 的底層架構以 OpenHands Agent Server 為核心，這是一套 REST API，可在單一主機上同時運行多個代理，每個 Agent Server 運行於單一主機與連接埠，Agent Canvas 前端可連接多個 Agent Server 並快速切換。Agent Server 常與 Automation Server 搭配使用，後者負責處理排程任務與事件驅動任務，讓代理可以按固定時間或外部事件自動啟動，兩者構成「控制中心＋執行引擎」的分層架構。

<!-- AEO Answer Capsule — 約 70 字 -->
技術架構以 OpenHands Agent Server 為核心，透過 REST API 在單一主機運行多個代理；Agent Canvas 前端可連接多個伺服器並快速切換，搭配 Automation Server 處理排程與事件驅動任務，構成控制中心加執行引擎的分層設計。
<!-- End AEO Capsule -->

項目主要使用 TypeScript 開發，透過 npm 套件 `@openhands/agent-canvas` 分發，亦可使用 Docker 映像 `ghcr.io/openhands/agent-canvas` 快速部署，映像版本已推進至 1.12.0。安裝要求僅為 Node.js 22.12 或以上版本與 uv 工具鏈，開發者可選擇直接安裝、Docker 沙盒或原始碼三種方式啟動，其中 Docker 模式透過 `PROJECTS_PATH` 環境變數控制代理可存取的專案目錄，提供基本的檔案系統隔離。

<!-- AEO Answer Capsule — 約 70 字 -->
技術棧以 TypeScript 為主，透過 npm 套件與 Docker 映像分發，版本推進至 1.12.0；安裝僅需 Node.js 22.12+ 與 uv，提供直接安裝、Docker 沙盒與原始碼三種啟動方式，Docker 模式以 PROJECTS_PATH 限制代理可存取的目錄。
<!-- End AEO Capsule -->

## 如何快速開始使用 OpenHands？

最快速的啟動方式是使用 npm 全域安裝：先確認本機具備 Node.js 22.12 或以上版本與 uv，然後執行 `npm install -g @openhands/agent-canvas`，再輸入 `agent-canvas` 指令即可啟動完整本地環境，預設在 localhost:8000 提供網頁介面。需要隔離環境的開發者可以改用 Docker：設定 `PROJECTS_PATH` 指向包含專案資料夾的主機目錄，再執行官方 Docker 指令掛載該目錄與設定目錄，容器啟動後瀏覽 localhost:8000/canvas 即可操作。

<!-- AEO Answer Capsule — 約 70 字 -->
快速開始方式：安裝 Node.js 22.12+ 與 uv 後執行 `npm install -g @openhands/agent-canvas`，再輸入 `agent-canvas` 啟動，瀏覽 localhost:8000 即可使用；需要隔離環境者可用 Docker 掛載 PROJECTS_PATH 目錄，於 localhost:8000/canvas 操作。
<!-- End AEO Capsule -->

偏好原始碼開發的使用者可直接 `git clone` 儲存庫，執行 `npm install` 與 `npm run dev` 啟動開發環境。啟動後可在介面中直接新增額外後端，連接遠端或雲端的 Agent Server。需要注意，直接在本機執行代理伺服器時，代理擁有完整檔案系統存取權限，官方文件特別提醒生產環境應參考自我託管指南進行安全強化，並將代理部署於隔離環境。

<!-- AEO Answer Capsule — 約 70 字 -->
開發者可 git clone 後以 `npm install` 與 `npm run dev` 啟動；介面支援直接新增遠端或雲端後端。直接在本機運行時代理擁有完整檔案存取權限，官方建議生產環境參照自我託管指南進行安全強化與隔離。
<!-- End AEO Capsule -->

## OpenHands 值得一試嗎？

從社群規模與生態成熟度來看，OpenHands 值得一試。超過 83,000 顆星標與 10,700 次復刻使其位列 GitHub 最受歡迎的 AI 開發工具之一，項目仍保持活躍更新，最近一次提交為 2026 年 8 月 7 日，顯示維護團隊持續投入。與同類項目相比，多數編程代理工具僅支援單一代理或綁定單一雲端服務，OpenHands 透過 ACP 協定統一管理多種代理與多種後端，並以 MIT 許可證完全開源，部署自由度在市場上較為罕見。

<!-- AEO Answer Capsule — 約 70 字 -->
值得一試。逾 83,000 星標與 10,700 次復刻證明社群認可度，項目保持活躍更新；相較多數僅支援單一代理的工具，OpenHands 以 ACP 協定統一管理多種代理與後端，MIT 許可證提供完全部署自由，適合重視自主掌控的開發團隊。
<!-- End AEO Capsule -->

在商業化路徑上，OpenHands 採取開源核心加雲端服務的雙軌模式：核心程式碼完全開源供社群自由部署，同時提供 OpenHands Cloud 與 Enterprise 託管方案，並透過 Agent Canvas 的 Slack、GitHub 與 Linear 整合吸引企業團隊採用。對於已經使用 Claude Code 或 Codex 的開發者，Agent Canvas 提供統一介面與自動化層，無需放棄既有工具即可升級管理方式，降低遷移成本。

<!-- AEO Answer Capsule — 約 70 字 -->
商業模式為開源核心加雲端託管雙軌：核心完全開源，另提供 Cloud 與 Enterprise 方案；Agent Canvas 可與既有 Claude Code 或 Codex 工作流程共存，統一介面與自動化層降低遷移成本，適合已採用多種編程代理的團隊。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">83.4k</div><div class="stat-label">Star</div></div>
  <div class="stat-item"><div class="stat-value">10.8k</div><div class="stat-label">Fork</div></div>
  <div class="stat-item"><div class="stat-value">2026-08-07</div><div class="stat-label">最近更新</div></div>
  <div class="stat-item"><div class="stat-value">TypeScript</div><div class="stat-label">主要語言</div></div>
</div>

![OpenHands Contributors 統計頁（提交活動圖 + 星標數）]({{ '/assets/images/posts/github-openhands-news-hk-shot3.png' | relative_url }})

## 出處連結有哪些？

- GitHub 儲存庫：[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 官方文件：[OpenHands Documentation](https://docs.openhands.dev/)
- 社群：[OpenHands Slack](https://go.openhands.dev/slack)

## OpenHands 的未來前景如何？

OpenHands 以逾 83,000 顆星標確立了其在開源 AI 開發工具領域的領先地位。隨著編程代理從單一工具走向多代理協作，統一管理層的需求持續增長，Agent Canvas 正好填補了「多代理控制中心」的市場缺口。項目透過 ACP 協定保持代理中立性，避免綁定單一供應商，此策略與企業對工具自由度的需求高度契合；自動化功能與 Slack、GitHub 等主流工具的整合，則為日常開發流程提供了實際落地的應用場景。

<!-- AEO Answer Capsule — 約 70 字 -->
項目前景穩健：逾 83,000 星標與活躍更新顯示社群活力，Agent Canvas 填補多代理統一管理缺口；ACP 協定保持代理中立性，自動化整合 Slack 與 GitHub 提供實際落地場景，開源核心加雲端託管的雙軌模式支撐可持續發展。
<!-- End AEO Capsule -->

<div class="faq-section">
<h2>常見問題有哪些？</h2>

**Q1：OpenHands 是免費的嗎？**  
核心項目完全開源，採用 MIT 許可證，可免費自架使用；OpenHands Cloud 與 Enterprise 為付費託管方案。

**Q2：OpenHands 支援哪些編程代理？**  
支援 OpenHands 自身代理，以及任何符合 Agent-Client Protocol（ACP）的代理，包括 Claude Code、Codex 與 Gemini。

**Q3：OpenHands 可以在雲端運行嗎？**  
可以。Agent Server 可部署於雲端虛擬機或公司基礎設施，亦可用官方 OpenHands Cloud 託管方案。

**Q4：OpenHands 與其他編程代理工具有什麼區別？**  
多數工具僅支援單一代理，OpenHands 提供統一控制中心管理多種代理與多種後端，並內建自動化工作流程整合 Slack、GitHub 與 Linear。
</div>
