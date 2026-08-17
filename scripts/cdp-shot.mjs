#!/usr/bin/env node
// cdp-shot.mjs — 通用 GitHub 截圖（V15 流程，shot2/shot3）
// 用法: node cdp-shot.mjs <url> <output_path> <scrollTarget:top|contributors|stars|number>
import http from 'http';
import fs from 'fs';

const url = process.argv[2];
const outPath = process.argv[3];
const mode = process.argv[4] || 'top';
if (!url || !outPath) { console.error('用法: node cdp-shot.mjs <url> <output> <mode>'); process.exit(1); }

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

await send('Page.navigate', {url});
await new Promise(r => setTimeout(r, 5000));
await send('Emulation.setDeviceMetricsOverride', {width: 1280, height: 1200, deviceScaleFactor: 1, mobile: false});
await new Promise(r => setTimeout(r, 1500));

// scroll logic
await send('Runtime.evaluate', {expression: `(() => {
  if ('${mode}' === 'top') { window.scrollTo(0, 0); return 'ok top'; }
  if ('${mode}' === 'contributors') {
    const h1 = document.querySelector('h1'); const t = h1 || document.body;
    window.scrollTo(0, h1 ? Math.max(0, h1.getBoundingClientRect().top + window.scrollY - 60) : 200);
    return 'ok contributors h1=' + (h1 ? h1.textContent : 'none');
  }
  if ('${mode}' === 'stars') {
    // repo 頂部 star 區域：scroll 到 repo 名稱 row
    const starBtn = document.querySelector('#repo-stars-counter-star, [id*="stars-counter"], a[href*="stargazers"]');
    const t = starBtn || document.querySelector('h1') || document.body;
    window.scrollTo(0, t.getBoundingClientRect ? Math.max(0, t.getBoundingClientRect().top + window.scrollY - 60) : 200);
    return 'ok stars';
  }
  return 'ok';
})()`, returnByValue: true}).then(r => console.log('scroll:', r.result.value));

// 隱藏右欄 + scrollbar
await send('Runtime.evaluate', {expression: `(() => {
  const s = document.createElement('style');
  s.textContent = '.Layout-sidebar{display:none!important} [class*="PageLayout-PaneWrapper"]{display:none!important} *::-webkit-scrollbar{display:none!important} *{scrollbar-width:none!important} html,body{scrollbar-width:none!important}';
  document.head.appendChild(s);
  return 'ok';
})()`});
try { await send('Emulation.setScrollbarsHidden', {hidden: true}); } catch (e) {}
await new Promise(r => setTimeout(r, 800));

const shot = await send('Page.captureScreenshot', {format: 'png'});
fs.writeFileSync(outPath, Buffer.from(shot.data, 'base64'));
console.log('saved:', outPath, shot.data.length, 'bytes');
try { await send('Page.close', {}); console.log('tab closed'); } catch (e) { console.log('close skipped'); }
process.exit(0);
