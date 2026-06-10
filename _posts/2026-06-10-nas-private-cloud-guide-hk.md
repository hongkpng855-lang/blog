---
layout: post
title: "2026 香港人 NAS 私有雲端儲存實戰指南：自建 Photo Backup、媒體串流同檔案同步嘅完整攻略"
date: 2026-06-10 08:45:00 +0800
categories: [tech]
tags: [NAS, 私有雲, 雲端儲存, Synology, QNAP, Photo Backup, Plex, Jellyfin, 香港, 2026]
author: "Sun ny"
image: /assets/images/posts/2026-06-10-nas-private-cloud-guide-hk-cover.svg
description: "Google Photos 開始收費、iCloud 成日唔夠位、公司文件分散喺幾部電腦——與其每個月俾月費，不如自建 NAS 私有雲。呢篇文由零講起，幫你揀機、設定、仲有香港人最常用嘅 5 大應用場景。"
---

## 前言：你仲爭一個屬於自己嘅雲端

你有冇試過 ——

打開手機先見到「iCloud 儲存空間已滿」，要你俾錢 upgrade？Google Photos 壓縮完啲相變到起晒格？公司份合約喺屋企電腦，Office 部機冇，要 whatsapp 俾自己？

香港人平均每人有 3 部 device（手機、平板、Notebook），但啲 files 從來冇一齊過。

**NAS（Network Attached Storage）** 就係你嘅私人雲端——放喺屋企、自己管、一次性硬件成本、唔使再俾月費。2026 年嘅 NAS，簡單到你 set 一次就用到退休。

## 第一步：你需要 NAS 嗎？先搞清楚你嘅 use case

NAS 唔係人人需要。如果你符合以下任何一個情況，NAS 就值得入手：

### ✅ 你應該買 NAS 嘅 5 個信號

1. **手機相片影片多過 50GB** —— iCloud / Google One 月費越俾越多，幾年落嚟夠買一部 NAS
2. **屋企多過 2 部電腦** —— 文件分散，想一個地方集中存取
3. **有睇戲/聽歌習慣** —— 自己 rip 咗 CD / 下載咗電影，想用電視/平板隨時睇
4. **做 Freelance / 自己生意** —— 要 backup 客戶文件、公司資料，唔想擺喺 Google Drive
5. **怕啲 data 唔見** —— 10 年前啲相同片仲喺度，但部舊電腦已經壞咗

### ❌ NAS 唔適合你嘅情況

- 你只需要 backup 電話相片（Google Photos 免費 compression 夠你用）
- 你所有 files 都放喺 Google / Microsoft 365，好滿意
- 你完全唔想搞 setup / 網絡設定

## 第二步：揀 NAS 硬件（2026 年香港買得到嘅主流選擇）

香港市場最普及係兩大品牌：**Synology** 同 **QNAP**。2026 年仲有 **DIY 方案**（TrueNAS / UnRAID）開始流行。

### Synology（入門首選，適合新手）

| 型號 | Bay數 | 適合 | 大約價格 |
|------|-------|------|---------|
| DS124 | 1-bay | 純 backup 相 + 文件 | $1,200 |
| DS224+ | 2-bay | 家庭用 + 基本媒體串流 | $2,200 |
| DS423+ | 4-bay | 重度用家 + 影片 library | $3,500 |
| DS923+ | 4-bay | 企業/進階用家 + 10GbE | $5,000 |

**推薦俾新手**：DS224+ 係香港最 popular 嘅家庭 NAS，價錢合理、效能足夠、DSM 系統最易上手。

**Synology 優勢**：軟件 DSM 係業界最好——App Store 式套件中心、一鍵安裝 Photo Station / Drive / Media Server，似用 iPhone 咁簡單。

### QNAP（性價比高，適合進階用家）

| 型號 | Bay數 | 適合 | 大約價格 |
|------|-------|------|---------|
| TS-233 | 2-bay | 入門家庭用 | $1,800 |
| TS-464 | 4-bay | 多媒體 + VM | $3,200 |
| TS-673A | 6-bay | 重度用家 | $5,500 |

**QNAP 優勢**：同硬件規格下比 Synology 平 20-30%，HDMI 直出電視播片、VM 支援更好。

### DIY NAS（最抵玩，但要自己搞）

如果你有舊電腦或者唔怕 setup，可以行 **TrueNAS Scale** 或 **UnRAID**：
- 硬件：舊 PC + 幾隻 HDD = $0（如果你有舊機）
- Software：TrueNAS 免費；UnRAID 約 USD$59 一次過
- 適合：想慳錢、鍾意 customize、有 Linux 基本知識嘅人

### 揀 Hard Disk（呢個先係最大開支）

NAS 要 7x24 運行，**唔可以用普通 Desktop HDD**（好快死）。一定要用 **NAS 專用 Hard Disk**：

| 品牌 | 型號 | 容量 | 大約價格（2026 香港） |
|------|------|------|---------------------|
| Seagate | IronWolf | 4TB | $680 |
| Seagate | IronWolf | 8TB | $1,200 |
| Seagate | IronWolf | 12TB | $1,800 |
| WD | Red Plus | 4TB | $650 |
| WD | Red Plus | 8TB | $1,150 |
| WD | Red Pro | 12TB | $1,900 |

**慳錢貼士**：一次過買 2 隻行 RAID 1（互相 mirror），死一隻都唔會冇 data。4TB x2 嘅組合最抵玩，約 $1,300 就搞掂儲存。

## 第三步：5 個香港人最常用嘅 NAS 應用

### 🏆 應用一：Phone Photo Backup（自動備份電話相片）

呢個係最主要嘅用途。無論 Synology Photos 定 QNAP QuMagie，設定都係三步搞掂：

```
1. 裝 App（Synology Photos / QNAP QuMagie）
2. 開「自動 backup」
3. 以後每次返到屋企連接 Wi-Fi，自動 upload 新相
```

**Synology Photos 殺手功能**：
- AI 人臉辨識（認到邊個係你、邊個係女朋友）
- 地點/日期自動分類
- 可以 share 相簿俾屋企人（唔使開 Google Account 俾佢哋）
- **Moments 模式**：似 Google Photos 咁睇相

**vs iCloud / Google Photos**：

| 功能 | NAS | iCloud 2TB | Google One 2TB |
|------|-----|-------------|----------------|
| 一次性成本 | $3,000-5,000 | — | — |
| 月費 | $0 | $78/月 | $55/月 |
| 3年總成本 | ~$4,000 | $2,808 | $1,980 |
| 5年總成本 | ~$4,000 | $4,680 | $3,300 |
| 原畫質 | ✅ 原檔保留 | ✅ | ❌ 會壓縮 |
| 私隱 | ✅ 你 control | ⚠️ Apple 都有 key | ❌ Google scan |
| 多人共用 | ✅ Free | 要 Family Sharing | 要 Family plan |

**結論**：用超過 3 年就回本，用 5 年仲慳過 Google One。

### 🏆 應用二：媒體串流（Movie / TV / Music Server）

將你嘅電影、電視劇、音樂放喺 NAS，用電視/平板/手機直接播。

**推薦軟件**：
- **Plex**（最易用，似 Netflix 介面，$0-USD$4.99/月）
- **Jellyfin**（完全免費開源，介面似 Plex）
- **Infuse**（Apple TV 用家最推薦，直接連 NAS 播）

**香港人特別場景**：
- 喺廳用 Apple TV / Android TV 睇 NAS 啲戲
- 搭地鐵時 offline sync 定幾套戲落 iPad
- 屋企人用唔同 device 各自睇唔同片

### 🏆 應用三：檔案同步（公司文件 + 電腦 backup）

NAS = 你嘅私人 Dropbox，但唔使俾月費。

- **Synology Drive**：似 Google Drive 嘅介面，電腦裝 client 自動 sync
- **QNAP Qsync**：同一功能
- **重要**：可以 set 版本控制——唔小心刪咗 file 都救得返

**工作流程例子**：
```
你 Office 改咗份合約 → 自動 sync 上 NAS
→ 返到屋企開電腦，自動 sync 落嚟
→ 喺街用手機 App 睇最新版本
→ 唔使再 USB / WhatsApp / Email 俾自己
```

### 🏆 應用四：BT 下載（Download Station）

NAS 可以 24 小時 BT 下載，唔使開電腦。

- Synology Download Station / QNAP Download Station
- 支援 BT / Magnet / HTTP / FTP
- Search 完直接 add task，自動 download
- 可以 set schedule（半夜先 DL，慳電）

### 🏆 應用五：Docker / 自建服務（進階玩家）

2026 年最流行嘅功能 —— 喺 NAS 行 Docker container：

| 服務 | 用途 | Docker Image |
|------|------|-------------|
| Home Assistant | 智能家居控制中心 | homeassistant/home-assistant |
| AdGuard Home |全屋 Ad-block + DNS | adguard/adguardhome |
| Vaultwarden | 自建密碼管理器 | vaultwarden/server |
| Jellyfin | 媒體串流 | jellyfin/jellyfin |
| Nginx Proxy Manager | 域名反向代理 | jc21/nginx-proxy-manager |

## 第四步：網絡設定（香港環境要注意嘅嘢）

### 寬頻要求
- NAS 行內網：100Mbps 寬頻已經夠（你 Router 嘅 LAN port 一定快過）
- 街外連返屋企：最少 100Mbps 寬頻（香港大部分 plan 都夠）
- **最重要**：upload speed！如果你成日要街外 access NAS，要揀上載快嘅 plan（Netvigator 1G 光纖上下載對稱）

### Router 設定
1. **固定 IP 俾 NAS** — 喺 Router DHCP Reservation set NAS 一個固定內網 IP
2. **QuickConnect (Synology) / myQNAPcloud** — 唔使搞 Port Forwarding，官方幫你做晒 tunnel
3. **VPN Server** — 如果想 security 行先，set 咗 VPN 先連入屋企網絡再 access NAS

### 🔒 保安設定（一定要做）

**唔跟以下設定，你嘅 NAS 好易俾人 hack：**

1. **熄咗 Admin account** — 開一個新 User 俾自己，停用預設 admin
2. **開 2FA** — Synology DSM 同 QNAP QTS 都支援 Google Authenticator
3. **熄咗唔用嘅服務** — 唔用 FTP？熄咗佢。唔用 Telnet？熄咗佢
4. **Auto Block** — set 5 次錯誤 login 就封 IP 24 小時
5. **防火牆** — 只 allow 香港 IP 或者特定國家 access
6. **定期更新** — DSM / QTS 一出 update 就升（多數係 security patch）

⚠️ **真實案例**：2024 年 QNAP 用家因為冇熄預設 port，俾 ransomware 加密咗全部 files。**呢啲嘢唔係講笑**。

## 第五步：Budget 方案比較（由平到貴）

### 💰 方案 A：最平入門（約 $2,500）
- Synology DS124（1-bay）$1,200
- Seagate IronWolf 4TB $680
- 總計：**約 $1,880**
- 得 1 隻 HDD，冇 RAID 保護，死碟就冇 data
- 適合：純 backup 相，唔介意風險

### 💰💰 方案 B：家庭標準（約 $3,500）⭐ 推薦
- Synology DS224+（2-bay）$2,200
- Seagate IronWolf 4TB x2 $1,360
- 總計：**約 $3,560**
- RAID 1 mirror，死一隻碟都冇事
- 適合：大部分家庭用家

### 💰💰💰 方案 C：進階玩家（約 $6,500）
- Synology DS423+（4-bay）$3,500
- Seagate IronWolf 8TB x2 $2,400
- 總計：**約 $5,900**
- RAID 1 + 預留擴充空間
- Docker 行多個 service

### 💰💰💰💰 方案 D：重度用家（約 $10,000+）
- Synology DS923+（4-bay）$5,000
- Seagate IronWolf 12TB x4 $7,200
- 總計：**約 $12,200**
- RAID 5（可用 36TB 空間）
- 10GbE network + SSD cache

## 常見迷思破解

### ❌ 「NAS 好複雜，唔係普通人玩」
2026 年 Synology DSM 嘅 UI 似 iPhone 咁直觀。大部分功能都係「Next > Next > Finish」就 set 好。我阿媽都識用 Synology Photos backup 相。

### ❌ 「NAS 好食電」
一部 2-bay NAS + 2 隻 HDD，平時 idle 約 20-30W。長開 24x7，一年電費約 **$200-300**。比起月費 cloud storage，微不足道。

### ❌ 「我有 Google Drive 就得啦，唔使 NAS」
Google Drive 係方便，但：
- 大檔案（影片/RAW 相）upload/download 好慢
- 公司機有時 block 咗 Google Drive
- Google 可以 scan 你嘅 content（雖然話唔會用嚟賣廣告）
- 冇咗網絡就用唔到

### ❌ 「死碟咪死晒啲 data？」
如果你行 RAID 1（2-bay）或 RAID 5（4-bay），死一隻碟都唔會冇 data。換隻新碟落去就 rebuild 返。

**但係**：RAID 唔係 backup！重要 data 要另外 backup（offline / offsite / cloud）。

## FAQ

### Q1: NAS 同 Router USB 插 HDD 有咩分別？
Router USB 只係最基本嘅 file sharing，冇版控、冇 AI 相簿、冇媒體 server、冇 Docker。係「有得用」同「好用」嘅分別。

### Q2: 我唔識 set 網絡嘢，會唔會搞唔掂？
Synology 有 QuickConnect，QNAP 有 myQNAPcloud — 只要上到網，佢哋幫你搞好晒 tunnel，唔使搞 port forwarding。跟官方 wizard 行就搞定。

### Q3: NAS 要放喺邊？
- 近 Router（LAN 線最好直接插）
- 通風位置（HDD 會熱，唔好密封櫃）
- 遠離震動/潮濕
- 可以放電視櫃 side / router 隔離

### Q4: Phone backup 要用 Wi-Fi 定可以 5G？
一般 set 自動用 Wi-Fi upload（節省 mobile data）。Synology Photos 可以 set「只有 Wi-Fi 時 backup」。

### Q5: 我想街外睇 NAS 啲片，夠快嗎？
睇你屋企上載速度。香港 1G 光纖上下載對稱，街外 4G/5G 睇 1080p 完全流暢。4K 可能會有 buffering，要轉碼。

### Q6: 我主要用 Mac，NAS 兼容嗎？
全部兼容。Synology / QNAP 支援 SMB / AFP / NFS，Mac Finder 直接 connect 就得。Time Machine backup 去 NAS 都得。

### Q7: 香港邊度買 NAS 平？
- **Jumbo（珍寶）** — 價格最透明
- **Centralfield** — 經常有 promo
- **Price.com.hk** — 格價必用
- **Amazon JP** — 日圓低時 Synology 可以平 20-30%（但要留意電壓同保養）

## 結語：自建雲端，一次投資長年回報

NAS 唔係一部機器 — 係你嘅私人雲端基建。

由 backup 電話相、到公司文件同步、到屋企媒體中心，一部 NAS 搞掂晒。一次性硬件成本，唔使再俾月費，data 喺晒你自己手。

2026 年嘅 NAS 比你想像中易 setup 同平。尤其係如果你屋企有 2 個人以上用、多部 device、同埋開始擔心 cloud storage 越嚟越貴，而家就係入手嘅好時候。

**下一步**：如果你仲諗緊邊部 NAS 適合你，可以睇埋我哋嘅 [智能家居入門指南](https://hongkpng855-lang.github.io/blog/tech/2026/06/10/smart-home-beginners-guide-hk.html) — NAS 其實係智能家居嘅大腦，兩者配合完美。

你有用 NAS 嗎？或者你考慮緊邊個 model？留言話我知！
