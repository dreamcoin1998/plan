import requests
import sys
from base64 import b64encode
from pathlib import Path

HOST = "https://cardiddecode.market.alicloudapi.com"
PATH = "/api/decode_cardid_aliyun"


def verify(url, appcode, fname):
    data = {"imgbase64": b64encode(Path(fname).read_bytes()).decode()}
    headers = {
        "Authorization": f"APPCODE {appcode}",
        "Content-Type": "application/json; charset=UTF-8",
    }
    requests.packages.urllib3.disable_warnings()
    r = requests.post(url, json=data, headers=headers, verify=False)
    r.raise_for_status()
    return r.json()


def main(appcode, image):
    url = HOST + PATH
    appcode = appcode  # appcode = 'xxx'
    fname = image  # fname = 'xxx.jpg'
    result = verify(url, appcode, fname)
    print(f"Response from ``{url}`` for ``{fname}``:\n{result}")


def load_appcode():
    for fname in ("appcode", "appcode.txt"):
        p = Path(fname)
        if p.exists():
            appcode = p.read_text().strip()
            break
    else:
        appcode = input("appcode: ").strip()
    return appcode


def image_name():
    if sys.argv[1:]:
        fname = sys.argv[1]
    else:
        fname = None
    if not fname or not Path(fname).exists():
        for suffix in (".jpg", ".png"):
            imgs = list(Path().glob(f"*{suffix}"))
            if imgs:
                fname = imgs[0]
                break
        else:
            fname = input("Image file name: ").strip()
    return fname