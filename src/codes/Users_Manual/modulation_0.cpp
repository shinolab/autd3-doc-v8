#include "autd3.hpp"

const auto m =
    autd3::modulation::Sine(150 * autd3::Hz)
        .WithReadsFPGAState(autd3::SamplingConfig::Freq(4000 * autd3::Hz));