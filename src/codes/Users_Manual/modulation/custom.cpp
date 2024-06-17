//~#include<autd3.hpp>
//~#include<vector>
//~int main() {
const std::vector buf = {0xFF, 0x00};
const auto m = autd3::modulation::Custom(buf, 4000 * autd3::Hz);
//~return 0; }