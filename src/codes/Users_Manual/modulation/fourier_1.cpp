#include "autd3.hpp"

const auto m = autd3::modulation::Sine(100.0 * Hz) +
               autd3::modulation::Sine(150.0 * Hz) +
               autd3::modulation::Sine(200.0 * Hz);
