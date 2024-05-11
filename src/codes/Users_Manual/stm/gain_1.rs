# extern crate autd3;
# use autd3::prelude::*;
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let stm = GainSTM::from_sampling_config(SamplingConfig::Freq(1 * Hz));
# let stm = stm.add_gain(Null::new());
# Ok(())
# }