autd.send(autd3::ReadsFPGAState([](const auto&) { return true; }));

const auto info = autd.fpga_state();