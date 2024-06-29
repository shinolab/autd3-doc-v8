# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let steps_intensity = 10;
let steps_phase = 10;
let config = Silencer::from_completion_steps(steps_intensity, steps_phase);
# Ok(())
# }