---
layout: post
title: "Agentic Engineering 入門：Karpathy 的軟體 3.0 新思維，品味比寫程式更重要"
date: 2026-05-05 03:39:00 +0800
categories: [tech]
tags: [AI Agent, Agentic Engineering, 軟體開發, Karpathy, 提示工程, 科技趨勢]
author: Sun ny
image: assets/images/posts/2026-05-05-Agentic-Engineering入門-Karpathy的軟體3-0新思維-cover.webp
description: "Karpathy 提出 Agentic Engineering 概念，宣告軟體 3.0 時代來臨。當 AI Agent 幫你寫程式，開發者的核心能力不再是 coding 技巧，而是「品味」與「判斷力」。一文看懂這個顛覆性新思維。"
---

還記得 Andrej Karpathy 嗎？OpenAI 共同創辦人、前 Tesla AI 總監，那個每次發文都讓科技圈炸鍋的男人。最近他又丟出一顆震撼彈——**Agentic Engineering**（代理工程），說這才是軟體 3.0 時代的真正核心。

你可能會想：又一個新名詞？跟 Vibe Coding 差在哪？跟我有什麼關係？別急，這篇文章帶你從零搞懂。

## 軟體 1.0 → 2.0 → 3.0：開發典範的三次跳躍

要理解 Agentic Engineering，先回頭看 Karpathy 之前提出的軟體版本論：

- **軟體 1.0**：人類手寫每一行邏輯，if-else、for 迴圈，一切自己來。這是我們最熟悉的傳統程式開發。
- **軟體 2.0**：人類提供資料和神經網路架構，讓機器學習出規則。神經網路的「權重」取代了人類寫的程式碼。
- **軟體 3.0**：人類用自然語言對 AI Agent 下指令，Agent 自動生成程式碼、測試、部署。人類的角色從「寫程式」變成「指揮」。

軟體 3.0 不是理論，它正在發生。你打開 Cursor、Windsurf 或 GitHub Copilot，就已經在體驗它了。

## Vibe Coding vs. Agentic Engineering：差在哪？

很多人把「用 AI 寫程式」統稱為 Vibe Coding——那種「隨手打個 prompt、看看出來什麼、再修一修」的隨性風格。Karpathy 自己也用 Vibe Coding 做小專案，但他明確指出：**Vibe Coding 不等於 Agentic Engineering**。

差別在哪？

| | Vibe Coding | Agentic Engineering |
|---|---|---|
| **心態** | 隨性、試探 | 系統性、工程化 |
| **過程** | prompt → 看結果 → 微調 | 設計 → 指派 → 驗證 → 迭代 |
| **適用** | 小專案、原型 | 大型系統、產品 |
| **品質** | 看運氣 | 可控、可重現 |

簡單說：**Vibe Coding 是隨手塗鴉，Agentic Engineering 是建築設計**。兩者都用到 AI，但後者把 Agent 當成團隊成員，需要規劃、分工、審查。

## 為什麼「品味」比寫程式更重要？

這是 Karpathy 最引人注目的觀點：在軟體 3.0 時代，開發者的核心競爭力不再是 coding 技巧，而是**品味（Taste）**。

什麼是品味？他說的是：

- **判斷什麼該做、什麼不該做**：AI 可以生成一百種方案，但只有你能決定哪一種是對的。
- **辨識好設計與壞設計**：程式碼 AI 寫得出，架構好不好只有人類能判斷。
- **在模糊中做決策**：需求不明確時，AI 會等你；品味讓你果斷選擇方向。

打個比方：AI 是廚房裡的超級助手，可以切菜、調火候、擺盤。但**菜單要你來定，味道要你來嘗**。沒有品味的廚師，即使有最好的幫手，也做不出米其林等級的料理。

## Agentic Engineering 的實戰心法

說了這麼多概念，實際怎麼做？以下整理三個關鍵實踐：

### 1. 把 Agent 當初級工程師，但你是 Tech Lead

別期待 Agent 一次到位。給它明確的任務邊界、驗收標準，然後**審查它的產出**。就像你帶 junior 工程師一樣：交代清楚、驗收嚴格、適時修正。

### 2. 用 prompt 寫 spec，不是寫程式

你的 prompt 不該是「幫我寫一個 login function」，而是「這個登入功能需要支援 email 和手機號碼兩種方式，錯誤訊息要友善、要擋 brute force、密碼要用 bcrypt」。**描述你要什麼，而不是怎麼做**。

### 3. 迭代比完美重要

先讓 Agent 跑出一版，再逐一修正。不要在一個 prompt 裡塞入所有需求——拆成小任務、逐步迭代，反而更可控。

## 非工程師也該關注的原因

你可能不是開發者，但 Agentic Engineering 的影響遠超過程式圈：

- **行銷人員**用 Agent 自動生成 A/B 測試文案
- **產品經理**用 Agent 快速做競品分析
- **創業者**用 Agent 一人完成 MVP 原型

麥肯錫最新報告更指出：**近七成行銷工作將被 AI 接手**。這不是危言聳聽，而是正在加速的現實。關鍵不是「會不會被取代」，而是「會不會用 Agent 放大自己的能力」。

## 從今天開始的三個行動

1. **試用一個 AI 編程工具**：Cursor、Windsurf、GitHub Copilot，選一個上手。不用會寫程式，會描述需求就行。
2. **練習寫好 prompt**：把你的需求當 spec 寫，越具體越好。這就是軟體 3.0 時代的核心技能。
3. **培養品味**：多看好產品、好設計、好架構。當 AI 幫你把執行成本降到零，決策品質就是你的天花板。

軟體 3.0 的世界裡，**會寫程式不再是護城河，會判斷才是**。Karpathy 說得好：「未來的 10x 工程師，不是寫程式快十倍的人，而是能讓 Agent 產出十倍價值的人。」

你準備好升級了嗎？
