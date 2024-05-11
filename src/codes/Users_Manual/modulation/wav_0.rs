# extern crate autd3_modulation_audio_file;
# extern crate autd3;
# use autd3::prelude::*;
use autd3_modulation_audio_file::Wav;

# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let path = "path/to/foo.wav";
let m = Wav::new(&path);
# Ok(())
# }