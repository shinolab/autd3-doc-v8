//~#include<autd3.hpp>
#include "autd3/modulation/audio_file.hpp"

//~int main() {
const auto path = "path/to/foo.fat";
const auto m = autd3::modulation::audio_file::RawPCM(path, 4000 * autd3::Hz);
//~return 0; }