//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder().add_device(autd3::AUTD3(autd3::Vector3::Zero())).open(autd3::link::Nop::builder());
auto dev = autd.geometry()[0];
const auto idx = dev.idx();
const auto enable = dev.enable();
dev.set_enable(false);
const auto sound_speed = dev.sound_speed();
dev.set_sound_speed(340e3);
dev.set_sound_speed_from_temp(15.);
const auto attenuation = dev.attenuation();
dev.set_attenuation(0);
const auto t = autd3::Vector3(1., 0., 0.);
const auto r = autd3::Quaternion(1., 0., 0., 0.);
dev.translate(t);
dev.rotate(r);
dev.affine(t, r);
const auto wavelength = dev.wavelength();
const auto wavenumber = dev.wavenumber();
//~return 0; }