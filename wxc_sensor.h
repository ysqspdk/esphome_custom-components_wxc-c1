#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/esp32_ble_tracker/esp32_ble_tracker.h"
#include <Arduino.h>
// #include <ctime>

#ifdef USE_ESP32

namespace esphome {
namespace wxc_sensor {

class c1 : public Component, public esp32_ble_tracker::ESPBTDeviceListener {
 public:
  void set_address(uint64_t address) { address_ = address; };

  bool parse_device(const esp32_ble_tracker::ESPBTDevice &device) override;
  void dump_config() override;
  float get_setup_priority() const override { return setup_priority::DATA; }  
  void set_battery(sensor::Sensor *battery) { battery_=battery; }
  void set_temperature(sensor::Sensor *temperature) { temperature_=temperature; }
  void set_humidity(sensor::Sensor *humidity) { humidity_=humidity; }
  void set_lux(sensor::Sensor *lux) { lux_=lux; }
  void set_sensor_amount(sensor::Sensor *sensor_amount) { sensor_amount_=sensor_amount; }
  void set_hall_state(sensor::Sensor *hall_state) { hall_state_=hall_state; }

 protected:
  uint64_t address_;
  sensor::Sensor *battery_{nullptr};
  sensor::Sensor *temperature_{nullptr};
  sensor::Sensor *humidity_{nullptr};
  sensor::Sensor *lux_{nullptr};
  sensor::Sensor *sensor_amount_{nullptr};
  sensor::Sensor *hall_state_{nullptr};
  // std::time_t last_handle = 0;
};

}  // namespace wxc_sensor
}  // namespace esphome

#endif
