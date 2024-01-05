#include "autd3.hpp"

const auto update_rate_intensity = 256;
const auto update_rate_phase = 256;
const auto config = autd3::ConfigureSilencer::fixed_update_rate(
    update_rate_intensity, update_rate_phase);