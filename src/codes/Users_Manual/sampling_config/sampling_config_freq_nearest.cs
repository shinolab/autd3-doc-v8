~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
~var s =
SamplingConfig.FreqNearest(4000.0 * Hz)
~;
// or
~var s2 =
SamplingConfig.DivisionRaw(5120)
~;