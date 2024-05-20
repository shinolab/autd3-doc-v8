~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
var m = new Sine(150u * Hz)
        .WithIntensity(new EmitIntensity(0xFF))
        .WithOffset(new EmitIntensity(0xFF / 2));