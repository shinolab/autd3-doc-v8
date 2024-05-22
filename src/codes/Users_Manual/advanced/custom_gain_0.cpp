//~#include "autd3.hpp"
//~#include <unordered_map>
//~#include <limits>
class FocalPoint final : public autd3::Gain<FocalPoint> {
 public:
  explicit FocalPoint(autd3::Vector3 point) : _point(std::move(point)) {}

  std::unordered_map<size_t, std::vector<autd3::Drive>> calc(
      const autd3::Geometry& geometry) const override {
    return transform(geometry, [&](const auto& dev) {
      return [&](const auto& tr) {
        const auto phase = (tr.position() - _point).norm() * dev.wavelength();
        return autd3::Drive{autd3::Phase(phase * autd3::rad),
                            std::numeric_limits<autd3::EmitIntensity>::max()};
      };
    });
  }

 private:
  autd3::Vector3 _point;
};
//~int main() { return 0; }