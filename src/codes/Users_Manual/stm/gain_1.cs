~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using static AUTD3Sharp.Units;
~using var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(Nop.Builder());
var stm = GainSTM.FromSamplingConfig(SamplingConfig.Freq(1u * Hz), [new Null(), new Null()]);