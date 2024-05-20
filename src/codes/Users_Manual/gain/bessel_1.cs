~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~var x = 0.0;
~var y = 0.0;
~var z = 0.0;
~var nx = 0.0;
~var ny = 0.0;
~var nz = 1.0;
~var theta = 0.0;
var g = new Bessel(
            new Vector3d(x, y, z),
            new Vector3d(nx, ny, nz),
            theta
        ).WithIntensity(EmitIntensity.Max);