//~#include<autd3.hpp>
//~int main() {
const auto g = autd3::gain::Custom([](const auto& dev) {
  return [](const auto& tr) {
    return autd3::Drive(autd3::Phase(0x00), autd3::EmitIntensity(0x00));
  };
});
//~return 0; }