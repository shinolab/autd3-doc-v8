//~#include<autd3.hpp>
#include "autd3/gain/holo.hpp"

using autd3::gain::holo::Pa;
//~int main() {
//~const auto x1 = 0.0;
//~const auto y1 = 0.0;
//~const auto z1 = 0.0;
//~const auto x2 = 0.0;
//~const auto y2 = 0.0;
//~const auto z2 = 0.0;
std::vector<std::pair<autd3::Vector3, autd3::gain::holo::Amplitude>> foci = {
    {autd3::Vector3(x1, y1, z1), 5e3 * autd3::gain::holo::Pa},
    {autd3::Vector3(x2, y2, z2), 5e3 * autd3::gain::holo::Pa},
};
const auto backend = std::make_shared<autd3::gain::holo::NalgebraBackend>();
auto g = autd3::gain::holo::GSPAT(backend, foci);
//~return 0; }