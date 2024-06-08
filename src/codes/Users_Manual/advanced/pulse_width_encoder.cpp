//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~#include<vector>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())}).open(autd3::link::Nop::builder());
autd.send(autd3::PulseWidthEncoder([](const auto& dev) {
  return [](const auto i) { return 0; };
}));
//~return 0; }