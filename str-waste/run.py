import datetime
import json
import sys
from pathlib import Path

import requests


def parse(stream):
    ds = {}
    for line in stream.split("\n"):
        if line.strip() == "BEGIN:VEVENT" and ds:
            yield ds
            ds = {}
        if line.startswith("DTSTART"):
            ds["date"] = str(
                datetime.datetime.strptime(
                    line.split(":")[-1].split("T")[0], "%Y%m%d"
                ).date()
            )
        if line.startswith("SUMMARY"):
            ds["summary"] = line.split(":")[-1].strip()


if __name__ == "__main__":
    # copy webhook secret into file .secret
    secret = (Path(__file__).parent / ".secret").open().read().strip()

    r = requests.get(url=sys.argv[1])
    key_map = {
        "Restmüll 02-wöchentl.": "waste_residual",
        "Altpapier 03-wöchentl.": "waste_paper",
        "Gelber Sack 03-wöchentl.": "waste_yellow_bag",
    }
    dataset = {"waste_yellow_bag": ""}
    for item in parse(r.text):
        _k = item.get("summary")
        if _k in key_map:
            dataset[key_map[_k]] = item.get("date")
            del key_map[_k]

    r = requests.post(f"http://localhost:8123/api/webhook/{secret}", json=dataset)
    assert r.status_code == 200
