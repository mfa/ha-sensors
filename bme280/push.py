#!/usr/bin/python

import requests
import smbus2
import bme280

from pathlib import Path


def push(data, secret):
    r = requests.post(
        f"http://192.168.0.88:8123/api/webhook/{secret}",
        json={
            "temperature": round(data["temperature"], 1),
            "pressure": int(data["pressure"]),
            "humidity": int(data["humidity"]),
        },
    )
    assert r.status_code == 200


if __name__ == "__main__":
    # copy webhook secret into file .secret
    secret = (Path(__file__).parent / ".secret").open().read().strip()

    port = 1
    address = 0x76
    bus = smbus2.SMBus(port)

    bme280.load_calibration_params(bus, address)
    sensor = bme280.sample(bus, address)

    push(
        {
            "temperature": sensor.temperature,
            "pressure": sensor.pressure,
            "humidity": sensor.humidity,
        },
        secret,
    )
