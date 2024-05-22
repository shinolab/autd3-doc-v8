~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~var x = 0.0;
~var y = 0.0;
~var z = 0.0;
var g = new Focus(new Vector3d(x, y, z))
            .WithIntensity(EmitIntensity.Max)
            .WithPhaseOffset(new Phase(0x00));