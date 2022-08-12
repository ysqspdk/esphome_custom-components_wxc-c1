import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, esp32_ble_tracker
from esphome.const import (
    CONF_MAC_ADDRESS,
    CONF_ID,
    CONF_BATTERY_LEVEL,
    CONF_TEMPERATURE,
    CONF_HUMIDITY,
    CONF_ILLUMINANCE,
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_ILLUMINANCE,
    ICON_PERCENT,
    ICON_THERMOMETER,
    ICON_WATER_PERCENT,
    STATE_CLASS_MEASUREMENT,
    UNIT_CELSIUS,
    UNIT_PERCENT,
    UNIT_LUX,
)

CONF_HUMIDITY = 'humidity'
CONF_TEMPERATURE = 'temperature'
CONF_BATTERY_LEVEL = 'battery'
CONF_ILLUMINANCE = 'lux'

DEPENDENCIES = ["esp32_ble_tracker"]

wxc_sensor_ns = cg.esphome_ns.namespace("wxc_sensor")
c1 = wxc_sensor_ns.class_(
    "c1", esp32_ble_tracker.ESPBTDeviceListener, cg.Component
)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(c1),
            cv.Required(CONF_MAC_ADDRESS): cv.mac_address,
            cv.Optional(CONF_BATTERY_LEVEL): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                icon=ICON_PERCENT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_THERMOMETER,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_HUMIDITY): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                icon=ICON_WATER_PERCENT,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_HUMIDITY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ILLUMINANCE): sensor.sensor_schema(
                unit_of_measurement=UNIT_LUX,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_ILLUMINANCE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional("sensor_amount"): sensor.sensor_schema(),
            cv.Optional("hall_state"): sensor.sensor_schema(),
        }
    )
    .extend(esp32_ble_tracker.ESP_BLE_DEVICE_SCHEMA)
    .extend(cv.COMPONENT_SCHEMA)
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await esp32_ble_tracker.register_ble_device(var, config)

    cg.add(var.set_address(config[CONF_MAC_ADDRESS].as_hex))

    if "battery" in config:
        sens = await sensor.new_sensor(config["battery"])
        cg.add(var.set_battery(sens))

    if "temperature" in config:
        sens = await sensor.new_sensor(config["temperature"])
        cg.add(var.set_temperature(sens))

    if "humidity" in config:
        sens = await sensor.new_sensor(config["humidity"])
        cg.add(var.set_humidity(sens))

    if "lux" in config:
        sens = await sensor.new_sensor(config["lux"])
        cg.add(var.set_lux(sens))

    if "sensor_amount" in config:
        sens = await sensor.new_sensor(config["sensor_amount"])
        cg.add(var.set_sensor_amount(sens))

    if "hall_state" in config:
        sens = await sensor.new_sensor(config["hall_state"])
        cg.add(var.set_hall_state(sens))
