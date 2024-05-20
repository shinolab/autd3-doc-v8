~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
new ControllerBuilder()
   .AddDevice(new AUTD3(new Vector3d(-AUTD3.DeviceWidth, 0, 0)))
   .AddDevice(new AUTD3(Vector3d.Zero))
~;