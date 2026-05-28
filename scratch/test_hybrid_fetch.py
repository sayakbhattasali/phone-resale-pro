import os
import sys
# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from streamlit_app import fetch_phone_image

for model in ["iPhone 11", "iPhone 12", "iPhone 13", "iPhone 14"]:
    print(f"Testing fetch_phone_image for 'Apple', '{model}'...")
    url = fetch_phone_image("Apple", model)
    print("Result:", url)
    print()
