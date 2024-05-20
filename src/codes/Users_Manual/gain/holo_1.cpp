//~#include<autd3.hpp>
//~#include <limits>
//~#include "autd3/gain/holo.hpp"
//~int main() {
const auto backend = std::make_shared<autd3::gain::holo::NalgebraBackend>();
auto g = autd3::gain::holo::GSPAT(backend).with_constraint(
    autd3::gain::holo::EmissionConstraint::Uniform(
        std::numeric_limits<autd3::EmitIntensity>::max()));
//~return 0; }