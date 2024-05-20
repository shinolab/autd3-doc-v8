~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
var autd = new ControllerBuilder().AddDevice(new AUTD3(Vector3d.Zero)).Open(Visualizer.Builder());

var center = autd.Geometry.Center + new Vector3d(0, 0, 150);
var g = new Focus(center);
autd.Send(g);

autd.Link.PlotField(new PlotConfig
{
    Fname = "xy.png"
},
    new PlotRange
    {
        XStart = center.X - 20,
        XEnd = center.X + 20,
        YStart = center.Y - 30,
        YEnd = center.Y + 30,
        ZStart = center.Z,
        ZEnd = center.Z,
        Resolution = 1
    },
    autd.Geometry,
    Segment.S0,
    0
);