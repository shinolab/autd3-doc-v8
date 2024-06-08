# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
Controller::builder([AUTD3::new(Vector3::zeros())]).with_ultrasound_freq(41 * kHz)
# .open(autd3::link::Nop::builder());
# }