//~#include <ranges>
//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~using namespace std::ranges::views;
//~int main() {
//~auto autd =
//~autd3::ControllerBuilder().add_device(autd3::AUTD3(autd3::Vector3::Zero())).open(autd3::link::Nop::builder());
const autd3::Vector3 center =
    autd.geometry().center() + autd3::Vector3(0, 0, 150);
const auto points_num = 200;
const auto radius = 30.0;
auto stm =
    autd3::FocusSTM::from_freq(1.0 * autd3::Hz)
        .add_foci_from_iter(
            iota(0) | take(points_num) | transform([&](auto i) {
              const auto theta = 2.0 * autd3::pi * static_cast<double>(i) /
                                 static_cast<double>(points_num);
              autd3::Vector3 p =
                  center +
                  radius * autd3::Vector3(std::cos(theta), std::sin(theta), 0);
              return p;
            }));
//~return 0; }