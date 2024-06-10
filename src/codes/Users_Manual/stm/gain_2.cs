~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using static AUTD3Sharp.Units;
~using var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(Nop.Builder());
var stm = GainSTM.FromFreq(1.0f * Hz, [new Null(), new Null()]).WithMode(GainSTMMode.PhaseFull);