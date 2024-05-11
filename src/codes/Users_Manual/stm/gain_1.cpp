#include "autd3.hpp"

auto stm = autd3::GainSTM::from_sampling_config(
    autd3::SamplingConfig::freq(1 * autd3::Hz));