~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.NativeMethods;
~using static AUTD3Sharp.Units;
~var autd =
Controller.Builder([]).WithUltrasoundFreq(41 * kHz)
~;