#!/usr/bin/env python3
"""memory-check.py — 檢查系統記憶體健康（2026-08-11 新增）
用途：cron 執行前檢查，記憶體不足時提前警告/清理 browser tabs
用法: python3 memory-check.py [--cleanup]
"""
import subprocess, sys, json, urllib.request, os

def get_mem():
    info = {}
    with open('/proc/meminfo') as f:
        for line in f:
            k, v = line.split(':')[0], int(line.split(':')[1].strip().split()[0])
            info[k] = v
    return info

def check(cleanup=False):
    mem = get_mem()
    total = mem['MemTotal'] / 1024  # MB
    avail = mem['MemAvailable'] / 1024
    swap_free = mem['SwapFree'] / 1024
    swap_total = mem['SwapTotal'] / 1024

    print(f"記憶體: 總 {total:.0f}MB / 可用 {avail:.0f}MB / Swap free {swap_free:.0f}MB ({swap_total:.0f}MB)")
    
    # 壓力評估
    avail_ratio = avail / total
    swap_ratio = swap_free / swap_total if swap_total > 0 else 1
    issues = []
    if avail_ratio < 0.25:
        issues.append(f"⚠️ 可用記憶體偏低 ({avail_ratio*100:.0f}%)")
    if swap_ratio < 0.1:
        issues.append(f"⚠️ Swap 接近爆滿 (free {swap_free:.0f}MB)")

    if not issues:
        print("✅ 記憶體健康")
        return 0

    for i in issues:
        print(i)
    
    # cleanup：關 browser tabs 釋放記憶體
    if cleanup:
        try:
            tabs = json.loads(urllib.request.urlopen('http://127.0.0.1:18800/json', timeout=5).read())
            # 唔關 active tab（保留最少 1 個），關其他
            to_close = tabs[1:] if len(tabs) > 1 else []
            print(f"  關閉 {len(to_close)} 個 browser tabs 釋放記憶體...")
            # 用 CDP close（簡化：直接 kill chromium 太重，留俾 cron agent 處理）
            print("  （tabs 清理由 cron agent 用 browser tool 執行）")
        except Exception as e:
            print(f"  browser check skip: {e}")
    return 1

if __name__ == '__main__':
    cleanup = '--cleanup' in sys.argv
    sys.exit(check(cleanup))
