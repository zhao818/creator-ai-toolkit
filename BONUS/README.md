# 🎁 附赠内容

---

## 1. 发布前终极检查清单

打印或保存这张清单。每次推送前 60 秒逐项勾过——**一篇文章因为漏了一个勾而翻车，你已经经历过。**

### 内容层
- [ ] 标题 ≤ 9 中文字
- [ ] 摘要 ≤ 17 中文字
- [ ] 核心命题句独立可站住
- [ ] 开头 3 秒钩子到位
- [ ] 至少 1 句可传播金句
- [ ] 结尾回扣开头
- [ ] 无 AI 套话（"在当今""总而言之""随着...的发展"）
- [ ] 术语全文统一（无混用）

### 排版层
- [ ] ① 开篇诗行 ← 蓝底 + 白字 + 暖金收尾
- [ ] ② 金句 × 3 ← 蓝底 + 金左边框 + ✦
- [ ] ③ 分区标题 ← 壹贰叁 + 蓝底 + 白字
- [ ] ④ 付费钩子（可选）← 红虚线框，60%-70% 位置
- [ ] ⑤ 收尾诗行 ← 蓝底 + 暖金，呼应开篇
- [ ] ⑥ 品牌尾签 ← ✦ + 美好需要创造 + 世界一隅 + 日期
- [ ] 核心要点区块（推荐）

### 技术层
- [ ] 所有样式内联（无 class）
- [ ] API 推送用 `ensure_ascii=False` + `charset=utf-8`
- [ ] 图片有 alt 文本
- [ ] 链接可点击

### 传播层
- [ ] 转发钩子至少 3 处（利他 + 身份 + 情绪）
- [ ] 收藏引导在结尾前
- [ ] 评论提问在结尾

---

## 2. 封面生成脚本

> Python 脚本，生成深海蓝+暖金品牌封面（900×383），可直接运行。

```python
"""
世界一隅 · 公众号封面生成器
用法: python cover_gen.py --title "AI的庄子解法" --subtitle "以有涯随无涯，AI时代庄子的警告" --category "哲学思辨"
输出: cover_ai-de-zhuang-zi-jie-fa.jpg (900×383, JPEG quality=95)
"""

from PIL import Image, ImageDraw, ImageFont
import argparse
import os

# === 品牌色 ===
DEEP_BLUE = (26, 26, 46)       # #1a1a2e 深海蓝
WARM_GOLD = (200, 160, 60)     # #c8a03c 暖金
LIGHT_GOLD = (220, 192, 94)    # #dcc05e 浅金
PALE_GRAY = (180, 180, 210)    # #b4b4d2 摘要灰白
DARK_BG = (18, 18, 38)         # #121226 顶栏底色

# === 字体 ===
# Windows 用户：微软雅黑
FONT_BOLD = "msyh.ttc"    # 粗体
FONT_NORMAL = "msyh.ttc"  # 常规
# Mac 用户替换为：
# FONT_BOLD = "/System/Library/Fonts/PingFang.ttc"
# FONT_NORMAL = "/System/Library/Fonts/PingFang.ttc"

W, H = 900, 383


def create_cover(title, subtitle, category, output_path):
    img = Image.new("RGB", (W, H), DEEP_BLUE)
    draw = ImageDraw.Draw(img)

    # === 顶栏 ===
    draw.rectangle([(0, 0), (W, 44)], fill=DARK_BG)
    try:
        top_font = ImageFont.truetype(FONT_NORMAL, 18)
    except IOError:
        top_font = ImageFont.load_default()
    top_text = "世界一隅 · WORLD CORNER"
    top_bbox = draw.textbbox((0, 0), top_text, font=top_font)
    top_w = top_bbox[2] - top_bbox[0]
    draw.text(((W - top_w) // 2, 10), top_text, fill=LIGHT_GOLD, font=top_font)

    # === 分类标签 ===
    try:
        cat_font = ImageFont.truetype(FONT_NORMAL, 15)
    except IOError:
        cat_font = ImageFont.load_default()
    cat_text = f"· {category} ·"
    cat_bbox = draw.textbbox((0, 0), cat_text, font=cat_font)
    cat_w = cat_bbox[2] - cat_bbox[0]

    cat_y = 70
    # 边框
    draw.rectangle(
        [(W // 2 - cat_w // 2 - 20, cat_y - 4), (W // 2 + cat_w // 2 + 20, cat_y + 28)],
        outline=WARM_GOLD, width=1
    )
    draw.text(((W - cat_w) // 2, cat_y), cat_text, fill=WARM_GOLD, font=cat_font)

    # === 金横线 ===
    draw.line([(W // 4, 115), (W * 3 // 4, 115)], fill=WARM_GOLD, width=2)

    # === 主标题 ===
    try:
        title_font = ImageFont.truetype(FONT_BOLD, 52)
    except IOError:
        title_font = ImageFont.load_default()
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_w = title_bbox[2] - title_bbox[0]
    draw.text(((W - title_w) // 2, 130), title, fill=WARM_GOLD, font=title_font)

    # === 副标题 ===
    try:
        sub_font = ImageFont.truetype(FONT_BOLD, 38)
    except IOError:
        sub_font = ImageFont.load_default()
    if subtitle:
        sub_bbox = draw.textbbox((0, 0), subtitle, font=sub_font)
        sub_w = sub_bbox[2] - sub_bbox[0]
        draw.text(((W - sub_w) // 2, 200), subtitle, fill=WARM_GOLD, font=sub_font)

    # === ✦ ===
    try:
        star_font = ImageFont.truetype(FONT_NORMAL, 22)
    except IOError:
        star_font = ImageFont.load_default()
    star_text = "✦"
    star_bbox = draw.textbbox((0, 0), star_text, font=star_font)
    star_w = star_bbox[2] - star_bbox[0]
    draw.text(((W - star_w) // 2, 255), star_text, fill=WARM_GOLD, font=star_font)

    # === 摘要（可选）===
    # 如需摘要，取消下面注释
    # try:
    #     desc_font = ImageFont.truetype(FONT_NORMAL, 18)
    # except IOError:
    #     desc_font = ImageFont.load_default()
    # desc_text = "你的摘要描述"
    # desc_bbox = draw.textbbox((0, 0), desc_text, font=desc_font)
    # desc_w = desc_bbox[2] - desc_bbox[0]
    # draw.text(((W - desc_w) // 2, 280), desc_text, fill=PALE_GRAY, font=desc_font)

    # === 底栏 ===
    draw.rectangle([(0, H - 44), (W, H)], fill=DARK_BG)
    try:
        bottom_font = ImageFont.truetype(FONT_NORMAL, 14)
    except IOError:
        bottom_font = ImageFont.load_default()
    from datetime import date
    bottom_text = f"美好需要创造 / {date.today().strftime('%Y.%m.%d')}"
    bottom_bbox = draw.textbbox((0, 0), bottom_text, font=bottom_font)
    bottom_w = bottom_bbox[2] - bottom_bbox[0]
    draw.text(((W - bottom_w) // 2, H - 34), bottom_text, fill=PALE_GRAY, font=bottom_font)

    # === 底角金点 ===
    dot_r = 4
    draw.ellipse([(W - 40, H - 30), (W - 40 + dot_r * 2, H - 30 + dot_r * 2)], fill=WARM_GOLD)
    draw.ellipse([(W - 25, H - 30), (W - 25 + dot_r * 2, H - 30 + dot_r * 2)], fill=WARM_GOLD)
    draw.ellipse([(W - 10, H - 30), (W - 10 + dot_r * 2, H - 30 + dot_r * 2)], fill=WARM_GOLD)

    img.save(output_path, "JPEG", quality=95)
    print(f"✅ 封面已生成：{output_path}")
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="世界一隅封面生成器")
    parser.add_argument("--title", required=True, help="主标题（≤9字）")
    parser.add_argument("--subtitle", default="", help="副标题")
    parser.add_argument("--category", default="专栏", help="分类标签")
    parser.add_argument("--output", default=None, help="输出路径")
    args = parser.parse_args()

    if args.output is None:
        safe_name = args.title.replace(" ", "-").replace("？", "").replace("，", "")
        args.output = f"cover_{safe_name}.jpg"

    create_cover(args.title, args.subtitle, args.category, args.output)
```

### 使用方法

```bash
# 安装依赖
pip install Pillow

# 生成封面
python cover_gen.py \
  --title "AI的庄子解法" \
  --subtitle "以有涯随无涯，殆矣" \
  --category "哲学思辨"

# 输出：cover_AI的庄子解法.jpg (900×383)
```

---

## 3. 中文乱码终极修法

公众号 API `POST /cgi-bin/draft/add` 推送中文内容时，最常见的坑：

### 错误症状
- 推送后在公众号后台看到 `\uXXXX` 而不是中文
- 手机上显示乱码

### 原因
Python `requests.post(url, json=data)` 内部用 `json.dumps(data)` 序列化，默认 `ensure_ascii=True`，所有非 ASCII 字符被转义为 `\uXXXX`。微信服务器不反转义。

### 修法（已验证 3 次）

```python
import json
import requests

# ✅ 正确姿势
headers = {'Content-Type': 'application/json; charset=utf-8'}
response = requests.post(
    url,
    data=json.dumps(data, ensure_ascii=False).encode('utf-8'),
    headers=headers
)
```

**永远不要用 `requests.post(url, json=data)` 发中文到微信 API。** 这个坑踩了 3 次才修好，不要再踩第 4 次。
