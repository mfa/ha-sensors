## sensors used in home assistant

This is a list of the sensors I use with raspberry PIs to push to homeassistant.
The repo exists primarily as a reference for me.

### homeassistant config structure

In my ``configuration.yaml`` I have this line:
```
template: !include_dir_merge_list includes/templates
```
and in ``includes/templates`` extra files for sensors (sometimes combined for a raspberry).
The structure in the sensor yaml files have to be lists, i.e. for a bme280:
```
- trigger:
    - platform: webhook
      webhook_id: !secret zero6-bme
      allowed_methods:
        - POST
      local_only: false
  unique_id: "zero6"
  sensor:
    - name: "zero6 Temperature"
      state: "{{ trigger.json.temperature }}"
      unit_of_measurement: "°C"
      device_class: temperature
      unique_id: "zero6_temperature"
    - name: "zero6 Humidity"
      state: "{{ trigger.json.humidity }}"
      unit_of_measurement: "%"
      device_class: humidity
      unique_id: "zero6_humidity"
    - name: "zero6 Pressure"
      state: "{{ trigger.json.pressure }}"
      unit_of_measurement: "hPa"
      device_class: atmospheric_pressure
      unique_id: "zero6_pressure"
```
