# extern crate autd3;
# extern crate tokio;
# extern crate autd3_link_visualizer;
# use autd3::prelude::*;
# use autd3_link_visualizer::{Visualizer, PlotConfig, PythonBackend};
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::builder([AUTD3::new(Vector3::zeros())])
#     .open(
Visualizer::builder().with_backend::<PythonBackend>()
# ).await?;
# autd.close().await?;
# Ok(())
# }