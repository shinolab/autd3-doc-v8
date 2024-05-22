//~#include<autd3.hpp>
//~#include <limits>
//~int main() {
//~const auto nx = 0.0;
//~const auto ny = 0.0;
//~const auto nz = 1.0;
auto g = autd3::gain::Plane(autd3::Vector3(nx, ny, nz))
             .with_intensity(std::numeric_limits<autd3::EmitIntensity>::max())
             .with_phase_offset(autd3::Phase(0x00));
//~return 0; }