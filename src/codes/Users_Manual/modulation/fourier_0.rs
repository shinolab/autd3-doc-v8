# use autd3::prelude::*;
use autd3::modulation::Fourier;

# #[allow(unused_variables)]
# fn main() {
let m = Fourier::new([Sine::new(100 * Hz), Sine::new(150 * Hz)]);
# }