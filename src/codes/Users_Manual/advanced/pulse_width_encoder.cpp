//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~#include<vector>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder().add_device(autd3::AUTD3(autd3::Vector3::Zero())).open(autd3::link::Nop::builder());
std::vector<uint16_t> table(65536);
autd.send(autd3::PulseWidthEncoder(table));
//~return 0; }