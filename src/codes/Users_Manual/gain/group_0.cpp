//~#include<optional>
//~#include<autd3.hpp>
//~int main() {
//~const auto x = 0.0;
//~const auto y = 0.0;
//~const auto z = 0.0;
const auto g =
    autd3::gain::Group(
        [](const auto& dev, const auto& tr) -> std::optional<const char*> {
          if (tr.idx() <= 100) return "null";
          return "focus";
        })
        .set("null", autd3::gain::Null())
        .set("focus", autd3::gain::Focus(autd3::Vector3(x, y, z)));
//~return 0; }