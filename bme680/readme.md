## install

code used: https://github.com/pimoroni/bme680-python

```
pip install bme680
```

## homeassistent example config

```
template:
  - trigger:
      - platform: webhook
        webhook_id: !secret bme680-secret
        allowed_methods:
          - POST
        # my home assistant is not internet accessable
        local_only: false
    unique_id: "zero2"
    sensor:
      - name: "zero2 Temperature"
        state: "{{ trigger.json.temperature }}"
        unit_of_measurement: "°C"
        device_class: temperature
        unique_id: "zero2_temperature"
      - name: "zero2 Humidity"
        state: "{{ trigger.json.humidity }}"
        unit_of_measurement: "%"
        device_class: humidity
        unique_id: "zero2_humidity"
      - name: "zero2 Pressure"
        state: "{{ trigger.json.pressure }}"
        unit_of_measurement: "hPa"
        device_class: atmospheric_pressure
        unique_id: "zero2_pressure"
      - name: "zero2 Gas"
        state: "{{ trigger.json.gas }}"
        unit_of_measurement: "Ohms"
        device_class: gas
        unique_id: "zero2_gas"
```
