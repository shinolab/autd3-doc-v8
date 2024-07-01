# use autd3::prelude::*;
# use autd3_gain_holo::{EmissionConstraint, NalgebraBackend, Pa, GSPAT};
# #[allow(unused_variables)]
# fn main() {
#     let x1 = 0.;
#     let y1 = 0.;
#     let z1 = 0.;
#     let x2 = 0.;
#     let y2 = 0.;
#     let z2 = 0.;
#     let foci = [
#         (Vector3::new(x1, y1, z1), 5e3 * Pa),
#         (Vector3::new(x2, y2, z2), 5e3 * Pa),
#     ];
let backend = std::sync::Arc::new(NalgebraBackend::default());
let g =
    GSPAT::new(backend, foci).with_constraint(EmissionConstraint::Uniform(EmitIntensity::MAX));
# }