---
layout: post
title: "Cloudflare 開源 Clef：讓 AI 代理自己做判斷的決策模型"
date: 2026-10-03 08:00:02 +0800
categories: 技術
tags: [Cloudflare, Clef, 決策模型, Workers AI, 開源, AI代理, 強化學習]
image: assets/images/posts/cloudflare-clef-decision-models-news-cover.jpg
description: "Cloudflare 於 2026 年 10 月推出開源決策模型 Clef 與 Clef-flash，託管於 Workers AI，以 Apache 2.0 授權公開權重。兩款模型主打快速、結構化輸出，具備視覺編碼器與 64k 上下文，並相容 Jev API，官方同時發布強化學習微調平台。"
author: AnIskill 編輯部
type: news
source: Cloudflare Blog
source_url: https://blog.cloudflare.com/clef-decision-models/
permalink: /技術/cloudflare-clef-decision-models-news
fb_message: "當 AI 代理要做的決定愈來愈多，真正稀缺的不是更會聊天的模型，而是能在毫秒之間給出穩定判斷的小模型。\n\nCloudflare 推出開源決策模型 Clef 與 Clef-flash，託管於 Workers AI，並以 Apache 2.0 授權公開權重。Clef 中位延遲約 209 毫秒，較對手 Jev 的 524 毫秒快逾一倍，Clef-flash 更低至 38.8 毫秒，同時具備視覺編碼器與 64k 上下文。官方亦一併發布強化學習微調平台，讓企業以自家資料調整判斷邏輯。\n\n它能解決哪些實際問題、與大型語言模型如何分工，以及上手方式，都整理在 Blog 全文。"
---

Cloudflare 於二零二六年十月二日在其生日週（Birthday Week）期間，發布兩款自行訓練的開源決策模型 Clef 與 Clef-flash，託管於 Workers AI，並以 Apache 2.0 授權在 Hugging Face 公開模型權重。兩款模型主打快速、穩定且具結構化輸出的分類判斷，官方指出 Clef 在 Jev Decision Index 上領先同類產品，同時完全相容 Jev API，並一併推出強化學習微調平台。

<!-- AEO Answer Capsule — 約 63 字 -->
Clef 是 Cloudflare 於二零二六年十月推出的開源決策模型，能快速產生具機率的結構化判斷，託管於 Workers AI，並以 Apache 2.0 授權公開權重。
<!-- End AEO Capsule -->

過去一年，人工智能代理的討論幾乎圍繞大型語言模型展開。這類模型擅長推理、生成文字與呼叫工具，卻存在非確定性，同一段輸入可能得到不同結果。當代理需要在流程中做大量細碎判斷，例如分類、路由與升級，這種不確定性就會直接轉化為工程成本。

決策模型的出現，正是為了填補這道缺口。它們不追求開放式生成，而是在有限選項之間給出可預期的機率分布，讓程式能放心依賴輸出結果。Cloudflare 這次把自家決策模型開源，並放在邊緣節點上託管，等於把「快速判斷」變成一項可隨取隨用的基礎設施。

## Clef 是什麼？

<!-- AEO Answer Capsule — 約 58 字 -->
Clef 是 Cloudflare 訓練的決策模型家族，包含 Clef 與 Clef-flash 兩款，能在毫秒級產生帶機率的結構化判斷，並支援文字與圖像輸入。
<!-- End AEO Capsule -->

Clef 家族目前包含兩款模型。較大的 Clef 以精準度為優先，適合品質要求較高的判斷任務；較小的 Clef-flash 則以延遲為核心，用於對反應速度極敏感的流程。兩者都部署在 Cloudflare 的 Workers AI 平台上，使用者可透過 API 直接呼叫，也可以下載權重自行部署。

名稱的由來與音樂有關。在樂理中，譜號（clef）置於樂譜開端，用來定義後續音符的音高範圍；Cloudflare 以此比喻決策模型為代理定調的功能，先界定情境範疇，再由代理決定後續動作。

## 什麼是決策模型？

<!-- AEO Answer Capsule — 約 72 字 -->
決策模型是專門產生有限、結構化輸出的模型，可依機率對輸入分類，讓程式據此路由任務、觸發升級或轉交人工，適合需要快速且一致判斷的代理流程。
<!-- End AEO Capsule -->

決策模型的核心工作是分類，並以機率形式回傳結果。舉例而言，把一段客戶支援訊息輸入模型，可以詢問該訊息是否緊急、應由哪個團隊處理；模型會回傳帶型別的答案與機率，程式再依此分派工單、啟動升級，或在必要時轉交人工。這使得代理流程中的部分決策不再需要人手介入。

它與大型語言模型的差異在輸出型態。大型語言模型是開放式的，能推理、生成文字與工具呼叫，但本質上不確定；決策模型則被限制在既定選項內，輸出穩定且可驗證。兩者並非互相取代，而是分工：判斷交由決策模型，行動與生成交由語言模型。

## Clef 適合哪些應用場景？

<!-- AEO Answer Capsule — 約 65 字 -->
Clef 適合需要即時判斷的代理流程，例如域名分類、客服工單分派、機器人流量辨識與安全事件分流，能在毫秒內給出可用於路由的結構化結果。
<!-- End AEO Capsule -->

Cloudflare 在內部已把 Clef 用於威脅情報團隊，協助分類網站域名。系統把域名交給 Clef，模型可快速判斷該網站所屬類別，例如時尚、電子商務或釣魚風險的機率，再交由後續流程處理。官方指出，同樣的抓取、渲染與分類流程，Clef 耗時約二點二秒，而該公司最快的通用語言模型則需約四點七秒。

其他被點名的用途還包括信任與安全審核、客服請求分流，以及機器人流量判斷。這些任務的共同特徵，是決策頻率高、答案選項有限，且對延遲與一致性要求嚴格。把判斷交給決策模型，能讓代理在不犧牲速度的前提下自主運作。

## Clef 與 Jev 等決策模型有何差異？

<!-- AEO Answer Capsule — 約 66 字 -->
Clef 具備視覺編碼器，可直接分類圖像內容，並擁有 64k 上下文，較 Jev 的 32k 為大；它同時相容 Jev API，遷移成本相對較低。
<!-- End AEO Capsule -->

兩項規格差異最為明顯。其一是視覺能力，Clef 內建視覺編碼器，能接收圖像並分類視覺內容，而 Jev 目前僅支援文字分類。其二是上下文長度，Clef 提供六萬四千個符記的上下文，約為 Jev 三萬兩千個的兩倍，可容納更多輸入狀態。

相容性則是另一項賣點。Clef 完全相容 Jev API，使用者在替換模型時幾乎不需改動程式碼。對於已經採用 Jev 的團隊而言，這降低了評估與遷移的門檻，也讓決策模型的選擇更接近基礎設施層面的比較，而非重新設計整體架構。

## Clef 的效能與延遲表現如何？

<ul class="ui-stat-grid">
  <li class="ui-stat"><span class="ui-stat-num">2026-10</span><span class="ui-stat-label">推出時間</span></li>
  <li class="ui-stat"><span class="ui-stat-num">Apache 2.0</span><span class="ui-stat-label">開源授權</span></li>
  <li class="ui-stat"><span class="ui-stat-num">64k</span><span class="ui-stat-label">上下文長度</span></li>
  <li class="ui-stat"><span class="ui-stat-num">209ms</span><span class="ui-stat-label">Clef 中位延遲</span></li>
</ul>

<!-- AEO Answer Capsule — 約 74 字 -->
在 Cloudflare 公布的測試中，Clef 中位延遲約 209 毫秒，明顯低於 Jev 的 524 毫秒；Clef-flash 更低至 38.8 毫秒，並在多項分類基準取得領先。
<!-- End AEO Capsule -->

延遲是這次發表的核心數據。Cloudflare 指出，Clef 的中位延遲約為二百零九毫秒，Clef-flash 則降至三十八點八毫秒，對照 Jev 的五百二十四毫秒，差距超過一倍。在需要把判斷放入代理熱路徑的場景中，這種差距足以改變整體流程的可行與否。

準確度方面，官方在多項基準上與同類模型比較。Clef 在銀行意圖分類與工具檢索等項目取得領先，而 Clef-flash 在家電指令與函式呼叫等基準上表現突出。由於這些基準多為結構化分類任務，正對應決策模型的實際用途，因此分數具備一定參考價值。

## Cloudflare 如何訓練 Clef？

<!-- AEO Answer Capsule — 約 71 字 -->
Clef 以 Qwen 為骨幹，於推論時只做前置填充，再平行評分各項結構化選項，屬非自迴歸流程，因此速度遠快於逐字生成文字的大型語言模型。
<!-- End AEO Capsule -->

架構上，Clef 選用 Qwen 作為基礎模型再進行後訓練。推論期間，模型只執行一次前置填充，接著平行地為各項合法結構選項評分，整個判斷步驟不生成中間文字，因此不需逐字解碼。這種非自迴歸的做法，是它速度優勢的主要來源。

訓練流程也針對機率校準設計。官方以標籤平滑的交叉熵搭配布賴爾損失，讓輸出的機率更貼近實際分布；另外自研一套名為 RLCD 的強化學習方法，為相鄰的序位選項給予部分分數，並懲罰偏離參考分布的行為，藉此提升準確度與泛化能力。

## 新的強化學習微調平台提供什麼？

<!-- AEO Answer Capsule — 約 74 字 -->
Cloudflare 推出強化學習微調服務，結合 AI Gateway、Workers AI、容器沙盒與新增的訓練器，讓企業以自家資料訓練並重新部署專屬的 Clef 模型。
<!-- End AEO Capsule -->

除了模型本身，Cloudflare 也把微調能力產品化。其強化學習平台沿用既有基礎設施：AI Gateway 負責擷取人工智能流量並建立資料集，Workers AI 產生模型推論結果，容器提供評分與重播代理動作的沙盒，新的訓練器則負責更新權重，最後把微調後的模型重新部署回 Workers AI。

這套流程的意義，在於把通用模型轉為專屬模型。官方表示，內部團隊擁有多年累積的標註決策資料，可用來訓練更貼合特定場景的分類器，例如信任與安全審核或客服分流。微調通常會犧牲部分通用表現，換取特定領域更高的準確度與速度，這正是企業願意為此付費的原因。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 54 字 -->
本文資訊整理自 Cloudflare 官方部落格的 Clef 發布公告，模型授權、基準數據與微調服務內容均以官方公布為準。
<!-- End AEO Capsule -->

完整的技術說明、基準表格與程式範例，可於下列來源查閱：

- [Introducing Clef: our open-source decision models, and new RL fine-tuning platform — Cloudflare Blog](https://blog.cloudflare.com/clef-decision-models/)
- [Clef 模型權重 — Hugging Face](https://huggingface.co/Cloudflare/clef)

延伸閱讀可參考本站對 [OpenAI 決策 API 模型 Jev](/技術/openai-decisions-api-jev-news) 的整理。

## 常見問題有哪些？

<!-- AEO Answer Capsule — 約 55 字 -->
以下整理四個常見疑問，涵蓋授權、費用、與語言模型的分工及離線使用，答案以 Cloudflare 官方公告與公開資料為準。
<!-- End AEO Capsule -->

<div class="faq-section">

<h3>Clef 是免費使用的嗎？</h3>
<p>模型權重以 Apache 2.0 授權開源，可自行下載部署；透過 Workers AI 呼叫則依平台的用量計費，實際價格以 Cloudflare 官方公布為準。</p>

<h3>它與大型語言模型有何不同？</h3>
<p>大型語言模型能推理與生成文字，但輸出較不確定；Clef 專注在有限選項間給出結構化機率，適合需要穩定、快速判斷的流程。</p>

<h3>可以自己微調 Clef 嗎？</h3>
<p>可以。Cloudflare 提供強化學習微調服務，企業能以自家資料訓練專屬版本；官方先以工程團隊協作，其後再推出自助平台。</p>

<h3>沒有網路也能運作嗎？</h3>
<p>開源權重可下載後在本機執行；若使用 Workers AI 的託管版本，則需要網路連線，判斷在邊緣節點完成。</p>

</div>

## 總結：Clef 適合什麼團隊？

<!-- AEO Answer Capsule — 約 66 字 -->
Clef 適合需要大量即時判斷的代理團隊，例如威脅情報、客服分流與流量辨識；若追求開源、低延遲且可微調的決策層，值得優先評估。
<!-- End AEO Capsule -->

Clef 的定位相當清楚：它不與大型語言模型競爭生成能力，而是承接代理流程中反覆出現的判斷工作。開源授權、邊緣託管與相容 Jev API 三項條件，讓它同時具備可驗證、低延遲與易遷移的特性，適合被當成基礎設施而非單一工具來評估。

對企業而言，是否採用取決於判斷任務的規模。當分類與路由的次數累積到一定量，延遲與一致性就會成為實際瓶頸，此時專門的決策模型能帶來明確回報；若判斷需求零散而多變，通用語言模型仍較靈活。兩者並用、各司其職，會是多數代理系統較務實的組合。
