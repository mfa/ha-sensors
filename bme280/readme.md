## install

```
pip install RPi.bme280
```

## homeassistent example config

```
template:
  - trigger:
      - platform: webhook
        webhook_id: !secret bme-secret
        allowed_methods:
          - POST
        # my home assistant is not internet accessable
        local_only: false
    unique_id: "zero1"
    sensor:
      - name: "zero1 Temperature"
        state: "{{ trigger.json.temperature }}"
        unit_of_measurement: "°C"
        device_class: temperature
        unique_id: "zero1_temperature"
      - name: "zero1 Humidity"
        state: "{{ trigger.json.humidity }}"
        unit_of_measurement: "%"
        device_class: humidity
        unique_id: "zero1_humidity"
      - name: "zero1 Pressure"
        state: "{{ trigger.json.pressure }}"
        unit_of_measurement: "hPa"
        device_class: atmospheric_pressure
        unique_id: "zero1_pressure"
```
