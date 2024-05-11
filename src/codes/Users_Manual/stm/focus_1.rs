# extern crate autd3;
# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let stm = FocusSTM::from_sampling_config(SamplingConfig::Freq(1 * Hz));
# Ok(())
# }