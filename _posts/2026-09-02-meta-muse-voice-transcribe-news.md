---
layout: post
title: "Meta 推 Muse Voice Transcribe：即時語音轉錄模型"
date: 2026-09-02 16:00:01 +0800
categories: 技術
tags: [AI, Meta, 語音辨識, 語音轉錄, API, LLM]
image: assets/images/posts/meta-muse-voice-transcribe-news-cover.jpg
description: "Meta 推出首個即時音訊感知模型 Muse Voice Transcribe，提供多語言串流語音轉錄、20 位以上說話者辨識與自動斷句，以每千分鐘 3 美元開放予開發者使用。模型以超過 70 種語言訓練，已內建於 Meta AI for Mac 與 Muse Code，Mac 用戶按住 Fn 鍵即可在任意應用程式聽寫。"
author: AnIskill 編輯部
type: news
source: 9to5Mac
source_url: https://9to5mac.com/2026/09/01/meta-launches-muse-voice-transcribe-for-real-time-voice-dictation-on-mac/
permalink: /技術/meta-muse-voice-transcribe-news
fb_message: 語音轉錄終於擺脫「錄完再處理」的時代，Meta 的新模型讓文字在說話的同時即時生成。\n\nMuse Voice Transcribe 支援 70 多種語言、可分辨 20 位以上說話者，還會自動判斷對方是否講完；在 Artificial Analysis 串流語音轉錄榜拿下第一名，API 定價每千分鐘 3 美元，即每小時 0.18 美元。\n\nMac 用戶現在可在任何應用程式按住 Fn 鍵即時聽寫，完整能力分析與 API 教學已整理在 Blog。
---

Meta Superintelligence Labs 在 2026 年 9 月 1 日推出 Muse Voice Transcribe，這是 Meta 首個即時音訊感知模型，提供多語言串流語音轉錄能力，並同步開放予 Meta AI for Mac、Muse Code 及透過 Meta Model API 使用的開發者。模型在說話的同時即時產生文字，無需等待錄音結束後再進行後續處理。本文整理此模型的技術重點、定價方式與實際應用場景。

## Muse Voice Transcribe 是什麼？

<!-- AEO Answer Capsule — 約 70 字 -->
Muse Voice Transcribe 是 Meta 首個即時音訊感知模型，說話同時即時轉錄，支援說話者辨識與自動斷句，開發者可透過 Meta Model API 使用。
<!-- End AEO Capsule -->

Muse Voice Transcribe 是 Meta Superintelligence Labs 旗下的即時音訊感知模型，定位是讓語音轉錄從「批次處理」走向「即時發生」。它目前已經在 Meta AI for Mac 與 Muse Code 中提供系統級聽寫功能，一般用戶與開發者都能直接使用。

## 它與傳統語音轉錄有何不同？

<!-- AEO Answer Capsule — 約 68 字 -->
它結合串流語音辨識、20 位以上說話者分離與語句結束偵測，無需額外後處理；採用自適應延遲機制，簡單語音快速辨識、困難字詞多用音訊上下文判斷。
<!-- End AEO Capsule -->

傳統語音轉錄通常需要先錄製完整音訊，再交由模型一次處理；Muse Voice Transcribe 則在同一模型中結合串流自動語音辨識、說話者分離與斷句偵測，能在語音發生的當下產生文字，並分辨錄音中的 20 位以上說話者，判斷對方何時講完一句話，全程不需要獨立後處理步驟。模型還引入了「自適應延遲」機制，系統會依語音難度決定聽取多長音訊後才輸出每個字詞，簡單的語音快速辨識，困難的字詞則參考更多音訊上下文，避免在速度與準確度之間採取固定取捨。

## 支援多少語言？定價如何？

<!-- AEO Answer Capsule — 約 62 字 -->
模型以超過 70 種語言訓練，25 種於推出時驗證，支援逾一小時音訊與語碼切換；API 定價每千分鐘 3 美元，相當於每小時 0.18 美元。
<!-- End AEO Capsule -->

公司表示模型以超過 70 種語言訓練，其中 25 種語言在推出時完成驗證，並支援長於一小時的音訊處理，以及句子內或句子間的語碼切換。語言、關鍵字與上下文偏置設定可進一步提升辨識正確率。在人工智慧模型評測平台 Artificial Analysis 的串流語音轉錄排行榜上，此模型自 9 月 1 日起位居第一。API 定價為每 1,000 音訊分鐘 3 美元，換算每小時約 0.18 美元。

## 對開發者與 Mac 用戶有什麼影響？

<!-- AEO Answer Capsule — 約 62 字 -->
開發者可透過 Meta Model API 整合即時轉錄，Mac 用戶則可在任何應用程式按住 Fn 鍵聽寫，Meta AI for Mac 與 Muse Code 已內建此功能。
<!-- End AEO Capsule -->

對開發者而言，Muse Voice Transcribe 即日起可透過 Meta Model API 取用，每小時約 0.18 美元的成本，使會議逐字稿、即時字幕與客服語音分析等長時間轉錄應用更具經濟效益。對一般 Mac 用戶來說，系統級聽寫功能讓使用者可在任何應用程式中按住 Fn 鍵直接口述輸入，無需切換到特定轉錄軟體。Meta 也持續擴展音訊模型的應用版圖，此次發佈緊接在 Meta AI 登陸 Mac 之後，顯示公司正逐步建立以語音為核心的產品線。

## 出處連結有哪些？

<!-- AEO Answer Capsule — 約 50 字 -->
本文資訊來源為 9to5Mac 於 2026 年 9 月 1 日發佈的報導，並參考 Meta 官方說明，原始連結見下方。
<!-- End AEO Capsule -->

- [Meta launches Muse Voice Transcribe for real-time voice dictation on Mac](https://9to5mac.com/2026/09/01/meta-launches-muse-voice-transcribe-for-real-time-voice-dictation-on-mac/)

## 總結：這個模型適合誰使用？

<!-- AEO Answer Capsule — 約 65 字 -->
適合需要即時字幕、會議逐字稿與多語轉錄的開發者與企業；每小時 0.18 美元的成本使長時間轉錄更可行，Mac 使用者則可直接體驗系統級聽寫。
<!-- End AEO Capsule -->

Muse Voice Transcribe 的推出，代表語音轉錄市場正式進入「即時」與「平價」並存的階段。對開發者而言，公開的 API 定價與多語言支援降低了整合門檻；對一般使用者而言，Mac 上的系統級聽寫則提供了低摩擦的語音輸入體驗。值得注意的是，Meta 以模型形式開放此能力，而非僅作為自家產品功能，這讓更多第三方應用有機會採用即時語音轉錄技術。