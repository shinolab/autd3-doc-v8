~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Link;
~using static AUTD3Sharp.Units;
~using var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(Nop.Builder());
var stm = FociSTM.FromSamplingConfig(SamplingConfig.Freq(1u * Hz), [Vector3.Zero, Vector3.Zero]);