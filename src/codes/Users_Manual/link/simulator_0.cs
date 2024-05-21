~using AUTD3Sharp;
using AUTD3Sharp.Link;

~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
~var autd = new ControllerBuilder().AddDevice(new AUTD3(Vector3d.Zero)).Open(
Simulator.Builder(8080)
~);