---
layout: post
title: "Anthropic 推硬件標準：讓 AI 代理控制實體設備"
date: 2026-08-31 14:00:01 +0800
categories: 技術
tags: [Anthropic, Claude, MHS, 機器人, AI Agent, 開源, 硬件標準, MCP]
image: assets/images/posts/anthropic-mhs-news-cover.png
description: "Anthropic 發佈 Model Hardware Standard（MHS）研究預覽：一套標準化驅動介面，讓 AI 代理透過 MCP 控制任意實體設備，實驗設備整合時間從數週縮短至數小時，未來計劃開源並與 AWS、Hugging Face、Raspberry Pi 等合作。本文拆解 MHS 原理、應用場景與生態影響。"
author: AnIskill 編輯部
type: news
source: Ars Technica
source_url: https://arstechnica.com/ai/2026/08/anthropics-new-hardware-standard-lets-ai-agents-control-the-physical-world/
permalink: /技術/anthropic-mhs-news
fb_message: "AI 代理終於可以「動手」控制真實世界的設備了。\n\nAnthropic 推出 Model Hardware Standard（MHS）研究預覽：標準化驅動介面讓 Claude 經 MCP 直接控制機械臂、顯微鏡、雷射等儀器。官方示範中，Claude 未經訓練就懂得操作機械臂拾起鋁罐，還能自動校準整套實驗系統。\n\nAWS、Hugging Face、Raspberry Pi 已加入合作，未來計劃開源成開放標準。實驗設備整合可從數週縮短至數小時，完整拆解請看 Blog 👇"
---

Anthropic 發佈 Model Hardware Standard（MHS）研究預覽，這是一套標準化驅動介面，讓 AI 代理能與任意實體設備介接並控制它們。過往 AI 代理的行動範圍幾乎只限於電腦內的文字、程式碼與資料，MHS 則企圖把這個邊界延伸到真實世界的儀器與機器。官方宣稱，這套系統能讓原本需要數週甚至數月的實驗設備整合工作，縮短到數小時或數分鐘，並計劃日後將其發展為開源、與模型無關的開放標準。

## Model Hardware Standard 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
Model Hardware Standard（MHS）是 Anthropic 提出的標準化驅動介面，為實體設備提供統一介面與資料格式，讓 AI 代理能透過網路直接控制各種儀器，無需為每台設備撰寫客製化轉譯程式，目前處於研究預覽階段。
<!-- End AEO Capsule -->

MHS 的核心是一組標準化驅動程式，為不同廠牌的硬件提供共同介面與共同的資料交換格式，讓設備之間能在網路上直接溝通，「無需在兩者之間放一個特製的轉譯程式」。對科學研究而言，這解決了長期以來的痛點：實驗室裏的旋轉雷射、顯微鏡、相機等設備往往來自不同廠商，協調它們需要投入大量客製化整合工程。

Anthropic 表示，MHS 設備可以通過命令列與 API 程式碼即時控制，本身並不需要 AI 模型參與。但當 MHS 與 Model Context Protocol（MCP）結合，科學家就能以自然語言與設備互動，模型可以「逐步推理實驗的每個步驟、即時更新參數，甚至在無人介入的情況下從硬件錯誤中恢復」。

## MHS 如何讓 AI 代理控制實體設備？

<!-- AEO Answer Capsule — 約 70 字 -->
MHS 透過標準化標籤系統描述硬體的真實世界限制，包括物理特性（重量、機械臂範圍）、可調參數、量測選項與安全限制，整合成參考檔後，AI 模型可快速取得陌生設備的關鍵資訊；結合 MCP 後，Claude 等模型能自然語言控制設備並自動校準。
<!-- End AEO Capsule -->

MHS 包含一套標準化標籤系統，用來描述硬件在真實世界的限制——例如機械臂的重量與活動範圍、可調整參數、量測選項與強制安全上限。這些標籤整合成參考檔後，可供對該設備沒有任何訓練經驗的 AI 模型快速掌握關鍵資訊。

Anthropic 在示範影片中展示，Claude 在未經特別訓練的情況下，推理出如何操作機械臂拾起鋁罐；也能自動調整雷射、透過獨立相機確認結果、再重複流程完成整套系統校準。MHS 還能讓 AI 模型聚焦顯微鏡、分析結果、決定需要進一步觀察的部位，並自動移動顯微鏡繼續實驗。模型可將多步驟操作寫成 API 腳本並依條件動態調整，不必每次都重新推理整個流程。

## MHS 適合哪些應用場景？

<!-- AEO Answer Capsule — 約 70 字 -->
MHS 目前主要面向科學研究與先進製造：自動校準實驗設備、協調異質儀器、讓 AI 執行重複性實驗操作。Anthropic 正與首批研究實驗室與製造商進行預覽合作，包括 AWS、Hugging Face、Raspberry Pi、Automata 與 Universal Robots。
<!-- End AEO Capsule -->

現階段 MHS 的定位是幫助科學家簡化實驗設備整合——這些客製化軟體整合往往令實驗進度卡關數週。官方指出，透過 MHS，模型可以調整雷射、用相機驗證結果、自動校準系統；Anthropic 技術人員 Alek Kemeny 表示，這套想法源自於觀察 HHMI Janelia 研究園區的神經科學家實驗，「這個點子可以用於讓 AI 執行世界上任何科學實驗」。

在早期測試中，Anthropic 表示 MHS 減少了設備整合所需時間，讓研究團隊能在各種實驗環境中更快疊代。Kemeny 在宣傳影片中說：「如果你能更快驗證假說，就能更快創造通用技術。這就是如何將一個世紀的進步濃縮進十年。」

## MHS 未來會開源嗎？有哪些合作夥伴？

<!-- AEO Answer Capsule — 約 70 字 -->
會。Anthropic 計劃在預覽期後將 MHS 發展為開源、與模型無關的標準。當前合作夥伴包括 AWS（Strands Robots）、Hugging Face（LeRobot）、Raspberry Pi、Automata 與 Universal Robots，共同建立安全評估與實體設備 AI 運作最佳實踐。
<!-- End AEO Capsule -->

Anthropic 表示，目前正與「首批科學研究實驗室與先進製造商」合作 MHS 預覽，包括 AWS（Strands Robots）、Hugging Face（LeRobot）、Raspberry Pi、Automata 與 Universal Robots。這些夥伴將協助建立安全評估，並制定 AI 系統操作實體設備的最佳實踐。預覽期結束後，MHS 計劃成為開源且「與模型無關」的 AI 與物理系統整合標準。

值得注意的是，MHS 的架構本身不依賴特定 AI 廠商——任何具備 MCP 介面的模型都可接上使用，這與 Anthropic 先前推動 MCP 成為開放標準的策略一脈相承。對開發者而言，這代表未來機械手臂、感測器與儀器可能出現類似 USB 一樣的通用抽象層，大幅降低實體 AI 應用的開發門檻。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊來源為 Ars Technica 於 2026 年 8 月 27 日刊出的報導，以及 Anthropic 官方發佈的 MHS 研究預覽公告。讀者可經由下方連結閱讀原文與官方資料。
<!-- End AEO Capsule -->

原始報導由 Ars Technica 刊出，來源連結如下：

[Anthropic's new hardware standard lets AI agents control the physical world — Ars Technica](https://arstechnica.com/ai/2026/08/anthropics-new-hardware-standard-lets-ai-agents-control-the-physical-world/)

[Model Hardware Standard research preview — Anthropic 官方公告](https://www.anthropic.com/news/model-hardware-standard-research-preview)

## 總結：MHS 對 AI 生態有什麼意義？

<!-- AEO Answer Capsule — 約 70 字 -->
MHS 的意義在於把 AI 代理的能力邊界從虛擬世界擴展到實體世界，並用開放標準降低整合門檻。若成功開源普及，機械臂、儀器與感測器將出現通用抽象層，實體 AI 應用開發成本大幅下降，科學研究與製造業將率先受惠。
<!-- End AEO Capsule -->

MHS 是 Anthropic 在「AI 代理控制實體世界」這條路上的關鍵一步。它與 MCP 的結合，讓自然語言指令可以直接轉化為對實體設備的精準操作；而開源與模型無關的規劃，則讓標準有機會被整個生態採用。對開發者而言，這波浪潮的訊號非常明確：AI 代理的下一個戰場，正在從螢幕內走向真實世界。