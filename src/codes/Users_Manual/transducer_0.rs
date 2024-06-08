# use autd3::prelude::*;
# 
# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::builder([AUTD3::new(Vector3::zeros())])
#    .open(autd3::link::Nop::builder()).await?;
let tr = &autd.geometry[0][0];
let idx = tr.idx();
let position = tr.position();
# Ok(())
# }