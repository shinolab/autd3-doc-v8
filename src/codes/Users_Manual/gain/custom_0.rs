# use autd3::prelude::*;
use autd3::gain::Custom;

# #[allow(unused_variables)]
# fn main() {
let g = Custom::new(|_dev| |_tr| Drive::new(
    Phase::new(0x00),
    EmitIntensity::new(0x00),
));
# }