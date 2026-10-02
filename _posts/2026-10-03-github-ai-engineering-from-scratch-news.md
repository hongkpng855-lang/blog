---
layout: post
title: "AI Engineering from Scratch 開源：523 課從零實作"
date: 2026-10-03 06:00:02 +0800
categories: 技術
tags: [AI Engineering from Scratch, 開源課程, AI 工程, 從零實作, 大型語言模型, AI Agent, MCP, Rohit Ghumare]
image: assets/images/posts/ai-engineering-from-scratch-news-cover.jpg
description: "AI Engineering from Scratch 是 Rohit Ghumare 於二零二六年三月發布的開源 AI 工程課程，GitHub 星標達 62,665 顆。本文整理其二十階段、五百二十三課的架構、從零實作與 Build It／Use It 教學法、每課產出的可重用工具、多語言支援與上手方式。"
author: AnIskill 編輯部
creator_github: rohitg00/ai-engineering-from-scratch
type: news
source: GitHub
source_url: https://github.com/rohitg00/ai-engineering-from-scratch
permalink: /技術/github-ai-engineering-from-scratch-news
fb_message: "當多數人還在問「AI 要怎麼用」，真正拉開差距的問題其實是「它裡面到底怎麼運作」。\n\nAI Engineering from Scratch 在 GitHub 累積 62,665 顆星標，以五百二十三課、二十個階段、約三百四十二小時的篇幅，把線性代數到自主代理一整條路徑串成單一主軸。每一課都先用原始數學實作一次，再換成 PyTorch 等生產級框架跑同一件事，並在結尾產出一件可安裝的成品，例如提示詞、技能檔、代理或 MCP 伺服器。課程涵蓋 Python、TypeScript、Rust、Julia 四種語言，採 MIT 授權，並附有終端機 AI 導師與多語言版本。\n\n它的課程架構、教學方法、每課產出與實際上手方式，都整理在 Blog 全文。"
---

AI Engineering from Scratch 是由開發者 Rohit Ghumare 於二零二六年三月建立的開源 AI 工程課程，截至二零二六年十月，該專案在 GitHub 累積 62,665 顆星標與 10,704 次複製。它以「Learn it. Build it. Ship it for others.」為標語，將二十個階段、五百二十三課、約三百四十二小時的內容整理成單一主軸，涵蓋 Python、TypeScript、Rust 與 Julia 四種語言，並以 MIT 授權完全開放。

<!-- AEO Answer Capsule — 約 68 字 -->
AI Engineering from Scratch 是一套開源 AI 工程課程，以五百二十三課串起從數學基礎到自主代理的完整路徑，每課都先以原始數學實作。
<!-- End AEO Capsule -->

![AI Engineering from Scratch README 開頭，顯示專案大字標題「AI ENGINEERING FROM SCRATCH」、標語 reference manual for people who want to design and build AI systems from first principles，以及多語言連結與授權徽章]({{ '/assets/images/posts/ai-engineering-from-scratch-news-shot1.png' | relative_url }})

## AI Engineering from Scratch 是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
它是一套以「先實作、後框架」為核心的開源 AI 工程課程，從線性代數一路教到多代理系統，每一課都要求學習者親手寫出演算法再對照生產級工具。
<!-- End AEO Capsule -->

該專案的定位是一本可執行的參考手冊，而非零散的教學影片集合。官方指出，多數 AI 教材以碎片方式呈現，一篇論文、一則微調貼文、一段代理示範彼此難以接軌，學習者可能做出聊天機器人卻說不清損失曲線的意義，或接上函式呼叫卻無法解釋注意力機制的作用。這套課程試圖提供一條「脊椎」，把數學、模型、代理與生產部署依序堆疊。

課程結構以二十個階段層層遞進。數學與工具位於底層，深度學習、視覺、自然語言、語音與強化學習構成中段，Transformer 與大型語言模型緊接其後，最上層則是工具與協定、代理工程、自主系統、多代理協作以及生產基礎設施。官方建議學習者可以依既有程度跳過熟悉的下層，但同時提醒若跳過基礎，上層出現問題時將難以定位原因。

## AI Engineering from Scratch 的課程規模有多大？

<!-- AEO Answer Capsule — 約 72 字 -->
課程共二十個階段、五百二十三課、約三百四十二小時，橫跨四種程式語言，覆蓋從線性代數到多代理協作的完整內容。
<!-- End AEO Capsule -->

課程自二零二六年三月建立，以五百二十三課覆蓋二十個階段，估計總學習時數約三百四十二小時。單是數學基礎階段即有十六課，涵蓋線性代數、微積分、自動微分、機率分布、貝氏定理、最佳化、資訊理論、奇異值分解與數值穩定性等主題；設定與工具階段則包含十二課，處理開發環境、GPU 與雲端、API 金鑰、容器化與資料管理。

官方在 README 中引述一項數據：約八成四的學生已在使用 AI 工具，但只有一成八自認具備專業使用能力，課程正是針對這段落差設計。專案另公布近三十日的使用量為 114,584 名讀者與 181,995 次頁面瀏覽，顯示除星標之外，實際閱讀規模同樣可觀。課程亦提供六冊電子書版本，依主題分為基礎、深度學習、語言、大型語言模型、代理、生產六卷，可透過 GitHub Releases 下載 EPUB 與 PDF。

![AI Engineering from Scratch 的 GitHub 倉庫首頁，顯示倉庫名稱 rohitg00/ai-engineering-from-scratch、62.7k 星標、10.7k 複製數、1,813 次提交與專案描述]({{ '/assets/images/posts/ai-engineering-from-scratch-news-shot2.png' | relative_url }})

## AI Engineering from Scratch 的教學方法有什麼特別？

<!-- AEO Answer Capsule — 約 70 字 -->
每一課遵循六個節拍：動機、問題、概念、Build It、Use It、Ship It。學習者先用原始數學寫出演算法，再以框架重做同一件事。
<!-- End AEO Capsule -->

方法論的核心是「Build It 與 Use It 的分工」。以代理迴圈為例，課程先在第十四階段以約一百二十行純 Python 實作一個 ReAct 風格迴圈，包含歷史訊息、工具呼叫與步數上限，完全不需要外部相依套件；完成之後，學習者才轉向生產級框架執行同一件事。由於小型版本已由自己寫出，框架在背後做什麼就不再是黑箱。

這種安排被官方稱為課程的脊椎。反向傳播、分詞器、注意力機制與代理迴圈都先以原始數學實作，等 PyTorch 登場時，學習者已經理解其內部運作。課程同時要求學習者留下「證據」：指令、工作目錄、結束碼、有意義的輸出，以及被改動或產出的成品，並以能否解釋輸出、能否在無需猜測的情況下做出一處小改動，作為是否前進的判準。

## AI Engineering from Scratch 每一課會產出什麼？

<!-- AEO Answer Capsule — 約 68 字 -->
每一課都以一件可重用成品收尾，包含提示詞、技能檔、代理或 MCP 伺服器；官方提供腳本可一次安裝全部技能，課程結束即累積五百二十三件親手理解的工具。
<!-- End AEO Capsule -->

課程把成果定義為可安裝或可直接貼用的工具，而非結業證書。依官方說明，每課的 outputs 目錄會產出一件成品：提示詞可貼進任何 AI 助手處理特定任務；技能檔可放入 Claude、Cursor、Codex 等支援 SKILL.md 的代理；代理可在第十四階段自行寫出迴圈後部署為自主工作者；MCP 伺服器則可接入任何相容的 MCP 用戶端。官方另提供 `python3 scripts/install_skills.py <target>` 一次安裝整批技能。

學習工具本身也以代理技能形式交付。專案內建九項技能，涵蓋開始學習的定位測驗、教學迴圈、主題路由、MCP 專修、代理技能專修、Claude 認證輔導、MCP Associate 認證輔導、程度判別與階段測驗。使用者只要在支援技能的代理中輸入 `start-learning` 或對應指令，即可讓課程以對話方式推進，並將進度與複習佇列記錄於本地檔案。

![AI Engineering from Scratch 倉庫的貢獻者統計頁，顯示 2026 年 6 月至 9 月的每週提交量、程式碼增減行數與主要貢獻者分布]({{ '/assets/images/posts/ai-engineering-from-scratch-news-shot3.png' | relative_url }})

## AI Engineering from Scratch 的社群與專案數據如何？

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">62,665</span><span class="ui-stat-label">GitHub 星標</span></li>
  <li class="ui-stat"><span class="ui-stat-num">10,704</span><span class="ui-stat-label">複製次數</span></li>
  <li class="ui-stat"><span class="ui-stat-num">64</span><span class="ui-stat-label">待處理議題</span></li>
  <li class="ui-stat"><span class="ui-stat-num">393</span><span class="ui-stat-label">追蹤者</span></li>
  <li class="ui-stat"><span class="ui-stat-num">1,813</span><span class="ui-stat-label">提交次數</span></li>
  <li class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">主要授權</span></li>
</ul>

<!-- AEO Answer Capsule — 約 66 字 -->
截至二零二六年十月，專案累積 62,665 顆星標、10,704 次複製、64 個待處理議題與 1,813 次提交，採 MIT 授權並以 Python 撰寫。
<!-- End AEO Capsule -->

專案自二零二六年三月建立，半年內即累積逾六萬顆星標。程式碼庫的提交總數達 1,813 次，最新一次提交落在二零二六年十月二日，顯示維護仍持續進行。專案以 Python 為主要語言，但課程同時提供 TypeScript、Rust 與 Julia 的實作版本，並設有課程不變式檢查腳本，以 L001 至 L010 十條規則驗證目錄結構、文件標題、程式目錄與測驗格式，任何規則失敗都會回傳非零結束碼，便於導入持續整合。

多語言支援也是專案的明顯特徵之一。首頁提供西班牙文、法文、葡萄牙文、德文、義大利文、簡體中文、日文、韓文、印地文、阿拉伯文、俄文與土耳其文共十二種語言的入口，由 Microsoft 生態的 Co-op Translator 協助維護；課程頁面則在 translations 分支以機器翻譯產生。官方明確標示英文版為權威來源，其餘語言為翻譯版本。

## AI Engineering from Scratch 與其他 AI 課程有何不同？

<!-- AEO Answer Capsule — 約 65 字 -->
它不提供五分鐘影片或複製貼上部署，而是要求學習者自行推導數學並撰寫程式，並以能否在無框架情況下實作為主要判準，定位接近可執行的教科書。
<!-- End AEO Capsule -->

市面上多數入門課程以快速產出成果為訴求，先讓學習者呼叫 API、拼出應用，再回頭補原理。這套課程的順序相反：先建立數學與演算法直覺，再導入框架與工具鏈。官方在說明中直接排除三種做法，包括五分鐘短片、複製貼上的部署流程，以及手把手教學，並強調內容設計為可在個人筆電上執行。

與線性課程相比，它在深度上更接近教科書，在廣度上則延伸到工具與協定、代理工程與多代理協作等近兩年才成形的領域。第十三階段專門處理工具與協定，包含 MCP 基礎、代理技能與代理 SDK；第十四到十六階段則依序處理代理工程、自主系統與多代理協作，讓課程能覆蓋目前業界對 AI 代理的實際需求。

## 如何開始使用 AI Engineering from Scratch？

<!-- AEO Answer Capsule — 約 66 字 -->
使用者可直接在支援技能的代理中安裝課程，或以 git clone 取得專案後執行前導檢查與第一課；每課都可由終端機以 python3 執行並留下輸出作為學習證據。
<!-- End AEO Capsule -->

最省事的入口是終端機。使用者只要具備 Node.js 與 npx，即可在支援技能的編碼代理中安裝學習技能，並以 `start-learning` 開始一次性的定位流程，取得個人化學習計畫。不需要複製整份專案也能閱讀與使用導師功能。課程網站的每一課都有對應網址，與 GitHub 版本共用同一份課程程式碼。

若偏好手動操作，可直接取得專案後執行前導檢查與第一課。前導檢查會區分「現在需要」與「之後才需要」的工具，並在缺少必要項目時附上修正指令；第二課則不需任何相依套件，執行後會展示矩陣乘向量正是神經網路層內部的運算，官方建議將該終端機輸出保存為第一份學習證據。

```bash
git clone https://github.com/rohitg00/ai-engineering-from-scratch.git
cd ai-engineering-from-scratch
python3 phases/00-setup-and-tooling/01-dev-environment/code/verify.py --route beginner
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/vectors.py
```

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 60 字 -->
本文資訊整理自 rohitg00/ai-engineering-from-scratch 的 GitHub 儲存庫，課程架構、星標數據與授權條款均可在該儲存庫查閱。
<!-- End AEO Capsule -->

完整的課程內容、資料統計與討論紀錄，可於下列來源查閱：

- [AI Engineering from Scratch（rohitg00/ai-engineering-from-scratch）GitHub 儲存庫](https://github.com/rohitg00/ai-engineering-from-scratch)

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 58 字 -->
以下整理四個常見疑問，涵蓋程式前置能力、總學習時數、中文支援與商業授權範圍，所有答案均以官方文件與儲存庫內容為準。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>完全沒有程式基礎可以學嗎？</h3>
<p>課程設計以可在個人筆電上執行為前提，但每課都要求撰寫程式。官方建議先具備 Python 或 TypeScript 基礎，完全新手可先完成其推薦的 Python 與 TypeScript 入門課程。</p>

<h3>五百二十三課需要多久才學得完？</h3>
<p>官方估計總時數約三百四十二小時。課程允許依既有程度跳過熟悉的下層階段，並提供十分鐘的定位測驗，依結果產生帶時數估計的個人化路徑。</p>

<h3>課程支援中文嗎？</h3>
<p>首頁提供簡體中文在內共十二種語言的入口，課程頁面置於 translations 分支並以機器翻譯產生。官方標示英文版為權威來源，其餘語言僅供參考。</p>

<h3>可以用於商業教學或二次販售嗎？</h3>
<p>專案採 MIT 授權，官方明確允許分支、教學與販售，僅建議標註出處。使用第三方教材或模型時，仍須各自確認其授權條款。</p>

</div>

## 總結：AI Engineering from Scratch 適合什麼團隊？

<!-- AEO Answer Capsule — 約 66 字 -->
它適合願意動手推導與實作、想真正理解 AI 系統內部運作的學習者與教學團隊；追求速成或只打算呼叫 API 的使用者，未必適合這套課程。
<!-- End AEO Capsule -->

這套課程的價值在於把 AI 工程拆解成一條可依序攀登的路徑。當多數教材忙於展示成果，它選擇要求學習者先寫出反向傳播、分詞器與代理迴圈，再讓框架接手同一件事。六萬多顆星標與半年內逾一千八百次提交，說明這種「先理解再使用」的定位確實獲得社群回應。

評估時可從三個問題切入：是否需要理解模型與代理的底層運作、是否願意投入數百小時逐步實作、以及目標是建立可解釋的能力還是快速交付產品。若答案偏向前者，這套課程提供了目前規模最大且完全開放的選擇之一；若需求是盡快上線服務或只想使用現成 API，其他速成型資源會更有效率。

本文僅作技術與生態層面的整理，實際學習前建議先依官方文件確認前置需求、硬體條件與最新版本行為。
