#include "autd3.hpp"

const auto m =
    autd3::modulation::Square(150.0 * autd3::Hz).with_low(0x00).with_high(0xFF);