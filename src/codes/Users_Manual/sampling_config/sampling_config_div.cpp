//~#include<autd3.hpp>
//~int main() {
const auto m = autd3::modulation::Sine(150 * autd3::Hz)
                   .with_sampling_config(autd3::SamplingConfig::Division(5120));
//~return 0; }