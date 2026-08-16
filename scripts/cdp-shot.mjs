#!/usr/bin/env node
// cdp-shot.mjs — 截 GitHub 頁面 top（repo 頂部 / stats）
// 用法: node cdp-shot.mjs <url> <out> <scrollExpr>
import http from 'http';
import fs from 'fs';

const url = process.argv[2];
const out = process.argv[3];
const scrollExpr = process.argv[4] || 'window.scrollTo(0,0)';
const waitMs = parseInt(process.argv[5] || '1500', 10);

const tabs = await new Promise((resolve, reject) => {
  http.get('http://127.0.0.1:18800/json', res => {
    let d = ''; res.on('data', c => d += c); res.on('end', () => resolve(JSON.parse(d)));
  }).on('error', reject);
});
let tab = tabs.find(t => t.type === 'page' && t.url.includes('github.com'));
if (!tab) tab = tabs.find(t => t.type === 'page');
if (!tab) { console.error('冇 browser tab'); process.exit(1); }

const ws = new WebSocket(tab.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
let id = 0; const pending = new Map();
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m.result); pending.delete(m.id); } };
const send = (method, params = {}) => new Promise(res => { const mid = ++id; pending.set(mid, res); ws.send(JSON.stringify({id: mid, method, params})); });

await send('Page.navigate', {url});
await new Promise(r => setTimeout(r, 5000));
await send('Emulation.setDeviceMetricsOverride', {width: 1280, height: 900, deviceScaleFactor: 1, mobile: false});
await new Promise(r => setTimeout(r, 1200));
// 隱藏 scrollbar
await send('Runtime.evaluate', {expression: `(() => { const s=document.createElement('style'); s.id='noscroll'; s.textContent='::-webkit-scrollbar{display:none!important}*{scrollbar-width:none!important}'; document.head.appendChild(s); return 'ok'; })()`});
await send('Runtime.evaluate', {expression: scrollExpr});
await new Promise(r => setTimeout(r, waitMs));
const shot = await send('Page.captureScreenshot', {format: 'png', captureBeyondViewport: false});
fs.writeFileSync(out, Buffer.from(shot.data, 'base64'));
console.log('saved:', out);
// 關 tab（防止 tabs 累積）
await send('Page.close');
ws.close();
