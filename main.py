import os
import requests

API_KEY = os.getenv("API_KEY")

def run():
    url = "https://api.siliconflow.cn/v1/images/generations"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "black-forest-labs/FLUX.1-schnell",
        "prompt": "Masterpiece, luxurious AI wealth empire, gold and digital lines, 8k",
        "batch_size": 1
    }
    response = requests.post(url, json=payload, headers=headers)
    print(f"执行状态: {response.status_code}")
    if response.status_code == 200:
        print(f"资产生成成功: {response.json()['images'][0]['url']}")

if __name__ == "__main__":
    run()
