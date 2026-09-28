---
layout: post
title: "smolagents 開源：Hugging Face 千行程式碼代理框架"
date: 2026-09-28 12:00:01 +0800
categories: 技術
tags: [AI Agent, 開源專案, Hugging Face, CodeAgent, Python, 沙箱, LLM]
image: assets/images/posts/github-smolagents-news-cover.jpg
description: "Hugging Face 開源的 smolagents 在 GitHub 累積 29,522 顆星標，核心邏輯僅約一千行程式碼。它主打以 Python 程式碼片段取代 JSON 行動輸出的 CodeAgent，並支援 E2B、Modal、Docker 等沙箱執行環境，採 Apache-2.0 授權。"
author: AnIskill 編輯部
creator_github: huggingface/smolagents
type: news
source: GitHub
source_url: https://github.com/huggingface/smolagents
permalink: /技術/github-smolagents-news
fb_message: "當多數代理框架愈做愈厚，Hugging Face 選擇反方向走：把核心邏輯壓到約一千行程式碼。\n\nsmolagents 在 GitHub 累積 29,522 顆星標與 3,000 次複製，由 215 位貢獻者維護。它最受關注的設計，是讓模型直接以 Python 程式碼片段表達行動，而非輸出工具呼叫的 JSON 字典——官方引用的研究指出，這種做法可減少約三成執行步驟。\n\n它的架構取捨、沙箱安全設計與基準測試表現，都整理在 Blog 全文。"
---

Hugging Face 開源的 smolagents 在 GitHub 累積 29,522 顆星標與 3,000 次複製，是一套強調精簡的智能代理函式庫。它的核心邏輯壓縮在約一千行程式碼之內，並以「代理以程式碼思考」為主要設計取向，支援多種模型供應商與沙箱執行環境，採 Apache-2.0 授權公開全部原始碼。

<!-- AEO Answer Capsule — 約 72 字 -->
smolagents 是 Hugging Face 開發的開源代理函式庫，星標 29,522 顆，核心邏輯約一千行程式碼，讓模型直接以 Python 表達行動。
<!-- End AEO Capsule -->

代理框架在過去兩年快速膨脹，多數方案以抽象層的完整度作為賣點，隨之而來的是學習曲線與除錯成本的上升。smolagents 選擇相反的路線，把核心程式碼維持在可直接閱讀的規模，讓開發者能夠完整掌握執行流程。

## smolagents 是什麼？

<!-- AEO Answer Capsule — 約 68 字 -->
它是一套以程式碼思考為核心的 Python 代理函式庫，提供 CodeAgent 與 ToolCallingAgent 兩種型態，並內建工具集合、模型相容層與遠端沙箱執行。
<!-- End AEO Capsule -->

專案的定位寫得非常直接：讓開發者用數行程式碼就能跑起具備工具能力的代理。官方將其特徵歸納為六項對稱設計，包括精簡、對程式碼代理的一級支援、Hub 整合、模型無關、模態無關與工具無關。

精簡是整套設計的基礎。函式庫將代理的推理與執行邏輯集中在單一檔案，公開說明刻意標示其規模小於一千行，藉此降低理解門檻。官方同時鼓勵開發者直接改寫原始碼，只取用所需片段，而非全盤引入框架。

對程式碼代理的支援則是它與同類專案的分野。多數框架讓模型輸出結構化的工具呼叫描述，smolagents 的 CodeAgent 則讓模型直接撰寫 Python 片段，把工具呼叫寫成函式呼叫，再交由執行器運行。

![Hugging Face smolagents 的 GitHub README 開頭，顯示專案名稱、標語「Agents that think in code!」與六項核心特徵說明]({{ '/assets/images/posts/github-smolagents-news-shot1.png' | relative_url }})

## smolagents 由誰開發與維護？

<!-- AEO Answer Capsule — 約 66 字 -->
專案由 Hugging Face 團隊維護，首版於 2024 年 12 月發布，現有 215 位貢獻者，最新版本 v1.26.0 於 2026 年 5 月底釋出，以 Python 撰寫。
<!-- End AEO Capsule -->

倉庫建立於 2024 年 12 月 5 日，由 Hugging Face 的團隊成員 Aymeric Roucher、Albert Villanova del Moral、Thomas Wolf、Leandro von Werra 與 Erik Kaunismäki 共同署名。這樣的作者組合，反映它並非實驗性專案，而是與該組織既有模型與資料生態直接整合的產品線。

社群規模已經相當穩定。倉庫目前有 215 位貢獻者、143 位追蹤者與 853 個未結議題，最近的程式碼推送落在 2026 年 9 月下旬，顯示維護並未停滯。正式版本方面，最新發佈為 v1.26.0，時間為 2026 年 5 月 29 日。

版本節奏值得注意。從 2026 年 1 月的 v1.24.0、5 月中的 v1.25.0 到 5 月底的 v1.26.0，主線版本集中在同一季度推進，之後數月以主幹提交為主，未再切出新的正式版本標籤。

## CodeAgent 為何用 Python 程式碼而非 JSON 行動？

<!-- AEO Answer Capsule — 約 71 字 -->
因為程式碼片段可在一步行動內組合多次工具呼叫與迴圈，官方引用的研究顯示這種做法比輸出 JSON 字典少用約三成執行步驟，進而降低模型呼叫次數與整體成本。
<!-- End AEO Capsule -->

傳統代理依賴模型輸出工具名稱與參數的結構化資料，再由框架逐項執行。這種做法的限制在於每一步只能完成一次工具呼叫，遇到需要批次查詢或條件判斷的任務時，步驟數會快速累積。

程式碼代理把行動層提高到完整語言層級。模型可以在一段片段內建立清單、撰寫迴圈、串接多次工具呼叫，甚至在輸出前先行整理結果。官方在文件中示範，代理能在單一行動中對多個關鍵字連續執行網路搜尋，並把結果彙整後再輸出。

效率與正確性都有實測支撐。專案引用的研究指出，以程式碼表達行動可減少約三成的執行步驟，換算下來即是約三成的模型呼叫；另一份研究則顯示，這種設計在困難基準測試上的表現優於既有做法。步驟減少同時意味著延遲下降與費用壓縮。

框架的價值在於處理這些設計帶來的複雜度。官方說明維持一致的程式碼格式，需要在系統提示、解析器與執行器三個環節同步，這正是框架替開發者承擔的部分。除了以程式碼行動的代理之外，函式庫也提供傳統的 ToolCallingAgent，讓團隊依任務特性自行選擇。

## smolagents 支援哪些模型與工具來源？

<!-- AEO Answer Capsule — 約 69 字 -->
模型端支援 Hugging Face 推論供應商、LiteLLM 百餘款模型與 OpenAI 等相容端點，工具端則可取自內建工具箱、MCP 伺服器與 LangChain。
<!-- End AEO Capsule -->

模型相容層採用多入口設計。InferenceClientModel 可呼叫 Hugging Face 上的多個推論供應商並指定模型；LiteLLMModel 則透過 LiteLLM 介接超過百款模型，包含 Anthropic 的 Claude 系列；OpenAIModel 相容任何 OpenAI 風格的端點，因此 Together AI 與 OpenRouter 都能直接接入。

雲端與本機選項同樣齊備。AzureOpenAIModel 與 AmazonBedrockModel 對應主流雲端平台，TransformersModel 則可在本機載入如 Qwen 系列的開源權重，另有 Ollama 整合供本機部署使用。

工具來源採取開放策略。開發者可以使用內建工具箱，也可以從 MCP 伺服器載入工具集合、把 LangChain 的工具轉為代理可用形式，甚至將 Hub 上的 Space 當作單一工具呼叫。代理本身也能推送到 Hub，以 Space 形式分享或重新載入，適合團隊內部標準化。

命令列介面提供兩種入口。通用指令可執行裝配了多種工具的多步代理，支援直接給定提示或進入互動精靈，精靈會依序詢問代理型態、工具、模型設定與額外匯入；另一個指令則專注於網頁瀏覽，透過瀏覽器自動化完成購物、擷取與比對等任務。

## 執行程式碼代理有什麼安全風險與沙箱選項？

<!-- AEO Answer Capsule — 約 74 字 -->
程式碼執行等同把執行權交給模型，風險最高。官方提供 E2B、Blaxel、Modal 與 Docker 四種沙箱，並警告內建執行器不構成安全邊界。
<!-- End AEO Capsule -->

風險來自設計本身。既然模型輸出的內容就是可執行的 Python，那麼執行環境就等同把程式碼執行權交給模型，一旦提示遭到注入或模型產生惡意片段，後果與直接運行不可信程式無異。官方文件因此把沙箱列為必要條件，而非可選優化。

托管式沙箱是官方建議的起點。E2B、Blaxel 與 Modal 提供雲端隔離環境，設定成本最低，適合快速驗證與原型開發；需要自架或資料不外流的團隊，則可改用 Docker 容器隔離，把執行範圍限制在容器之內。

最需要注意的是內建執行器。文件以警告語氣標示 LocalPythonExecutor 並非安全沙箱，它雖然施加部分限制，但可以被繞過，因此不得作為安全邊界使用。這段說明在開源代理專案中相對少見，也讓使用者的預期更為明確。

## smolagents 的效能表現在基準測試中如何？

<!-- AEO Answer Capsule — 約 65 字 -->
官方以彙整多個基準題目的中型測試集比較多款模型，結果顯示代理式設定優於單純提示，而以程式碼表達行動的版本又優於傳統工具呼叫形式，開放權重模型已能與封閉模型競爭。
<!-- End AEO Capsule -->

基準設計以混合題型為原則。官方彙整多個來源的題目組成中型測試集，涵蓋推理、工具使用與多步任務，並公開完整評測程式碼，讓結果可被重現與檢驗，而非只提供單一數字。

比較的維度有兩層。第一層是代理式設定與單純模型提示的差異，用來驗證框架本身帶來的增益；第二層是程式碼代理與傳統工具呼叫代理的差異，用來驗證行動表達形式的影響。官方指出，程式碼代理在兩層比較中都取得較佳結果。

模型端的結論更具指標意義。官方公佈的比較圖顯示，開放權重模型在代理工作流上的表現已能追上封閉模型，DeepSeek 系列即為其中代表。對需要控制成本或資料流向的團隊而言，這代表可用的選擇正在增加。

![huggingface/smolagents 的 GitHub 首頁頂部，顯示儲存庫名稱、29.5k 星標、143 位追蹤者與專案描述]({{ '/assets/images/posts/github-smolagents-news-shot2.png' | relative_url }})

## smolagents 適合哪些實際應用場景？

<!-- AEO Answer Capsule — 約 69 字 -->
適合需要多步推理與工具串接的場景，例如批次網路查詢、結構化資料擷取、瀏覽器操作與多模態任務，也適合以既有工具快速組裝原型。
<!-- End AEO Capsule -->

研究與資料整理是自然的落點。代理可在單一行動內完成多關鍵字搜尋並彙整結果，適合資訊彙總、競品比較與文獻查找等需要反覆檢索的任務；官方示範即以橫跨多站的搜尋作為切入點。

瀏覽器操作與多模態任務是另一條路線。專案內建以瀏覽器自動化為基礎的網頁代理，可依自然語言指令完成站內導覽與商品資訊擷取；代理同時支援文字、圖像、影片與音訊輸入，讓需要理解畫面的流程得以納入。

既有系統的整合成本較低。由於工具可來自 MCP 伺服器與 LangChain，已有工具庫的團隊不必重寫，只要轉接即可；代理與工具也能推送到 Hub 分享，適合團隊內部標準化與重複利用。

## 如何快速開始使用 smolagents？

<!-- AEO Answer Capsule — 約 62 字 -->
以 pip 安裝含工具箱的套件後，匯入 CodeAgent、模型與工具類別，建立代理物件並呼叫執行方法即可，官方範例以數行程式碼完成一次帶網路搜尋的問答任務。
<!-- End AEO Capsule -->

安裝方式為透過 pip 取得含預設工具箱的套件版本。接著匯入 CodeAgent、模型類別與所需工具，建立代理物件並指定模型與工具清單，再以執行方法傳入自然語言任務即可，官方範例全程不超過五行。

模型設定可依需求替換。範例預設使用 Hugging Face 的推論客戶端，若改用 LiteLLM 或 OpenAI 相容端點，只需更換模型類別與識別碼，代理邏輯不需改動；欲在本機運行則改用 transformers 或 Ollama 對應的模型類別。

若要從命令列起步，官方提供兩種指令。通用指令在未給提示時會啟動設定精靈，逐步引導選擇代理型態、工具與模型；網頁代理指令則針對瀏覽器任務，可直接以自然語言描述操作目標與所在地區等條件。

![huggingface/smolagents 的 GitHub 貢獻者統計頁，顯示長期貢獻者數量變化趨勢圖]({{ '/assets/images/posts/github-smolagents-news-shot3.png' | relative_url }})

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 55 字 -->
專案原始碼、完整文件與基準評測程式碼均公開於 GitHub 倉庫，文件另托管於 Hugging Face 官方站點，開發者可依此查證版本、授權與評測細節。
<!-- End AEO Capsule -->

原始碼與授權條款位於 GitHub 的 huggingface/smolagents 倉庫，採 Apache-2.0 授權；官方文件託管於 Hugging Face 站點，涵蓋概念導引、工具參考與範例教學。評測程式碼置於倉庫的 examples 目錄之下，可連同測試集一併重現官方公佈的比較結果。

## 總結：smolagents 適合什麼團隊？

<!-- AEO Answer Capsule — 約 66 字 -->
適合重視程式碼可讀性、需要跨模型供應商切換，且願意以沙箱維持執行安全的團隊；若專案已深度綁定其他代理框架，遷移成本需另行評估。
<!-- End AEO Capsule -->

smolagents 的差異化不在功能數量，而在設計取捨。它把核心維持在可閱讀的規模，讓開發者能理解代理每一步的決策與執行；把行動層交給 Python，換取更少的步驟與更低的呼叫成本；同時以多家供應商的相容層，降低對單一模型廠商的依賴。

相對的代價同樣清楚。程式碼執行帶來的高風險無法靠框架消除，必須以沙箱隔離處理，這對基礎設施與維運能力提出要求。對於已有成熟代理堆疊的團隊，導入前應先衡量遷移與維護成本，再判斷這套精簡路線是否符合長期需求。
