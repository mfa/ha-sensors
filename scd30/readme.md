# scd30

## sensor

<https://www.sensirion.com/en/environmental-sensors/carbon-dioxide-sensors/carbon-dioxide-sensors-co2/>

## install

tested on raspbian (buster)
(this assumes the sensor code is run as root! -- not tested as user)

```
pip install scd30_i2c
```

activate systemd service:
```
cp scd30.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable scd30
systemctl start scd30
```

### clockspeed stretching

the `i2c1_set_clkt_tout` originates from <https://github.com/raspihats/raspihats/tree/master/clk_stretch>
and is compiled as described in <https://github.com/laurenzgamper/scd30#i2c-clock-stretching>

## homeassistent example config

```
template:
  - trigger:
      - platform: webhook
        webhook_id: !secret co2-secret
        allowed_methods:
          - POST
        # my home assistant is not internet accessable
        local_only: false
    unique_id: "scd30"
    sensor:
      - name: "SCD30 Temperature"
        state: "{{ trigger.json.temperature }}"
        unit_of_measurement: "°C"
        device_class: temperature
        unique_id: "scd30_temperature"
      - name: "SCD30 Humidity"
        state: "{{ trigger.json.humidity }}"
        unit_of_measurement: "%"
        device_class: humidity
        unique_id: "scd30_humidity"
      - name: "SCD30 CO2"
        state: "{{ trigger.json.co2 }}"
        unit_of_measurement: ppm
        device_class: carbon_dioxide
        unique_id: "scd30_co2"
```
