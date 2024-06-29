~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
var buf = new byte[] { 0xFF, 0x00 };
var m = new Custom(buf, 4000 * Hz);