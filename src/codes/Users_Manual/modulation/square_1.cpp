//~#include<autd3.hpp>
//~int main() {
const auto m = autd3::modulation::Square(150 * autd3::Hz)
                   .with_low(autd3::EmitIntensity(0x00))
                   .with_high(autd3::EmitIntensity(0xFF));
//~return 0; }