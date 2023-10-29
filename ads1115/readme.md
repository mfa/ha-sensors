## install

https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15

```
pip install adafruit-circuitpython-ads1x15
```

I use this for Light Dependent Resistor: https://en.wikipedia.org/wiki/Photoresistor

### homeassistent example config

```
template:
  - trigger:
      - platform: webhook
        webhook_id: !secret ads1115-secret
        allowed_methods:
          - POST
        # my home assistant is not internet accessable
        local_only: false
    unique_id: "zero1"
    sensor:
      - name: "zero1 illuminance"
        state: "{{ trigger.json.illuminance }}"
        unit_of_measurement: "lx"
        device_class: illuminance
        unique_id: "zero1_illuminance"
```
