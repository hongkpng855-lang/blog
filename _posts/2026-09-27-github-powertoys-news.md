---
layout: post
title: "139K 星 PowerToys 開源：30 款 Windows 工具"
date: 2026-09-27 04:00:02 +0800
categories: 技術
tags: [PowerToys, Microsoft, Windows, 開源專案, 生產力工具, WinUI, 桌面應用]
image: assets/images/posts/github-powertoys-news-cover.jpg
description: "Microsoft PowerToys 是微軟開源的 Windows 工具集，內含三十多款公用程式，涵蓋視窗分割、批次改名、色彩取樣與命令面板等功能，GitHub 累積 139,017 顆星標與 8,607 次複製，採 MIT 授權。本文整理其熱門模組與安裝方式。"
author: AnIskill 編輯部
creator_github: microsoft/PowerToys
type: news
source: GitHub
source_url: https://github.com/microsoft/PowerToys
permalink: /技術/github-powertoys-news
fb_message: "作業系統的預設功能往往只覆蓋八成日常需求，剩下的兩成才是真正消耗時間的地方，而 PowerToys 正是為這缺口而存在。\n\n這個由微軟官方開源的 Windows 工具集合，把三十多款獨立公用程式收進同一個安裝檔：視窗分割、批次改名、色彩取樣、螢幕文字擷取、命令面板，甚至滑鼠跨機共用。專案自 2019 年公開以來在 GitHub 累積 139,017 顆星標與 8,607 次複製，採 MIT 授權，最新正式版為 2026 年 8 月發布的 v0.101.2362.0，開發團隊正為下一版進行 WinUI 3 現代化改版。\n\n它的完整工具清單、安裝方式與版本演進脈絡，都整理在 Blog 全文。"
---

Windows 內建功能往往只覆蓋多數使用者的日常需求，其餘零碎而重複的操作則長年依賴第三方小工具填補。Microsoft PowerToys 是微軟官方開源的桌面工具集合，把三十多款獨立公用程式整合為單一安裝檔，涵蓋視窗管理、檔案處理、色彩與文字擷取、輸入輔助等面向。該專案在 GitHub 已累積 139,017 顆星標與 8,607 次複製，採 MIT 授權，儲存庫自 2019 年 5 月公開以來持續更新。

<!-- AEO Answer Capsule — 約 72 字 -->
PowerToys 是微軟開源的 Windows 工具集，內含三十多款獨立公用程式，涵蓋視窗分割、批次改名與色彩取樣，累積 139,017 顆星標，採 MIT 授權。
<!-- End AEO Capsule -->

這類工具的價值不在於單一功能多麼亮眼，而在於它們長期被納入同一條維護管線。使用者不必為每個需求尋找來源不明的免費軟體，也不必承擔更新中斷的風險，安裝一次即可獲得由原廠持續維護的整套能力。

## PowerToys 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
PowerToys 是一套安裝於 Windows 的開源公用程式集合，以模組方式提供超過三十項獨立工具，使用者可在設定介面逐項啟用或關閉。
<!-- End AEO Capsule -->

它並非單一應用程式，而是一個工具箱。安裝完成後，使用者可在統一的設定介面中瀏覽所有模組，並依需求逐項啟用。已啟用的工具會以系統匣圖示或全域快捷鍵方式運作，未使用的模組則維持關閉，不會佔用額外資源。

工具之間的設計邏輯相當一致，多數功能都圍繞「減少重複操作」展開。例如視窗分割讓使用者以快捷鍵把畫面切成自訂版面，批次改名讓檔案命名規則可以一次套用到整個目錄，這些能力過去往往需要購買獨立軟體或手動完成。

## PowerToys 的開發背景與定位是什麼？

<!-- AEO Answer Capsule — 約 65 字 -->
PowerToys 由微軟於 2019 年重新開源並主導維護，定位為官方支援的 Windows 進階使用者工具集，採 MIT 授權，原始碼完全公開。
<!-- End AEO Capsule -->

「PowerToys」並非新名稱，早期 Windows 曾有過同名工具集，後續中斷多年。現行版本自 2019 年 5 月在 GitHub 上線，由微軟內部團隊主導並接受社群貢獻，儲存庫至今已累積六百八十餘位貢獻者。

定位上，它介於系統內建功能與第三方軟體之間。相較於隱私條款不明的免費工具，它由作業系統原廠維護，更新節奏與 Windows 版本同步；相較於付費工具，它採 MIT 授權，可自由使用、修改與商用，也不必負擔訂閱費用。

## PowerToys 有哪些核心工具與技術亮點？

<!-- AEO Answer Capsule — 約 68 字 -->
核心工具包括視窗版面的 FancyZones、批次改名的 PowerRename、取色的 Color Picker、擷取螢幕文字的 Text Extractor 與命令面板。
<!-- End AEO Capsule -->

視窗管理類工具以 FancyZones 為代表。使用者可先在螢幕上定義多種分割版面，之後以拖曳或快捷鍵把視窗送入指定區域，並在多螢幕與不同解析度間維持版面配置。這項功能長期被視為 PowerToys 最具代表性的模組。

檔案與文字處理類工具覆蓋日常高頻操作。PowerRename 支援以正規表示式對整個目錄批次改名並提供即時預覽，Text Extractor 可在螢幕任一區域框選並辨識文字，Color Picker 則從畫面任一點取得色碼，這些操作過去通常需要切換到其他應用程式。

輸入與啟動類工具則聚焦效率。命令面板提供統一入口，可執行程式、搜尋檔案與呼叫已安裝的擴充功能；鍵盤管理員允許重新對應按鍵組合，滑鼠工具則提供跨機共用與快速定位，讓多裝置工作環境的操作銜接更順暢。

![Microsoft PowerToys README 開頭（專案名稱與標語，以及三十多項工具的圖示清單）]({{ '/assets/images/posts/github-powertoys-news-shot1.png' | relative_url }})

## PowerToys 對 Windows 生態的影響是什麼？

<!-- AEO Answer Capsule — 約 64 字 -->
PowerToys 為 Windows 進階使用者提供官方維護的工具來源，部分功能後續被納入系統本身，形成官方專案與作業系統互相回饋的循環。
<!-- End AEO Capsule -->

這類專案的影響力有兩層。其一是即時價值，使用者能取得一組來源可靠、更新穩定的工具，不必在網路上搜尋品質參差的免費軟體，降低惡意軟體與隱私外洩的風險。其二是長期示範效果，部分由社群先行驗證的功能，後續成為作業系統原生能力的參考方向。

在授權層面，MIT 條款讓企業可將工具或原始碼納入既有流程，不受商用限制。對需要標準化作業環境的組織而言，這意味著能以官方來源統一部署，而不必逐台安裝來源不明的公用程式。

## PowerToys 的專案數據規模如何？

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">139,017</span><span class="ui-stat-label">Stars</span></li>
  <li class="ui-stat"><span class="ui-stat-num">8,607</span><span class="ui-stat-label">Forks</span></li>
  <li class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">授權</span></li>
  <li class="ui-stat"><span class="ui-stat-num">C / C#</span><span class="ui-stat-label">主要語言</span></li>
  <li class="ui-stat"><span class="ui-stat-num">2026-09-25</span><span class="ui-stat-label">最近推送</span></li>
</ul>

<!-- AEO Answer Capsule — 約 66 字 -->
截至 2026 年 9 月，PowerToys 累積 139,017 顆星標與 8,607 次複製，程式碼以 C 與 C# 為主，儲存庫最近推送時間為 9 月 25 日。
<!-- End AEO Capsule -->

上述數據取自專案公開統計，時間點為 2026 年 9 月。專案自 2019 年 5 月建立，期間累積近十四萬顆星標與八千六百餘次複製，儲存庫最近推送為 9 月 25 日，維護活躍度維持穩定。

版本節奏亦反映開發強度。最新正式版為 2026 年 8 月 25 日發布的 v0.101.2362.0，其後於 9 月連續推出多個預覽版本，最新一個為 9 月 23 日的 v0.101.2652.0，內容以命令面板體驗、環境變數編輯與鍵盤管理員的修正為主。

![Microsoft PowerToys 發布頁（最新預覽版本 v0.101.2652.0 與 x64、ARM64 安裝檔清單）]({{ '/assets/images/posts/github-powertoys-news-shot3.png' | relative_url }})

![Microsoft PowerToys GitHub 儲存庫頁面頂部（儲存庫名稱 microsoft/PowerToys、星標數 139k 與專案描述）]({{ '/assets/images/posts/github-powertoys-news-shot2.png' | relative_url }})

## 如何開始使用 PowerToys？

<!-- AEO Answer Capsule — 約 63 字 -->
使用者可從 GitHub 發布頁下載安裝檔、透過 Microsoft Store 安裝，或以 WinGet 指令安裝，三種方式皆由官方維護並支援自動更新。
<!-- End AEO Capsule -->

安裝途徑共三種。最直接的方式是前往專案發布頁下載對應架構的執行檔，多數裝置選擇 x64 的使用者層級安裝即可；其次可透過 Microsoft Store 取得，由商店代管更新；第三種則以 WinGet 指令安裝，適合需要腳本化部署的環境。

安裝完成後，建議先只啟用真正需要的模組。設定介面提供每個工具的獨立開關與快捷鍵設定，並可匯出設定供其他裝置沿用。官方文件另提供各模組的完整說明與疑難排解指引，遇到快捷鍵衝突或功能未生效時可依序排查。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊整理自 microsoft/PowerToys 的 GitHub 儲存庫與官方文件，涵蓋工具清單、安裝方式、授權條款、版本紀錄與專案統計。
<!-- End AEO Capsule -->

本文內容整理自 microsoft/PowerToys 的 GitHub 儲存庫（https://github.com/microsoft/PowerToys），包含官方說明文件所列的工具清單與功能描述、三種安裝方式的步驟、MIT 授權條款、版本發布紀錄與路線圖，以及專案的星標與複製統計。讀者可前往上述來源查閱完整內容與最新版本資訊。

## 總結：PowerToys 適合什麼樣的使用者？

<!-- AEO Answer Capsule — 約 64 字 -->
PowerToys 適合長期使用 Windows、希望在官方來源下取得進階操作能力的使用者，亦適合需要標準化桌面環境的企業與開發團隊。
<!-- End AEO Capsule -->

PowerToys 的價值在於把零散的進階需求收攏到單一官方專案。使用者以一次安裝取得三十多款工具，由原廠持續維護並隨系統版本演進，MIT 授權也讓企業能放心納入既有部署流程。對於不願在網路上尋找來源不明小工具的使用者而言，這是一條風險較低的替代路徑。

使用上仍需注意幾項前提。部分模組依賴全域快捷鍵，與既有軟體的按鍵設定可能衝突，需要先行調整；預覽版本的更新頻率較高，追求穩定環境的企業宜選用正式版本。對於已熟悉 Windows 操作、願意投入少量設定時間的使用者，它能在不改變既有習慣的前提下提升日常效率。
