//~#include<autd3.hpp>
//~#include "autd3/link/simulator.hpp"
//~int main() {
//~auto autd = autd3::ControllerBuilder()
//~                .add_device(autd3::AUTD3(autd3::Vector3::Zero()))
//~                .open(autd3::link::Simulator::builder(8080));
autd.link().update_geometry(autd.geometry());
//~return 0; }