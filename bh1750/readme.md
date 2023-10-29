## BM1750

BH1750 ambient light sensor

datasheet: <https://www.mouser.com/datasheet/2/348/bh1750fvi-e-186247.pdf>

needs ``smbus`` for I2C communication and a convert function to get readable values

### homeassistent example config

```
template:
  - trigger:
      - platform: webhook
        webhook_id: !secret bh1750-secret
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
