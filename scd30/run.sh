#!/bin/sh

# i2c clock stretching
/home/pi/scd30/i2c1_set_clkt_tout 20000

python3 /home/pi/scd30/scd30_push.py
