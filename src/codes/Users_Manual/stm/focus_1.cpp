//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder().add_device(autd3::AUTD3(autd3::Vector3::Zero())).open(autd3::link::Nop::builder());
auto stm = autd3::FocusSTM::from_sampling_config(
    autd3::SamplingConfig::Freq(1 * autd3::Hz));
//~return 0; }