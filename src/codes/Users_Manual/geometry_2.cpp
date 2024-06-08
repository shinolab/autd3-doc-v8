//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
using autd3::pi;
using autd3::rad;
autd3::ControllerBuilder(
    {autd3::AUTD3(autd3::Vector3::Zero()),
     autd3::AUTD3(autd3::Vector3(autd3::AUTD3::DEVICE_WIDTH, 0, 0))
         .with_rotation(autd3::EulerAngles::ZYZ(0 * rad, pi / 2 * rad,
                                                0 * rad))})
    //~;
    //~return 0; }