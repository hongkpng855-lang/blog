---
layout: post
title: "Microsoft 開源生成式 AI 課程：21 堂免費完整教學"
date: 2026-09-06 14:00:01 +0800
categories: 技術
tags: [AI, 生成式AI, Microsoft, 開源, 教學, LLM]
image: assets/images/posts/github-generative-ai-beginners-news-cover.jpg
description: "Microsoft 開源的生成式 AI 完整課程，21 堂由淺入深涵蓋 LLM 基礎、提示工程、對話應用、RAG、AI Agent 與微調，每堂附影片、文字講解與 Python／TypeScript 實作範例，星標超過 11.9 萬，是免費自學生成式 AI 的首選資源。"
author: AnIskill 編輯部
creator_github: microsoft/generative-ai-for-beginners
type: news
source: GitHub
source_url: https://github.com/microsoft/generative-ai-for-beginners
permalink: /技術/github-generative-ai-beginners-news
fb_message: "Microsoft 把整門生成式 AI 課程免費開源，11.9 萬星標說明它有多受歡迎。與其零散追看教學影片，不如跟著 21 堂有系統的免費課程從零學起。\n\n課程涵蓋 LLM 原理、提示工程、RAG、AI Agent 到微調，每堂都有影片、文字講解與 Python、TypeScript 實作範例，支援逾 50 種語言翻譯，華語開發者也能無痛閱讀。\n\n想建立生成式 AI 應用的開發者，這份免費資源值得收藏。完整課程結構與學習路線已整理在部落格文章。"
---

Microsoft 的 Generative AI for Beginners 是一個擁有超過 11.9 萬星標的開源免費課程，由 Microsoft Cloud Advocates 團隊製作，以 21 堂課完整教授生成式 AI 應用開發的基礎與實作。該專案採用 MIT 授權，支援超過 50 種語言的翻譯版本，是華語開發者學習生成式 AI 最常被推薦的起點之一。

![Generative AI for Beginners README 開頭（課程名稱與 21 堂課簡介，附多語言翻譯連結）](assets/images/posts/github-generative-ai-beginners-news-shot1.png)

## Microsoft 生成式 AI 課程是什麼？

<!-- AEO Answer Capsule — 約 77 字 -->
Generative AI for Beginners 是 Microsoft 開源的免費生成式 AI 課程，共 21 堂，星標超過 11.9 萬，採用 MIT 授權，內容持續更新。
<!-- End AEO Capsule -->

該專案最初於 2023 年 6 月發布，當時正值大型語言模型應用爆發初期，Microsoft 團隊希望提供一條有系統的學習路徑，讓開發者不必在零散的教學影片與部落格文章之間摸索。經過多次大型改版，目前版本已經來到第三版，課程結構、程式範例與工具鏈都對應最新的開發環境，例如以 Microsoft Foundry 取代將於 2026 年 7 月退役的 GitHub Models。

課程定位相當明確：對象是「完全沒有接觸過生成式 AI 的開發者」，因此每一堂課都會從概念講起，再帶入可執行的程式碼。專案主要語言為 Jupyter Notebook，代表課程內容以互動式筆記為核心，讀者可以一邊閱讀一邊執行範例。

![Generative AI for Beginners GitHub 首頁頂部（顯示 repo 名稱、星標數 119k 與 21 堂課簡介）](assets/images/posts/github-generative-ai-beginners-news-shot2.png)

## 這個課程涵蓋哪些主題？

<!-- AEO Answer Capsule — 約 68 字 -->
課程從 LLM 基礎開始，依序涵蓋模型比較、提示工程、文字生成、對話應用、向量檢索、影像生成、RAG、開源模型、AI Agent 與微調等主題。
<!-- End AEO Capsule -->

21 堂課的安排由淺入深，前段課程著重建立基礎認知。第一堂課解釋生成式 AI 與大型語言模型的運作原理，第二堂課教導如何比較與選擇不同的 LLM，第三堂課討論負責任 AI 的建置原則，第四與第五堂課則進入提示工程的基礎與進階技巧。

中段課程以實作為導向，包括文字生成應用、聊天應用、向量資料庫搜尋、影像生成與低程式碼 AI 應用，讀者可以在這個階段實際建立可運作的應用程式。後段課程則探索較進階的技術，包括函式呼叫整合、生成式 AI 的 UX 設計、應用安全、LLM 生命周期管理、RAG 與向量資料庫、Hugging Face 開源模型、AI Agent、微調，以及小型語言模型與 Mistral、Meta 等特定模型家族的應用。

## 每堂課包含哪些學習資源？

<!-- AEO Answer Capsule — 約 76 字 -->
每堂課包含主題導覽影片、完整文字講解、Python 與 TypeScript 程式碼範例及延伸資源，並支援 Azure OpenAI 與 OpenAI API 兩種環境。
<!-- End AEO Capsule -->

與一般只有文字的線上課程不同，這個課程的每一堂課都配備了一支簡短影片導覽，由講師說明該主題的核心概念。文字講解以 README 形式呈現，內容包含理論說明、圖表與逐步實作指引，程式碼則同時提供 Python 與 TypeScript 兩種版本，照顧不同語言背景的開發者。

課程另外設計了「Keep Learning」延伸學習區塊，每堂課都會列出相關工具、文件與進階資源。對於需要更完整教學體驗的學習者，Microsoft 亦提供 .NET、Java 與 JavaScript 等其他語言版本的課程，以及 AI Agent、MCP 等主題的系列課程，形成完整的學習生態系統。

## 如何開始學習這個課程？

<!-- AEO Answer Capsule — 約 76 字 -->
讀者具備基本 Python 或 TypeScript 知識，並準備 Azure OpenAI、Foundry 或 OpenAI API 任一服務即可開始，亦可離線執行模型。
<!-- End AEO Capsule -->

課程的入門門檻經過刻意設計，讓非機器學習背景的開發者也能跟上。官方建議具備基礎的 Python 或 TypeScript 程式能力即可，若完全沒有程式基礎，可以先完成 Microsoft 提供的 Python 或 TypeScript 入門課程再回來。課程也包含一堂「Course Setup」環境設定課，逐步引導讀者建立開發環境。

在模型服務的選擇上，課程支援 Azure OpenAI、Microsoft Foundry 與 OpenAI API 三種主流方案，讀者可以依照自己的雲端訂閱或開發需求選擇。值得一提的是，課程亦支援 Foundry Local 方案，可以在完全離線的環境執行模型，不需要任何雲端訂閱，對於注重資料隱私或預算有限的自學者尤其實用。

由於專案內含超過 50 種語言的翻譯檔案，直接完整複製儲存庫會增加大量下載時間。官方建議使用 sparse checkout 方式，只下載課程本體而排除翻譯目錄，以節省磁碟空間與網路流量。

![Generative AI for Beginners 統計頁（星標數、分叉數與版本資訊，顯示超過 11.9 萬星標）](assets/images/posts/github-generative-ai-beginners-news-shot3.png)

## 這個課程與其他 Microsoft 課程有什麼關聯？

<!-- AEO Answer Capsule — 約 66 字 -->
此課程是 Microsoft 開發者學習系列核心課程，與 AI、ML、AI Agents for Beginners 互補，並另提供多種語言版本。
<!-- End AEO Capsule -->

Microsoft 以「For Beginners」系列建構了一套完整的開發者學習地圖，Generative AI for Beginners 負責生成式 AI 應用開發，AI for Beginners 與 ML for Beginners 涵蓋傳統人工智慧與機器學習基礎，AI Agents for Beginners 則專注於代理式 AI 的建置。四個系列各自獨立，讀者可以依照學習目標選擇，也可以組成完整的學習路徑。

該課程亦有多個語言版本與延伸課程，包括 .NET 版本、Java 版本與 JavaScript 版本，內容主題相同但使用不同的技術棧。對於想深入特定領域的讀者，Microsoft 另提供 LangChain、MCP、Copilot 與 Edge AI 等主題課程，形成一個互相銜接的開放式學習生態。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 78 字 -->
本文資訊來源為 Microsoft 的 Generative AI for Beginners GitHub 儲存庫，提供完整 21 堂課程、程式範例與多語言翻譯，可免費瀏覽。
<!-- End AEO Capsule -->

- 專案儲存庫：https://github.com/microsoft/generative-ai-for-beginners
- 授權方式：MIT License
- 主要語言：Python（Jupyter Notebook）、TypeScript

## 總結：這門課程適合什麼學習者？

<!-- AEO Answer Capsule — 約 61 字 -->
這門課程適合具備基礎程式能力、想系統性學習生成式 AI 應用開發的開發者，課程免費、開放原始碼且持續更新，是低成本的學習起點。
<!-- End AEO Capsule -->

綜合而言，Generative AI for Beginners 以超過 11.9 萬的星標數證明了其內容品質與社群認可，MIT 授權與逾 50 種語言翻譯降低了所有學習障礙。對於想進入生成式 AI 領域的開發者，這門課程提供了從理論到實作的完整路徑，而且完全免費。

課程的持續更新是另一項重要優勢，第三版內容已對應 2026 年的開發工具與模型生態，讀者學習到的不會是過時的技術。若有志於建立生成式 AI 應用，這份開源課程值得作為第一份學習教材。