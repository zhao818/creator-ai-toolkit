"""
发布「创造者AI工具包」到闲鱼
价格：¥9.9 尝鲜价
"""
import sys, os
sys.path.insert(0, r'C:\Users\zhaot\world-corner-blog\scripts')

from platforms.goofish import GoofishPlatform

# 读取 README 作为商品描述素材
readme_path = os.path.expanduser(r'~\creator-ai-toolkit\README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    body_md = f.read()

# 商品元数据
meta = {
    "title": "创造者AI工具包",
    "goofish_title": "创造者AI工具包 · 三套AI写作工作流 · Prompt模板+品牌排版+选题融合",
    "goofish_price": "9.9",
}

# 发布
gp = GoofishPlatform()
result = gp.publish(meta, body_md)

print("\n=== 发布结果 ===")
print(result)
