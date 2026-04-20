#!/usr/bin/env python3
import os
import re

posts_dir = "/home/hongk/.openclaw/workspace/jekyll-blog/_posts"

fixed_count = 0
error_count = 0

for filename in sorted(os.listdir(posts_dir)):
    if not filename.endswith('.md'):
        continue
    
    filepath = os.path.join(posts_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到 front matter (--- 之間的內容)
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        print(f"⚠️ {filename}: 找不到 front matter")
        error_count += 1
        continue
    
    front_matter = match.group(1)
    body = content[match.end():]
    
    # 解析 front matter 為字典
    lines = front_matter.split('\n')
    fields = {}
    order = []
    
    for line in lines:
        if ':' in line and not line.strip().startswith('#'):
            key = line.split(':')[0].strip()
            value = line[len(key)+1:].strip()
            if key not in fields:
                fields[key] = value
                order.append(key)
            # 如果已經存在，跳過（只保留第一個）
    
    # 重建 front matter
    new_front_lines = ['---']
    for key in order:
        if key in fields:
            new_front_lines.append(f"{key}: {fields[key]}")
    new_front_lines.append('---')
    
    new_content = '\n'.join(new_front_lines) + '\n' + body
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    # 檢查修復結果
    image_count = sum(1 for k in order if k == 'image')
    if image_count > 1:
        print(f"❌ {filename}: 仍有 {image_count} 個 image")
        error_count += 1
    elif 'image' in fields:
        print(f"✅ {filename}: 已修復")
        fixed_count += 1
    else:
        print(f"ℹ️ {filename}: 無 image 欄位")

print(f"\n修復完成: {fixed_count} 個檔案, 錯誤: {error_count} 個")
