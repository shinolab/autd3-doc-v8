//~#include<autd3.hpp>
//~int main() {
const auto m = autd3::modulation::Sine(150 * autd3::Hz)
                   .with_intensity(0xFF)
                   .with_offset(0xFF / 2);
//~return 0; }