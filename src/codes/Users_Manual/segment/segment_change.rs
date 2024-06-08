# use autd3::prelude::*;
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::builder([AUTD3::new(Vector3::zeros())]).open(autd3::link::Nop::builder()).await?;
autd.send(SwapSegment::Gain(Segment::S1)).await?;
# Ok(())
# }