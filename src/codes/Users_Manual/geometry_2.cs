~using System;
~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using static AUTD3Sharp.Units;
Controller.Builder([
   new AUTD3(Vector3.Zero),
   new AUTD3(new Vector3(AUTD3.DeviceWidth, 0, 0))
         .WithRotation(EulerAngles.ZYZ(0 * rad, MathF.PI / 2 * rad, 0 * rad))
])
~;