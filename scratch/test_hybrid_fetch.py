import os
import sys
# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from streamlit_app import fetch_phone_image

print("Testing fetch_phone_image for 'Apple', 'iPhone 11'...")
url = fetch_phone_image("Apple", "iPhone 11")
print("Result:", url)
