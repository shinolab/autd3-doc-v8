//~#include<autd3.hpp>
//~int main() {
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
const auto g =
    autd3::gain::Focus(autd3::Vector3(x, y, z))
        .with_intensity(std::numeric_limits<autd3::EmitIntensity>::max())
        .with_phase_offset(autd3::Phase(0x00));
//~return 0; }