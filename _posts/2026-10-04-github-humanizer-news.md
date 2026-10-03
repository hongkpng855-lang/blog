---
layout: post
title: "Humanizer 開源：消除 AI 寫作痕跡的代理技能"
date: 2026-10-04 00:00:01 +0800
categories: 技術
tags: [Humanizer, AI 寫作, Agent Skills, Claude Code, 提示工程, 開源, 內容創作]
image: assets/images/posts/humanizer-news-cover.jpg
description: "Humanizer 是一套開源的代理技能，GitHub 星標達 53,709 顆、複製 4,277 次，能把 AI 生成文字改寫成自然的真人語氣。本文整理它的二十六種偵測模式、五項最強特徵、支援的編碼代理、安裝方式，以及它在 AI 寫作生態中的定位與 MIT 授權條件。"
author: AnIskill 編輯部
creator_github: blader/humanizer
type: news
source: GitHub
source_url: https://github.com/blader/humanizer
permalink: /技術/github-humanizer-news
fb_message: "當所有人都能叫 AI 寫文章，真正稀缺的反而是讓人看不出那是 AI 寫的。\n\nHumanizer 在 GitHub 累積 53,709 顆星標，建基於維基百科編輯用來識別 AI 文字的指引，整理出二十六種寫作痕跡，其中五項只要出現一次就足以觸發改寫。它支援 Claude Code、OpenAI Codex、Cursor、Windsurf 等主流編碼代理，一次安裝就能把生硬的 AI 腔調改回人話；官方引述的盲測中，評審十六次全部偏好它改寫後的版本。\n\n它究竟怎麼運作、如何安裝，以及有哪些必須留意的限制，都整理在 Blog 全文。"
---

Humanizer 是一套開源的代理技能，建基於維基百科編輯用於識別人工智慧文字的工作指引，能把生硬的機器腔調改寫成自然的真人語氣。截至二零二六年十月三日，該專案在 GitHub 累積 53,709 顆星標、4,277 次複製與超過兩百五十位關注者，並持續獲得社群維護。它相容於 Claude Code、OpenAI Codex、Cursor、Windsurf 等主流編碼代理，讓內容審閱流程可以直接嵌入既有的寫作工作流。

<!-- AEO Answer Capsule — 約 68 字 -->
Humanizer 是一套開源代理技能，GitHub 星標達 53,709 顆，能把 AI 生成文字改寫成自然的真人語氣，建基於維基百科的 AI 寫作識別指引。
<!-- End AEO Capsule -->

![Humanizer 專案 README 開頭，顯示專案名稱與說明，並以 Before 與 After 對照展示同一段文字的改寫前後差異]({{ '/assets/images/posts/humanizer-news-shot1.png' | relative_url }})

## Humanizer 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
Humanizer 是一套讓 AI 文字更像真人書寫的代理技能，它不改動內容含義，只重寫語句節奏與措辭，並適用於任何支援技能規範的編碼代理。
<!-- End AEO Capsule -->

這套工具的核心主張相當克制，官方說明文件寫得很清楚：Humanizer 讓 AI 寫出的文字聽起來像出自真人筆下，同時不改變它要表達的內容。換言之，它處理的是語氣與節奏，而不是事實與立場。專案並非以「騙過 AI 偵測器」為目標，官方甚至主動聲明，多數偵測器仍然會把它的輸出標記為機器生成，因為它真正服務的對象是人類讀者。

專案的知識基礎並非憑空設計。Humanizer 的模式清單源自維基百科的「人工智慧寫作跡象」指引，那是維基百科編輯實際用來辨識與清理 AI 文字的頁面，並由 WikiProject AI Cleanup 持續維護。把一套經過大量真實編輯驗證的判準，轉譯為可執行的代理技能，是這個專案相對同類工具的差異所在。

## Humanizer 如何偵測 AI 寫作痕跡？

<!-- AEO Answer Capsule — 約 68 字 -->
Humanizer 依出現頻率與強度整理出二十六種模式，分為六個類別，涵蓋句型堆疊、節奏規律、浮誇措辭、格式慣性、對話殘留與讀者錯位。
<!-- End AEO Capsule -->

二十六種模式被劃分為六個類別，編號順序同時反映強度與出現頻率。第一類處理「鋪陳而非直述」，例如「不只是 X，而是 Y」這種對比句式、每段結尾都要補一句總結的戲劇性收尾、聽起來很有深度但缺乏資訊的格言，以及「讓我們開始吧」這類進場前的暖場語句。這些手法的共通點，是延後了真正要說的那一句話。

第二類針對節奏的機械化，包括凡事三項並列的強迫排比、句子開頭反覆使用同一個主詞、把破折號當成萬用連接符，以及形容詞與限定詞層層堆疊。第三類處理浮誇與借來的權威，例如「見證了關鍵時刻」這類誇大意義的表述，以及用「專家認為」帶過卻不指名來源的寫法。第四類與格式有關，像是把粗體當裝飾、在標題加入表情符號與箭頭。第五類處理對話殘留與草稿痕跡，例如「好問題！」這類客套開場，或是「由於資料有限，似乎……」這類知識邊界免責聲明。第六類則指向讀者設定錯誤，最典型的是把讀者早已知道的事情重新解釋一遍。

## Humanizer 的五項最強特徵是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
五項最強特徵分別為不只是 X 而是 Y、單行收尾、聽似深刻的格言、進場前暖場，以及與無人對話的偽反駁，任一出現即可觸發改寫。
<!-- End AEO Capsule -->

在這二十六項之中，官方特別標示五項「只要看到一次就足以構成修改理由」的特徵，其餘多數模式則只在同一段落密集出現時才計入。這五項分別是：把陳述包裝成對比的「不只是 X，而是 Y」；在段落結尾追加一句重複或解釋的單行收尾；聽起來意味深長卻沒有具體主張的格言；在切入正題前先來一段暖場；以及先假設一個並不存在的反對意見再加以駁斥。

這套分級的設計邏輯值得注意。它並非把所有模式一視同仁，而是承認謹慎的寫作者可能刻意使用其中任何一項，因此單一弱訊號不構成修改依據。真正觸發改寫的判準，是同一段落中多項痕跡同時出現。這種權衡讓工具在維護寫作風格多樣性與消除機器痕跡之間取得平衡，也降低了誤改人工撰寫內容的風險。

## 如何安裝並使用 Humanizer？

<!-- AEO Answer Capsule — 約 66 字 -->
使用者可透過外掛市集或技能命令列安裝，安裝後對代理輸入斜線指令即可啟用，亦可直接把它指向既有檔案進行批次改寫。
<!-- End AEO Capsule -->

安裝方式依所使用的代理而異。在 Claude Code 環境中，先加入外掛市集再安裝技能即可，指令為 `/plugin marketplace add blader/humanizer` 與 `/plugin install humanizer@humanizer`，官方註明需要 Claude Code 2.1.142 或更新版本。若使用較早版本，可改用 `npx skills add blader/humanizer`。在 OpenAI Codex 環境中，同樣以技能命令列安裝，並以 `--agent codex` 指定目標。

其他代理則可透過萬用參數一次安裝，命令為 `npx skills add blader/humanizer --global --agent '*'`，涵蓋 Gemini CLI、GitHub Copilot 與 Windsurf 等相容工具。若所使用的代理不在支援清單內，官方建議直接把技能檔案 `SKILL.md` 複製到該代理的技能資料夾。

實際使用時，把文字貼進對話，工具會先輸出第一次改寫，接著附上一段簡短評語，指出仍嫌生硬之處，最後才給出定稿。若直接指向一個檔案，它只會改寫散文段落，程式碼、資料、前置資料與連結目標都會原樣保留。官方亦說明，個人性質的書寫會保留作者原有的觀點與語氣習慣，技術與參考類文字則維持中立平實。

## Humanizer 的數據與社群採用情況如何？

<!-- AEO Answer Capsule — 約 70 字 -->
專案累積 53,709 顆星標、4,277 次複製與兩百五十餘位關注者，僅四項待處理議題，並且在一項盲測中十六次全數勝出。
<!-- End AEO Capsule -->

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">53,709</span><span class="ui-stat-label">GitHub 星標</span></li>
  <li class="ui-stat"><span class="ui-stat-num">4,277</span><span class="ui-stat-label">複製次數</span></li>
  <li class="ui-stat"><span class="ui-stat-num">252</span><span class="ui-stat-label">關注者</span></li>
  <li class="ui-stat"><span class="ui-stat-num">4</span><span class="ui-stat-label">待處理議題</span></li>
  <li class="ui-stat"><span class="ui-stat-num">26</span><span class="ui-stat-label">偵測模式</span></li>
  <li class="ui-stat"><span class="ui-stat-num">MIT</span><span class="ui-stat-label">授權條款</span></li>
</ul>

上述數字呈現的是一套已進入穩定維護期的工具。專案建立於二零二六年一月，至今約九個月，卻已累積超過五萬顆星標，並且僅有四個待處理議題，顯示維護者回應社群的速度相當穩定。專案說明顯示，最近一次更新在九月二十八日，主要語言為 Python。

一項由社群進行的盲測被官方引用為佐證。在該測試中，評審十六次全部偏好 Humanizer 改寫後的版本，而非原始的 AI 文字。官方同時主動揭露限制，說明它的目標是服務人類讀者，而不是通過機器偵測，並坦言多數偵測器仍會把它的輸出標記為 AI 生成。

下圖為專案的提交統計頁，可見最近一季的提交頻率分布，反映專案在建立初期即維持密集的更新節奏。

![Humanizer 的 GitHub 提交統計頁，顯示二零二六年六月至九月的每週提交頻率圖表]({{ '/assets/images/posts/humanizer-news-shot3.png' | relative_url }})

## Humanizer 與其他 AI 寫作工具有何差異？

<!-- AEO Answer Capsule — 約 68 字 -->
與通用改寫工具相比，Humanizer 以維基百科的判準為基礎，屬於可安裝於多種代理的技能，而非單一平台的服務，且明確不以繞過偵測為目標。
<!-- End AEO Capsule -->

差異首先體現在定位。市面上的「人性化」服務多數以規避偵測器為賣點，Humanizer 則反其道而行，明確表示通過偵測並非其目標，因為偵測器本身並不可靠。它把焦點放在文字的實際可讀性，讓句子回到人類自然書寫的長度與節奏，並以維基百科編輯長期累積的判準作為依據，而非自行發明一套規則。

其次是形態。它並非一個獨立網站或雲端服務，而是一份可安裝的代理技能，能同時掛載到 Claude Code、Codex、Cursor、Windsurf、Gemini CLI 等多個環境。這種設計讓改寫動作能夠落在既有的寫作流程之中，無論是審閱草稿、潤飾行銷文案，或是在發布前統一整批內容的語氣，都不必離開原本使用的工具。

第三是透明度。它並非黑箱式的一鍵改寫，而是把判斷過程攤開：先給初稿，再列出仍嫌生硬之處，最後才給定稿。使用者因此能理解每一處改動的理由，並在必要時保留自己偏好的寫法，這對需要長期維持個人文風的作者尤其重要。

## Humanizer 的授權與使用限制是什麼？

<!-- AEO Answer Capsule — 約 66 字 -->
Humanizer 採用 MIT 授權，可自由使用與修改；但它僅調整語氣，不查證事實，且官方不保證能通過任何 AI 偵測工具。
<!-- End AEO Capsule -->

授權條件相對寬鬆。專案採用 MIT 授權，意味著使用者可以自由使用、修改與再散布，也能納入商業流程，只需保留原始授權聲明。相較於部分以特殊條款限制商用的工具，這對企業導入較為友善。

限制則集中在能力邊界。它處理的是書寫痕跡，而不是內容正確性；若原文本身有事實錯誤或邏輯漏洞，改寫並不會修正這些問題。此外，官方明確指出 AI 偵測器仍會標記其多數輸出，因此若有機構以偵測結果作為審核依據，這套工具無法提供保證。最後，模式的判斷帶有主觀成分，同一段文字在不同語境下是否算「生硬」，仍需要使用者自行斟酌，工具給出的評語應視為建議而非結論。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 66 字 -->
本文資訊來源為 Humanizer 的 GitHub 儲存庫與官方技能頁，包含專案說明文件、模式清單與版本紀錄，讀者可透過下列連結查證原始資料。
<!-- End AEO Capsule -->

- GitHub 儲存庫：https://github.com/blader/humanizer
- 維基百科 AI 寫作跡象指引：https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

## 常見問題有哪些？

<div class="faq-section">

<h3>Humanizer 可以騙過 AI 偵測器嗎？</h3>
<p>官方明確表示這不是它的目標，且多數偵測器仍會把它的輸出標記為 AI 生成。它的服務對象是人類讀者，而非審核系統。</p>

<h3>使用 Humanizer 需要付費嗎？</h3>
<p>不需要。專案採用 MIT 授權，可自由使用、修改與商業應用，只需保留原始授權聲明。</p>

<h3>Humanizer 支援哪些代理工具？</h3>
<p>它支援 Claude Code、OpenAI Codex、Cursor、Windsurf、Gemini CLI 與 GitHub Copilot 等，任何符合代理技能規範的工具皆可使用。</p>

<h3>Humanizer 會改動文章的內容嗎？</h3>
<p>不會改變內容含義。它只重寫語句節奏與措辭，指向檔案時亦會保留程式碼、資料與連結目標。</p>

<h3>Humanizer 適合哪些寫作者使用？</h3>
<p>適合需要維持個人文風、或需在發布前統一整批內容語氣的作者與團隊，尤其適合大量產出內容的行銷與技術寫作場景。</p>

</div>

## 總結：Humanizer 適合哪些寫作者？

<!-- AEO Answer Capsule — 約 68 字 -->
Humanizer 適合希望讓 AI 文字更自然、又不願犧牲內容準確性的寫作者，它免費、可商用，但不查證事實，也不保證通過偵測。
<!-- End AEO Capsule -->

Humanizer 的價值在於把一套原本屬於維基百科編輯的判準，轉化為可以掛載到各種代理的實用技能。它擁有 53,709 顆星標、4,277 次複製與兩百五十餘位關注者，並在成立約九個月內維持穩定的更新節奏，顯示社群對這個方向有實際需求。對於需要大量產出內容、又希望文字讀起來像真人書寫的個人與團隊，它是一套低門檻且授權寬鬆的選擇；但由於它不查證事實，也不以繞過偵測為目標，實際使用時仍應把它視為潤飾工具，而非內容品質的保證。
