//~#include<autd3.hpp>
//~int main() {
const auto m =
    autd3::modulation::Sine(150 * autd3::Hz)
        .with_transform([](const size_t idx, const autd3::EmitIntensity d)
                            -> autd3::EmitIntensity { return d / 2; });
//~return 0; }