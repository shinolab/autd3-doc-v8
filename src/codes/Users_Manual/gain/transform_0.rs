# extern crate autd3;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
let g = Uniform::new(EmitIntensity::MAX).with_transform(|_dev| |_tr, d| Drive::new(
    Phase::from((d.phase().radian() + PI) * rad),
    d.intensity() / 2,
));
# }