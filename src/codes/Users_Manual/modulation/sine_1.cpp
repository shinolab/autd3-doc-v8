//~#include<autd3.hpp>
//~int main() {
const auto m = autd3::modulation::Sine(150 * autd3::Hz)
                   .with_intensity(autd3::EmitIntensity(0xFF))
                   .with_offset(autd3::EmitIntensity(0xFF) / 2);
//~return 0; }