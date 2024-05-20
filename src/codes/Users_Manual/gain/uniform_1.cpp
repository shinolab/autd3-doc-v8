//~#include<autd3.hpp>
//~#include <limits>
//~int main() {
const auto g =
    autd3::gain::Uniform(std::numeric_limits<autd3::EmitIntensity>::max())
        .with_phase(autd3::Phase(0));
//~return 0; }