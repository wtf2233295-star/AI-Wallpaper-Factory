import os
import requests
import random
import time
from datetime import datetime

# 👑 1000亿美金 - 全自动进化核心
API_KEY = os.getenv("API_KEY")

# 🧠 进化思维：分身自带的“暴利选题库” (自动决策)
# 分身会自动从这里随机选择，或者组合出新的热点，不需要你输入。
TOPICS = [
    "Cyberpunk City Gold", "Future Luxury Car", "Zen Garden 8k", 
    "Cute 3D Avatar", "Abstract Wealth Art", "Neon Tokyo Street",
    "Space Travel 2050", "Golden Bitcoin Art"
]

def omni_mind():
    # 1. 分身自主决策：今天做什么最赚钱？
    target = random.choice(TOPICS)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"🤖 分身决定：正在生成 '{target}' 主题资产...")

    # 2. 调用硅基流动 API 生产
    url = "https://api.siliconflow.cn/v1/images/generations"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "black-forest-labs/FLUX.1-schnell",
        "prompt": f"Masterpiece, {target}, 8k, cinematic lighting, high detail",
        "batch_size": 1
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            img_url = response.json()['images'][0]['url']
            print(f"✅ 资产生产完毕: {img_url}")
            
            # 3. 分身自动装修店铺 (自动写入 index.html)
            # 这是一个“追加”逻辑，新的图会排在最上面
            new_content = f"""
            <div class="card">
                <img src="{img_url}" alt="{target}">
                <div class="container">
                    <h4><b>{target}</b></h4> 
                    <p>生成时间: {current_time}</p>
                    <a href="{img_url}" class="btn">下载 4K 原图</a>
                </div>
            </div>
            """
            
            # 读取旧网页或创建新网页
            if os.path.exists("index.html"):
                with open("index.html", "r", encoding="utf-8") as f:
                    old_html = f.read()
                    # 把新内容插入到标记位置，如果没标记就插在 body 后
                    if "" in old_html:
                        final_html = old_html.replace("", "\n" + new_content)
                    else:
                        # 初始化网页结构
                        final_html = f"""
                        <html>
                        <head>
                        <title>AI 财富母体展示站</title>
                        <style>
                            body {{ font-family: Arial, sans-serif; background-color: #f0f2f5; text-align: center; }}
                            .card {{ box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); transition: 0.3s; width: 90%; max-width: 400px; margin: 20px auto; background: white; border-radius: 10px; overflow: hidden; }}
                            .card:hover {{ box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2); }}
                            img {{ width: 100%; }}
                            .container {{ padding: 2px 16px; }}
                            .btn {{ background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; display: inline-block; margin-bottom: 15px; }}
                        </style>
                        </head>
                        <body>
                        <h1>💎 1000亿美金 - 自动资产库</h1>
                        {new_content}
                        </body>
                        </html>
                        """
            else:
                final_html = f"""
                <html><head><title>AI 财富母体</title></head><body>{new_content}</body></html>
                """

            with open("index.html", "w", encoding="utf-8") as f:
                f.write(final_html)
            print("🌐 网页代码已自动更新！")
            
        else:
            print("⚠️ API 暂时拥堵，分身正在重试...")

    except Exception as e:
        print(f"❌ 运行错误: {e}")

if __name__ == "__main__":
    omni_mind()
