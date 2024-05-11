autd.send(autd3::PhaseFilter([](const auto& dev) {
  return [](const auto& tr) { return autd3::Phase(0); };
}));