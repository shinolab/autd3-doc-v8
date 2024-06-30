//~#include<autd3.hpp>
//~#include <limits>
//~int main() {
//~const auto nx = 0.0;
//~const auto ny = 0.0;
//~const auto nz = 1.0;
auto g = autd3::gain::Plane(autd3::Vector3(nx, ny, nz))
             .with_intensity(0xFF)
             .with_phase_offset(0x00);
//~return 0; }