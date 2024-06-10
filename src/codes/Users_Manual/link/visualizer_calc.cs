~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(Visualizer.Builder());

var center = autd.Geometry.Center + new Vector3(0, 0, 150);
var g = new Focus(center);
autd.Send(g);

var points = new List<Vector3> { center };
var p = autd.Link.CalcField(points, autd.Geometry, Segment.S0, 0);
Console.WriteLine($"Acoustic pressure at ({center.X}, {center.Y}, {center.Z}) = ({p[0]})");