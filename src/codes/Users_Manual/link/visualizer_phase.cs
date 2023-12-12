var autd = Controller.Builder().AddDevice(new AUTD3(Vector3d.zero)).OpenWith(Visualizer.Builder());

var center = autd.Geometry.Center + new Vector3d(0, 0, 150);
var g = new Focus(center);
autd.Send(g);

autd.Link.PlotPhase(new PlotConfig
{
    Fname = "phase.png"
}, autd.Geometry);