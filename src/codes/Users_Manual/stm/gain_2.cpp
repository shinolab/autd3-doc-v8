#include "autd3.hpp"

auto stm =
    autd3::GainSTM::from_freq(1.0 * autd3::Hz).with_mode(autd3::GainSTMMode::PhaseFull);