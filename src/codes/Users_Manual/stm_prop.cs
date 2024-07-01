~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Link;
~using static AUTD3Sharp.Units;
~using var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(Nop.Builder());
var stm = FociSTM.FromSamplingConfig(1u * Hz, [Vector3.Zero, Vector3.Zero]);
var f = stm.Freq;                 // -> 1Hz
var p = stm.Period;               // -> 1s
var fs = stm.SamplingConfig.Freq; // -> 2Hz