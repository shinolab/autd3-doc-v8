autd.send(autd3::ConfigurePhaseFilter([](const auto& dev, const auto& tr) {
  return autd3::Phase(0);
}));