#include "autd3/link/visualizer.hpp"

auto autd = autd3::Controller::builder()
                .add_device(autd3::AUTD3(autd3::Vector3::Zero()))
                .open_with(autd3::link::Visualizer::builder());

autd3::Vector3 center = autd.geometry().center() + autd3::Vector3(0, 0, 150);
autd3::gain::Focus g(center);
autd.send(g);

autd3::link::PlotConfig config;
config.fname = "phase.png";
autd.link<autd3::link::Visualizer>().plot_phase(config, autd.geometry());
