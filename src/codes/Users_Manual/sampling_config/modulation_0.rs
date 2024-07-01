# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
let m = autd3::modulation::Sine::new(150 * Hz)
            .with_sampling_config(4000 * Hz);
// or
let m = autd3::modulation::Sine::new(150 * Hz)
            .with_sampling_config(std::time::Duration::from_micros(250));
# }