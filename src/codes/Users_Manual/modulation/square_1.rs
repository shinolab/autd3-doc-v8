# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
let m = autd3::modulation::Square::new(150 * Hz)
            .with_low(u8::MIN)
            .with_high(u8::MAX);
# }