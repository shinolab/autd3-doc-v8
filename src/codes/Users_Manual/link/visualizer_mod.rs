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

let m = Sine::new(150.);
autd.send(m).await?;

autd.link.plot_modulation(
    PlotConfig {
        fname: Path::new("mod.png").into(),
        ..PlotConfig::default()
    },
)?;
# autd.close().await?;
# Ok(())
# }
