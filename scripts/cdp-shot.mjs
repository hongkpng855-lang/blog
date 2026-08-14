#!/usr/bin/env node
// cdp-shot.mjs — 通用 GitHub 頁面截圖（開新 tab → 截圖 → 關 tab，防記憶體累積）
// 用法: node cdp-shot.mjs <url> <mode:top|readme|contributors|stargazers> <output_path>
import http from 'http';
import fs from 'fs';

const url = process.argv[2];
const mode = process.argv[3] || 'top';
const outPath = process.argv[4];
if (!url || !outPath) { console.error('用法: node cdp-shot.mjs <url> <mode> <output>'); process.exit(1); }

// 開新 tab（PUT /json/new?<url>）
const newTab = await new Promise((resolve, reject) => {
  const req = http.request({host: '127.0.0.1', port: 18800, path: '/json/new?' + encodeURIComponent(url), method: 'PUT'}, res => {
    let d = '';
    res.on('data', c => d += c);
    res.on('end', () => {
      try { resolve(JSON.parse(d)); } catch (e) { reject(new Error('new tab fail: ' + d.slice(0,200))); }
    });
  });
  req.on('error', reject);
  req.end();
});

const ws = new WebSocket(newTab.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
let id = 0;
const pending = new Map();
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m.result); pending.delete(m.id); } };
const send = (method, params = {}) => new Promise(res => { const mid = ++id; pending.set(mid, res); ws.send(JSON.stringify({id: mid, method, params})); });

await new Promise(r => setTimeout(r, 6000)); // 等頁面 load
await send('Emulation.setDeviceMetricsOverride', {width: 1400, height: 900, deviceScaleFactor: 1, mobile: false});
await new Promise(r => setTimeout(r, 1500));

// 隱藏 scrollbar
await send('Runtime.evaluate', {expression: `(() => {
  const s = document.createElement('style');
  s.textContent = '::-webkit-scrollbar{display:none!important} html,body{scrollbar-width:none}';
  document.head.appendChild(s);
  return 'ok';
})()`});

let pos = 'y=0';
if (mode === 'readme') {
  const sc = await send('Runtime.evaluate', {expression: `(() => {
    const rd = document.querySelector('.markdown-body');
    if (!rd) return 'no-readme';
    const img = rd.querySelector('img');
    const h1 = rd.querySelector('h1');
    const t = h1 || img || rd;
    const top = t.getBoundingClientRect().top + window.scrollY;
    window.scrollTo(0, Math.max(0, top - 50));
    return 'ok scrollY=' + window.scrollY;
  })()`, returnByValue: true});
  pos = 'readme ' + sc.result.value;
} else if (mode === 'contributors') {
  const sc = await send('Runtime.evaluate', {expression: `(() => {
    const h2s = [...document.querySelectorAll('h2')];
    const c = h2s.find(h => h.innerText.trim().toLowerCase().startsWith('contributors'));
    if (c) { const top = c.getBoundingClientRect().top + window.scrollY; window.scrollTo(0, Math.max(0, top - 60)); return 'ok y=' + window.scrollY; }
    // fallback: 頁底
    window.scrollTo(0, document.body.scrollHeight * 0.55);
    return 'fallback y=' + window.scrollY;
  })()`, returnByValue: true});
  pos = 'contrib ' + sc.result.value;
} else if (mode === 'stargazers') {
  const sc = await send('Runtime.evaluate', {expression: `(() => {
    const canvas = document.querySelector('canvas');
    if (canvas) { const top = canvas.getBoundingClientRect().top + window.scrollY; window.scrollTo(0, Math.max(0, top - 80)); return 'ok y=' + window.scrollY; }
    return 'no-canvas y=' + window.scrollY;
  })()`, returnByValue: true});
  pos = 'stars ' + sc.result.value;
}
console.log('mode:', mode, '|', pos);
await new Promise(r => setTimeout(r, 1200));

const shot = await send('Page.captureScreenshot', {format: 'png'});
fs.writeFileSync(outPath, Buffer.from(shot.data, 'base64'));
console.log('saved:', outPath, shot.data.length, 'bytes');

try { await send('Page.close', {}); console.log('tab closed'); } catch (e) { console.log('close skip:', e.message); }
process.exit(0);
