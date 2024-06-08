//~#include<autd3.hpp>
//~int main() {
const auto m =
    autd3::modulation::Sine(150 * autd3::Hz)
        .with_transform([](const size_t idx, const uint8_t d) -> uint8_t {
          return static_cast<uint8_t>(d / 2);
        });
//~return 0; }