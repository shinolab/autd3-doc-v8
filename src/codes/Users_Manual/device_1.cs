~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = new ControllerBuilder().AddDevice(new AUTD3(Vector3d.Zero)).Open(Nop.Builder());
~{
  var tr = autd.Geometry[0][0];
  ~}
foreach (var tr in autd.Geometry[0])
{
  // do something
}