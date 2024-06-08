//~#include<chrono>
//~#include<autd3.hpp>
//~#include "autd3/link/soem.hpp"
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())}).open(
autd3::link::SOEM::builder().with_timeout(std::chrono::milliseconds(20))
    //~);
    //~return 0; }