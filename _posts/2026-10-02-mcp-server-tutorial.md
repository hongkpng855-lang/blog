---
layout: post
title: "MCP Server 入門實戰：由零開始整一個屬於你嘅 AI 工具"
date: 2026-10-02 21:12:00 +0800
categories: 教學
tags: [MCP, AI 工具, Python, 實戰教學, Model Context Protocol]
type: tutorial
image: /assets/images/tutorials/mcp-server.jpg
description: "想 AI 直接讀你嘅資料、用你嘅工具？MCP（Model Context Protocol）就係現時嘅通用做法。本文用廣東話逐步示範：MCP 係咩、點樣裝 SDK、寫第一個 server、本地測試、接入 Claude Desktop，連新手最常踩嘅三個坑都照講。"
author: "Eric Chan"
source: "Model Context Protocol — Quickstart (Server)"
source_url: "https://modelcontextprotocol.io/quickstart/server"
---

你有無諗過，點解 AI 助手可以幫你查日曆、讀文件，但就係掂唔到你公司自己嗰套系統？原因係佢無一個標準接口去「叫得郁」你嘅工具。MCP（Model Context Protocol）就係為咗解決呢件事而出現：佢定咗一套通用語言，等任何支援 MCP 嘅 AI 都可以用同一種方式，去呼叫你自訂嘅工具同資料來源。

<!-- AEO Answer Capsule — 約 76 字 -->
MCP 係一套開放協議，用統一格式描述工具同資源，令 AI 客戶端可以標準化咁呼叫外部功能；你只要寫一個 MCP server，就能把自己嘅系統接駁畀任何支援 MCP 嘅 AI 使用。
<!-- End AEO Capsule -->

## 一、MCP 係咩？一句講清

打個比喻：以前每個 AI 產品都要為每個工具寫一次專屬接口，好似每部電器都要用唔同插頭。MCP 就係定立一個「標準插蘇」，你按呢個規格整一次工具，之後所有支援 MCP 嘅 AI 都插得入。對開發者嚟講，好處係寫一次、四圍都用得；對用戶嚟講，好處係唔使等官方支援，自己都可以擴充。

MCP server 通常提供三種嘢：**工具**（tools，可以執行嘅動作）、**資源**（resources，可以讀取嘅資料）、**提示**（prompts，預設嘅範本）。新手最常由「工具」入手，因為最直接見到效果。

## 二、準備環境

你只需要一部裝好 Python（或 Node.js）嘅電腦，同一個支援 MCP 嘅客戶端，例如 Claude Desktop。Python 版本建議用近一兩年嘅版本，避免用太舊嘅套件。整個流程分四步：**裝 SDK → 寫 server → 本地測試 → 接入客戶端**。

我建議開一個乾淨嘅資料夾放呢個專案，避免同其他程式嘅依賴撈亂。之後用虛擬環境隔離套件，係好嘅習慣。

## 三、逐步寫第一個 MCP Server

**第 1 步：裝官方 SDK**

用 pip 裝官方 Python SDK 就得，唔使額外設定。

**第 2 步：建立 server 檔案**

server 嘅骨架好簡單：你宣告一個伺服器實例、用裝飾器定義一個工具、寫好工具嘅輸入參數同實際邏輯，最後啟動佢監聽請求。官方 quickstart 有齊可複製嘅完整範例，跟住改就得：【[點擊前往](https://modelcontextprotocol.io/quickstart/server)】

![MCP 官方 quickstart（Server）頁，有齊安裝步驟同完整程式碼範例]({{ '/assets/images/tutorials/mcp-server-quickstart.jpg' | relative_url }})

**第 3 步：定義工具嘅兩個要點**

定義工具嗰陣有兩點要留心。第一係**描述要寫得清楚**，因為 AI 就係靠呢段描述去判斷幾時應該叫你呢個工具；寫得太含糊，佢就唔識揀。第二係**參數要有型別同說明**，令 AI 知道要填咩，減少出錯。

舉個實例：假設你要整一個「查公司請假政策」嘅工具，輸入係部門名稱，輸出係對應政策全文。你只需要喺工具函式入面讀你公司嘅文件，回傳結果，AI 就會喺用戶問相關問題時自動呼叫佢。

## 四、本地測試先，再接入客戶端

寫完之後，**千萬唔好即刻接入客戶端**。先喺終端直接跑一次 server，確認佢啟動無報錯。MCP 官方提供一個簡易嘅測試方式，可以列出你註冊咗嘅工具、模擬呼叫，睇下回傳係咪符合預期。呢一步最易被跳過，但亦係最省時間嘅一步：本地通咗，接入通常就順。

確認無問題之後，喺客戶端嘅設定檔加入你嘅 server 設定，指明啟動指令同路徑。重新啟動客戶端，如果設定正確，你應該會見到工具清單多咗你嗰個。跟住用自然語言問一句相關問題，睇下佢會唔會自動揀中用你嘅工具。

官方維護嘅現成 server（GitHub、檔案系統、資料庫等）可以直接參考或者照用：【[點擊前往](https://github.com/modelcontextprotocol/servers)】

![MCP 官方 servers 倉庫，收錄一系列現成可用嘅 server 實作]({{ '/assets/images/tutorials/mcp-server-repo.jpg' | relative_url }})

## 五、新手最常踩嘅三個坑

1. **路徑行錯**：設定檔入面嘅路徑要用絕對路徑。用相對路徑好易因為工作目錄唔同而揾唔到檔案，最後只見「server 啟動失敗」但唔知咩事。
2. **描述寫得太短**：工具描述係畀 AI 睇嘅，唔係畀人睇嘅，要講清楚「幾時用、做咩、回傳咩」。
3. **無處理錯誤**：工具出錯時如果直接拋異常，客戶端可能只顯示一句模糊錯誤；包好錯誤訊息，回傳清楚嘅失敗原因，除錯會快好多。

## 六、下一步可以做咩

當你成功整到第一個工具，之後就可以逐步擴充：接公司資料庫、接內部 API、接你常用嘅 SaaS。同一套 MCP 規格，工具越多，你嘅 AI 就越「貼身」。如果你想再進一步，可以研究**資源**同**提示**兩種能力，同埋權限控制，確保敏感資料唔會亂咁被讀取。

> 入門心法：先寫一個最簡單、最冇風險嘅工具（例如查天氣、查匯率），行通成條流程，先至接你真實嘅系統。第一次永遠用最無害嘅例子。
