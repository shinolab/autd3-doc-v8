//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
auto stm = autd3::GainSTM::from_sampling_config(
    autd3::SamplingConfig::Freq(1 * autd3::Hz));
//~return 0; }