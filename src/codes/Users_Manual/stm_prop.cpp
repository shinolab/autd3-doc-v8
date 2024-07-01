//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())}).open(autd3::link::Nop::builder());
std::vector<std::array<autd3::Vector3, 1>> foci = {
    std::array{autd3::Vector3(0, 0, 0)},
    std::array{autd3::Vector3(0, 0, 0)},
};
const auto stm = autd3::FociSTM<1>::from_freq(1.0f * autd3::Hz, foci);
const auto f = stm.freq();                     // -> 1Hz
const auto p = stm.period();                   // -> 1s
const auto fs = stm.sampling_config().freq();  // -> 2Hz
                                               //~return 0; }