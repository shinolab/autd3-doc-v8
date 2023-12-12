# extern crate autd3;
# extern crate tokio;
# extern crate autd3_link_visualizer;
# use autd3::prelude::*;
use autd3_link_visualizer::{Visualizer, PlotConfig};

use std::path::Path;

# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
let mut autd = Controller::builder()
    .add_device(AUTD3::new(Vector3::zeros()))
    .open_with(Visualizer::builder()).await?;

let center = autd.geometry.center() + Vector3::new(0., 0., 150.0 * MILLIMETER);
let g = Focus::new(center);
autd.send(g).await?;

autd.link.plot_phase(
    PlotConfig {
        fname: Path::new("phase.png").into(),
        ..PlotConfig::default()
    },
    &autd.geometry,
)?;
# autd.close().await?;
# Ok(())
# }
