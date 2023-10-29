#!/usr/bin/python

import requests
import bme680

from pathlib import Path


def push(data, secret):
    r = requests.post(
        f"http://192.168.0.88:8123/api/webhook/{secret}",
        json={
            "temperature": round(data["temperature"], 1),
            "pressure": int(data["pressure"]),
            "humidity": int(data["humidity"]),
            "gas": int(data["gas"]),
        },
    )
    assert r.status_code == 200


if __name__ == "__main__":
    # copy webhook secret into file .secret
    secret = (Path(__file__).parent / ".secret").open().read().strip()

    sensor = bme680.BME680(0x77)

    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)
    sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

    sensor.set_gas_heater_temperature(320)
    sensor.set_gas_heater_duration(150)
    sensor.select_gas_heater_profile(0)

    print(
        {
            "temperature": sensor.data.temperature,
            "pressure": sensor.data.pressure,
            "humidity": sensor.data.humidity,
            "gas": sensor.data.gas_resistance,
        },
        secret,
    )
