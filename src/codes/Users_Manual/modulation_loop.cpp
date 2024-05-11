#include "autd3.hpp"

const auto m = autd3::modulation::Sine(150).with_loop_behavior(
    autd3::LoopBehavior::infinite());  // infinite loop
const auto m = autd3::modulation::Sine(150).with_loop_behavior(
    autd3::LoopBehavior::finite(10));  // 10 times loop
const auto m = autd3::modulation::Sine(150).with_loop_behavior(
    autd3::LoopBehavior::once());  // equivalent to finite(1)