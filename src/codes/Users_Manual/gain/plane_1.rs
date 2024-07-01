# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
# let x = 0.;
# let y = 0.;
# let z = 0.;
# let nx = 0.;
# let ny = 0.;
# let nz = 0.;
# let theta = 0.;
let g = Plane::new(Vector3::new(nx, ny, nz))
            .with_intensity(0xFF)
            .with_phase_offset(0x00);
# }