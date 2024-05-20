~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = new ControllerBuilder().AddDevice(new AUTD3(Vector3d.Zero)).Open(Nop.Builder());
~{
  var dev = autd.Geometry[0];
  ~}
foreach (var dev in autd.Geometry)
{
  // do something
}