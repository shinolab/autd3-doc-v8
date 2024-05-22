//~#include "autd3.hpp"
//~#include <vector>
//~#include <limits>
class BurstModulation final : public autd3::Modulation<BurstModulation> {
 public:
  std::vector<autd3::EmitIntensity> calc(
      const autd3::Geometry&) const override {
    std::vector buffer(_buf_size,
                       std::numeric_limits<autd3::EmitIntensity>::min());
    buffer[_buf_size - 1] = std::numeric_limits<autd3::EmitIntensity>::max();
    return buffer;
  }

  explicit BurstModulation(const size_t buf_size = 4000) noexcept
      : Modulation(autd3::SamplingConfig::Freq(4000 * autd3::Hz)),
        _buf_size(buf_size) {}

 private:
  size_t _buf_size;
};
//~int main() { return 0; }