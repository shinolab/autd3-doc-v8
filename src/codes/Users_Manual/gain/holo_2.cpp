//~#include<autd3.hpp>
#include "autd3/gain/holo.hpp"

//~int main() {
const auto backend = std::make_shared<autd3::gain::holo::NalgebraBackend>();
auto g = autd3::gain::holo::GSPAT(backend).with_repeat(100);
//~return 0; }