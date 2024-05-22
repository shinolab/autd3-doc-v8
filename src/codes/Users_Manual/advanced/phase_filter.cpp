//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder().add_device(autd3::AUTD3(autd3::Vector3::Zero())).open(autd3::link::Nop::builder());
autd.send(autd3::PhaseFilter::additive([](const auto& dev) {
  return [](const auto& tr) { return autd3::Phase(0); };
}));
//~return 0; }