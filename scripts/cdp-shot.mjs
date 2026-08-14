#!/usr/bin/env node
// cdp-shot.mjs — 通用 GitHub 頁面截圖（top / 指定 scrollY）
// 用法: node cdp-shot.mjs <repo_url> <output_path> [scrollY] [height]
import http from 'http';
import fs from 'fs';

const repoUrl = process.argv[2];
const outPath = process.argv[3];
const scrollY = parseInt(process.argv[4] || '0', 10);
const height = parseInt(process.argv[5] || '900', 10);
if (!repoUrl || !outPath) { console.error('用法: node cdp-shot.mjs <repo_url> <output_path> [scrollY] [height]'); process.exit(1); }

const tabs = await new Promise((resolve, reject) => {
  http.get('http://127.0.0.1:18800/json', res => {
    let d = '';
    res.on('data', c => d += c);
    res.on('end', () => { try { resolve(JSON.parse(d)); } catch (e) { reject(e); } });
  }).on('error', reject);
});

let tab = tabs.find(t => t.type === 'page' && t.url.includes('github.com'));
if (!tab) tab = tabs.find(t => t.type === 'page');
if (!tab) { console.error('冇 browser tab'); process.exit(1); }

const ws = new WebSocket(tab.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
let id = 0;
const pending = new Map();
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m.result); pending.delete(m.id); } };
const send = (method, params = {}) => new Promise(res => { const mid = ++id; pending.set(mid, res); ws.send(JSON.stringify({id: mid, method, params})); });

await send('Page.navigate', {url: repoUrl});
await new Promise(r => setTimeout(r, 6000));
await send('Emulation.setDeviceMetricsOverride', {width: 1280, height, deviceScaleFactor: 1, mobile: false});
await new Promise(r => setTimeout(r, 1500));

// 隱藏 scrollbar
await send('Runtime.evaluate', {expression: `(() => { const s = document.createElement('style'); s.textContent = '*::-webkit-scrollbar{display:none!important} *{scrollbar-width:none!important}'; document.head.appendChild(s); return 'ok'; })()`});
await new Promise(r => setTimeout(r, 500));

if (scrollY > 0) {
  await send('Runtime.evaluate', {expression: `window.scrollTo(0, ${scrollY})`});
  await new Promise(r => setTimeout(r, 1200));
}

const shot = await send('Page.captureScreenshot', {format: 'png', captureBeyondViewport: false});
fs.writeFileSync(outPath, Buffer.from(shot.data, 'base64'));
console.log(`saved: ${outPath} (${fs.statSync(outPath).size} bytes)`);

// 關閉 tab（記憶體防護）
await send('Page.close').catch(() => {});
ws.close();
console.log('tab closed (memory freed)');
