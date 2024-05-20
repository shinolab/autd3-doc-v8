//~#include<autd3.hpp>
//~int main() {
const auto m = autd3::modulation::Sine(100 * autd3::Hz) +
               autd3::modulation::Sine(150 * autd3::Hz) +
               autd3::modulation::Sine(200 * autd3::Hz);
//~return 0; }