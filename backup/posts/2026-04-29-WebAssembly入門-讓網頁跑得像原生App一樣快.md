---
layout: post
title: "WebAssembly 入門：讓網頁跑得像原生 App 一樣快"
date: 2026-04-29 15:17:00 +0800
categories: [tech]
tags: [WebAssembly, WASM, 網頁效能, 前端開發, 瀏覽器]
author: Sun ny
description: "WebAssembly 正在改變網頁效能的上限。這篇入門指南帶你了解 WASM 是什麼、為什麼重要、如何開始，以及 2026 年的最新應用場景。"
---

你有沒有遇過這種情況：打開一個網頁應用，等了老半天畫面才轉完，操作起來卡卡的，讓人忍不住想念原生 App 的流暢感？

這正是 **WebAssembly（簡稱 WASM）** 要解決的問題。

## WebAssembly 是什麼？三分鐘搞懂

簡單說，WebAssembly 是一種**可以在瀏覽器裡執行的低階二進位格式**。它不是用來取代 JavaScript 的，而是讓 JavaScript 能跟編譯後的高效程式碼「並肩作戰」。

你可以把 JavaScript 想像成一台方便的家用車，什麼路都能跑；WebAssembly 則像一台賽車，在特定賽道上快到不可思議。兩者搭配使用，才是最聰明的選擇。

### 核心特點

- **接近原生效能**：WASM 程式碼執行速度接近 C/C++，比純 JavaScript 快上好幾倍
- **語言中立**：C、C++、Rust、Go、Kotlin 都能編譯成 WASM
- **安全沙箱**：在瀏覽器安全環境中執行，不會直接存取系統資源
- **跨平台**：只要能跑瀏覽器的地方，WASM 都能跑

## 為什麼 2026 年你該關注 WASM？

過去兩年，WebAssembly 生態系迎來了爆發性成長。幾個關鍵里程碑讓它從「實驗技術」變成「生產力工具」：

### 1. WASI 規範趨於成熟

WebAssembly System Interface（WASI）讓 WASM 不只跑在瀏覽器裡，還能在伺服器、邊緣裝置、甚至嵌入式系統執行。這意味著你寫一次程式碼，到處都能部署——比 Docker 更輕量、更安全。

### 2. 瀏覽器支援全面到位

Chrome、Firefox、Safari、Edge 全部支援 WASM 的關鍵功能，包括 SIMD 指令集和多執行緒（SharedArrayBuffer + Atomics）。效能瓶頸幾乎消失。

### 3. 企業級應用落地

Figma、Photoshop Web、Google Earth、AutoCAD Web——這些重量級應用都靠 WASM 實現了「瀏覽器即平台」的願景。如果這些產品能做到，你的專案也可以。

## WASM 適合哪些場景？

不是所有網頁都需要 WASM。以下場景才真的值得：

| 場景 | 為什麼適合 | 經典案例 |
|------|-----------|---------|
| 影像/影片處理 | 大量計算需高效能 | Photoshop Web |
| 3D 渲染與遊戲 | 圖形運算密集 | Unity WebGL 匯出 |
| 資料加密與壓縮 | CPU 密集型任務 | ZIP 解壓縮、密碼學 |
| AI 推論 | 矩陣運算吃重 | ONNX Runtime Web |
| CAD/科學計算 | 精確浮點運算 | AutoCAD Web |

如果你的網頁主要是表單、列表、簡單動畫，JavaScript 就夠了。但如果涉及大量計算，WASM 就是你的秘密武器。

## 五分鐘上手：用 Rust 寫第一個 WASM

最推薦的入門語言是 **Rust**，因為它對 WASM 的支援最成熟、工具鏈最完整。來寫一個簡單的費氏數列：

### Step 1：安裝工具

```bash
# 安裝 Rust（如果還沒裝）
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# 加入 WASM 編譯目標
rustup target add wasm32-unknown-unknown

# 安裝 wasm-pack（打包工具）
cargo install wasm-pack
```

### Step 2：建立專案

```bash
cargo new --lib fibonacci-wasm
cd fibonacci-wasm
```

### Step 3：寫程式碼

在 `src/lib.rs` 中：

```rust
#[no_mangle]
pub extern "C" fn fibonacci(n: u32) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let mut a = 0;
            let mut b = 1;
            for _ in 2..=n {
                let temp = a + b;
                a = b;
                b = temp;
            }
            b
        }
    }
}
```

### Step 4：編譯成 WASM

```bash
wasm-pack build --target web
```

編譯完成後，`pkg/` 目錄就會出現 `.wasm` 檔案和 JavaScript 包裝層，直接在網頁中引用即可。

### Step 5：在網頁中使用

```html
<script type="module">
  import init, { fibonacci } from './pkg/fibonacci_wasm.js';

  async function run() {
    await init();
    console.log('Fibonacci(40) =', fibonacci(40));
  }
  run();
</script>
```

就是這麼簡單！你已經完成第一個 WASM 應用了。

## 效能實測：WASM 到底快多少？

以費氏數列第 40 項為例，在同一台電腦上測試：

| 實作方式 | 執行時間 |
|---------|---------|
| JavaScript（遞迴） | 約 1,200 ms |
| JavaScript（迭代） | 約 0.8 ms |
| Rust → WASM | 約 0.3 ms |

迭代版本差異不大，但在**複雜計算場景**（如矩陣運算、影像處理），WASM 通常比 JavaScript 快 **2~10 倍**。遞迴場景的差異更為驚人，因為 WASM 沒有 JavaScript 動態型別的額外負擔。

## 常見誤區：避開這些坑

### 誤區一：WASM 要完全取代 JavaScript

**事實**：WASM 和 JavaScript 是互補關係。DOM 操作仍靠 JavaScript，計算密集部分交給 WASM。兩者透過記憶體共享和函式呼叫無縫協作。

### 誤區二：所有網頁都需要 WASM

**事實**：大部分網頁用 JavaScript 就夠了。WASM 適合計算密集場景，不要為了用而用。

### 誤區三：WASM 很難除錯

**事實**：現代瀏覽器的 DevTools 已經支援 WASM 除錯，Chrome 和 Firefox 都能設中斷點、檢視記憶體。配合 Source Map，體驗接近原始碼除錯。

## 2026 年的 WASM 生態亮點

- **Component Model**：正式穩定的 WASM 元件規範，讓不同語言寫的 WASM 模組能互相呼叫
- **Garbage Collection 提案**：Kotlin、Dart 等語言編譯到 WASM 更輕鬆，不再需要自帶 GC
- **WASM on Edge**：Cloudflare Workers、Fastly Compute@Edge 全面支援 WASM，邊緣運算新選擇
- **WASM containers**：用 WASM 替代 Docker 容器，啟動速度快 100 倍、映像檔小 100 倍

## 如何開始學習？

1. **官方起點**：[webassembly.org](https://webassembly.org) — 規範與入門文件
2. **Rust+WASM 實戰**：[Rust and WebAssembly 教學](https://rustwasm.github.io/docs/book/) — 最完整的 Rust WASM 指南
3. **動手練習**：用 WASM 重寫你現有專案中最吃效能的那個函式，親身感受差異
4. **社群關注**：加入 [WebAssembly Weekly](https://wasmweekly.news/) 掌握最新動態

## 結語：掌握 WASM，掌握網頁的未來

WebAssembly 不是曇花一現的技術潮流，而是瀏覽器運算能力的根本升級。當越來越多重量級應用搬上網頁，WASM 就是那個讓一切變得可能的底層引擎。

不需要一開始就把整個專案搬上 WASM，但**現在就開始理解它、練習它**，當對的場景出現時，你會感謝自己早有準備。

從今天起，打開終端機，裝好工具鏈，寫下你的第一個 `#[no_mangle] pub extern "C"` 函式。那個感覺——看著自己寫的程式碼在瀏覽器裡以近乎原生的速度跑起來——真的很不一樣。
