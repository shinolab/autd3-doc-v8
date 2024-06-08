# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
let m = Sine::new(150 * Hz).with_transform(|_i, d| d / 2);
# }