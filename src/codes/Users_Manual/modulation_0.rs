# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let m = autd3::modulation::Sine::new(150 * Hz)
            .with_sampling_config(SamplingConfig::Freq(4000 * Hz));
# Ok(())
# }