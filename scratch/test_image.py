import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from ddgs import DDGS
import time

_TRUSTED_DOMAINS = {
    "gsmarena.com", "apple.com", "samsung.com", "oneplus.com", "google.com",
    "mi.com", "xiaomi.com", "store.google.com", "motorola.com", "nokia.com",
    "vivo.com", "oppo.com", "realme.com", "iqoo.com", "nothing.tech",
    "honor.com", "asus.com", "sony.com", "htc.com", "tcl.com",
    "amazon.com", "amazon.in", "flipkart.com", "croma.com", "bestbuy.com",
    "reliancedigital.in", "vijaysales.com",
    "gadgets360.com", "91mobiles.com", "smartprix.com", "mysmartprice.com",
    "pricebaba.com", "fonearena.com", "gizmochina.com", "phoneradar.com",
    "digit.in", "techradar.com", "tomsguide.com", "cnet.com",
    "notebookcheck.net", "kimovil.com", "phonearena.com",
    "xda-developers.com", "androidauthority.com", "droidlife.com",
    "techadvisor.com", "pocket-lint.com", "indianexpress.com",
    "cdn.mos.cms.futurecdn.net", "m-cdn.phonearena.com",
    "fdn.gsmarena.com", "fdn2.gsmarena.com",
    "images-na.ssl-images-amazon.com", "m.media-amazon.com",
    "rukminim1.flixcart.com", "rukminim2.flixcart.com",
    "i.gadgets360cdn.com", "cdn.pocket-lint.com",
    "image.oppo.com", "image.realme.net",
    "static.tomsguide.com", "static.digit.in",
    "i01.appmifile.com",
    "freepik.com", "img.freepik.com",
    "istockphoto.com", "media.istockphoto.com",
    "pngimg.com", "pngwing.com",
}
_BLOCKED_PATH_WORDS = frozenset([
    "forum", "thread", "leak", "attach", "avatar", "profile",
    "meme", "wallpaper", "thumbnail", "placeholder", "18+", "nsfw",
    "adult", "xxx", "porn", "nude", "sexy",
])

def _domain_of(url):
    from urllib.parse import urlparse
    host = urlparse(url).hostname or ""
    return host.lower().removeprefix("www.")

def _is_trusted_url(url):
    domain = _domain_of(url)
    if not domain:
        return False
    parts = domain.split(".")
    for i in range(len(parts) - 1):
        candidate = ".".join(parts[i:])
        if candidate in _TRUSTED_DOMAINS:
            path_lower = url.lower()
            if any(w in path_lower for w in _BLOCKED_PATH_WORDS):
                return False
            return True
    return False

phones = [
    "iPhone 11", "iPhone 12", "iPhone 13", "iPhone 14", "iPhone 15",
    "iPhone 11 Pro", "iPhone 12 Pro", "iPhone 13 Pro", "iPhone 14 Pro", "iPhone 15 Pro"
]

ddgs = DDGS()

for model in phones:
    query = f'Apple {model} smartphone official product image white background'
    try:
        results = ddgs.images(query, max_results=10, safesearch="strict")
        found = False
        if results:
            for r in results:
                img_url = r.get("image", "")
                if _is_trusted_url(img_url):
                    print(f"[OK] {model} -> {img_url}")
                    found = True
                    break
        if not found:
            print(f"[FAIL] {model}")
            for r in results or []:
                print("   ", r.get("image"))
    except Exception as e:
        print(f"Error {model}:", e)
    time.sleep(1)
