//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())}).open(autd3::link::Nop::builder());
autd.send(autd3::SwapSegment::Modulation(autd3::Segment::S1,
                                         autd3::TransitionMode::Immediate));
//~return 0; }