# extern crate autd3;
# extern crate tokio;
# extern crate autd3_link_visualizer;
# use autd3::prelude::*;
# use autd3_link_visualizer::{Visualizer, PlotConfig};

# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::builder()
#     .add_device(AUTD3::new(Vector3::zeros()))
#     .open_with(
Visualizer::builder().with_gpu(-1)
# ).await?;
# autd.close().await?;
# Ok(())
# }