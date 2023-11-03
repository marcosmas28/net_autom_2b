


curl -s -X GET -H "Authorization: Token e246318564837e7c2f399037eacf1c1d79565446" https://demo.netbox.dev/api/dcim/devices/ | jq


curl -s -X GET -H "Authorization: Token e246318564837e7c2f399037eacf1c1d79565446" https://demo.netbox.dev/api/dcim/devices/246/ | jq




* pynetbox library

Device Bulk Creation

```
import pynetbox
nb = pynetbox.api(
    'http://ltrooctfeappr01:8000/',
    token='3cd0582c1b680c9a0a9be593bc99315ae15062de'
)
nb.dcim.devices.create([
    {"name":"radio004","device_role": 13, "device_type": 94, "site": 1340, "platform": 25, "custom_fields": {"base_station_name": "3209", "device_hostname": "radio004"}},
    {"name":"radio001","device_role": 13, "device_type": 94, "site": 1340, "platform": 25, "custom_fields": {"base_station_name": "3209", "device_hostname": "radio001"}},
    {"name":"radio002","device_role": 13, "device_type": 94, "site": 1340, "platform": 25, "custom_fields": {"base_station_name": "3209", "device_hostname": "radio002"}},
    {"name":"radio003","device_role": 13, "device_type": 94, "site": 1340, "platform": 25, "custom_fields": {"base_station_name": "3209", "device_hostname": "radio003"}}
])
```
