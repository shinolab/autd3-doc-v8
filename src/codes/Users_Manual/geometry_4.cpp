//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder().add_device(autd3::AUTD3(autd3::Vector3::Zero())).open(autd3::link::Nop::builder());
//~{
auto dev = autd.geometry()[0];
//~}
//~{
for (auto& dev : autd.geometry()) {
  // do something
}
//~}
//~return 0; }