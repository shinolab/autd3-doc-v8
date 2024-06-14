//~#include <ranges>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~using namespace std::ranges::views;
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder({autd3::AUTD3(autd3::Vector3::Zero())}).open(autd3::link::Nop::builder());
const autd3::Vector3 center =
    autd.geometry().center() + autd3::Vector3(0, 0, 150);
const auto points_num = 200;
const auto radius = 30.0f;
auto stm = autd3::FociSTM<2>::from_freq(
    1.0f * autd3::Hz,
    iota(0) | take(points_num) | transform([&](auto i) {
      const auto theta = 2.0f * autd3::pi * static_cast<float>(i) /
                         static_cast<float>(points_num);
      autd3::Vector3 p = center + autd3::Vector3(radius * std::cos(theta),
                                                 radius * std::sin(theta), 0);
      return autd3::ControlPoints<2>(
                 std::array{autd3::ControlPoint(center + p).with_offset(0x00),
                            autd3::ControlPoint(center - p).with_offset(0x00)})
          .with_intensity(0xFF);
    }));
//~return 0; }