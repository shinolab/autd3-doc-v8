~using System;
~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using static AUTD3Sharp.Units;
new ControllerBuilder()
   .AddDevice(new AUTD3(Vector3d.Zero))
   .AddDevice(
      new AUTD3(new Vector3d(AUTD3.DeviceWidth, 0, 0))
         .WithRotation(EulerAngles.FromZyz(0 * rad, Math.PI / 2 * rad, 0 * rad)))
~;