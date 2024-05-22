//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder().add_device(autd3::AUTD3(autd3::Vector3::Zero())).open(autd3::link::Nop::builder());
autd.send(autd3::SwapSegment::modulation(autd3::Segment::S1,
                                         autd3::TransitionMode::Immediate));
//~return 0; }