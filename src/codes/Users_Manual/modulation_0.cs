~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
var m = new Sine(150u * Hz).WithSamplingConfig(SamplingConfig.Freq(4000 * Hz));