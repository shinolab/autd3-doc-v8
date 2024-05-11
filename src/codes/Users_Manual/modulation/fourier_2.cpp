#include "autd3.hpp"

const auto m = autd3::modulation::Sine(100.0 * autd3::Hz) +
               autd3::modulation::Sine(150.0 * autd3::Hz)
                   .with_phase(autd3::pi / 2.0 * autd3::rad);