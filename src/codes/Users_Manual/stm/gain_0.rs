# extern crate autd3;
# extern crate tokio;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::builder().open(autd3::link::Nop::builder()).await?;
let center = autd.geometry.center() + Vector3::new(0., 0., 150.0 * mm);
let point_num = 200;
let radius = 30.0 * mm;
let stm = GainSTM::from_freq(1.0 * Hz).add_gains_from_iter((0..point_num).map(|i| {
    let theta = 2.0 * PI * i as f64 / point_num as f64;
    let p = radius * Vector3::new(theta.cos(), theta.sin(), 0.0);
    Focus::new(center + p)
}));
# Ok(())
# }