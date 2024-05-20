//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder().add_device(autd3::AUTD3(autd3::Vector3::Zero())).open(autd3::link::Nop::builder());
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
autd.group([](const autd3::Device& dev) -> std::optional<const char*> {
      if (dev.idx() == 0) {
        return "null";
      } else if (dev.idx() == 1) {
        return "focus";
      } else {
        return std::nullopt;
      }
    })
    .set("null", autd3::gain::Null())
    .set("focus", autd3::gain::Focus(autd3::Vector3(x, y, z)))
    .send();
//~return 0; }