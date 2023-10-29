#!/usr/bin/python
import smbus
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

    def convertToNumber(data):
        return((data[1] + (256 * data[0])) / 1.2)

    bus = smbus.SMBus(1)
    _data = bus.read_i2c_block_data(0x23, 0x20)
    push({"illuminance": round(convertToNumber(_data))}, secret)
