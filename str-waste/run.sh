#!/bin/bash

python $(dirname -- "${BASH_SOURCE[0]}")/run.py "https://service.stuttgart.de/lhs-services/aws/api/ical?street=Rathausplatz&streetnr=1"
