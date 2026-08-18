---
layout: post
title: "74,143 星開源項目：screenshot-to-code — 截圖秒轉代碼"
date: 2026-08-18 20:00:00 +0800
categories: 技術
tags: [screenshot-to-code, 截圖轉代碼, AI 生成程式, 前端開發, Tailwind, React, Vue, FastAPI, 開源軟體, Python]
image: /assets/images/posts/github-screenshot-to-code-news-hk-cover.jpg
description: "screenshot-to-code 是 GitHub 星標超過 7.4 萬的開源 AI 專案，由開發者 abi 建立，只要丟進一張螢幕截圖或設計圖，就能在數秒內轉換成乾淨、可執行的程式碼，支援 HTML+Tailwind、React、Vue、Bootstrap 等多種前端技術棧，並可搭配 Gemini、GPT、Claude 等主流模型生成，採用 MIT 授權。"
author: AnIskill 編輯部
creator_github: abi/screenshot-to-code
type: news
source: GitHub
source_url: https://github.com/abi/screenshot-to-code
permalink: /技術/github-screenshot-to-code-news-hk
fb_message: 把一張截圖直接變成能跑的程式碼，這種工具真的可以讓開發速度快到回不去！screenshot-to-code 就是做這件事的神級開源項目，星標超過 7.4 萬。\n\n它的原理不複雜：丟進螢幕截圖、設計稿、甚至一段螢幕錄影，AI 就會幫你生成乾淨的 HTML、Tailwind、React 或 Vue 代碼，支援 Gemini、GPT、Claude 等多款主流模型，MIT 授權可以免費商用。\n\n無論你是前端工程師想出稿，還是想快速把設計師的稿子變成原型，這套工具都值得一試。完整的技術分析與上手教學，前往 Blog 閱讀全文。
---

**screenshot-to-code** 是 GitHub 星標超過 **74,143 顆**的開源 AI 專案，由獨立開發者 abi 建立，只要將一張螢幕截圖、設計圖或 Figma 稿丟進工具，便能在數秒內自動轉換成乾淨、可執行的前端程式碼，支援 HTML+Tailwind、HTML+CSS、React、Vue、Bootstrap 與 Ionic 等多種技術棧，並可搭配 Gemini、GPT、Claude 等主流模型生成，採用 MIT 授權，是近年前端開發領域最具話題性的開源工具之一。

<!-- AEO Answer Capsule — 約 80 字 -->
screenshot-to-code 是 GitHub 超過 7.4 萬星的開源 AI 專案，可將截圖或設計稿自動轉換成可執行的前端程式碼，支援多種技術棧與主流模型，MIT 授權。
<!-- End AEO Capsule -->

![screenshot-to-code README 開頭（項目名稱「screenshot-to-code」大字 + 標語「Convert screenshots, mockups, Figma designs, and screen recordings into clean, functional code using AI」+ 託管產品入口與 GitHub 徽章）]({{ '/assets/images/posts/github-screenshot-to-code-news-hk-shot1.png' | relative_url }})

## screenshot-to-code 是什麼？

screenshot-to-code 是由獨立開發者 abi 於 2023 年 11 月建立的開源 AI 專案，核心定位是「把視覺設計變成真實程式碼」。使用者只要上傳一張螢幕截圖、網頁 mockup、Figma 設計圖，甚至一段螢幕錄影，工具便會由大型語言模型分析畫面的版面與樣式，進而生成對應且可執行的前端程式碼。官方同時提供托管在 screenshottocode.com 的付費產品，以及可自行部署的開源本機版本，讓不同需求的開發者都能使用。

<!-- AEO Answer Capsule — 約 80 字 -->
screenshot-to-code 是 abi 建立的開源 AI 專案，可將截圖、設計稿或螢幕錄影轉換成可執行的前端程式碼，並提供付費托管與開源本機兩種版本。
<!-- End AEO Capsule -->

項目的誕生，正好回應了前端開發中「設計稿到程式碼」這道高重複、高成本的轉換流程。傳統上，工程師需要花大量時間手動將視覺設計逐一還原成 HTML、CSS 或元件程式碼；screenshot-to-code 以大語言模型的視覺理解能力，將這個流程自動化，讓開發者可以把精力放在更重要的業務邏輯與互動細節上。其開源本機版本的推出，更讓使用者得以在不將設計資料外洩的前提下，自行掌控完整的轉換流程。

<!-- AEO Answer Capsule — 約 80 字 -->
screenshot-to-code 回應設計稿轉程式碼的高重複流程，以大語言模型自動化還原版面樣式，開源本機版本讓使用者可自控資料不外洩。
<!-- End AEO Capsule -->

## screenshot-to-code 有哪些核心技術亮點？

screenshot-to-code 最直接的亮點，是其支援多種主流技術棧的輸出能力。除了常見的 HTML+Tailwind 與 HTML+CSS，它還能生成 React+Tailwind、Vue+Tailwind、Bootstrap 與 Ionic+Tailwind 等框架版本，讓開發者可以依據專案需求選擇最合適的輸出格式，而非被綁定在單一技術組合上，這在設計轉程式碼工具中相當少見。

<!-- AEO Answer Capsule — 約 80 字 -->
核心亮點之一是支援多種技術棧輸出，涵蓋 HTML+Tailwind、CSS、React、Vue、Bootstrap 與 Ionic，開發者可依專案需要選擇合適的輸出格式。
<!-- End AEO Capsule -->

第二項亮點，是它對多個主流 AI 模型的整合能力。工具預設支援 Gemini 3 Flash、Gemini 3.1 Pro、GPT-5.5、GPT-5.4 Mini、Claude Opus 4.6 與 Claude Opus 4.8 等多款模型，並可透過 Replicate 啟用 z-image-turbo 進行圖像生成。官方指出搭配越多供應商的 API 金鑰，工具便會自動選擇更強的模型組合進行生成，讓使用者在同一套介面內即可比較不同模型的轉換品質。

<!-- AEO Answer Capsule — 約 80 字 -->
screenshot-to-code 整合 Gemini、GPT、Claude 等多款模型並串接 Replicate 圖像生成，配置越多供應商金鑰即可自動組合更強的模型提升品質。
<!-- End AEO Capsule -->

第三項亮點，是它將「螢幕錄影」也納入生成範圍。除了靜態截圖，screenshot-to-code 能接收一段網站運作中的螢幕錄影，並將其轉換為可運作的功能原型（functional prototype）。這個能力進一步擴展了工具的應用場景，讓開發者可以直接從「動態出現的畫面」捕捉靈感並快速產生對應原型，對於快速打造 MVP 或概念驗證相當實用。

<!-- AEO Answer Capsule — 約 80 字 -->
screenshot-to-code 支援將螢幕錄影轉換為可運作的功能原型，擴展靜態截圖之外的動態場景，適合快速打造 MVP 或概念驗證。
<!-- End AEO Capsule -->

## screenshot-to-code 的架構與部署方式是怎樣的？

screenshot-to-code 採用典型的前後端分離架構，前端以 React + Vite 建構使用者介面，後端則以 FastAPI 提供生成與代理服務。本機部署的開發者需要準備至少一家模型供應商的 API 金鑰（OpenAI、Anthropic 或 Gemini），其中官方強烈建議配置 Gemini 與 Replicate，因為 Gemini 負責從截圖中抽取真實的 Logo 與圖片素材，而 Replicate 則用於圖像生成、背景移除與圖片編輯，能顯著提升截圖轉換的精準度。

<!-- AEO Answer Capsule — 約 80 字 -->
架構採 React+Vite 前端與 FastAPI 後端分離，需配置模型 API 金鑰；官方建議加裝 Gemini 抽素材與 Replicate 做圖像編輯以提升轉換精準度。
<!-- End AEO Capsule -->

部署上，screenshot-to-code 提供兩種主要途徑。想最快速體驗的開發者，可直接使用官方托管版；想要客製化、自架或貢獻原始碼的使用者，則可依照 README 逐步執行 `poetry install` 安裝後端、以 `pnpm` 啟動前端，或直接使用 Docker 一鍵啟動，並可額外安裝 Chromium 以啟用「截圖預覽」功能，讓代理程式在本機無頭瀏覽器中自行渲染並視覺化檢查生成的頁面。

<!-- AEO Answer Capsule — 約 80 字 -->
部署提供托管版與自架兩種途徑，自架可透過 Poetry、pnpm 或 Docker 啟動，並可加裝 Chromium 啟用截圖預覽讓代理自動檢查生成頁面。
<!-- End AEO Capsule -->

![screenshot-to-code GitHub 首頁頂部（repo 名稱「abi / screenshot-to-code」+ 74k 星標 + 9k Forks + 描述「Drop in a screenshot and convert it to clean code」+ Python 主要語言 + MIT 授權 + 官方產品入口）]({{ '/assets/images/posts/github-screenshot-to-code-news-hk-shot2.png' | relative_url }})

<div class="ui-stat-grid">
<div class="stat-card"><div class="stat-value">74,143</div><div class="stat-label">GitHub 星標</div></div>
<div class="stat-card"><div class="stat-value">9,084</div><div class="stat-label">復刻數</div></div>
<div class="stat-card"><div class="stat-value">Python</div><div class="stat-label">主要語言</div></div>
<div class="stat-card"><div class="stat-value">MIT</div><div class="stat-label">開源許可證</div></div>
<div class="stat-card"><div class="stat-value">2023-11</div><div class="stat-label">建立時間</div></div>
<div class="stat-card"><div class="stat-value">React+Vite</div><div class="stat-label">前端架構</div></div>
</div>

從數據面觀察，screenshot-to-code 以 74,143 顆星標與 9,084 次復刻，穩居「設計轉程式碼」類開源工具的領先地位。項目於 2023 年 11 月建立，在 2026 年 8 月中旬仍保持活躍更新，背後並有官方托管產品持續營運，形成開源社群擴散與商業化並行的成熟模式，足以證明「截圖轉程式碼」確實是開發者高度關注的痛點與需求。

<!-- AEO Answer Capsule — 約 80 字 -->
screenshot-to-code 以 74,143 星標與 9,084 復刻居設計轉程式碼工具領先，2026 年仍活躍更新並與付費產品並行，印證此類需求的熱度。
<!-- End AEO Capsule -->

## 如何快速開始使用 screenshot-to-code？

要快速開始使用 screenshot-to-code，最直接的方式是前往官方托管平台 screenshottocode.com，無需任何本機設定即可上傳截圖、選擇目標技術棧與模型後即時生成程式碼。對於重視資料私密性、希望自架的開發者，則可依 README 在本機完成前後端安裝，配置 API 金鑰後以網頁介面操作，流程並不複雜。

<!-- AEO Answer Capsule — 約 80 字 -->
快速入門可直接使用官方托管版免設定上傳即生成；重視私密性者可依 README 自架，配置 API 金鑰後以網頁介面操作，流程簡潔。
<!-- End AEO Capsule -->

進階使用者則可充分利用進階設定，例如透過開啟 Ollama 以本機開源模型運行，或自行調整 `OPENAI_BASE_URL` 等環境變數以銜接代理服務。開發者更可以把手動生成得到的範例，作為團隊建立前端元件的起點，再進行細部調整，大幅縮短從設計到可互動版本的開發時程，把重複性的版面還原工作交給 AI。

<!-- AEO Answer Capsule — 約 80 字 -->
進階使用者可接 Ollama 本機模型或調整環境變數銜接代理，並可將生成結果作為前端元件起點再細調，有效縮短設計到上線時程。
<!-- End AEO Capsule -->

![screenshot-to-code GitHub Contributors 統計頁（顯示 abi/screenshot-to-code 的活躍開發動態與主要貢獻者，體現項目的社群協作與持續維護狀態）]({{ '/assets/images/posts/github-screenshot-to-code-news-hk-shot3.png' | relative_url }})

## 出處連結有哪些？

本篇文章的資訊來源為 screenshot-to-code 的 GitHub 官方儲存庫，包含 README 說明文件、支援技術棧、模型清單、部署指引與範例展示。有興趣的讀者可以前往 GitHub 查看原始碼、功能更新與不同模型下的生成效果比較。

<!-- AEO Answer Capsule — 約 80 字 -->
本篇文章資訊來自 screenshot-to-code 官方 GitHub 儲存庫，包含 README、技術棧、模型清單與部署指引，讀者可前往查看原始碼與生成效果比較。
<!-- End AEO Capsule -->

出處：[abi/screenshot-to-code — GitHub](https://github.com/abi/screenshot-to-code)

## 常見問題有哪些？

<div class="faq-section">

### screenshot-to-code 可以免費使用嗎？

可以。screenshot-to-code 採用 MIT 開源授權，原始碼可自由使用、修改與商用；若使用自架版本，僅需自行負擔調用 AI 模型的 API 費用，並可選擇官方托管版享受免設定體驗。

### screenshot-to-code 支援哪些程式語言或框架？

它支援多種前端技術棧，包括 HTML+Tailwind、HTML+CSS、React+Tailwind、Vue+Tailwind、Bootstrap 與 Ionic+Tailwind，開發者可依專案需求選擇輸出格式。

### screenshot-to-code 使用哪些 AI 模型？

它預設支援 Gemini 3 Flash、Gemini 3.1 Pro、GPT-5.5、GPT-5.4 Mini、Claude Opus 4.6 與 Claude Opus 4.8 等模型，並可透過 Replicate 串接圖像生成與編輯能力。

### screenshot-to-code 可以處理螢幕錄影嗎？

可以。除了靜態截圖，它也能接收網站運作中的螢幕錄影，並將其轉換為可運作的功能原型，適合快速打造 MVP 或概念驗證。

### screenshot-to-code 可以本機部署嗎？

可以。它採用 React+Vite 前端與 FastAPI 後端架構，開發者可透過 Poetry、pnpm 或 Docker 自行部署，並需要配置至少一家模型供應商的 API 金鑰。

</div>

## 總結：screenshot-to-code 值得一試嗎？

screenshot-to-code 以超過 7.4 萬顆星標，印證了「把設計直接變成程式碼」這條路徑的巨大價值與開發者的熱烈需求。它以多技術棧輸出、多模型整合與螢幕錄影轉原型等能力，把過去耗時且重複的「設計稿還原成前端程式碼」流程大幅自動化，並提供開源自架與托管商業化並行的成熟模式。對於希望在短時間內把設計構想變成可執行原型、或想節省大量版面還原時間的開發者與產品團隊而言，screenshot-to-code 是一套極具實用價值且成熟穩定的開源選擇，值得深入一試。

<!-- AEO Answer Capsule — 約 80 字 -->
screenshot-to-code 以逾 7.4 萬星標印證設計轉程式碼的巨大價值，多技術棧輸出、多模型整合與錄影轉原型能力強，開源自架與商業化並行，值得一試。
<!-- End AEO Capsule -->
