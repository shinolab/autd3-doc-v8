# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
let steps_intensity = 10;
let steps_phase = 10;
let config = Silencer::from_completion_steps(steps_intensity, steps_phase);
// or
let time_intensity = std::time::Duration::from_micros(250);
let time_phase = std::time::Duration::from_micros(250);
let config = Silencer::from_completion_time(time_intensity, time_phase);
# }