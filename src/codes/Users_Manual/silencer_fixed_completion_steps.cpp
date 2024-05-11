#include "autd3.hpp"

const auto steps_intensity = 10;
const auto steps_phase = 10;
const auto config =
    autd3::Silencer::fixed_completion_steps(steps_intensity, steps_phase);