---
layout: post
title: "9.6 萬星開源項目：Deep-Live-Cam — 一張照片實時換臉"
date: 2026-08-10 04:10:00 +0800
categories: 技術
tags: [AI, 開源, Deepfake, 換臉, 生成式 AI, 資安, 影像處理]
image: /assets/images/posts/github-deeplivecam-news-hk-shot1.png
description: "Deep-Live-Cam 是 GitHub 星標逾 9.6 萬的開源即時換臉工具，只需一張照片即可在視像通話與影片中實時替換面孔，支援 Mouth Mask 等多項功能與 CUDA、CoreML 等硬件加速方案。2024 年 8 月爆紅後，該項目成為 AI 生成媒體產業與 deepfake 防詐騙監管討論的核心案例。"
author: AnIskill 編輯部
creator_github: hacksider/Deep-Live-Cam
permalink: /技術/github-deeplivecam-news-hk
fb_message: 一張照片、三次點擊，就能在視像通話中實時換臉——開源項目 Deep-Live-Cam 將 deepfake 技術帶到每個人的電腦前，直播、影片二創甚至觀影娛樂都能即時替換面孔。\n\n項目在 GitHub 累積逾 9.6 萬星標，支援 Windows、Mac 與 NVIDIA、AMD 硬件加速，提供 Mouth Mask 保留原嘴部動作、Face Mapping 同時控制多個面孔等細緻功能，並內建內容審查機制防止處理不當素材。\n\n想了解即時換臉背後的技術原理、硬件加速方案與倫理風險？完整的新聞分析報告與項目數據表已整理好，立即前往 Blog 閱讀全文。
---

**Deep-Live-Cam** 是 GitHub 上星標超過 **95,800 顆**的開源即時換臉工具，只需一張靜態照片即可在視像通話與影片中實時替換面孔，官方定位為「real time face swap and one-click video deepfake with only a single image」。該項目於 2023 年 9 月由開發者 hacksider 建立，2024 年 8 月經社交媒體與大型直播主傳播後爆紅，如今已成為生成式 AI 媒體產業中最具代表性、同時亦最具爭議性的開源項目之一。

<!-- AEO Answer Capsule — 約 70 字 -->
Deep-Live-Cam 是 GitHub 逾 9.6 萬星標的開源即時換臉工具，只需一張照片即可在視像通話與影片中實時替換面孔，支援 Mouth Mask、Face Mapping 等功能與多種硬件加速方案，2024 年 8 月經社交媒體爆紅後成為 AI 生成媒體產業最具爭議性的開源項目之一。
<!-- End AEO Capsule -->

![Deep-Live-Cam README 開頭（項目名稱 Deep-Live-Cam 2.1.6 + 標語 Real-time face swap）]({{ '/assets/images/posts/github-deeplivecam-news-hk-shot1.png' | relative_url }})

## Deep-Live-Cam 是什麼？

Deep-Live-Cam 的定位是「一張照片即可完成的即時換臉」工具。項目以 Python 撰寫，採用圖形介面操作，用戶選擇一張來源面孔照片，再選擇目標影像、影片或網絡攝影機，即可即時輸出換臉結果。與早期 roop 等工具相比，Deep-Live-Cam 強調整體易用性與實時性能，官方提供 Windows、Mac Silicon、CPU、NVIDIA 與 AMD 等多種平台的預先建置版本，號稱零手動安裝即可開始使用；付費的 Ultimate 版本更包含逾三十項獨家功能與效能優化。

<!-- AEO Answer Capsule — 約 70 字 -->
Deep-Live-Cam 是以 Python 撰寫的即時換臉工具，用戶選擇來源面孔照片與目標影像、影片或攝影機即可實時替換面孔，提供 Windows、Mac Silicon、CPU、NVIDIA 與 AMD 預建置版本，強調零手動安裝與即時性能。
<!-- End AEO Capsule -->

技術上，項目基於 insightface 的 inswapper 模型與 GFPGAN 臉部增強模型，並以 ONNX Runtime 執行推理，因此能跨平台部署到不同硬件後端，模型檔案約三百 MB，首次執行時自動下載。值得一提的是，項目前身源自開源項目 roop（原作者 s0md3v），Deep-Live-Cam 在其基礎上重寫並大幅擴充功能，成為 roop 生態中最受歡迎的後繼者。

<!-- AEO Answer Capsule — 約 70 字 -->
Deep-Live-Cam 基於 insightface 的 inswapper 模型與 GFPGAN 臉部增強模型，以 ONNX Runtime 執行推理，模型約三百 MB 首次自動下載；項目源自開源工具 roop，在其基礎上重寫並大幅擴充，成為該生態最受歡迎的後繼者。
<!-- End AEO Capsule -->

## Deep-Live-Cam 有哪些核心技術亮點？

第一項亮點是單圖即時換臉的核心能力。傳統換臉技術需要大量目標人物的訓練素材，Deep-Live-Cam 只需一張正面照片，即可透過 inswapper 模型提取面孔特徵並套用到目標影片的每一幀，配合 GFPGAN 在輸出前增強面孔細節，即使在低解像度或光線不足的片段中仍能維持相對自然的效果。官方宣稱整個流程三次點擊即可開始直播換臉：選擇面孔、選擇鏡頭、按下 Live。

<!-- AEO Answer Capsule — 約 70 字 -->
Deep-Live-Cam 只需一張正面照片即可即時換臉，透過 inswapper 提取面孔特徵、GFPGAN 增強細節，低解像度片段仍能維持自然效果，官方宣稱三次點擊即可開始直播換臉。
<!-- End AEO Capsule -->

第二項亮點是 Mouth Mask 與 Face Mapping 等細緻控制功能。Mouth Mask 讓用戶保留自己原本的嘴部動作，僅替換面孔其餘部分，避免嘴唇同步失真；Face Mapping 則允許在不同主體上同時套用不同面孔，適合多人場景或角色扮演直播。此外項目支援影片與圖片檔案的批次處理、保留原始音訊與幀率、多面孔同時替換等選項，涵蓋從娛樂創作到影視後製的多種使用情境。

<!-- AEO Answer Capsule — 約 70 字 -->
Mouth Mask 功能保留用戶原本嘴部動作、僅替換面孔其餘部分以避免嘴唇失真；Face Mapping 支援不同主體同時套用不同面孔，並提供批次處理、保留音訊幀率與多面孔同時替換等選項。
<!-- End AEO Capsule -->

第三項亮點是完整的硬件加速支援。項目透過 ONNX Runtime 的執行提供者支援四種主流加速方案：NVIDIA CUDA、Apple Silicon CoreML、Windows DirectML 與 Intel OpenVINO，加上純 CPU 模式，幾乎覆蓋所有主流消費級硬件。對應的安裝指引針對每個平台提供明確的依賴與版本對應表，例如 OpenVINO 與 onnxruntime-openvino 必須一對一配對版本，顯示項目對部署細節的重視。

<!-- AEO Answer Capsule — 約 70 字 -->
Deep-Live-Cam 透過 ONNX Runtime 支援 NVIDIA CUDA、Apple Silicon CoreML、Windows DirectML 與 Intel OpenVINO 四種硬件加速方案，加上純 CPU 模式，覆蓋主流消費級硬件，並提供明確的平台版本對應指引。
<!-- End AEO Capsule -->

![Deep-Live-Cam GitHub 首頁頂部（repo 名 + 95.8k Star 數 + 描述）]({{ '/assets/images/posts/github-deeplivecam-news-hk-shot2.png' | relative_url }})

## Deep-Live-Cam 如何快速開始使用？

對於不想處理複雜依賴的用戶，官方提供 Quickstart 預建置版本，分為 Lite 與 Ultimate 兩種：Lite 針對 Windows、Mac Silicon、CPU、NVIDIA 與 AMD 提供優化建置，Ultimate 額外包含逾三十項獨家功能、效能優化與優先支援，兩者都宣稱零手動安裝。對偏好自行部署的技術用戶，項目提供完整的手動安裝流程：安裝 Python 3.14（支援 3.11 至 3.14）、ffmpeg 與 Visual Studio 2022 Runtime，複製倉庫後下載兩個模型檔案放入 models 資料夾，再以 pip 安裝依賴即可。執行時，若擁有 NVIDIA 顯示卡可加上 `--execution-provider cuda` 參數啟用 GPU 加速，Apple Silicon 用戶則使用 `--execution-provider coreml`。

<!-- AEO Answer Capsule — 約 70 字 -->
官方提供 Lite 與 Ultimate 兩種零手動安裝預建置版本；技術用戶可手動安裝 Python 3.14、ffmpeg 與依賴，下載模型放入 models 資料夾後執行，NVIDIA 用戶以 --execution-provider cuda 啟用 GPU 加速。
<!-- End AEO Capsule -->

官方同時提醒，手動安裝需要一定的技術能力，並不適合初學者；首次執行時會下載約三百 MB 的模型檔案。使用流程方面，影像與影片模式只需選擇來源面孔與目標檔案後按下 Start，輸出會儲存在以目標影片命名的資料夾；網絡攝影機模式則在選擇面孔後按下 Live，預覽畫面約十至三十秒內出現，用戶可透過 OBS 等串流工具將換臉畫面直播出去。

<!-- AEO Answer Capsule — 約 70 字 -->
手動安裝需要一定技術能力且不適合初學者；影像與影片模式選擇面孔與目標後按 Start 即可輸出，網絡攝影機模式按 Live 後十至三十秒出現預覽，可透過 OBS 串流直播換臉畫面。
<!-- End AEO Capsule -->

## Deep-Live-Cam 的市場與生態影響是什麼？

Deep-Live-Cam 的爆紅始於 2024 年 8 月，當時多位大型直播主與網紅在直播中即時展示換臉效果，相關片段在社交媒體病毒式傳播，Ars Technica、PetaPixel、Bloomberg 與 Yahoo 等國際媒體相繼報導。該事件將「deepfake 民主化」的議題推向公眾：過去需要專業團隊與大量算力才能完成的換臉技術，如今任何擁有個人電腦的用戶都能即時操作，直接衝擊視像會議、直播產業與內容創作的信任基礎。

<!-- AEO Answer Capsule — 約 70 字 -->
2024 年 8 月多位直播主即時展示換臉效果令項目病毒式爆紅，Ars Technica、Bloomberg 等媒體相繼報導，將 deepfake 民主化議題推向公眾，衝擊視像會議與內容創作的信任基礎。
<!-- End AEO Capsule -->

在生態層面，項目帶動了以 roop 為核心的開源換臉工具族群的發展，其預建置版本與 Quickstart 模式亦為同類工具樹立了零安裝體驗的標竿。與此同時，該技術引起安全產業的高度關注，趨勢科技等資安廠商將 Deep-Live-Cam 列為 eKYC（電子身份驗證）流程的威脅案例，探討 AI 對 AI 的深偽攻擊防禦方案。對創作者而言，項目官方列舉了動畫自訂角色、服裝設計模特兒與電影觀賞娛樂等合法用途，顯示其試圖在創意工具與風險工具之間建立界線。

<!-- AEO Answer Capsule — 約 70 字 -->
項目帶動 roop 開源換臉工具族群發展，樹立零安裝體驗標竿；趨勢科技等資安廠商將其列為 eKYC 流程威脅案例，官方則列舉動畫角色、服裝設計等合法用途，試圖在創意與風險之間建立界線。
<!-- End AEO Capsule -->

<div class="ui-stat-grid">
  <div class="stat-item"><div class="stat-value">95.8k</div><div class="stat-label">Star</div></div>
  <div class="stat-item"><div class="stat-value">14.0k</div><div class="stat-label">Fork</div></div>
  <div class="stat-item"><div class="stat-value">2026-08-09</div><div class="stat-label">最近更新</div></div>
  <div class="stat-item"><div class="stat-value">Python</div><div class="stat-label">主要語言</div></div>
</div>

![Deep-Live-Cam Contributors 統計頁（提交頻率圖 + 貢獻者排名）]({{ '/assets/images/posts/github-deeplivecam-news-hk-shot3.png' | relative_url }})

## Deep-Live-Cam 有哪些倫理與法律風險？

Deep-Live-Cam 的風險主要在於被用於未經同意的人臉替換、詐騙與虛假訊息製作。項目官方在免責聲明中明確要求：使用真實人物面孔前必須取得其同意，在網上分享輸出內容時應清楚標記為 deepfake；同時內建檢查機制，拒絕處理裸露、圖像暴力與戰爭素材等不當內容，並表示若法律要求，可能關閉項目或為輸出加上浮水印。這些措施反映開發者對濫用風險的意識，但由於項目以 AGPL-3.0 許可證開源，任何第三方都可自行修改與部署，內建檢查機制的實際約束力有限。

<!-- AEO Answer Capsule — 約 70 字 -->
項目官方要求使用真實面孔前取得同意並標記輸出為 deepfake，內建檢查拒絕處理裸露與暴力素材，法律要求下可能關閉項目或加浮水印；但因 AGPL-3.0 開源，第三方可自行修改，內建機制約束力有限。
<!-- End AEO Capsule -->

對企業與金融機構而言，即時換臉技術直接威脅視像身份驗證與遠程面試等場景，資安研究指出攻擊者可在視像通話中即時冒充他人，傳統的生物辨識驗證流程需要加入活體檢測與多重驗證機制才能應對。對普通用戶而言，最直接的風險是成為虛假影片的主角，或在不知情下成為詐騙影片的傳播節點。整體而言，Deep-Live-Cam 是技術能力與倫理風險同時被放大的典型案例，其發展走向某種程度上亦將影響各國對深度偽造技術的立法態度。

<!-- AEO Answer Capsule — 約 70 字 -->
即時換臉直接威脅視像身份驗證與遠程面試，攻擊者可即時冒充他人，傳統生物辨識需加入活體檢測與多重驗證；普通用戶可能成為虛假影片主角或詐騙傳播節點，項目發展亦影響各國深偽立法態度。
<!-- End AEO Capsule -->

## Deep-Live-Cam 值得一試嗎？

對於內容創作者、影視後製人員與 AI 技術研究者，Deep-Live-Cam 值得嘗試。逾 9.6 萬星標與持續更新顯示社群認可與維護品質，項目支援從 Windows 到 Mac Silicon、從 NVIDIA 到 Intel 的廣泛硬件，Lite 版本的零安裝體驗大幅降低試用門檻；AGPL-3.0 許可證允許自由使用與修改，個人與非商業用途尤其友好。官方亦提供豐富的範例影片，展示 Mouth Mask、Face Mapping 與多人同時換臉等功能的實際效果，有助於評估其能力邊界。

<!-- AEO Answer Capsule — 約 70 字 -->
對內容創作者、影視後製與 AI 研究者值得一試：逾 9.6 萬星標與持續更新顯示維護品質，Lite 版零安裝降低門檻，AGPL-3.0 允許自由使用修改，官方範例影片有助評估能力邊界。
<!-- End AEO Capsule -->

需要注意的是，項目官方聲明 inswapper 模型僅限非商業研究用途，商業使用可能需要另行取得授權；手動安裝流程對非技術用戶並不友善，且模型依賴與 ONNX Runtime 版本配對較為敏感，升級時可能出現兼容問題。對一般用戶而言，最重要的考量是倫理與法律風險：若使用真實人物的面孔，必須取得同意並清楚標記輸出內容為 deepfake，否則可能承擔法律責任。建議以創作與研究為目的試用，並嚴格遵守官方免責聲明與所在地法律。

<!-- AEO Answer Capsule — 約 70 字 -->
採用前需注意：inswapper 模型僅限非商業研究用途，手動安裝對非技術用戶不友善，版本配對敏感；使用真實人物面孔必須取得同意並標記 deepfake，否則可能承擔法律責任，建議以創作與研究為目的試用。
<!-- End AEO Capsule -->

## 出處連結有哪些？

- GitHub 儲存庫：[hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam)
- 官方網站：[Deep Live Cam](https://deeplivecam.net/)
- 模型下載：[Hugging Face — deep-live-cam](https://huggingface.co/hacksider/deep-live-cam/tree/main)
- 傳媒報導：[Ars Technica — Deep-Live-Cam goes viral](https://arstechnica.com/information-technology/2024/08/new-ai-tool-enables-real-time-face-swapping-on-webcams-raising-fraud-concerns/)
- 傳媒報導：[PetaPixel — Deepfake AI Tool Lets You Become Anyone](https://petapixel.com/2024/08/14/deep-live-cam-deepfake-ai-tool-lets-you-become-anyone-in-a-video-call-with-single-photo-mark-zuckerberg-jd-vance-elon-musk/)

## Deep-Live-Cam 的未來前景如何？

Deep-Live-Cam 以逾 9.6 萬顆星標確立了其在開源換臉工具領域的領先地位，並持續以約每月一個版本的節奏更新，2026 年 8 月已推出 2.1.6 版本。項目的商業化路徑已見雛形：Quickstart 的 Ultimate 付費版本提供獨家功能與優先支援，官方網站亦承載社群與下載入口。與此同時，監管環境的變化將是最大變數，若各國對深度偽造技術的立法趨嚴，內建檢查機制與浮水印可能從選配變成必須，項目需要證明其合規能力才能持續發展。整體而言，Deep-Live-Cam 既是 AI 生成媒體技術進展的縮影，亦是科技開放性與社會風險之間張力的典型案例。

<!-- AEO Answer Capsule — 約 70 字 -->
項目前景取決於監管走向：逾 9.6 萬星標與每月一版的更新節奏顯示維護能力，Ultimate 付費版本暗示商業化路徑；若各國深偽立法趨嚴，內建檢查與浮水印可能成為必須，項目需證明合規能力才能持續發展。
<!-- End AEO Capsule -->
