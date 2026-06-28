# 工作流 ② · 品牌排版一键生成

> 深海蓝 #1a1a2e + 暖金 #c8a03c
>
> Markdown → 品牌 HTML，6 区块一键组装

---

## 设计系统

| 用途 | 色值 | 说明 |
|------|------|------|
| 深海蓝（背景） | `#1a1a2e` | 全幅蓝底区块背景 |
| 暖金（标题/高亮） | `#c8a03c` | 品牌主色，金句、标题 |
| 浅金（副标题/点缀） | `#dcc05e` | 收尾诗行点缀 |
| 红色（付费钩子框） | `#e74c3c` | 虚线边框 |
| 深红（付费钩子字） | `#c0392b` | 钩子正文 |
| 正文文字 | `#333` | 15px, 行高 2.0 |
| 次级文字 | `#999` | 尾签日期 |
| 核心要点背景 | `#f8f8f8` | 总结区块 |

---

## 6 区块模板（按顺序，不可调换）

### ① 开篇诗行

```html
<section style="background:#1a1a2e;padding:32px 20px 28px 20px;margin-bottom:24px;">
<p style="color:#c8a03c;font-size:12px;letter-spacing:6px;text-align:center;margin:0 0 20px 0;">世 界 一 隅</p>
<p style="color:#ffffff;font-size:16px;line-height:2.2;text-align:center;margin:0;">
[分行诗行内容，白字]<br>
<span style="color:#c8a03c;font-weight:bold;">[收尾句，暖金粗体]</span>
</p>
</section>
```

**使用说明**：诗行一般 3-5 行，最后一行用暖金粗体收束。诗行内容与文章主题呼应，不是随便写的装饰——它是文章情绪的入口。

### ② 金句（×3，放在正文各关键位置）

```html
<section style="margin:28px 0;padding:20px 18px;background:#1a1a2e;border-left:5px solid #c8a03c;">
<p style="color:#c8a03c;font-size:15px;line-height:2.0;margin:0;text-align:center;font-weight:bold;">
✦<br><br>金句内容
</p>
</section>
```

**使用说明**：
- 每篇文章至少 3 处金句
- 分别放在：开头转折处、中间展开处、结尾升华处
- 金句必须能脱离上下文独立传播（读者截图发朋友圈不需要解释）
- `border-left: 5px solid #c8a03c` 是品牌核心识别元素——不要改

### ③ 分区标题

```html
<section style="margin:32px 0 16px 0;padding:10px 0 10px 16px;background:#1a1a2e;border-left:5px solid #c8a03c;">
<p style="color:#ffffff;font-size:17px;font-weight:bold;margin:0;letter-spacing:2px;">壹 · 分区标题</p>
</section>
```

**使用说明**：用中文数字（壹贰叁肆伍），不用阿拉伯数字。这是品牌调性的一部分。

### ④ 正文内容

```html
<p style="font-size:15px;line-height:2.0;color:#333;text-indent:2em;margin:12px 0;">
正文段落内容。
</p>
```

**使用说明**：
- `text-indent:2em`：首行缩进
- `line-height:2.0`：手机阅读舒适行距
- 段落不超过 4 行（手机屏幕），超过就加空行或小标题断开

**代码块样式**：
```html
<pre style="background:#1a1a2e;color:#c8a03c;padding:16px;border-radius:6px;font-size:13px;line-height:1.8;overflow-x:auto;">
代码内容
</pre>
```

**小标题**：
```html
<p style="color:#1a1a2e;font-size:16px;margin:20px 0 8px 0;"><strong>小标题</strong></p>
```

### ⑤ 收尾诗行

```html
<section style="background:#1a1a2e;padding:32px 20px 28px 20px;margin:36px 0 24px 0;">
<p style="color:#c8a03c;font-size:12px;letter-spacing:6px;text-align:center;margin:0 0 20px 0;">世 界 一 隅</p>
<p style="color:#c8a03c;font-size:15px;line-height:2.2;text-align:center;margin:0;">
[诗行内容，暖金]<br>
<span style="color:#dcc05e;">[点缀句，浅金]</span><br>
<span style="color:#c8a03c;font-weight:bold;">[收尾句，暖金粗体]</span>
</p>
</section>
```

**使用说明**：呼应开篇诗行，形成首尾闭环。收尾诗行的情绪应该是"读完文章后的余韵"，不是简单重复开篇。

### ⑥ 品牌尾签

**前面先放核心要点（可选但推荐）**：
```html
<section style="margin:24px 0;padding:20px 18px;background:#f8f8f8;border-radius:6px;">
<h3 style="color:#1a1a2e;font-size:16px;margin:0 0 12px 0;">核心要点</h3>
<ul style="color:#333;font-size:14px;line-height:2.0;margin:0;padding-left:20px;">
<li><strong>要点标题</strong>：一句话总结。</li>
<li><strong>要点标题</strong>：一句话总结。</li>
<li><strong>要点标题</strong>：一句话总结。</li>
</ul>
</section>
```

**品牌尾签（最终版，禁止修改）**：
```html
<p style="text-align:center;margin:36px 0 12px 0;">
<span style="display:inline-block;margin:0 12px;color:#c8a03c;font-size:16px;vertical-align:middle;">✦</span>
</p>
<p style="text-align:center;margin:0 0 6px;font-size:15px;color:#1a1a2e;font-weight:700;letter-spacing:2px;">美好需要创造</p>
<p style="text-align:center;margin:0 0 6px;font-size:12px;color:#c8a03c;letter-spacing:3px;">世界一隅 · WORLD CORNER</p>
<p style="text-align:center;margin:0 0 20px;font-size:11px;color:#aaa;letter-spacing:1px;">2026年X月X日</p>
<p style="margin:0;font-size:12px;color:#999;">📂 相关参考</p>
<p style="margin:4px 0 0;font-size:13px;">&nbsp; &nbsp; &nbsp; &nbsp;[参考链接] &nbsp; &nbsp;</p>
```

---

## 付费墙钩子（可选）

如果文章设置付费墙：

```html
<section style="margin:36px 0 20px 0;padding:18px 16px;background:#fff5f5;border:2px dashed #e74c3c;border-radius:4px;">
<p style="color:#e74c3c;font-size:13px;font-weight:bold;margin:0 0 10px 0;text-align:center;letter-spacing:2px;">
▼ 免费阅读截止 · 以下付费 ▼
</p>
<p style="color:#c0392b;font-size:15px;line-height:2.0;margin:0;text-indent:2em;">
钩子段落正文——让读者觉得"后面不看亏了"
</p>
</section>
```

**放置位置**：文章 60%-70% 处。钩子要留悬念，不是"后面更精彩"这种废话，是具体的预告。

---

## AI Prompt · Markdown → 品牌 HTML 转换

```markdown
## Prompt 模板

将以下 Markdown 内容转换为品牌 HTML 格式，用于微信公众号发布。

### 品牌规范
- 品牌色：深海蓝 #1a1a2e + 暖金 #c8a03c + 浅金 #dcc05e
- 红色系（付费钩子用）：边框 #e74c3c / 文字 #c0392b
- 正文：font-size:15px; line-height:2.0; color:#333; text-indent:2em
- 代码块：background:#1a1a2e; color:#c8a03c; padding:16px; border-radius:6px
- 金句区块：background:#1a1a2e; border-left:5px solid #c8a03c; color:#c8a03c; font-weight:bold
- 分区标题：background:#1a1a2e; border-left:5px solid #c8a03c; color:#fff; 中文数字编号
- 所有样式必须内联（公众号不支持 class）

### 输出要求
1. 开篇生成诗行（蓝底 + 白字 + 暖金收尾），与文章主题呼应
2. 在文章中合适位置插入 3 个金句区块
3. 用中文数字（壹贰叁）分区
4. 收尾生成诗行（蓝底 + 暖金），与开篇呼应
5. 尾部添加品牌签（✦ + 美好需要创造 + 世界一隅 + 日期）
6. 作者写"美好需要创造"
7. 用 HTML 源码格式输出

### 开始转换
[粘贴你的 Markdown 内容]
```

---

## 🚨 中文乱码解决方案

公众号 API 推送时最常见的问题——中文变 `\uXXXX`：

```python
# ❌ 错误：json= 参数内部 ensure_ascii=True
requests.post(url, json=data)

# ✅ 正确
import json
headers = {'Content-Type': 'application/json; charset=utf-8'}
requests.post(url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers)
```

---

## 发布约束速查

| 约束 | 值 |
|------|-----|
| 标题 | ≤ 9 中文字 |
| 摘要 | ≤ 17 中文字 |
| 笔名 | 美好需要创造 |
| IP | 需在公众号后台加白名单 |
| Content-Type | `application/json; charset=utf-8` |

---

## 推送前逐块检查

- [ ] ① 开篇诗行 ← 蓝底 + 白字分行 + 暖金粗体收尾
- [ ] ② 金句 × 3 ← 蓝底 + 金左边框 + ✦ + 暖金粗体居中
- [ ] ③ 分区标题 ← 蓝底 + 金左边框 + 白字壹贰叁...
- [ ] ④ 付费钩子（可选）← 红虚线框
- [ ] ⑤ 收尾诗行 ← 蓝底 + 暖金分行
- [ ] ⑥ 品牌尾签 ← ✦ + 美好需要创造 + 世界一隅 + 日期
- [ ] 核心要点区块（推荐）← 文章末尾 3-5 条总结
