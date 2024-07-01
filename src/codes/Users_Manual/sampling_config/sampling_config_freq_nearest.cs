~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
~var s =
SamplingConfig.FreqNearest(4000.0f * Hz)
~;
// or
~var sp =
SamplingConfig.PeriodNearest(TimeSpan.FromMicroseconds(250))
~;