# extern crate autd3;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let stm = GainSTM::from_freq(1.0 * Hz, [Null::new(), Null::new()])?
    .with_mode(GainSTMMode::PhaseFull);
# Ok(())
# }