# extern crate autd3;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let stm =
    GainSTM::from_sampling_config(SamplingConfig::Freq(1 * Hz), [Null::new(), Null::new()]);
# Ok(())
# }