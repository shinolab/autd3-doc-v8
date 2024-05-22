//~#include<autd3.hpp>
//~int main() {
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
//~const auto nx = 0.0;
//~const auto ny = 0.0;
//~const auto nz = 1.0;
//~const auto theta = 0.0;
const auto g = autd3::gain::Bessel(
    autd3::Vector3(x, y, z), autd3::Vector3(nx, ny, nz), theta * autd3::rad);
//~return 0; }