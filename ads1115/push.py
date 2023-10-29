#!/usr/bin/python
from pathlib import Path

import adafruit_ads1x15.ads1015 as ADS
import board
import busio
import requests
import smbus
from adafruit_ads1x15.analog_in import AnalogIn


def push(data, secret):
    r = requests.post(
        f"http://192.168.0.88:8123/api/webhook/{secret}",
        json=data,
    )
    assert r.status_code == 200


if __name__ == "__main__":
    # copy webhook secret into file .secret
    secret = (Path(__file__).parent / ".secret").open().read().strip()

    ads = ADS.ADS1015(busio.I2C(board.SCL, board.SDA))
    chan0 = AnalogIn(ads, ADS.P0)
    chan1 = AnalogIn(ads, ADS.P1)

    push({
        "illuminance1": chan0.value,
        "illuminance2": chan1.value,
    }, secret)
