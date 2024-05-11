#include "autd3.hpp"

auto m = autd3::modulation::Fourier(autd3::modulation::Sine(100.0 * autd3::Hz))
             .add_component(autd3::modulation::Sine(150.0 * autd3::Hz))
             .add_components_from_iter(
                 std::vector{autd3::modulation::Sine(200.0 * autd3::Hz)});
