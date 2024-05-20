//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder().add_device(autd3::AUTD3(autd3::Vector3::Zero())).open(autd3::link::Nop::builder());
const auto num_dev = autd.geometry().num_devices();
const auto num_tr = autd.geometry().num_transducers();
const auto center = autd.geometry().center();
//~return 0; }