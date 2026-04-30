---
layout: post
title: "WebAssembly 入門：讓網頁跑出原生應用速度的下一代技術"
date: 2026-04-30 08:00:00 +0800
categories: [tech]
tags: [WebAssembly, Wasm, 網頁開發, 前端效能, 程式語言]
author: Sun ny
image: /assets/images/posts/2026-04-30-WebAssembly入門-讓網頁跑出原生應用的速度-cover.webp
description: "WebAssembly 正在改變網頁開發的遊戲規則，讓瀏覽器執行接近原生應用的速度。本文帶你從零搞懂 Wasm 是什麼、能做什麼，以及如何踏出第一步。"
---

你有沒有想過，為什麼網頁上的 3D 遊戲就是比桌機版卡？為什麼瀏覽器裡的影片轉檔總是要等那麼久？

答案很簡單：**JavaScript 不夠快**。

別誤會，JavaScript 是很棒的語言，但當你需要在瀏覽器裡做大量數學運算——像是 3D 渲染、影像處理、AI 推論——它就力有未逮了。這時候，**WebAssembly（簡稱 Wasm）** 就登場了。

## WebAssembly 是什麼？

簡單來說，WebAssembly 是一種**可以在瀏覽器裡執行的二進位格式**。它不是一門你要從頭學的新語言，而是讓你用 C、C++、Rust、Go 這些高效能語言寫出來的程式，**直接在瀏覽器裡跑**。

你可以把它想成瀏覽器的「渦輪增壓器」：原本 JavaScript 引擎已經很快了，但遇上計算密集的任務，Wasm 可以再快個 2 到 20 倍。

### 三個關鍵特色

1. **接近原生速度**：Wasm 編譯後的程式碼體積小、解析快，執行效率接近原生應用
2. **語言中立**：不是新語言，而是編譯目標。Rust、C++、Go、AssemblyScript 都能編譯成 Wasm
3. **安全沙箱**：跟 JavaScript 一樣跑在瀏覽器沙箱裡，無法直接存取系統資源

## WebAssembly 能做什麼？

你可能在不知不覺中已經用過 Wasm 了。以下是幾個常見的應用場景：

### 🎮 遊戲引擎

Unity 和 Unreal Engine 都支援將遊戲編譯成 Wasm，直接在瀏覽器裡跑。你玩過的網頁版 3D 遊戲，背後很可能就是 Wasm 在驅動。

### 🎬 影音處理

FFmpeg 已經被移植到 Wasm，讓你在瀏覽器裡就能做影片轉檔，完全不需要上傳到伺服器。隱私更好，速度也不賴。

### 🤖 AI 推論

TensorFlow.js 的 Wasm 後端比純 JavaScript 版本快上好幾倍。在瀏覽器裡跑模型推論，不再是遙不可及的夢想。

### 🖼️ 圖片編輯

Photoshop 網頁版就是用 Wasm 實現的，證明了即使是複雜的桌面軟體也能搬進瀏覽器。

## Wasm vs JavaScript：不是競爭，是合作

很多人誤以為 Wasm 要取代 JavaScript，其實完全不是這樣。兩者的關係更像是這樣：

| 特性 | JavaScript | WebAssembly |
|------|-----------|-------------|
| **擅長** | DOM 操作、事件處理、邏輯控制 | 數學運算、影像處理、效能瓶頸 |
| **執行方式** | JIT 編譯 | 預先編譯（AOT） |
| **除錯** | 容易，原始碼可讀 | 需要 Source Map 輔助 |
|**學習門檻** | 低 | 中（需理解編譯流程） |

**最佳實踐**：用 JavaScript 處理 UI 互動和 DOM，用 Wasm 處理計算密集的任務。兩者透過簡單的 API 互相呼叫，各司其職。

## 五步踏上 Wasm 之路

想開始玩 WebAssembly，不用一次學會 C++ 或 Rust。以下是漸進式的入門路線：

### 第一步：從 Rust 開始

Rust 是目前 Wasm 生系最成熟的語言，工具鏈最完整。安裝好 Rust 後，一行指令就能建立 Wasm 專案：

```bash
cargo install wasm-pack
cargo new --lib my-wasm-project
```

### 第二步：試試 AssemblyScript

如果你只會 JavaScript，**AssemblyScript** 是最友善的選擇。它的語法跟 TypeScript 幾乎一樣，但編譯出來的是 Wasm：

```typescript
export function fibonacci(n: i32): i32 {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}
```

### 第三步：用現成工具鏈

- **wasm-pack**：Rust→Wasm 的打包神器
- **Emscripten**：C/C++→Wasm 的經典工具
- **wasm2wat / wat2wasm**：Wasm 二進位與文字格式互轉

### 第四步：在 JavaScript 中呼叫

Wasm 模組匯出後，在 JS 裡呼叫就跟用普通函數一樣簡單：

```javascript
const { fibonacci } = await import('./my_wasm_module.js');
console.log(fibonacci(10)); // 55
```

### 第五步：部署上線

Wasm 檔案就像 CSS 或圖片一樣，直接放在網頁伺服器上就能用。記得設定正確的 MIME type：`application/wasm`。

## 2026 年的 Wasm 生態

進入 2026 年，WebAssembly 生態已經成熟許多：

- **WASI（WebAssembly System Interface）** 讓 Wasm 跳出瀏覽器，在伺服器端也能跑
- **元件模型（Component Model）** 讓不同語言寫的 Wasm 模組能互相呼叫
- **GC 提案** 讓 Java、Kotlin 等有垃圾回收機制的語言也能輕鬆編譯成 Wasm
- **Wasm 在 Edge Computing 的應用** 越來越廣，CDN 邊緣節點跑 Wasm 已成主流

## 給你的行動建議

如果你是前端開發者，不需要馬上把整個專案改寫成 Wasm。但下次遇到效能瓶頸時，不妨問自己：**「這段計算，Wasm 能幫上忙嗎？」**

從一個小模組開始，感受那種「瀏覽器居然這麼快」的驚喜。一旦體驗過，你就回不去了。

WebAssembly 不是未來，它已經是現在。差別只在於，你什麼時候開始用而已。
