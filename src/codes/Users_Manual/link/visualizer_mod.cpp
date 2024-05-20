//~#include<autd3.hpp>
#include "autd3/link/visualizer.hpp"

//~int main() {
auto autd = autd3::ControllerBuilder()
                .add_device(autd3::AUTD3(autd3::Vector3::Zero()))
                .open(autd3::link::Visualizer::builder());

autd3::modulation::Sine m(150 * autd3::Hz);
autd.send(m);

autd3::link::PlotConfig config;
config.fname = "mod.png";
autd.link().plot_modulation(config, autd3::Segment::S0);
//~return 0; }