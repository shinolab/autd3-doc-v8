~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Link;
~using static AUTD3Sharp.Units;
~using var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(Nop.Builder());
var center = autd.Geometry.Center + new Vector3(0, 0, 150);
const int pointNum = 200;
const float radius = 30.0f;
var stm = GainSTM.FromFreq(1.0f * Hz, Enumerable.Range(0, pointNum).Select(i =>
{
    var theta = 2.0f * MathF.PI * i / pointNum;
    return new Focus(center + radius * new Vector3(MathF.Cos(theta), MathF.Sin(theta), 0));
}));