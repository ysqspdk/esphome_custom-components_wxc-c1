#include "wxc_sensor.h"
#include "esphome/core/log.h"

#ifdef USE_ESP32
#define CHECK_INTERVAL 200

namespace esphome {
namespace wxc_sensor {

static const char *const TAG = "wxc_sensor";
static unsigned long lastMs = 0;

void c1::dump_config() {
  ESP_LOGCONFIG(TAG, "wxc sensor");
  LOG_SENSOR("  ", "battery", this->battery_);
  LOG_SENSOR("  ", "temperature", this->temperature_);
  LOG_SENSOR("  ", "humidity", this->humidity_);
  LOG_SENSOR("  ", "lux", this->lux_);
  LOG_SENSOR("  ", "sensor_amount", this->sensor_amount_);
  LOG_SENSOR("  ", "hall_state", this->hall_state_);
}

bool c1::parse_device(const esp32_ble_tracker::ESPBTDevice &device)
{
  if (millis() - lastMs >= CHECK_INTERVAL)
  {
    lastMs = millis();
    // std::time_t curr = std::time(nullptr);
    // if (curr <= last_handle) {
    //   return false;
    // }
    // last_handle = curr;
    if (device.address_uint64() != this->address_)
    {
      ESP_LOGVV(TAG, "parse_device(): unknown MAC address.");
      return false;
    }
    ESP_LOGVV(TAG, "parse_device(): MAC address %s found.", device.address_str().c_str());

    bool success = false;
    for (auto &service_data : device.get_service_datas())
    {
      auto raw = service_data.data;
      if (this->battery_ != nullptr)
        this->battery_->publish_state(raw[1]);
      if (this->temperature_ != nullptr)
        this->temperature_->publish_state(((float)(raw[3] << 8 | raw[2])) / 100);
      if (this->humidity_ != nullptr)
        this->humidity_->publish_state(((float)(raw[5] << 8 | raw[4])) / 100);
      if (this->lux_ != nullptr)
        this->lux_->publish_state(((float)(raw[7] << 8 | raw[6])));
      if (this->sensor_amount_ != nullptr)
        this->sensor_amount_->publish_state(raw[8]);
      if (this->hall_state_ != nullptr)
        this->hall_state_->publish_state(raw[9]);
    }
    return true;
  }
}
} // namespace wxc_sensor
}  // namespace esphome

#endif
