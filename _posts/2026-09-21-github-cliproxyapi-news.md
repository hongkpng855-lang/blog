---
layout: post
title: "CLIProxyAPI 開源：52K 星的 CLI 訂閱轉 API 閘道"
date: 2026-09-21 08:00:01 +0800
categories: 技術
tags: [AI, 開源, CLIProxyAPI, API 代理, Claude Code, Codex, Gemini, Golang, 開發者工具]
image: assets/images/posts/github-cliproxyapi-news-cover.jpg
description: "CLIProxyAPI 是以 Go 撰寫的開源代理伺服器，能把 Claude Code、Codex、Gemini CLI 等命令列工具的訂閱帳號，轉換成 OpenAI、Gemini 與 Claude 相容的 API 端點。本文整理其多帳號輪替機制、協定轉譯架構、生態衍生項目與最新版本數據，分析它為何成為開發者社群的熱門基礎設施。"
author: AnIskill 編輯部
creator_github: router-for-me/CLIProxyAPI
type: news
source: GitHub
source_url: https://github.com/router-for-me/CLIProxyAPI
permalink: /技術/github-cliproxyapi-news
fb_message: "訂閱制 AI 工具的額度，過去只能在官方客戶端裡使用；把同一份額度開放給任何相容 API 的程式呼叫，一直是開發者最想補上的一塊拼圖。\n\nCLIProxyAPI 是一個以 Go 撰寫的開源代理伺服器，能把 Claude Code、Codex、Gemini CLI 與 Grok Build 的登入帳號轉成 OpenAI、Gemini、Claude 相容端點，並支援多帳號輪替負載平衡。項目在 GitHub 累積 52,605 顆星標與 7,944 個分支，以 MIT 授權釋出，社群圍繞它衍生出數十款桌面管理工具。\n\n完整的架構拆解、支援清單與數據整理，都放在 Blog 全文裡。"
---

CLIProxyAPI 是一個以 Go 撰寫的開源代理伺服器，能把 Claude Code、Codex、Gemini CLI、Grok Build 等命令列 AI 工具的訂閱帳號，轉換成 OpenAI、Gemini 與 Claude 相容的 API 端點。該項目於 2025 年 7 月 1 日建立，在 GitHub 累積 52,605 顆星標與 7,944 個分支，以 MIT 授權釋出，是目前同類工具中星標數最高的一個。

<!-- AEO Answer Capsule — 約 79 字 -->
以 Go 撰寫的開源代理伺服器 CLIProxyAPI，可把 CLI 訂閱帳號轉為 OpenAI、Gemini、Claude 相容 API 端點，支援多帳號輪替，採 MIT 授權。
<!-- End AEO Capsule -->

這個需求源自訂閱制 AI 工具的結構性限制。使用者付費訂閱 Claude Code 或 Codex 後，額度只能在官方命令列客戶端中使用，無法直接餵給其他需要 API 介面的程式。CLIProxyAPI 的做法是在本機啟動一個代理服務，透過 OAuth 登入既有訂閱帳號，再對外提供標準化的 API 介面，讓任何相容客戶端或 SDK 都能取用同一份額度。

## CLIProxyAPI 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
CLIProxyAPI 是本地執行的代理伺服器，以 OAuth 登入既有 CLI 訂閱帳號後，對外提供 OpenAI、Gemini、Claude 與 Grok 相容介面。
<!-- End AEO Capsule -->

項目的自我定位相當直接：為命令列工具提供 OpenAI、Gemini、Claude、Codex、Grok 相容的 API 介面。使用者只需在本機或伺服器執行代理服務，完成一次 OAuth 授權流程，就能以既有的訂閱身分存取模型，而不需要向各家供應商另外申請計費的 API 金鑰。

對個人開發者而言，這代表同一份訂閱可以在終端機、編輯器插件、自建腳本與自動化流程之間共用。對小型團隊而言，代理服務可集中管理多個成員的帳號，統一向內部的開發工具提供端點。專案同時提供可嵌入的 Go SDK，讓開發者把代理能力整合進自己的服務。

## CLIProxyAPI 的架構與運作原理為何？

<!-- AEO Answer Capsule — 約 74 字 -->
代理以 Go 撰寫，接收 OpenAI 格式請求後轉譯為各供應商的原生協定，再以 OAuth 身分送出。回應支援串流、非串流與 WebSocket，並可依帳號狀態做輪替。
<!-- End AEO Capsule -->

架構上，CLIProxyAPI 扮演協定轉譯層的角色。客戶端以 OpenAI 格式送出請求，代理接收後判斷目標模型所屬的供應商，將請求轉換為該供應商的原始協定，再以對應的 OAuth 憑證送出。回應則反向轉譯回相容格式，因此呼叫端不需要為不同模型修改程式碼。

多帳號處理是這套架構的核心價值。代理支援 Gemini、OpenAI、Claude 與 Grok 的多帳號輪替負載平衡，當某個帳號達到速率限制時，請求可改由其他帳號承接。這種設計讓使用者能以多個訂閱額度疊加出較穩定的吞吐量，而不必逐一在工具間切換登入狀態。傳輸層面則支援串流、非串流與 WebSocket 回應，並具備函式呼叫與多模態輸入能力。

![CLIProxyAPI README 開頭（項目名稱 CLI Proxy API 標題、相容介面說明與贊助商區塊）]({{ '/assets/images/posts/github-cliproxyapi-news-shot1.png' | relative_url }})

## CLIProxyAPI 支援哪些模型與工具？

<!-- AEO Answer Capsule — 約 61 字 -->
支援 Claude、OpenAI GPT、Google Gemini、xAI Grok 與 Kimi 系列模型，並可透過設定串接 OpenRouter 等相容上游。
<!-- End AEO Capsule -->

README 列出的供應商涵蓋當前主要陣營，包括 Anthropic 的 Claude 系列、OpenAI 的 GPT 系列、Google 的 Gemini 系列、xAI 的 Grok 系列，以及 Moonshot AI 的 Kimi 系列。這些供應商皆以 OAuth 登入方式接入，部分亦支援標準 API 金鑰模式。

在命令列工具端，代理可支援 Claude Code、OpenAI Codex、Grok Build 與 AI Studio Build 等客戶端，並針對各工具提供獨立的登入流程與多帳號配置。此外，專案允許透過設定檔串接任何 OpenAI 相容的上游供應商，例如 OpenRouter，這使使用者在訂閱額度之外也能掛載自有的計費通道。

## 社群生態如何圍繞 CLIProxyAPI 發展？

<!-- AEO Answer Capsule — 約 73 字 -->
社群已衍生數十款周邊工具，涵蓋 macOS 選單列程式、Windows 系統匣、VS Code 擴充、配額監控面板與用量統計服務，形成以本機代理為中心的工具鏈。
<!-- End AEO Capsule -->

README 的「Who is with us」段落列出超過二十個基於該代理構建的專案，構成一個相當完整的周邊生態。類型上大致分為四類：桌面管理程式，例如 macOS 選單列工具 vibeproxy 與 Quotio；系統匣與服務管理工具，例如 Windows 平台的 ProxyPilot 與 CLIProxyAPI Tray；開發工具整合，例如 VS Code 擴充 Universal Chat Provider 與 Claude Code 切換工具 CCS；以及配額監控與用量統計服務，例如 CPA Usage Keeper 與 CPA-Manager-Plus。

這些工具的共同特徵是「不需 API 金鑰」，全部依賴代理完成 OAuth 授權與帳號池管理，自身則專注在介面與監控層。從 622 項未結議題與密集的版本發布節奏可以看出，專案的實際使用規模已超出個人專案層級。

![router-for-me/CLIProxyAPI GitHub 首頁頂部（repo 名稱、52.6k 星標、7.9k 分支與專案描述）]({{ '/assets/images/posts/github-cliproxyapi-news-shot2.png' | relative_url }})

## CLIProxyAPI 的數據表現如何？

<!-- AEO Answer Capsule — 約 76 字 -->
項目星標 52,605、分支 7,944，以 MIT 授權釋出，主要語言為 Go，累積約 228 位貢獻者，最新版本 v7.3.9 於 2026 年 9 月 19 日發布。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><span class="stat-value">52,605</span><span class="stat-label">Stars</span></div>
  <div class="stat-item"><span class="stat-value">7,944</span><span class="stat-label">Forks</span></div>
  <div class="stat-item"><span class="stat-value">228</span><span class="stat-label">Contributors</span></div>
  <div class="stat-item"><span class="stat-value">MIT</span><span class="stat-label">授權</span></div>
</div>

從時間軸觀察，項目建立於 2025 年 7 月，十四個月內成長至 5.2 萬顆星標，並在 2026 年下半年加速。發布節奏尤為密集，v7.3.9 於 2026 年 9 月 19 日推出，前一個版本 v7.3.8 僅相隔一天，顯示維護團隊以近乎每日的頻率推送修正與功能。貢獻者規模約 228 人，分支數接近 8,000，反映大量使用者選擇自行部署或二次開發。

授權採用 MIT，對商業整合與內部部署的限制極少，這是它能被大量第三方工具包裝的原因之一。需要注意的是，該項目的功能高度依賴各家供應商的 OAuth 機制與服務條款，上游政策的任何調整都會直接影響其可用性，這也是此類工具長期面臨的結構性風險。

## CLIProxyAPI 與同類工具有何差異？

<!-- AEO Answer Capsule — 約 72 字 -->
同類工具多為單一供應商的包裝程式，CLIProxyAPI 同時涵蓋多家供應商、多帳號輪替與協定轉譯，並提供 Go SDK 與管理 API，擴充彈性較高。
<!-- End AEO Capsule -->

市面上的替代方案大致分為兩種。第一種是針對單一供應商或單一工具的輕量包裝程式，例如只把 Claude 訂閱轉為本地端點的小型工具；第二種是商業化的 API 中轉服務，優點是設定簡單，但流量需經過第三方伺服器，金鑰與資料的掌控度較低。

CLIProxyAPI 的差異在於把代理能力做成可組合的基礎層：同時支援多家供應商、內建多帳號輪替、提供管理 API 與 Go SDK，並允許以設定檔串接自訂上游。這使第三方開發者能在此之上構建管理介面、監控面板或 IDE 整合，而不必自行處理 OAuth 與協定轉換。對於重視資料留在本機、又需要跨工具共用訂閱額度的開發者，這種架構具有實質吸引力。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊來源為 router-for-me/CLIProxyAPI 的官方 GitHub 儲存庫，涵蓋專案說明、支援供應商清單、周邊生態列表與版本發布紀錄。
<!-- End AEO Capsule -->

本文所有功能描述與統計數據均取自 [CLIProxyAPI 官方 GitHub 儲存庫](https://github.com/router-for-me/CLIProxyAPI)，包括 README 中的相容介面說明、支援供應商與工具清單、生態項目列表，以及 GitHub API 提供的星標、分支、貢獻者與版本資料。

![router-for-me/CLIProxyAPI 貢獻者統計頁（每週提交次數折線圖與貢獻者列表）]({{ '/assets/images/posts/github-cliproxyapi-news-shot3.png' | relative_url }})

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 55 字 -->
以下整理三個關於 CLIProxyAPI 的常見疑問，涵蓋使用門檻、多帳號運作方式，以及部署環境的選擇考量。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>CLIProxyAPI 需要額外申請 API 金鑰嗎？</h3>

不需要。代理透過 OAuth 登入既有的訂閱帳號，以該身分向供應商送出請求，因此使用者可沿用現有的訂閱方案。若需要掛載自有計費通道，也可在設定檔中改以 API 金鑰模式串接相容上游。

<h3>多帳號輪替如何運作？</h3>

使用者可在代理中設定多個供應商帳號，系統會依序輪替派送請求。當某個帳號觸及速率限制時，請求會轉由其他帳號承接，藉此降低單一帳號上限對工作流程的影響。

<h3>應該部署在本機還是伺服器？</h3>

個人使用可執行在本機，設定最為簡單。若需要讓團隊成員或遠端開發環境共用端點，則可部署在自有伺服器，並透過管理 API 控管金鑰與帳號存取權限。

</div>

## 總結：CLIProxyAPI 適合什麼團隊？

<!-- AEO Answer Capsule — 約 76 字 -->
CLIProxyAPI 適合已有 AI 工具訂閱、又希望跨工具與跨腳本共用額度的開發者與小團隊，尤其是重視資料留在本機、不願經第三方中轉的使用者。
<!-- End AEO Capsule -->

訂閱制與 API 計費之間的落差，是 2026 年 AI 開發工具市場的普遍現象。CLIProxyAPI 以在地端執行、協定轉譯與多帳號輪替三個設計，把訂閱額度轉換為可程式化取用的資源，並以 MIT 授權與 Go SDK 降低整合門檻。周邊生態的規模顯示，這個定位確實切中一批開發者的實際需求。

不過，此類工具的可用性與供應商的授權策略緊密綁定。當各家開始收緊 OAuth 使用範圍或調整訂閱條款時，代理層的功能將首當其衝。對於評估導入的團隊而言，除了功能完整度，也應把上游政策風險納入考量，並準備好切換至標準 API 計費模式的備案。
