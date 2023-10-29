#!/usr/bin/python
import bmp180
import requests

from pathlib import Path


def push(data, secret):
    r = requests.post(
        f"http://192.168.0.88:8123/api/webhook/{secret}",
        json=data,
    )
    assert r.status_code == 200


if __name__ == "__main__":
    # copy webhook secret into file .secret
    secret = (Path(__file__).parent / ".secret").open().read().strip()

    bmp = bmp180.bmp180(0x77)
    push({"temperature": round(bmp.get_temp(), 1)}, secret)
