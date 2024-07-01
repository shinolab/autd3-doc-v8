# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
# let s = 
SamplingConfig::FreqNearest(4000.0 * Hz)
# ;
// or
# let s = 
SamplingConfig::PeriodNearest(std::time::Duration::from_micros(250))
# ;
# }