# extern crate autd3;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
# let s = 
SamplingConfig::FreqNearest(4000.0 * Hz)
# ;
// or
# let s = 
SamplingConfig::DivisionRaw(5120)
# ;
# Ok(())
# }