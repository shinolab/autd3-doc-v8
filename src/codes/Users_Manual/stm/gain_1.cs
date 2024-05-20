~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Link;
~using static AUTD3Sharp.Units;
~using var autd = new ControllerBuilder().AddDevice(new AUTD3(Vector3d.Zero)).Open(Nop.Builder());
var stm = GainSTM.FromSamplingConfig(SamplingConfig.Freq(1u * Hz));