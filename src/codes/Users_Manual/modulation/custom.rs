# use autd3::prelude::*;
# use autd3::modulation::Custom;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let buf = vec![0xFF, 0x00];
let m = Custom::new(buf, 4000 * Hz);
# Ok(())
# }