# extern crate autd3;
# extern crate tokio;
# use autd3::prelude::*;
# 
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let mut autd = Controller::builder([AUTD3::new(Vector3::zeros())])
#    .open(autd3::link::Nop::builder()).await?;
let mut dev = &mut autd.geometry[0];
let idx = dev.idx();
dev.enable = false;
dev.sound_speed = 340e3;
dev.set_sound_speed_from_temp(15.);
let t = Vector3::new(1., 0., 0.);
let r = UnitQuaternion::from_quaternion(Quaternion::new(1., 0., 0., 0.));
dev.translate(t);
dev.rotate(r);
dev.affine(t, r);
let wavelength = dev.wavelength();
let wavenumber = dev.wavenumber();
let rotation = dev.rotation();
let x_dir = dev.x_direction();
let y_dir = dev.y_direction();
let axial_dir = dev.axial_direction();
# Ok(())
# }