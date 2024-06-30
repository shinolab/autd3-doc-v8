# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
let m = autd3::modulation::Sine::new(150 * Hz)
            .with_intensity(0xFF)
            .with_offset(0xFF / 2);
# }