//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
const auto m = autd3::modulation::Sine(150 * autd3::Hz);
const auto fs = m.sampling_config().freq();  // -> 4kHz
                                             //~return 0; }