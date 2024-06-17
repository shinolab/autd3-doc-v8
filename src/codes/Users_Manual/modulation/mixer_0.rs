# use autd3::prelude::*;
# use autd3::modulation::Mixer;
# #[allow(unused_variables)]
# fn main() {
let m = Mixer::new([Sine::new(100 * Hz), Sine::new(150 * Hz)]);
# }