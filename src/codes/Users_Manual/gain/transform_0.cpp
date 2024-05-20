//~#include<autd3.hpp>
//~#include <limits>
//~int main() {
const auto g =
    autd3::gain::Uniform(std::numeric_limits<autd3::EmitIntensity>::max())
        .with_transform([](const auto& dev, const auto& tr, auto d) -> auto {
          d.intensity = d.intensity / 2;
          d.phase = autd3::Phase((d.phase.radian() + autd3::pi) * autd3::rad);
          return d;
        });
//~return 0; }