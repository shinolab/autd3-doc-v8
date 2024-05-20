~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Link;
~using static AUTD3Sharp.Units;
~using var autd = new ControllerBuilder().AddDevice(new AUTD3(Vector3d.Zero)).Open(Nop.Builder());
var center = autd.Geometry.Center + new Vector3d(0, 0, 150);
const int pointNum = 200;
const double radius = 30.0;
var stm = GainSTM.FromFreq(1.0 * Hz).AddGainsFromIter(Enumerable.Range(0, pointNum).Select(i =>
{
    var theta = 2.0 * Math.PI * i / pointNum;
    return new Focus(center + radius * new Vector3d(Math.Cos(theta), Math.Sin(theta), 0));
}));