//~#include<autd3.hpp>
#include <autd3/modulation/custom.hpp>

//~#include<vector>
//~int main() {
std::vector<uint8_t> buf = {0xFF, 0x00};
const auto m = autd3::modulation::Custom(std::move(buf), 4000 * autd3::Hz);
//~return 0; }