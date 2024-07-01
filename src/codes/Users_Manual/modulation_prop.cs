~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
var m = new Sine(150u * Hz);
var fs = m.SamplingConfig.Freq; // -> 4kHz