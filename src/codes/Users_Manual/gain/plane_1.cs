~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp;
~var nx = 0.0;
~var ny = 0.0;
~var nz = 1.0;
var g = new Plane(new Vector3d(nx, ny, nz))
                .WithIntensity(EmitIntensity.Max)
                .WithPhaseOffset(new Phase(0x00));