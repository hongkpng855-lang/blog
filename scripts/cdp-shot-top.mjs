#!/usr/bin/env node
// cdp-shot-top.mjs — 截 GitHub repo 首頁頂部（shot2），截完關 tab
// 用法: node cdp-shot-top.mjs <repo_url> <output_path>
import http from 'http';
import fs from 'fs';

const repoUrl = process.argv[2];
const outPath = process.argv[3];
if (!repoUrl || !outPath) { console.error('用法: node cdp-shot-top.mjs <repo_url> <output_path>'); process.exit(1); }

const tabs = await new Promise((resolve, reject) => {
  http.get('http://127.0.0.1:18800/json', res => {
    let d = '';
    res.on('data', c => d += c);
    res.on('end', () => { try { resolve(JSON.parse(d)); } catch (e) { reject(e); } });
  }).on('error', reject);
});

let tab = tabs.find(t => t.type === 'page' && t.url.includes(repoUrl.split('/')[3] + '/' + repoUrl.split('/')[4]));
if (!tab) tab = tabs.find(t => t.type === 'page');
if (!tab) { console.error('冇 browser tab'); process.exit(1); }

const ws = new WebSocket(tab.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
let id = 0;
const pending = new Map();
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m.result); pending.delete(m.id); } };
const send = (method, params = {}) => new Promise(res => { const mid = ++id; pending.set(mid, res); ws.send(JSON.stringify({id: mid, method, params})); });

// 確保 URL 正確
if (!tab.url.includes('github.com')) {
  await send('Page.navigate', {url: repoUrl});
  await new Promise(r => setTimeout(r, 5000));
}

// viewport 1280 寬
await send('Emulation.setDeviceMetricsOverride', {width: 1280, height: 1600, deviceScaleFactor: 1, mobile: false});
await new Promise(r => setTimeout(r, 1500));

// scroll 去頂 + 隱藏 scrollbar
await send('Runtime.evaluate', {expression: `(() => {
  window.scrollTo(0,0);
  const s = document.createElement('style');
  s.textContent = '::-webkit-scrollbar{display:none!important} html,body{scrollbar-width:none}';
  document.head.appendChild(s);
  return 'ok';
})()`});
await new Promise(r => setTimeout(r, 800));

// 截圖
const shot = await send('Page.captureScreenshot', {format: 'png'});
fs.writeFileSync(outPath, Buffer.from(shot.data, 'base64'));
console.log('saved:', outPath, shot.data.length, 'bytes');

// 關 tab 釋放記憶體
try { await send('Page.close', {}); console.log('tab closed'); } catch (e) { console.log('tab close skipped:', e.message); }
process.exit(0);
