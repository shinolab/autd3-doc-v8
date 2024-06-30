~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp;
~var nx = 0.0f;
~var ny = 0.0f;
~var nz = 1.0f;
var g = new Plane(new Vector3(nx, ny, nz))
                .WithIntensity(0xFF)
                .WithPhaseOffset(0x00);