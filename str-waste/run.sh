#!/bin/bash

cd $(dirname -- "${BASH_SOURCE[0]}")
uv run --no-project --with requests run.py "https://service.stuttgart.de/lhs-services/aws/api/ical?street=Rathausplatz&streetnr=1"
