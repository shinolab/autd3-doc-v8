# use autd3::prelude::*;
use autd3_modulation_audio_file::Csv;

# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let path = "path/to/foo.csv";
let m = Csv::new(&path, 4000 * Hz);
# Ok(())
# }