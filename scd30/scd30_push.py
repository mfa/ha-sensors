import requests
import time

from pathlib import Path

from scd30_i2c import SCD30


def push(data, secret):
    r = requests.post(f"http://192.168.0.88:8123/api/webhook/{secret}", json={
        "co2": round(data[0], 2),
        "temperature": round(data[1], 1),
        "humidity": int(data[2]),
    })
    assert r.status_code == 200


if __name__ == "__main__":
    # copy webhook secret into file .secret
    secret = (Path(__file__).parent / ".secret").open().read().strip()

    scd30 = SCD30()
    scd30.set_measurement_interval(2)
    scd30.start_periodic_measurement()
    while True:
        if scd30.get_data_ready():
            m = scd30.read_measurement()
            if m is not None:
                push(m, secret)
                push_old(m)
                time.sleep(2)
            else:
                time.sleep(0.2)
    scd30.stop_periodic_measurement()
