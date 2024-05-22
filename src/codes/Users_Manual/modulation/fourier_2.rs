# extern crate autd3;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main()  {
let m = Sine::new(100 * Hz) + Sine::new(150 * Hz).with_phase(PI / 2.0 * rad);
# }