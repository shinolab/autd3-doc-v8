# use autd3::prelude::*;
# use autd3_link_visualizer::*;
# use std::path::Path;
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
let mut autd = Controller::builder([AUTD3::new(Vector3::zeros())])
    .open(Visualizer::builder()).await?;

let center = autd.geometry.center() + Vector3::new(0., 0., 150.0 * mm);

autd.send(Focus::new(center)).await?;

autd.link.plot_field(
    PlotConfig {
        fname: Path::new("xy.png").into(),
        ..PlotConfig::default()
    },
    PlotRange{ 
        x_range: center.x - 20.0..center.x + 20.0,
        y_range: center.y - 30.0..center.y + 30.0,
        z_range: center.z..center.z,
        resolution: 1.
    },
    &autd.geometry,
    Segment::S0,
    0
)?;
# autd.close().await?;
# Ok(())
# }
