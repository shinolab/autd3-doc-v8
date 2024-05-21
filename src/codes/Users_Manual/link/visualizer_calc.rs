# extern crate autd3;
# extern crate tokio;
# extern crate autd3_link_visualizer;
# use autd3::prelude::*;
# use autd3_link_visualizer::Visualizer;
# use std::path::Path;
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
let mut autd = Controller::builder()
    .add_device(AUTD3::new(Vector3::zeros()))
    .open(Visualizer::builder()).await?;

let center = autd.geometry.center() + Vector3::new(0., 0., 150.0 * mm);

autd.send(Focus::new(center)).await?;

let p = autd.link.calc_field(&[center], &autd.geometry, Segment::S0, 0)?;
println!(
    "Acoustic pressure at ({}, {}, {}) = {}",
    center.x, center.y, center.z, p[0]
);

# autd.close().await?;
# Ok(())
# }
