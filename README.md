# esphome_custom-components_wxc-c1
## esphome自制组件 接入王小菜开源的门窗传感器
### 示例
```
sensor:
  - platform: wxc_sensor
    mac_address: "A4:C1:38:46:FD:6C"
    id: wxc_c1_001
    battery:
      name: "WXC_C1_001_battery"
    temperature:
      name: "WXC_C1_001_temperature"
    humidity:
      name: "WXC_C1_001_humidity"
    lux:
      name: "WXC_C1_001_lux"
    # sensor_amount:
    #   name: "WXC_C1_001_sensor_amount"
    hall_state:
      name: "WXC_C1_001_hall_state"
      internal: true
      on_value:
        then:
          - binary_sensor.template.publish:
              id: door_001
              state: !lambda 'return x;'

binary_sensor:
  - platform: template
    device_class: door
    icon: mdi:door
    id: door_001
    name: "WXC_C1_001_Door_State"

```
