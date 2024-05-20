~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
~using static AUTD3Sharp.Units;
var autd = new ControllerBuilder().AddDevice(new AUTD3(Vector3d.Zero)).Open(Visualizer.Builder());

var m = new Sine(150u * Hz);
autd.Send(m);

autd.Link.PlotModulation(new PlotConfig
{
    Fname = "mod.png"
}, Segment.S0);