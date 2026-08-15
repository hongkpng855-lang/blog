#!/usr/bin/env node
// cdp-shot.mjs — 通用 CDP 截圖（GitHub 新聞流程 shot2/shot3 用）
// 用法: node cdp-shot.mjs <url> <output_path> <mode:top|scrollToSelector|scrollToBottom> [selector]
import http from 'http';
import fs from 'fs';

const url = process.argv[2];
const outPath = process.argv[3];
const mode = process.argv[4] || 'top';
const selector = process.argv[5] || '';

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

let tab = tabs.find(t => t.type === 'page' && t.url.includes('github.com'));
if (!tab) tab = tabs.find(t => t.type === 'page');

// 冇 tab 就開新 tab（用 CDP 開新 tab 需要 /json/new）
if (!tab) {
  const created = await new Promise((resolve, reject) => {
    const req = http.request({host: '127.0.0.1', port: 18800, path: '/json/new?' + encodeURIComponent('about:blank'), method: 'PUT'}, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => { try { resolve(JSON.parse(d)); } catch (e) { reject(e); } });
    });
    req.on('error', reject);
    req.end();
  });
  tab = created;
}
if (!tab) { console.error('冇 browser tab'); process.exit(1); }

const ws = new WebSocket(tab.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
let id = 0;
const pending = new Map();
ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m.result); pending.delete(m.id); } };
const send = (method, params = {}) => new Promise(res => { const mid = ++id; pending.set(mid, res); ws.send(JSON.stringify({id: mid, method, params})); });

// 導航
await send('Page.navigate', {url});
await new Promise(r => setTimeout(r, 9000));

// viewport
await send('Emulation.setDeviceMetricsOverride', {width: 1280, height: 900, deviceScaleFactor: 1, mobile: false});
await new Promise(r => setTimeout(r, 1500));

// scroll 模式
const expr = `(() => {
  if (${JSON.stringify(mode)} === 'top') { window.scrollTo(0, 0); return 'top'; }
  if (${JSON.stringify(mode)} === 'scrollToSelector') {
    const el = document.querySelector(${JSON.stringify(selector)});
    if (!el) return 'no-sel:' + ${JSON.stringify(selector)};
    const top = el.getBoundingClientRect().top + window.scrollY;
    window.scrollTo(0, Math.max(0, top - 50));
    return 'ok scrollY=' + window.scrollY;
  }
  window.scrollTo(0, document.body.scrollHeight);
  return 'bottom scrollY=' + window.scrollY;
})()`;
const sc = await send('Runtime.evaluate', {expression: expr, returnByValue: true});
console.log('scroll:', sc.result.value);
await new Promise(r => setTimeout(r, 1200));

// 隱藏 scrollbar
await send('Runtime.evaluate', {expression: `(() => {
  const s = document.createElement('style');
  s.textContent = '::-webkit-scrollbar{display:none!important} html,body{scrollbar-width:none}';
  document.head.appendChild(s);
  return 'ok';
})()`});
await new Promise(r => setTimeout(r, 500));

// 截圖
const shot = await send('Page.captureScreenshot', {format: 'png'});
fs.writeFileSync(outPath, Buffer.from(shot.data, 'base64'));
console.log('saved:', outPath, shot.data.length, 'bytes');

// 用完關 tab（釋放記憶體）
try {
  await send('Page.close', {});
  console.log('tab closed (memory freed)');
} catch (e) {
  console.log('tab close skipped:', e.message);
}
process.exit(0);
