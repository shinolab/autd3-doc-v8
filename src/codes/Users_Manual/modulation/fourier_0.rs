# extern crate autd3;
# use autd3::prelude::*;
# use autd3::modulation::Fourier;
# #[allow(unused_variables)]
# fn main()  {
let m = Fourier::from(Sine::new(100 * Hz))
        .add_component(Sine::new(150 * Hz))
        .add_components_from_iter([Sine::new(200 * Hz)]);
# }