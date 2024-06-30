~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~using static AUTD3Sharp.Units;
~var x = 0.0f;
~var y = 0.0f;
~var z = 0.0f;
~var nx = 0.0f;
~var ny = 0.0f;
~var nz = 1.0f;
~var theta = 0.0f;
var g = new Bessel(
            new Vector3(x, y, z),
            new Vector3(nx, ny, nz),
            theta * rad
        )
        .WithIntensity(0xFF)
        .WithPhaseOffset(0x00);