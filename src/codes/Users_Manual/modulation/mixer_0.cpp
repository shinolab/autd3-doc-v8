//~#include<autd3.hpp>
#include <autd3/modulation/mixer.hpp>

//~int main() {
const auto m =
    autd3::modulation::Mixer({autd3::modulation::Sine(100 * autd3::Hz),
                                autd3::modulation::Sine(150 * autd3::Hz)});

//~return 0; }