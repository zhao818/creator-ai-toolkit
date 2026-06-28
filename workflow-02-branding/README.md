# 工作流 ② · 品牌排版一键生成（预览版）

> 深海蓝 #1a1a2e + 暖金 #c8a03c
>
> 💰 完整版含：6 区块完整 CSS 代码 + Markdown → HTML 转换 Prompt + 中文乱码终极修法

---

## 设计系统

| 用途 | 色值 | 说明 |
|------|------|------|
| 深海蓝（背景） | `#1a1a2e` | 全幅蓝底区块背景 |
| 暖金（标题/高亮） | `#c8a03c` | 品牌主色，金句、标题 |
| 浅金（副标题/点缀） | `#dcc05e` | 收尾诗行点缀 |
| 正文文字 | `#333` | 15px, 行高 2.0 |

---

## 6 区块排版系统

```
① 开篇诗行    ← 深海蓝全幅 + 白字分行 + 暖金粗体收尾
② 金句 × 3    ← 深海蓝全幅 + 金左边框 + ✦ 前缀
③ 分区标题    ← 深海蓝全幅 + 金左边框 + 白字壹贰叁编号
④ 正文内容    ← 15px / 2.0行高 / 首行缩进
⑤ 收尾诗行    ← 深海蓝全幅 + 暖金分行
⑥ 品牌尾签    ← ✦ + 美好需要创造 + 世界一隅 + 日期
```

---

## 效果展示

### ① 开篇诗行

<!-- 效果示意 -->
<div style="background:#1a1a2e;padding:32px 20px 28px;margin-bottom:24px;">
<p style="color:#c8a03c;font-size:12px;letter-spacing:6px;text-align:center;">世 界 一 隅</p>
<p style="color:#fff;font-size:16px;line-height:2.2;text-align:center;">
分行诗行<br>
<span style="color:#c8a03c;font-weight:bold;">收尾金句</span>
</p>
</div>

### ② 金句区块

<div style="margin:28px 0;padding:20px 18px;background:#1a1a2e;border-left:5px solid #c8a03c;">
<p style="color:#c8a03c;font-size:15px;line-height:2.0;text-align:center;font-weight:bold;">
✦<br><br>金句内容——可独立传播的一句话
</p>
</div>

> `border-left: 5px solid #c8a03c` 是品牌核心识别元素——读者看到金左边框就知道是你的文章。

### ③ 分区标题

<div style="margin:32px 0 16px;padding:10px 0 10px 16px;background:#1a1a2e;border-left:5px solid #c8a03c;">
<p style="color:#fff;font-size:17px;font-weight:bold;letter-spacing:2px;">壹 · 分区标题</p>
</div>

> 用中文数字（壹贰叁肆伍），不用阿拉伯数字。

### ⑥ 品牌尾签

<div style="text-align:center;margin:36px 0 12px;">
✦
</div>
<p style="text-align:center;font-weight:700;color:#1a1a2e;">美好需要创造</p>
<p style="text-align:center;color:#c8a03c;font-size:12px;">世界一隅 · WORLD CORNER</p>

---

## 发布约束

| 约束 | 值 |
|------|-----|
| 标题 | ≤ 9 中文字 |
| 摘要 | ≤ 17 中文字 |
| 笔名 | 美好需要创造 |
| 样式要求 | 所有样式必须内联（公众号不支持 class） |

---

## 💰 完整版包含

- 6 个区块的完整 CSS 代码（复制即用，不需要改）
- Markdown → 品牌 HTML 的 AI 转换 Prompt
- 付费墙钩子区块（红虚线框模板）
- 核心要点区块模板
- 🚨 中文乱码终极修法（踩了 3 次才修好的 `ensure_ascii=False` 方案）
- 推送前逐块检查清单

> 🛒 闲鱼搜「**创造者AI工具包**」¥9.9 买断
