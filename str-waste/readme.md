## Stuttgart waste

this pushes the next waste disposal dates to homeassistant.

source for link in `run.sh`: https://service.stuttgart.de/lhs-services/aws/abfallkalender


### homeassistant config

```
template:
  - trigger:
	  - platform: webhook
		webhook_id: !secret waste-disposal
		allowed_methods:
		  - POST
		local_only: true
	unique_id: "waste"
	sensor:
	  - name: "waste: residual"
		state: "{{ trigger.json.waste_residual }}"
		device_class: date
		unique_id: "waste_residual"
	  - name: "waste: paper"
		state: "{{ trigger.json.waste_paper }}"
		device_class: date
		unique_id: "waste_paper"
	  - name: "waste: yellow bag"
		state: "{{ trigger.json.waste_yellow_bag }}"
		device_class: date
		unique_id: "waste_yellow_bag"
```
