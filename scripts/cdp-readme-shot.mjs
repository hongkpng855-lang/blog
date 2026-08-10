#!/usr/bin/env node
// cdp-readme-shot.mjs — 用 CDP 截 GitHub README 開頭（V15 流程）
// 用法: node cdp-readme-shot.mjs <repo_url> <output_path>
import http from 'http';
import fs from 'fs';

const repoUrl = process.argv[2];
const outPath = process.argv[3];
if (!repoUrl || !outPath) { console.error('用法: node cdp-readme-shot.mjs <repo_url> <output_path>'); process.exit(1); }

// 攞 browser 現有 tab（或開新 tab）
const tabs = await new Promise((resolve, reject) => {
  http.get('http://127.0.0.1:18800/json', res => {
    let d = '';
    res.on('data', c => d += c);
    res.on('end', () => {
      try { resolve(JSON.parse(d)); } catch (e) { reject(e); }
    });
  }).on('error', reject);
});

// 搵已有 tab 或者用第一個 page tab
let tab = tabs.find(t => t.type === 'page' && t.url.includes('github.com'));
if (!tab) tab = tabs.find(t => t.type === 'page');
if (!tab) { console.error('冇 browser tab'); process.exit(1); }

const ws = new WebSocket(tab.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
let id = 0;
const pending = new Map();
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m.result); pending.delete(m.id); } };
const send = (method, params = {}) => new Promise(res => { const mid = ++id; pending.set(mid, res); ws.send(JSON.stringify({id: mid, method, params})); });

// 導航去 repo
await send('Page.navigate', {url: repoUrl});
await new Promise(r => setTimeout(r, 5000));

// 加大 viewport（Light mode 默認）
await send('Emulation.setDeviceMetricsOverride', {width: 1280, height: 1600, deviceScaleFactor: 1, mobile: false});
await new Promise(r => setTimeout(r, 1500));

// scroll 去 README 內容（預留 sticky header ~50px）
const sc = await send('Runtime.evaluate', {expression: `(() => {
  const rd = document.querySelector('.markdown-body');
  if (!rd) return 'no-readme';
  const img = rd.querySelector('img');
  const h1 = rd.querySelector('h1');
  const t = img || h1 || rd;
  const top = t.getBoundingClientRect().top + window.scrollY;
  window.scrollTo(0, Math.max(0, top - 50));
  return 'ok scrollY=' + window.scrollY;
})()`, returnByValue: true});
console.log('scroll:', sc.result.value);
await new Promise(r => setTimeout(r, 1000));

// 隱藏右欄 + scrollbar
await send('Runtime.evaluate', {expression: `(() => {
  const s = document.createElement('style');
  s.textContent = '.Layout-sidebar{display:none!important} ::-webkit-scrollbar{display:none!important} html,body{scrollbar-width:none}';
  document.head.appendChild(s);
  return 'ok';
})()`});
await new Promise(r => setTimeout(r, 600));

// 截圖
const shot = await send('Page.captureScreenshot', {format: 'png'});
fs.writeFileSync(outPath, Buffer.from(shot.data, 'base64'));
console.log('saved:', outPath, shot.data.length, 'bytes');

// 2026-08-11：截圖完成後關閉 tab（釋放記憶體，防止 cron 連環失敗）
try {
  await send('Page.close', {});
  console.log('tab closed (memory freed)');
} catch (e) {
  console.log('tab close skipped:', e.message);
}
process.exit(0);
