var autd = Controller.Builder().AddDevice(new AUTD3(Vector3d.zero)).OpenWith(Visualizer.Builder());

var center = autd.Geometry.Center + new Vector3d(0, 0, 150);
var g = new Focus(center);
autd.Send(g);

var points = new List<Vector3d> { center };
var p = autd.Link<Visualizer>().CalcField(points, autd.Geometry);
Console.WriteLine($"Acoustic pressure at ({center.x}, {center.y}, {center.z}) = ({p[0]})");
