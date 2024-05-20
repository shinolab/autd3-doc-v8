//~#include<autd3.hpp>
#include "autd3/modulation/audio_file.hpp"

//~int main() {
const auto path = "path/to/foo.wav";
const auto m = autd3::modulation::audio_file::Wav(path);
//~return 0; }