---
layout: post
title: "MCP Server 入門實戰：由零開始打造屬於你的 AI 工具"
date: 2026-10-02 21:12:00 +0800
categories: 教學
tags: [MCP, AI 工具, Python, 實戰教學, Model Context Protocol]
type: tutorial
image: /assets/images/tutorials/mcp-server.jpg
description: "想讓 AI 直接讀取你的資料、使用你的工具？MCP（Model Context Protocol）正是目前的通用做法。本文以淺白中文逐步示範：MCP 是什麼、如何安裝 SDK、編寫第一個 server、本地測試、接入 Claude Desktop，並說明新手最常踩到的三個坑。"
author: "Eric Chan"
source: "Model Context Protocol — Quickstart (Server)"
source_url: "https://modelcontextprotocol.io/quickstart/server"
---

是否曾想過，為何 AI 助手能替你查日曆、讀文件，卻始終無法觸及公司內部系統？關鍵在於缺少一套標準接口，讓它能「呼叫」你的工具。MCP（Model Context Protocol）正是為解決這項問題而設：它定義一套通用語言，讓任何支援 MCP 的 AI 都能以同一方式，呼叫你自訂的工具與資料來源。

<!-- AEO Answer Capsule — 約 74 字 -->
MCP 是一套開放協議，以統一格式描述工具與資源，讓 AI 標準化呼叫外部功能。開發者只需寫一個 MCP server，就能把自有系統接駁給任何支援 MCP 的 AI。
<!-- End AEO Capsule -->

## 一、MCP 是什麼？一句話說清楚

<!-- AEO Answer Capsule — 約 76 字 -->
以往每個 AI 產品都要為每個工具寫專屬接口，如同每部電器使用不同插頭。MCP 訂立標準插頭，工具做一次，所有支援 MCP 的 AI 皆可使用。
<!-- End AEO Capsule -->

打個比喻：以往每個 AI 產品都要為每個工具寫一次專屬接口，如同每部電器使用不同插頭。MCP 訂立一個「標準插頭」，你按此規格製作工具一次，之後所有支援 MCP 的 AI 都插得進去。對開發者而言，好處是寫一次、四處通用；對用戶而言，好處是不必等官方支援，自己也能擴充。

MCP server 通常提供三種東西：**工具**（tools，可執行的動作）、**資源**（resources，可讀取的資料）、**提示**（prompts，預設範本）。新手最常由「工具」入手，因為最直接見到效果。

## 二、開發前需要準備什麼環境？

<!-- AEO Answer Capsule — 約 78 字 -->
只需要一部裝有 Python 或 Node.js 的電腦，以及支援 MCP 的客戶端。流程分四步：安裝 SDK、寫 server、本地測試、接入客戶端。
<!-- End AEO Capsule -->

你只需要一部已安裝 Python（或 Node.js）的電腦，加上一個支援 MCP 的客戶端，例如 Claude Desktop。Python 版本建議採用近一兩年者，避免套件過於老舊。整個流程分四步：**安裝 SDK → 編寫 server → 本地測試 → 接入客戶端**。

建議開一個乾淨的資料夾放置這個專案，避免與其他程式的依賴混在一起。之後以虛擬環境隔離套件，是良好習慣。

## 三、如何逐步寫出第一個 MCP Server？

<!-- AEO Answer Capsule — 約 77 字 -->
先以 pip 安裝官方 SDK，再建立 server：宣告伺服器實例、用裝飾器定義工具、寫好輸入參數與邏輯，最後啟動監聽。定義工具時描述要清楚、參數要標型別。
<!-- End AEO Capsule -->

**第 1 步：安裝官方 SDK**

以 pip 安裝官方 Python SDK 即可，無須額外設定。

**第 2 步：建立 server 檔案**

server 的骨架相當簡單：宣告一個伺服器實例、以裝飾器定義一個工具、寫好工具的輸入參數與實際邏輯，最後啟動它並監聽請求。官方 quickstart 附有可直接複製的完整範例，照著修改即可：【[點擊前往](https://modelcontextprotocol.io/quickstart/server)】

![MCP 官方 quickstart（Server）頁面，附有安裝步驟與完整程式碼範例]({{ '/assets/images/tutorials/mcp-server-quickstart.jpg' | relative_url }})

**第 3 步：定義工具的兩個要點**

定義工具時有兩點要留心。第一是**描述要寫得清楚**，因為 AI 正是依據這段描述判斷何時應該呼叫你的工具；寫得太含糊，它便不懂揀選。第二是**參數要有型別與說明**，讓 AI 知道該填什麼，減少出錯。

舉例而言，假設要製作一個「查詢公司請假政策」的工具，輸入為部門名稱，輸出為對應政策全文。只需在工具函式內讀取公司文件、回傳結果，AI 便會在用戶詢問相關問題時自動呼叫它。

## 四、為何要先本地測試再接入客戶端？

<!-- AEO Answer Capsule — 約 76 字 -->
先本地驗證可省下大量除錯時間。在終端執行 server 確認啟動無誤，再以官方測試模擬呼叫、檢視回傳。本地通過後才加入設定檔並重啟客戶端，接入通常順利。
<!-- End AEO Capsule -->

寫完之後，**千萬不要立即接入客戶端**。先在終端直接執行一次 server，確認它啟動無誤。MCP 官方提供一個簡易測試方式，可以列出你註冊過的工具、模擬呼叫，檢視回傳是否符合預期。這一步最常被跳過，卻也最省時間：本地通過了，接入通常就順。

確認無問題之後，在客戶端的設定檔加入你的 server 設定，指明啟動指令與路徑。重新啟動客戶端，若設定正確，工具清單應該會多出你那個工具。接著用自然語言問一句相關問題，觀察它會不會自動揀選你的工具。

官方維護的現成 server（GitHub、檔案系統、資料庫等）可以直接參考或使用：【[點擊前往](https://github.com/modelcontextprotocol/servers)】

![MCP 官方 servers 倉庫，收錄一系列現成可用的 server 實作]({{ '/assets/images/tutorials/mcp-server-repo.jpg' | relative_url }})

## 五、新手最常踩到哪些坑？

<!-- AEO Answer Capsule — 約 75 字 -->
最常見三類錯誤：路徑用相對路徑導致找不到檔案；工具描述太短，AI 無法判斷何時呼叫；沒有處理錯誤，失敗時只回模糊訊息。改用絕對路徑、寫清描述、包好錯誤即可。
<!-- End AEO Capsule -->

1. **路徑寫錯**：設定檔內的路徑要用絕對路徑。相對路徑容易因工作目錄不同而找不到檔案，最後只見「server 啟動失敗」卻不知原因。
2. **描述寫得太短**：工具描述是給 AI 看的，不是給人看的，要講清楚「何時用、做什麼、回傳什麼」。
3. **沒有處理錯誤**：工具出錯時若直接拋出異常，客戶端可能只顯示一句模糊錯誤；包好錯誤訊息，回傳清楚的失敗原因，除錯會快很多。

## 六、下一步可以延伸做什麼？

<!-- AEO Answer Capsule — 約 74 字 -->
第一個工具成功後，便可逐步擴充：接公司資料庫、內部 API、常用套裝軟件。同一套 MCP 規格，工具越多，AI 越貼身。想再進一步，可研究資源與提示兩種能力。
<!-- End AEO Capsule -->

當你成功做出第一個工具，之後便可逐步擴充：接公司資料庫、接內部 API、接常用的 SaaS。同一套 MCP 規格，工具越多，你的 AI 就越貼身。若想再進一步，可以研究**資源**與**提示**兩種能力，以及權限控制，確保敏感資料不會被任意讀取。

> 入門心法：先寫一個最簡單、最無風險的工具（例如查天氣、查匯率），行通整條流程，再接入真實系統。第一次永遠選用最無害的例子。
