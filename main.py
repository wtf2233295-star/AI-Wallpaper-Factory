import os
import requests
import time

API_KEY = os.getenv("API_KEY")

def boss_strategy():
    # 💡 进化逻辑：不再随机生成，而是根据“暴利关键词”生成
    targets = ["Cyberpunk Wealth", "Divine Architecture", "Future Luxury"]
    for target in targets:
        print(f"📡 正在捕捉全球趋势: {target}")
        url = "https://api.siliconflow.cn/v1/images/generations"
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        payload = {
            "model": "black-forest-labs/FLUX.1-schnell",
            "prompt": f"Masterpiece, {target}, 8k, extremely detailed, cinematic lighting",
            "batch_size": 1
        }
        
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            img_url = response.json()['images'][0]['url']
            print(f"💰 资产已入库: {img_url}")
            # 这里是聪明的核心：未来我会教你在这里加一行代码，直接把图发到你的小程序服务器
        time.sleep(2) # 避开频率限制

if __name__ == "__main__":
    boss_strategy()
