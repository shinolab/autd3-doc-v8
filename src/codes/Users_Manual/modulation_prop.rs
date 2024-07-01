# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let m = autd3::modulation::Sine::new(150 * Hz);
let fs = m.sampling_config().freq(); // -> 4kHz
# Ok(())
# }