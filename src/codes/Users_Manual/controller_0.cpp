autd.send(autd3::ConfigureReadsFPGAState([](const auto&) { return true; }));

const auto info = autd.fpga_state();