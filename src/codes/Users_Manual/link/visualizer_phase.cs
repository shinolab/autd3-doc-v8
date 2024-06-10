~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(Visualizer.Builder());

var center = autd.Geometry.Center + new Vector3(0, 0, 150);
var g = new Focus(center);
autd.Send(g);

autd.Link.PlotPhase(new PlotConfig
{
    Fname = "phase.png"
}, autd.Geometry, Segment.S0, 0);