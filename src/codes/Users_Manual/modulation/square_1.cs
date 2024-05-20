~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
var m = new Square(150u * Hz)
        .WithLow(new EmitIntensity(0x00))
        .WithHigh(new EmitIntensity(0xFF));