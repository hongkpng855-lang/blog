#!/usr/bin/env node
// cdp-shot.mjs — 用 CDP 截當前 page 指定區域
// 用法: node cdp-shot.mjs <out_path> <mode:top|readme|stats> [repo_url]
import http from 'http';
import fs from 'fs';
const outPath = process.argv[2];
const mode = process.argv[3] || 'top';
const repoUrl = process.argv[4];

const tabs = await new Promise((resolve, reject) => {
  http.get('http://127.0.0.1:18800/json', res => {
    let d=''; res.on('data', c=>d+=c); res.on('end', ()=>{ try{resolve(JSON.parse(d));}catch(e){reject(e);} });
  }).on('error', reject);
});
let tab = tabs.find(t => t.type === 'page');
if (!tab) { console.error('冇 browser tab'); process.exit(1); }
const ws = new WebSocket(tab.webSocketDebuggerUrl);
await new Promise((res, rej)=>{ ws.onopen=res; ws.onerror=rej; });
let id=0; const pending=new Map();
ws.onmessage=e=>{ const m=JSON.parse(e.data); if(m.id&&pending.has(m.id)){pending.get(m.id)(m.result);pending.delete(m.id);} };
const send=(method,params={})=>new Promise(res=>{const mid=++id;pending.set(mid,res);ws.send(JSON.stringify({id:mid,method,params}));});

if (repoUrl) { await send('Page.navigate',{url:repoUrl}); await new Promise(r=>setTimeout(r,6000)); }
await send('Emulation.setDeviceMetricsOverride',{width:1280,height:1600,deviceScaleFactor:1,mobile:false});
await new Promise(r=>setTimeout(r,1200));

// 隱藏右欄 + scrollbar
await send('Runtime.evaluate',{expression:`(()=>{
  const s=document.createElement('style');
  s.textContent='[class*="PageLayout-PaneWrapper"]{display:none!important} .Layout-sidebar{display:none!important} *::-webkit-scrollbar{display:none!important} *{scrollbar-width:none!important} html,body{scrollbar-width:none!important}';
  document.head.appendChild(s);
  if ("${mode}"==="top"){ window.scrollTo(0,0); }
  else if ("${mode}"==="readme"){ const rd=document.querySelector('.markdown-body'); if(rd){const h1=rd.querySelector('h1')||rd.querySelector('img')||rd; const top=h1.getBoundingClientRect().top+window.scrollY; window.scrollTo(0,Math.max(0,top-50));} }
  else if ("${mode}"==="stats"){ window.scrollTo(0, document.body.scrollHeight*0.15); }
  return window.scrollY;
})()`,returnByValue:true});
await new Promise(r=>setTimeout(r,1500));

const shot = await send('Page.captureScreenshot',{format:'png'});
fs.writeFileSync(outPath, Buffer.from(shot.data,'base64'));
console.log('saved:', outPath, fs.statSync(outPath).size, 'bytes');
ws.close();
