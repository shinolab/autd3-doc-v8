var autd = Controller.Builder().AddDevice(new AUTD3(Vector3d.zero, Vector3d.zero)).OpenWith(Visualizer.Builder());

var m = new Sine(150);
autd.Send(m);

autd.Link.PlotModulation(new PlotConfig
{
    Fname = "mod.png"
});