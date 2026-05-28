import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if not SERPER_API_KEY:
    print("Error: SERPER_API_KEY not found in .env")
    exit(1)

brand_str = "Apple"
model_str = "iPhone 11"
search_query = f"{brand_str} {model_str} smartphone official stock product shot transparent background"

url = "https://google.serper.dev/images"
payload = json.dumps({"q": search_query})
headers = {
    'X-API-KEY': SERPER_API_KEY,
    'Content-Type': 'application/json'
}

try:
    response = requests.request("POST", url, headers=headers, data=payload, timeout=5)
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        images = data.get("images", [])
        print(f"\nTop 10 search results for query: '{search_query}':\n")
        for i, img in enumerate(images[:10]):
            print(f"[{i+1}] Title: {img.get('title')}")
            print(f"    URL: {img.get('imageUrl')}")
            print(f"    Source: {img.get('source')}\n")
    else:
        print("Error response:", response.text)
except Exception as e:
    print("Request failed:", e)
