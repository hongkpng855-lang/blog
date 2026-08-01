---
layout: post
title: "AI 整 3D 教育筆記頁教學：ChatGPT Images 2.0 一句 Prompt 將任何主題變成靚筆記（附實測）"
date: 2026-08-01 17:30:00 +0800
categories: 技術
tags: [ChatGPT, AI 繪圖, 3D 筆記, 教育, Prompt, OpenAI, 學習工具, 科技教學, 香港, auto-publish, chatgpt-images]
image: /assets/images/posts/2026-08-01-chatgpt-images-3d-notebook-cover.jpg
description: "最近網絡流傳好多「3D 教育筆記頁」——好似醫學生手寫 revision notes 咁靚嘅解剖筆記，原來係用 ChatGPT Images 2.0 一句 Prompt 生成！呢篇文拆解個 Prompt 點運作、點樣改做自己嘅主題，仲有我哋親身實測——用同一個風格整咗我哋自己嘅 3D 筆記圖。"
author: "陳志豪 Eric Chan"
---

# AI 整 3D 教育筆記頁教學：ChatGPT Images 2.0 一句 Prompt 將任何主題變成靚筆記（附實測）

> **你有冇見過嗰啲「3D 解剖筆記」？**
>
> 人體骨骼、耳朵、胃部 — 全部畫到好似醫學生手寫嘅 revision notes 咁靚，仲有 3D 模型、手寫標註、彩色間線。好多人以為係設計師逐頁畫，其實 — **係 AI 一句 Prompt 生成**。

最近喺 Facebook 見到 AI 知識帳號 Chris KE 分享咗一條好正嘅 prompt，用 **ChatGPT Images 2.0** 可以將任何主題變成「3D 教育筆記頁」。我即刻實測咗，跟住仲用佢個風格整咗我哋自己嘅筆記圖。

呢篇文同你拆解成個玩法：個 prompt 點運作、點改成自己嘅主題、同埋我嘅實測結果。

---

## <svg class="ui-icon"><use href="#ui-robot"/></svg>呢個風格係咩？

「3D 教育筆記頁」風格 = 三個元素撈埋：

1. **3D 模型**：主題主體（例如人體器官）用超像真 3D 渲染，有質感、有光影
2. **手寫筆記**：藍色原子筆手寫字、紅線 pointer 指住結構、彩色 marker 間標題
3. **螺旋筆記本**：成個版面喺一本打開嘅 spiral notebook 上面，似學生真跡

出嚟嘅效果好「人味」— 完全唔似 AI 生成，因為**手寫字 + 紙張質感**正正係 AI 圖最唔擅長但 ChatGPT Images 2.0 做到嘅嘢。

---

## <svg class="ui-icon"><use href="#ui-newspaper"/></svg>條 Prompt 拆解（自己執過版）

以下係整理過嘅 prompt（原本嗰條係英文，我加咗中文註解）：

```
Create an ultra-realistic educational anatomy notebook page
designed like the handwritten revision notes of an outstanding medical student.

Center the page around a medically accurate 3D model of the [BODY PART],
placed on an open spiral-bound notebook.
Combine premium scientific illustration with realistic handwritten notes
to create a modern, visually engaging study page.

The anatomical model should be the primary focal point,
rendered with textbook-level accuracy, lifelike textures,
realistic biological colors, subtle reflections, soft ambient lighting,
natural depth, and physically based materials.
Use gentle pastel color accents to distinguish major anatomical regions
without compromising realism.

Arrange handwritten annotations around the illustration using blue ink
with natural handwriting variation.
Connect every label to its correct structure using thin red pointer lines
with precise endpoints.
Keep the page spacious, balanced, and uncluttered with generous white space.

At the top, write the handwritten heading:
Human Body 3D Notes
Below it, add a larger handwritten title:
[BODY PART]
Underline both titles neatly using colored marker strokes.
Organize the remaining content into clearly separated handwritten study sections...
```

**運作原理（中文解釋）：**

| Prompt 部分 | 作用 |
|-------------|------|
| `handwritten revision notes of an outstanding medical student` | 設定成「學生手寫筆記」風格，唔似 AI |
| `medically accurate 3D model` | 主體要 3D 渲染 + 解剖學準確 |
| `lifelike textures, soft ambient lighting, physically based materials` | 3D 質感關鍵字 |
| `blue ink with natural handwriting variation` | 手寫字 + 唔好太工整（自然筆跡） |
| `thin red pointer lines with precise endpoints` | 紅色指線連住標註同結構 |
| `generous white space` | 排版要鬆動，唔好逼滿 |

---

## <svg class="ui-icon"><use href="#ui-download"/></svg>點樣用（步驟）

1. 開 **ChatGPT**（要支援 Images 2.0 嘅版本/訂閱）
2. 模型揀 **GPT-4o / Images 2.0**
3. 貼上面條 prompt，將 `[BODY PART]` 改成你嘅主題（例如 `the human heart`、`the lungs`）
4. 等 30-60 秒生成
5. 唔滿意可以叫佢「調整顏色」「換角度」「加多啲手寫字」

**唔淨止解剖** — 將 `educational anatomy notebook page` 改做 `educational astronomy notebook page`、`educational history notebook page`，一樣得！主題隨你換。

---

## <svg class="ui-icon"><use href="#ui-eye"/></svg>我哋嘅實測：用同一個風格整我哋嘅筆記

我參考咗呢個「3D 筆記頁」風格，用我哋自己嘅方法（HTML + 渲染）整咗兩張**我哋自己嘅 3D 筆記圖** — 主題係早排寫嘅《NotebookLM 8 個研究 Prompts》：

![NotebookLM 8 個 Prompts（上半場 1-4）]({{ '/assets/images/posts/2026-08-01-notebooklm-prompts-1.png' | relative_url }})

![NotebookLM 8 個 Prompts（下半場 5-8）]({{ '/assets/images/posts/2026-08-01-notebooklm-prompts-2.png' | relative_url }})

**實測心得：**
- ✅ 螺旋筆記本 + 手寫字 + 彩色卡片，跟到個神髓
- ✅ 文字 100% 精準（我哋用 HTML 整，唔會好似純 AI 圖咁出亂碼字）
- 💡 純 AI 生成嘅 3D 筆記圖文字會亂（尤其中文）— 想文字精準，用 HTML/CSS 重製係最穩陣

---

## <svg class="ui-icon"><use href="#ui-bulb"/></svg>應用場景

- **學生**：將教科書章節變成靚筆記，溫書都開心啲
- **老師/內容創作者**：整教學圖卡，放教材、IG、Blog
- **醫護/科普**：解剖、生理主題超適合（本身 prompt 就係解剖向）
- **任何知識型內容**：將「無聊」嘅主題整到「睇得落眼」

---

## <svg class="ui-icon"><use href="#ui-alert"/></svg>3 個常見錯誤

1. **主題太多字** — 生成圖入面文字太多會亂碼。**Keep it simple**，每頁一個主題
2. **中文主題** — 中文手寫字 AI 好易出錯。中文內容建議用 HTML/CSS 重製（好似我哋咁），英文先用純 AI 生成
3. **貪心加太多元素** — prompt 已經好長，唔好再加「加多啲顏色」「加個背景」— 出嚟會亂

---

## <svg class="ui-icon"><use href="#ui-question"/></svg>FAQ

**Q1：一定要訂閱先用到？**
ChatGPT Images 2.0 部分功能要 Plus/Pro 訂閱。免費版試唔到最新 Images 2.0，但可以試下舊版 DALL-E。

**Q2：可以攞嚟做商業用途？**
生成內容嘅使用權限跟 OpenAI 服務條款，商業用途通常可以，但建議你自行確認最新條款。

**Q3：點解我生成嘅冇咁靚？**
通常係 prompt 唔夠詳細。上面條 prompt 已經係完整版，直接複製貼上，只改 `[BODY PART]`。

**Q4：有冇其他工具做到？**
Midjourney 都得，但 ChatGPT Images 2.0 對「文字渲染」同「跟 prompt 指示」最強 — 呢類多指示 prompt 啱晒佢。

---

## <svg class="ui-icon"><use href="#ui-bulb"/></svg>總結

「3D 教育筆記頁」係 2026 年 AI 繪圖其中一個最實用嘅風格 — 唔係為靚而靚，係**真係整到教學用嘅嘢**。一條 prompt，將任何主題變成學生會鍾意睇嘅筆記。

我哋實測完，仲將個風格變成自己嘅 workflow — 想知點整，可以參考我哋嘅做法（HTML 重製版，文字 100% 精準）。試下整一張你自己主題嘅 3D 筆記，保證你上癮 😄

> **「試過先講」** — 呢個風格我親身玩過，攞去用啦！
