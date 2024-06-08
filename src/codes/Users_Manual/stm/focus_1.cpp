//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())}).open(autd3::link::Nop::builder());
//~std::vector<std::array<autd3::Vector3, 1>> foci = {
//~    std::array{autd3::Vector3(0, 0, 0)},
//~    std::array{autd3::Vector3(0, 0, 0)},
//~};
auto stm = autd3::FociSTM<1>::from_sampling_config(
    autd3::SamplingConfig::Freq(1 * autd3::Hz), foci);
//~return 0; }