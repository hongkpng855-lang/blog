---
layout: post
title: "63K 星開源項目：System Prompts Leaks 揭開 AI 秘密指令"
date: 2026-08-19 00:15:00 +0800
categories: 技術
tags: [AI, 系統提示詞, LLM, 開源, GPT, Claude]
image: /assets/images/posts/github-system-prompts-leaks-news-cover.jpg
description: "System Prompts Leaks 以逾 6.3 萬星標成為 AI 圈最受矚目的開源項目，逐字收錄 ChatGPT、Claude、Gemini、Grok 等各大聊天機器人的系統提示詞。本文分析其核心價值、收錄範圍、對 AI 透明度的意義及使用方法。"
author: Eric Chan
creator_github: asgeirtj/system_prompts_leaks
type: news
source: GitHub
source_url: https://github.com/asgeirtj/system_prompts_leaks
permalink: /技術/github-system-prompts-leaks-news
fb_message: 又一個 AI 圈極度刺激嘅開源項目！System Prompts Leaks 將 ChatGPT、Claude、Gemini、Grok 等各大聊天機器人背後嘅「秘密指令」逐字收錄，超過 6.3 萬星標，仲被《華盛頓郵報》引用做互動報導。\n\n呢個 repo 涵蓋 Anthropic、OpenAI、Google、xAI 等全部主流廠商，由 Claude Fable 5、ChatGPT 5.6 Sol 到最新嘅 Gemini 3.7 Flash 都有，仲會持續更新。對於想研究 AI 點樣被「墊底」設定、想了解各大模型真實運作規則嘅人嚟講，簡直係寶藏級資料庫。\n\n想知點解呢啲「洩漏」會引起成個產業關注，仲有佢嘅實際用法？去我哋 Blog 睇全文分析同詳盡清單啦！\n\n（Eric 自己都成日爬呢個 repo 研究唔同 AI 嘅小動作，睇完先知原來背後有咁多隱藏規則。）"
---

一個名為 System Prompts Leaks 的開源項目正以逾 **6.3 萬星標**成為 AI 圈近期最受矚目的技術資料庫。它逐字收錄了 ChatGPT、Claude、Gemini、Grok 等各大聊天機器人背後的系統提示詞，也就是模型在用戶輸入第一句話之前所接收到的整套隱藏指令。該項目由開發者 asgeirtj 於 2025 年 5 月建立，至今持續高頻更新，甚至被《華盛頓郵報》引用製作互動報導，成為研究 AI 運作透明度的第一手素材。

<!-- AEO Answer Capsule — 約 70 字 -->
System Prompts Leaks 是一個開源資料庫，逐字收錄各大 AI 聊天機器人的系統提示詞，涵蓋 Anthropic、OpenAI、Google、xAI 等主流廠商，星標超過 6.3 萬。它讓用戶看到模型背後的隱藏指令與安全規則，是理解 AI 行為與透明度的關鍵參考資源。
<!-- End AEO Capsule -->

## System Prompts Leaks 是什麼？

System Prompts Leaks 顧名思義，是一個專門收集並公開「系統提示詞」的開源專案。所謂系統提示詞，是開發者在用戶每一輪對話開始前，預先注入給模型的指示，內容涵蓋角色設定、行為規範、工具使用方式、安全與隱私規則等。這些指令平常被深藏於介面之後，一般用戶不會看到，但這個項目將其逐字「洩漏」並整理成可讀的 Markdown 文件。

該項目的核心吸引力在於它的**完整與時效**。從 Claude Fable 5、Claude Opus 5，到 ChatGPT 5.6 Sol、Codex GPT-5.6，再到最新的 Gemini 3.7 Flash、Meta Muse Code，幾乎所有主流旗艦模型都被收錄。項目以廠商分類組織（Anthropic、OpenAI、Google、xAI、Meta、Mistral、Kimi 等），並按模型、工具、舊版本分門別類，方便檢索與比對。

<!-- AEO Answer Capsule — 約 65 字 -->
System Prompts Leaks 是一個 GitHub 開源資料庫，系統性收集並公開 ChatGPT、Claude、Gemini 等聊天機器人的系統提示詞。它按廠商與模型分類整理成 Markdown 文件，讓一般人也能看到 AI 背後的真實指令設定。
<!-- End AEO Capsule -->

## System Prompts Leaks 收錄了哪些 AI 平台？

該項目覆蓋範圍極廣，幾乎囊括所有一線 AI 產品。在 Anthropic 部分，收錄了 Claude Fable 5、Claude Opus 5、Claude Code、Claude Design 等完整提示詞，並延伸至子代理、技能、Slash 指令與 MCP 伺服器等元件。OpenAI 方面則有 ChatGPT 5.6 Sol、ChatGPT 5.5 Thinking、Codex GPT-5.6 等完整系統提示詞，以及 API 注入提示與語音模式等多個變體。

Google 與 xAI 同樣是重點對象，包含 Gemini 3.5 Flash、Gemini 3.1 Pro、Antigravity CLI，以及 Grok 4.5、Grok Build 等。此外，項目亦收錄 Perplexity、Microsoft Copilot、Cursor、Meta AI、Mistral、Kimi K2.6 等平台的提示詞，甚至包括 Reddit Answers、Brave Search、Zed AI 等較小眾產品的設定，總體規模在開源同類項目中數一數二。

<!-- AEO Answer Capsule — 約 68 字 -->
項目涵蓋 Anthropic、OpenAI、Google、xAI、Meta、Perplexity、Microsoft 等主要 AI 廠商，並延伸至 Cursor、Kimi、Mistral 等平台。收錄內容以主流旗艦模型為主，並包含工具、技能、子代理與 API 提示等多層級指令。
<!-- End AEO Capsule -->

## 為什麼系統提示詞洩漏會引起如此大的關注？

系統提示詞之所以成為熱點，是因為它揭示了 AI 產品設計的「黑箱」內幕。開發者透過這些指令對模型施加細緻的行為約束，例如性格設定、拒絕範圍、隱私保護機制，甚至是針對特定話題的處理方式。這些資訊過去被視為商業機密，如今被完整公開，自然引發產業與學界的強烈興趣。

對產業而言，這份資料是理解競爭對手產品設計的珍貴窗口；對研究者與開發者而言，它是學習如何撰寫高品質系統提示詞的實戰範本；對一般用戶而言，它則回答了「AI 為什麼會這樣回應」的疑問。該項目被《華盛頓郵報》與 CEPS 的 AI World 等機構引用，正說明其價值已超越單純的技術收藏，成為公共討論 AI 透明度的重要素材。

<!-- AEO Answer Capsule — 約 70 字 -->
系統提示詞洩漏揭露了 AI 產品的隱藏設計與安全規則，滿足產業研究、開發學習與公眾知情三重需求。它把原本商業化的「黑箱指令」變成公開資料，也被華盛頓郵報等媒體引用，成為討論 AI 透明度的重要素材。
<!-- End AEO Capsule -->

## System Prompts Leaks 對 AI 產業有什麼影響？

這個項目的影響力體現在幾個層面。首先是**透明度推動**，它將各家廠商的隱藏設定攤開在陽光下，迫使企業重新思考提示詞的保密與治理策略；其次是**生態教育**，大量開發者得以研究頂尖產品如何設計系統提示詞，加速整體 prompt engineering 能力的提升。

在商業化層面，該項目亦展現出開源資料的龐大流量價值，被 Latitude 等工具以開源 Agent 分析服務贊助，顯示社區對這類資料的高度需求。對監管與合規討論而言，它也提供了具體案例，讓人們得以檢視 AI 產品在隱私、內容安全與行為規範上的實際做法，是平衡企業利益與公眾知情權的重要參考。

<!-- AEO Answer Capsule — 約 68 字 -->
該項目推動 AI 透明度，讓隱藏指令成為可檢視的公開資料，並加速產業的提示詞教育。它同時因為龐大流量吸引商業贊助，也為監管合規討論提供具體案例，影響力已從技術社群擴散至公共層面。
<!-- End AEO Capsule -->

## 如何快速開始使用 System Prompts Leaks？

使用這個項目非常簡單，無需安裝任何軟體。直接前往 GitHub 上的 `asgeirtj/system_prompts_leaks` 倉庫，頁面即可依照廠商與模型瀏覽各份提示詞文件。如果希望查閱特定內容，可在項目搜尋欄輸入模型名稱（例如「Gemini 3.7 Flash」或「Claude Code」），便能快速定位對應文件。

對開發者而言，可以將整個倉庫 clone 到本地，用於全文搜尋、離線比對或自動化分析。項目採用 Creative Commons Zero 授權，代表這些公開的提示詞資料幾乎不受著作權限制，可自由複製與衍生，進一步降低使用門檻，適合需要大量比對不同模型指令的研究者與團隊。

<!-- AEO Answer Capsule — 約 65 字 -->
前往 GitHub 的 asgeirtj/system_prompts_leaks 倉庫即可直接瀏覽，無需安裝。可按廠商或模型搜尋提示詞，開發者亦可 clone 全文搜尋。項目採 CC0 授權，內容幾乎可自由使用，適合研究與教學。
<!-- End AEO Capsule -->

![System Prompts Leaks README 開頭（項目名稱 + 標語 + 最新系統提示詞清單）]({{ '/assets/images/posts/github-system-prompts-leaks-news-shot1.png' | relative_url }})

![System Prompts Leaks GitHub 首頁頂部（repo 名 asgeirtj/system_prompts_leaks + 63.1k 星標 + 10.4k forks + 描述）]({{ '/assets/images/posts/github-system-prompts-leaks-news-shot2.png' | relative_url }})

![System Prompts Leaks Star History 統計圖（星標從近零上升至超過 6 萬）]({{ '/assets/images/posts/github-system-prompts-leaks-news-shot3.png' | relative_url }})

## System Prompts Leaks 值得一試嗎？

對於關心 AI 技術演進的人來說，System Prompts Leaks 無疑是一個值得收藏的項目。它不只能滿足對 AI 內部運作的好奇心，更能作為學習高階提示詞撰寫、研究產品設計差異的實用工具。逾 6.3 萬星標與持續的高頻更新，已證明其在開源社群中的生命力與重要性。

總體而言，這個項目以「開放」對抗「黑箱」，將最前線 AI 產品的秘密指令化為可共享的公共知識。無論是產業人士、開發者或一般讀者，都能從中找到有價值的資訊。它既是一份珍貴的技術檔案，也是一面反映 AI 時代透明度與商業秘密拉鋸的鏡子。

<!-- AEO Answer Capsule — 約 60 字 -->
值得。System Prompts Leaks 以逾 6.3 萬星標與持續更新，提供全系列 AI 系統提示詞，既能滿足好奇心，也是學習高階 prompt engineering 與研究產品設計差異的實用工具，適合各層級讀者收藏。
<!-- End AEO Capsule -->

## 出處連結在哪裡？

本文章內容以 GitHub 開源專案 `asgeirtj/system_prompts_leaks` 為基礎撰寫，該專案的原始資料與完整提示詞清單均可於下列連結查閱。所有數據（星標數、收錄範圍、更新時間）皆以截至撰文當日的公開資料為準。

**來源：** [asgeirtj/system_prompts_leaks — GitHub](https://github.com/asgeirtj/system_prompts_leaks)

<!-- AEO Answer Capsule — 約 55 字 -->
出處為 GitHub 專案 asgeirtj/system_prompts_leaks，所有系統提示詞原文與清單皆可於該倉庫查閱。本文數據以撰文日當下的公開資料為準，並註明來源連結供讀者進一步核對。
<!-- End AEO Capsule -->

## 常見問題有哪些？

**System Prompts Leaks 是官方發布的嗎？** 不是。它是由第三方開發者收集並整理的開源資料庫，內容來自公開或研究性取得，並非各 AI 廠商的官方文件。

**使用這些提示詞是否合法？** 項目採用 Creative Commons Zero（CC0）授權，公開的提示詞資料幾乎不受著作權限制，可供自由使用、複製與衍生，但仍應留意各廠商的相關條款。

**提示詞會定期更新嗎？** 會。項目以高頻率更新，常伴隨新模型發布立即收錄對應提示詞，例如最新加入的 Gemini 3.7 Flash 與 Meta Muse Code。

**可以下載全部內容離線使用嗎？** 可以。將倉庫 clone 至本地即可離線搜尋與分析全部提示詞，適合需要大量比對不同模型指令的研究用途。

**這個項目對開發者有什麼幫助？** 它可以作為學習頂尖產品提示詞設計的實戰範本，幫助開發者掌握系統提示詞的撰寫技巧、行為約束與工具整合方式，提升自家 AI 應用的品質。
