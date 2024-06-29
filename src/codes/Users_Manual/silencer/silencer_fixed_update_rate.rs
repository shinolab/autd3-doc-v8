# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let update_rate_intensity = 256;
let update_rate_phase = 256;
let config = Silencer::from_update_rate(update_rate_intensity, update_rate_phase);
# Ok(())
# }