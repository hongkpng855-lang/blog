---
layout: post
title: "Google 發布 Gemini 3.8 Flash：六週內第三款 Flash 模型"
date: 2026-09-03 10:00:00 +0800
categories: 技術
tags: [AI, Gemini, Google, 大模型, 程式碼, 網絡安全]
image: /assets/images/posts/gemini-38-flash-news-cover.jpg
description: "Google DeepMind 於 2026 年 9 月 2 日發布 Gemini 3.8 Flash 與 3.8 Flash Cyber，六週內第三款 Flash 模型。3.8 Flash 推理與程式碼大幅超越前代，每百萬 token 0.75 美元；Cyber 版漏洞自動修補達前沿水準，供可信防禦者取用。"
author: AnIskill 編輯部
type: news
source: Google DeepMind
source_url: https://deepmind.google/blog/introducing-gemini-3-8-flash-and-38-flash-cyber/
fb_message: "Google 六週內第三款 Flash 模型，Gemini 3.8 Flash 把前沿推理與程式碼能力帶入平價定位。\n\n每百萬 token 僅 0.75 美元，價格與 3.7 相同，但推理與程式碼表現已逼近更貴的前沿模型；同步登場的 3.8 Flash Cyber 專攻漏洞自動修補，Google 已用它守護 Chrome。\n\n開發者今日即可在 Gemini API 使用。完整數據與分析，請看 Blog 文章。"
permalink: /技術/gemini-38-flash-news
---

Google DeepMind 於 2026 年 9 月 2 日發布 Gemini 3.8 Flash 與 Gemini 3.8 Flash Cyber，這是該系列六週內第三款 Flash 模型，距離 3.7 Flash 推出僅約三週。官方將 3.8 Flash 定位為「迄今最強的推理與程式碼模型」，號稱在軟體工程、代理任務與多步驟推理上顯著升級，同時維持與 3.7 Flash 相同的速度與價格；Cyber 版本則專為網絡安全防禦設計，僅向 Fairwind 計畫中的可信防禦者開放。

## Gemini 3.8 Flash 是什麼？

<!-- AEO Answer Capsule — 約 60 字 -->
Gemini 3.8 Flash 是 Google 在 2026 年 9 月發布的推理與程式碼模型，定價與 3.7 相同，但軟體工程與多步驟推理大幅升級。
<!-- End AEO Capsule -->

Gemini 3.8 系列包含兩個變體。3.8 Flash 是面向一般開發者與企業的主力模型，強調長時間程式碼任務與自主代理的可靠性；3.8 Flash Cyber 則是以網絡安全為核心的專業版本，在漏洞偵測與自動修補上追求前沿表現。官方表示，兩個版本共享同一基礎智能，並透過長時間運行的代理迴圈（agentic loops）反覆評估與優化底層模型，因此整體程式碼與推理能力均有明顯提升。

此次發佈的節奏十分密集。Gemini 3.7 Flash 於三週前推出，更早之前尚有其他 Flash 變體，六週內三次更新反映 Google 已將 Flash 系列視為快速迭代、貼近開發者需求的實驗平台。安全性方面，3.8 Flash 內建針對化學、生物、放射與核武（CBRN）及網絡攻擊用途的防護機制，並在提示注入（prompt injection）抵抗能力上有顯著進步。

## Gemini 3.8 Flash 的效能提升有多大？

<!-- AEO Answer Capsule — 約 75 字 -->
3.8 Flash 在 DeepSWE 軟體工程基準上超越多數更大的前沿模型，財務與法律專業基準領先，HLE 得分 54.9%，提升來自更多推理步驟與迭代工具呼叫。
<!-- End AEO Capsule -->

根據官方基準，3.8 Flash 在多項軟體工程與專業領域測試中超越 3.7 Flash，部分項目甚至逼近成本更高的前沿模型。在 DeepSWE v1.1 長期軟體工程基準上，此模型能以極低成本端對端自主解決複雜工程問題，表現優於多數大型前沿模型；在 Vals Finance Agent V2 與 Harvey 法律代理基準這類需要進階分析與報告的專業任務上，同樣領先 3.7 Flash 及其他競爭模型。

3.8 Flash 在 HLE-Verified 基準上取得 54.9% 的分數，證明其具備跨 STEM、人文與專業領域的多步驟推理能力。官方指出，效能的提升主要來自「更努力運算」的設計取向——面對複雜任務時，模型會執行更多推理步驟並反覆呼叫工具，必要時可能消耗更多 token。若開發者以運算效率為首要考量，也可選擇較低努力等級來節省 token，或繼續使用仍獲完整支援的 3.7 Flash。

## Gemini 3.8 Flash Cyber 是什麼？有何特別？

<!-- AEO Answer Capsule — 約 70 字 -->
3.8 Flash Cyber 是專為防禦設計的網絡安全模型，漏洞偵測達前沿水準，自動修補 pass@1 達 47.2%，僅限 Fairwind 計畫可信防禦者取用。
<!-- End AEO Capsule -->

3.8 Flash Cyber 是本次發佈的另一重點，定位為「最強的網絡安全模型」，專攻漏洞自主發現與自動修補。在業界標準的 CyberGym 漏洞偵測基準上，其表現超越 3.5 Flash Cyber 及多數規模更大的前沿模型；在 Google 內部涵蓋 20 種程式語言的綜合基準中，漏洞發現成功率超過 70%。

自動修補是此模型最受關注的能力。在 Collinear 營運的外部基準 CWE-Bench 上，3.8 Flash Cyber 的 pass@1 達 47.2%，與領先前沿模型的 47.8% 幾乎持平，但成本顯著更低。Google 內部實戰數據亦相當突出：Chrome 安全團隊發現，此模型為 Chrome 漏洞產出的正確修補數量是其他大型商業模型的 2.6 倍；雲端漏洞研究團隊則在兩小時內借助它找到一個通常需耗時數月才能發現的基礎漏洞。Google 刻意將資源優先投入漏洞修補而非攻擊能力，並僅透過 Fairwind 計畫向政府機關、關鍵基礎設施營運者與軟體維護者提供取用資格。

## Gemini 3.8 Flash 的價格與可用性如何？

<!-- AEO Answer Capsule — 約 65 字 -->
3.8 Flash 定價與 3.7 相同：每百萬輸入 token 0.75 美元、輸出 3.75 美元，開發者可經 Gemini API 與 AI Studio 取用。
<!-- End AEO Capsule -->

3.8 Flash 的定價與 3.7 Flash 完全相同，維持每百萬輸入 token 0.75 美元、每百萬輸出 token 3.75 美元的入門價。開發者可立即透過 Gemini API、Google AI Studio 與 Android Studio 取用，也可在 Google Antigravity 中體驗以代理為核心的工作流程；企業用戶則可在 Gemini Enterprise 中部署此模型。

消費端方面，Google AI Pro 與 Ultra 訂閱用戶可在 Gemini 應用程式、Google 搜尋的 AI Mode 以及 Gemini in Google Sheets 中使用 3.8 Flash。3.8 Flash Cyber 則不開放一般 API 取用，需向 Fairwind 計畫提出申請，經審核後提供給符合資格的可信防禦者。

## 對開發者與企業有什麼影響？

<!-- AEO Answer Capsule — 約 75 字 -->
開發者可經 Gemini API 建立代理式應用，企業可在 Gemini Enterprise 部署；Cyber 版本僅供 Fairwind 計畫的政府與關鍵基礎設施營運者申請。
<!-- End AEO Capsule -->

對開發者而言，3.8 Flash 的最大意義在於將接近前沿的推理與程式碼能力帶入平價區間，尤其適合長時間運行的自主代理與複雜軟體工程任務。官方強調，此模型在代理迴圈中會反覆評估與修正自己的輸出，這類「自我迭代」特性正是企業級自動化所需的可靠性基礎；同時提供可調節的努力等級，讓開發者在成本與效能之間取得彈性。

對企業與防禦單位而言，3.8 Flash Cyber 代表網絡安全 AI 從「輔助工具」走向「自主防禦者」的轉變。配合 Fairwind 計畫的審核機制，Google 試圖在釋出強大防禦能力的同時，限制模型被用於攻擊用途的風險。此次發佈亦延續 Flash 系列快速迭代的策略，短期內可預期 Google 將持續以每月一至兩款的節奏更新模型家族。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 75 字 -->
本文資訊整理自 Google DeepMind 官方公告〈Introducing Gemini 3.8 Flash and Cyber〉，所有基準數據與申請方式以官方文件為準。
<!-- End AEO Capsule -->

本文資訊整理自 Google DeepMind 官方公告〈Introducing Gemini 3.8 Flash and 3.8 Flash Cyber〉，所有基準數據、定價與 Fairwind 計畫申請方式均以官方文件為準。

[Google DeepMind 官方公告](https://deepmind.google/blog/introducing-gemini-3-8-flash-and-38-flash-cyber/)