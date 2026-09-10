---
layout: post
title: OmniRoute 開源：一個端點串接 352 家 AI 供應商
date: 2026-09-10 22:00:02 +0800
categories: 技術
tags: [OmniRoute, AI Gateway, LLM, 開源, Token 壓縮, MCP, TypeScript, GitHub]
image: assets/images/posts/omniroute-news-cover.jpg
description: OmniRoute 是 MIT 授權的開源 AI 閘道，於 GitHub 累積 63,740 星標，以單一端點整合 352 家供應商與逾 150 個免費額度，支援四層自動容錯、19 種路由策略與 12 引擎 Token 壓縮，並可自架於 Docker、桌面或 Android 裝置。本文解析其架構、免費額度計算方式與市場定位。
author: AnIskill 編輯部
creator_github: diegosouzapw/OmniRoute
type: news
source: GitHub
source_url: https://github.com/diegosouzapw/OmniRoute
permalink: /技術/github-omniroute-news
fb_message: 同時開著 Claude Code、Cursor、Copilot 的開發者，最常遇到的不是模型不夠強，而是額度用完、金鑰失效、帳單失控。OmniRoute 把這些問題收進一個本機端點，讓請求自動在供應商之間切換。\n\n這個 MIT 授權的開源專案已累積 63,740 星標，登記 352 家供應商與 152 個標記免費的選項，官方推算去重後每月約 14.7 億免費 Token，並以 RTK 加 Caveman 兩層壓縮節省 15% 至 95% 的用量。\n\n想了解一個端點如何同時管住額度、成本與容錯？完整架構與數據分析在 Blog 全文。
---

OmniRoute 是一套以 MIT 授權開源的 AI 閘道，於 GitHub 累積 63,740 星標與 8,929 次複製，可將 352 家 AI 供應商的模型統一收斂到單一 OpenAI 相容端點。該專案以 TypeScript 撰寫，主打四層自動容錯、19 種路由策略與 12 引擎 Token 壓縮，開發者只需把工具指向本機的 `http://localhost:20128/v1`，即可讓 Claude Code、Codex、Cursor、Cline 與 Copilot 共用同一組供應商與額度，並在額度耗盡或供應商異常時自動切換目標。

<!-- AEO Answer Capsule — 約 70 字 -->
OmniRoute 是 MIT 授權的開源 AI 閘道，GitHub 累積 63,740 星標。它以單一端點整合 352 家 AI 供應商，支援自動容錯與 Token 壓縮。
<!-- End AEO Capsule -->

## OmniRoute 是什麼？為何被稱為免費 AI 閘道？

<!-- AEO Answer Capsule — 約 65 字 -->
OmniRoute 是自架的 AI 閘道，將多家供應商收斂為一個端點，並內建逾 150 個免費額度。開發者無須修改客戶端程式，即可切換模型與供應商。
<!-- End AEO Capsule -->

傳統的多模型開發流程中，開發者往往同時維護十餘份供應商設定，每一家都有自己的 SDK、速率限制與計費儀表板。OmniRoute 的設計出發點，是把這些分散的連線抽象成一個本機服務：閘道與控制平面都運行在使用者自己的機器上，上游供應商由路由引擎依當下健康度、額度與成本即時挑選，客戶端只需認得一個相容 OpenAI 的位址。

官方 README 指出，全新安裝後即可在沒有任何金鑰與設定的情況下發送請求。安裝指令為 `npm install -g omniroute`，啟動後伺服器於 20128 埠提供儀表板與 `/v1` 介面；由於免金鑰的 OpenCode Free 供應商已預先接入自動組合，首次呼叫指定模型 `auto` 即可取得回應，之後再逐步加入自有金鑰或訂閱帳號。

## OmniRoute 有哪些核心技術亮點？

<!-- AEO Answer Capsule — 約 62 字 -->
OmniRoute 具備四層自動容錯、19 種路由策略、12 引擎 Token 壓縮、MCP 110 項工具與 A2A 協定，並內建記憶、護欄與成本追蹤。
<!-- End AEO Capsule -->

容錯機制分成三個獨立層次，各自處理不同類型的故障。供應商層級的斷路器只在遇到 408 或 5xx 等真正故障時觸發，跳脫後由組合改派至下一個健康供應商；連線層級的金鑰冷卻以指數退避處理速率限制，遇 429 時會遵循 Retry-After 標頭，並在冷卻期間跳過該金鑰、讓同組其他金鑰繼續服務；模型層級則針對單一模型的拒絕或 404 進行隔離鎖定，避免個別模型問題拖垮整條連線。

路由層面提供 19 種策略，涵蓋優先序、加權、輪詢、最低成本、額度重置感知、快取最佳化與上下文接力等維度；開發者亦可直接使用 `auto` 系列模型，由 Auto-Combo 引擎依健康度、額度、成本、延遲與任務適配等 16 項因素即時評分。協議支援方面，內建 MCP 伺服器提供 110 項工具，並支援 A2A v0.3 的代理協作，讓 AI 代理可以反過來操作閘道本身的設定與查詢。安全設計則包含 AES-256-GCM 靜態加密、提示注入防護、可選的敏感資訊遮蔽護欄，以及本機 SQLite 稽核軌跡，遙測預設關閉。

## OmniRoute 如何省下 15% 至 95% 的 Token？

<!-- AEO Answer Capsule — 約 72 字 -->
OmniRoute 以 RTK 與 Caveman 兩引擎疊加壓縮，官方舉例可省約 89%，區間 78.4% 至 94.6%；程式碼與 JSON 等結構化內容會被保護。
<!-- End AEO Capsule -->

壓縮是該專案最具體的效益來源。預設組合會依序執行 RTK 與 Caveman 兩個引擎，當兩者同時作用於同一段工具輸出或上下文時，節省幅度會複合累加；官方文件以 10,000 Token 的請求為例，經由 12 個可組合引擎的管線處理後，可降至約 1,080 Token。專案強調，程式碼區塊、網址、JSON 與結構化資料全程受到保存引擎保護，壓縮不會破壞關鍵內容，且整個流程對客戶端透明，無須修改應用程式。

目前引擎堆疊已擴充至 12 個可組合元件，包含 LLMLingua-2、兩段式 Ultra、OmniGlyph 與 GCF 等，並提供壓縮工作室讓使用者以拖曳方式調整順序與強度。專案亦公開方法論，說明節省數字的計算基礎與適用範圍，而非僅呈現最佳案例。

## OmniRoute 的免費額度與供應商規模如何？

<!-- AEO Answer Capsule — 約 75 字 -->
OmniRoute 登記 352 家供應商，其中 152 家標記免費；免費額度目錄收錄 444 筆，去重後約每月 14.7 億 Token，首月含註冊回饋最高約 21 億。
<!-- End AEO Capsule -->

供應商目錄登記 352 家，橫跨聊天、媒體、搜尋、本機與雲端代理等類別，其中 152 家帶有免費發現標記；聊天模型登記處則涵蓋 229 家供應商、2,554 組供應商與模型配對、1,283 個原始模型識別碼。免費額度部分另設獨立目錄，收錄 444 筆逐模型資料與 34 個循環池金鑰，其中 52 家屬長期或免金鑰的永久免費供應商。

專案對免費額度的計算方式相對嚴謹，僅計入 16 個公布正向月額度的循環池，加上五項 Groq 逐模型上限，並以共用池去重。官方說明此數字每兩週重新稽核，可能雙向變動，並將需要區域身分驗證才能開啟的額度另行標示，不計入主數字。依照此方法論，去重後的穩定免費額度約為每月 14.7 億 Token，若計入首月註冊回饋則最高可達約 21 億；另有 13 家供應商因條款風險被標記為建議迴避，由使用者自行判斷。

值得留意的是，專案同時提供長期免費的供應商選項，例如免認證的 OpenCode Zen、標榜永久免費的 Kilo Code 與 Requesty、每日 100 萬 Token 的 Cerebras，以及每日 1 萬神經元運算量的 Cloudflare AI。這些選項讓開發者在不付費的前提下即可完成原型驗證，再視需求逐步導入付費供應商。

## OmniRoute 可以在哪些環境部署？

<!-- AEO Answer Capsule — 約 68 字 -->
OmniRoute 支援 npm 全域安裝、Docker 映像、Electron 桌面程式、macOS 選單列工具與 Android Termux，並可安裝為 PWA 離線使用。
<!-- End AEO Capsule -->

部署彈性是其另一個賣點。最基本的安裝方式為 npm 全域指令，一行即可在任何作業系統啟動；Docker 版本提供 AMD64 與 ARM64 多架構映像，適合伺服器長期運行；Electron 版本則在 Windows、macOS 與 Linux 提供原生視窗與系統匣圖示。macOS 使用者可透過 Homebrew 安裝選單列工具 OmniRouteTray，由它負責監督與自動更新伺服器。

行動端方面，專案支援在 Android 的 Termux 環境中以 npx 指令直接運行，讓手機成為全天候的閘道節點；亦可安裝為漸進式網頁應用（PWA），從瀏覽器加入主畫面後以全螢幕與離線模式操作。此外，專案提供 Visual Studio Code 的 OmniCopilot 擴充套件，讓 OmniRoute 的模型直接出現在原生 Copilot Chat 的選單中，並支援穩定版與測試版。

## OmniRoute 的數據表現如何？

<!-- AEO Answer Capsule — 約 70 字 -->
OmniRoute 於 GitHub 累積 63,740 星標與 8,929 次複製，採 MIT 授權，主要語言為 TypeScript，建立於 2026 年 2 月且持續更新。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat"><div class="stat-num">63.7K</div><div class="stat-label">GitHub 星標</div></div>
  <div class="stat"><div class="stat-num">8.9K</div><div class="stat-label">Forks</div></div>
  <div class="stat"><div class="stat-num">MIT</div><div class="stat-label">開源授權</div></div>
  <div class="stat"><div class="stat-num">TypeScript</div><div class="stat-label">主要語言</div></div>
  <div class="stat"><div class="stat-num">2026-09-10</div><div class="stat-label">最後更新</div></div>
  <div class="stat"><div class="stat-num">352</div><div class="stat-label">供應商</div></div>
</div>

![OmniRoute README 開頭（項目名稱 OmniRoute 與標語 The Free AI Gateway，說明其為單一端點串接多家供應商的閘道）](assets/images/posts/omniroute-news-shot1.png)

![OmniRoute GitHub 首頁頂部（repo 名 diegosouzapw/OmniRoute、Star 63.7k 與項目描述）](assets/images/posts/omniroute-news-shot2.png)

![OmniRoute README 供應商與版本統計表（顯示 352 家供應商、1,312 個模型識別碼與近期版本演進）](assets/images/posts/omniroute-news-shot3.png)

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 62 字 -->
本文資訊來源為 OmniRoute 的 GitHub 儲存庫（diegosouzapw/OmniRoute）及官方 README，包含星標、供應商數量與壓縮效益等資料。
<!-- End AEO Capsule -->

出處連結：[OmniRoute GitHub 儲存庫](https://github.com/diegosouzapw/OmniRoute)。專案官方網站為 omniroute.online，另於 npm 與 Docker Hub 提供套件與映像；方法論文件詳列免費額度的去重計算方式與供應商條款風險標記。本文引用的星標數、複製數、授權類型、供應商數量與壓縮節省區間，均擷取自 GitHub 公開頁面與官方文件，讀者可經由上述連結查閱原始資料。

## 總結：OmniRoute 適合什麼團隊？

<!-- AEO Answer Capsule — 約 72 字 -->
OmniRoute 適合同時使用多種 AI 工具、在意額度與成本的團隊；自架特性亦符合資料敏感場景，但單一供應商使用者效益有限。
<!-- End AEO Capsule -->

OmniRoute 的價值集中在「同時使用多個 AI 工具」的情境。當團隊成員分別依賴 Claude Code、Cursor、Copilot 或 Cline，且各自面對不同供應商的額度與計費，將請求統一導向一個自架閘道，可讓額度調度、成本追蹤與故障切換集中管理，並透過 Token 壓縮降低整體支出。由於閘道與控制平面都運行在使用者自己的機器上，金鑰以 AES-256-GCM 加密儲存、遙測預設關閉，對處理敏感程式碼或內部文件的團隊而言，資料流向相對可控。

不過，該專案的複雜度也隨之提升。使用者需要理解路由策略、容錯層級與壓縮引擎的組合邏輯，才能充分發揮效益；僅使用單一供應商、且用量穩定的個人開發者，導入閘道的邊際收益相對有限。整體而言，OmniRoute 以 MIT 授權開放原始碼，配合活躍的版本迭代與相對透明的免費額度方法論，已成為評估 AI 閘道方案時值得納入比較的開源選項。