# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
# let x = 0.;
# let y = 0.;
# let z = 0.;
let g = Group::new(|_dev| |tr| match tr.idx() {
                0..=100 => Some("null"),
                101..=200 => Some("focus"),
                _ => None,
            })
            .set("null", Null::new())
            .set("focus", Focus::new(Vector3::new(x, y, z)));
# }