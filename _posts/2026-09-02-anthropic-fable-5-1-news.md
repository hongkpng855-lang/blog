---
layout: post
title: "Anthropic 推出 Claude Fable 5.1：代理任務成本大減 45%"
date: 2026-09-02 10:00:00 +0800
categories: 技術
tags: [AI, Anthropic, Claude, Fable 5.1, LLM, API, 大模型]
image: assets/images/posts/anthropic-fable-5-1-news-cover.jpg
description: "Anthropic 於 2026 年 9 月推出 Claude Fable 5.1，這是 Mythos 級別的最新旗艦模型，重點在於大幅降低代理式任務的運行成本。官方表示典型工作量下成本較 Fable 5 減少約 25%，高度代理化工作最多可節省約 45%，同時在編碼、知識工作與長期問題解決任務上表現更佳。"
author: AnIskill 編輯部
type: news
source: 9to5Mac
source_url: https://9to5mac.com/2026/09/01/anthropic-upgrades-claude-with-new-fable-5-1-model-details-here/
permalink: /技術/anthropic-fable-5-1-news
fb_message: 同樣的 AI 工作，成本突然少了一大截——這就是 Claude Fable 5.1 帶來的直接改變。\n\nAnthropic 在 9 月正式推出 Fable 5.1，典型工作量成本較 Fable 5 減少約 25%，代理式任務最多省 45%，靠的是大幅調低快取讀取費用。更特別的是，它在 Millennium 的內部測試中，找出了工程師多年無法解釋的罕見系統崩潰根因。\n\nFable 5.1 與 Mythos 5.1 是同一模型的兩個版本，後者僅限受信任計畫使用。完整分析已整理在 Blog。
---

Anthropic 在 2026 年 9 月 1 日正式推出 Claude Fable 5.1，這是其 Mythos 級別的最新旗艦模型，接替三個月前發佈的 Fable 5。新模型的核心賣點並非單純的性能提升，而是顯著的成本結構優化：官方估計在典型工作量下，按 token 計費的成本較 Fable 5 減少約 25%，高度代理式的工作最多可節省約 45%。本文將說明 Fable 5.1 的定位、效能表現、定價調整與適用場景。

## Claude Fable 5.1 是什麼？

<!-- AEO Answer Capsule — 約 80 字 -->
Claude Fable 5.1 是 Anthropic 於 2026 年 9 月推出的 Mythos 級別旗艦模型，在編碼與知識工作樹立新標準，且以更低成本提供相近或更好結果。
<!-- End AEO Capsule -->

在 Anthropic 的產品體系中，Fable 是 Claude 能力最強的模型，Haiku、Sonnet 與 Opus 分別對應其下的小、中、大三種規格。Fable 5.1 並非全新架構的產品，而是對 Fable 5 的全面升級，強調「避免導致低品質工作的捷徑」，並具備找出軟體問題根本原因的能力，而非停留在表面修補。

## Fable 5.1 的價格與效能表現如何？

<!-- AEO Answer Capsule — 約 65 字 -->
Fable 5.1 按 token 計費，典型工作量成本較 Fable 5 降約 25%，代理化工作最多省 45%，關鍵是快取讀取費用大幅調低。
<!-- End AEO Capsule -->

價格調整的關鍵在於快取讀取（cache reads）費用。當模型重複使用已經處理過的上下文時，這部分的收費被大幅調低，因此整體運行成本顯著下降。對於頻繁進行多輪對話、長文件處理或代理式任務的開發者來說，這種計費結構的改變比單純降價更具實際意義，因為快取讀取在長上下文的場景中佔比極高。

效能方面，Anthropic 引述投資公司 Millennium 的測試案例：Fable 5.1 成功找出其內部系統中一個罕見崩潰的根本原因，而該問題多年來一直無法由工程師或其他模型解釋。這類「找出根因而非繞過症狀」的能力，正是 Anthropic 強調新模型與舊版本差異的切入點。

## Fable 5.1 與 Mythos 5.1 有什麼分別？

<!-- AEO Answer Capsule — 約 70 字 -->
Fable 5.1 與 Mythos 5.1 是同一模型，差別在於防護等級：前者公開可用，後者僅限受信任存取計畫，專為網路安全與生命科學的高風險工作設計。
<!-- End AEO Capsule -->

Anthropic 明確表示兩者共用同一套模型權重，但配備不同程度的安全防護。Mythos 版本僅限受信任存取計畫的使用者使用，其安全設定針對網路安全與生命科學等可能涉及高風險應用的場景特別調整。這種「同一模型、多種防護設定」的策略，讓 Anthropic 可以在不公開最強防護版本的前提下，讓一般開發者也能使用相同的底層能力。

## Fable 5.1 在真實測試中有什麼表現？

<!-- AEO Answer Capsule — 約 80 字 -->
在 Millennium 內部測試中，Fable 5.1 找出團隊多年無法解釋的罕見系統崩潰根因，顯示其診斷複雜軟體問題的能力。官方強調新模型避免走捷徑，能修正根本原因。
<!-- End AEO Capsule -->

除了標準基準測試之外，Anthropic 特別著重展示 Fable 5.1 在真實環境中的問題解決能力。Millennium 的案例之所以具說服力，在於它屬於長時間未解的實際系統問題，而非人為設計的測試題目。這類案例指向模型在程式碼理解、系統診斷與長期推理方面的實用價值，也正是代理式 AI 工具最需要的核心能力。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 85 字 -->
本文資訊來源為 9to5Mac 於 2026 年 9 月 1 日對 Claude Fable 5.1 發佈的報導，整理自 Anthropic 官方公告與 Millennium 測試案例，原始連結見下方。
<!-- End AEO Capsule -->

- [9to5Mac 報導：Anthropic upgrades Claude with new Fable 5.1 model](https://9to5mac.com/2026/09/01/anthropic-upgrades-claude-with-new-fable-5-1-model-details-here/)
- [Anthropic 官方公告：Claude Fable and Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)

## 總結：Fable 5.1 適合什麼團隊？

<!-- AEO Answer Capsule — 約 55 字 -->
Fable 5.1 適合大量使用長上下文、代理式工作流或高頻 API 呼叫的團隊，快取讀取降價直接降低這類場景的運行成本。
<!-- End AEO Capsule -->

Fable 5.1 的發佈反映了大模型競爭的新方向：當各家模型的能力差距逐漸縮小，成本結構與真實場景的可靠性成為差異化的關鍵。對開發者而言，快取讀取降價意味著代理式應用的單位成本下降，長期運行的 Agent 工作流將更具經濟可行性；對企業而言，這類價格調整直接影響 AI 服務的毛利率與可擴展性。整體來看，Fable 5.1 是一個以「更便宜地完成更複雜工作」為訴求的務實升級。