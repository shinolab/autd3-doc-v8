//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder().add_device(autd3::AUTD3(autd3::Vector3::Zero())).open(autd3::link::Nop::builder());
const auto m =
    autd3::modulation::Static::with_intensity(autd3::EmitIntensity(0xFF));
//~return 0; }