#include "autd3/link/visualizer.hpp"

auto autd = autd3::Controller::builder()
                .add_device(autd3::AUTD3(autd3::Vector3::Zero()))
                .open_with(autd3::link::Visualizer::builder());

autd3::modulation::Sine m(150);
autd.send(m);

autd3::link::PlotConfig config;
config.fname = "mod.png";
autd.link<autd3::link::Visualizer>().plot_modulation(config);
