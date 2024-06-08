//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())}).open(autd3::link::Nop::builder());
const auto tr = autd.geometry()[0][0];
const auto idx = tr.idx();
const auto position = tr.position();
//~return 0; }