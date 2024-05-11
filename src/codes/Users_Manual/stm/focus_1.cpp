#include "autd3.hpp"

auto stm = autd3::FocusSTM::from_sampling_config(
    autd3::SamplingConfig::from_frequency(1 * autd3::Hz));