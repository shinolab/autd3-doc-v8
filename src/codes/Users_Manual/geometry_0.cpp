//~#include<chrono>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
autd3::ControllerBuilder(
    {autd3::AUTD3(autd3::Vector3::Zero()),
     autd3::AUTD3(autd3::Vector3(autd3::AUTD3::DEVICE_WIDTH, 0, 0))})
    //~;
    //~return 0; }