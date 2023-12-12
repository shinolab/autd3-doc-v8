var autd = Controller.Builder().AddDevice(new AUTD3(Vector3d.zero)).OpenWith(Visualizer.Builder());

var center = autd.Geometry.Center + new Vector3d(0, 0, 150);
var g = new Focus(center);
autd.Send(g);

autd.Link<Visualizer>().PlotField(new PlotConfig
{
    Fname = "xy.png"
},
    new PlotRange
    {
        XStart = center.x - 20,
        XEnd = center.x + 20,
        YStart = center.y - 30,
        YEnd = center.y + 30,
        ZStart = center.z,
        ZEnd = center.z,
        Resolution = 1
    },
    autd.Geometry);
