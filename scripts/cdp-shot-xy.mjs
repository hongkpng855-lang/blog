#!/usr/bin/env node
// cdp-shot-xy.mjs — 用 CDP 截 GitHub repo 頁面指定位置（top / sidebar）
// 用法: node cdp-shot-xy.mjs <repo_url> <position: top|sidebar|readme> <output_path>
import http from 'http';
import fs from 'fs';

const repoUrl = process.argv[2];
const position = process.argv[3] || 'top';
const outPath = process.argv[4];
if (!repoUrl || !outPath) { console.error('用法: node cdp-shot-xy.mjs <repo_url> <top|sidebar|readme> <output_path>'); process.exit(1); }

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
await new Promise(r => setTimeout(r, 5000));
await send('Emulation.setDeviceMetricsOverride', {width: 1280, height: 1600, deviceScaleFactor: 1, mobile: false});
await new Promise(r => setTimeout(r, 1500));

// 隱藏 scrollbar + 右欄（sidebar 位置時保留右欄）
await send('Runtime.evaluate', {expression: `(() => {
  const s = document.createElement('style');
  s.textContent = '::-webkit-scrollbar{display:none!important} html,body{scrollbar-width:none}';
  document.head.appendChild(s);
  return 'ok';
})()`});
await new Promise(r => setTimeout(r, 600));

if (position === 'top') {
  await send('Runtime.evaluate', {expression: 'window.scrollTo(0, 0); "ok"', returnByValue: true});
  await new Promise(r => setTimeout(r, 800));
} else if (position === 'sidebar') {
  // scroll 到 About 側邊欄可見（通常喺首屏已有；確保 repo 統計入鏡）
  await send('Runtime.evaluate', {expression: 'window.scrollTo(0, 0); "ok"', returnByValue: true});
  await new Promise(r => setTimeout(r, 800));
} else if (position === 'readme') {
  await send('Runtime.evaluate', {expression: `(() => {
    const rd = document.querySelector('.markdown-body');
    if (!rd) return 'no-readme';
    const img = rd.querySelector('img');
    const h1 = rd.querySelector('h1');
    const t = img || h1 || rd;
    const top = t.getBoundingClientRect().top + window.scrollY;
    window.scrollTo(0, Math.max(0, top - 50));
    return 'ok';
  })()`, returnByValue: true});
  await new Promise(r => setTimeout(r, 1000));
}

const shot = await send('Page.captureScreenshot', {format: 'png'});
fs.writeFileSync(outPath, Buffer.from(shot.data, 'base64'));
console.log('saved:', outPath, shot.data.length, 'bytes');

try { await send('Page.close', {}); console.log('tab closed'); } catch (e) { console.log('tab close skipped'); }
process.exit(0);
