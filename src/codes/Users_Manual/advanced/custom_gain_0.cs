~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~using static AUTD3Sharp.Units;
using AUTD3Sharp.Derive;
~var g = new FocalPoint(Vector3.Zero);

[Gain]
public partial class FocalPoint
{
    private readonly Vector3 _point;

    public FocalPoint(Vector3 point)
    {
        _point = point;
    }

    private Func<Device, Func<Transducer, Drive>> Calc(Geometry geometry)
    {
        return Transform(dev => tr =>
        {
            var tp = tr.Position;
            var dist = (tp - _point).L2Norm;
            var phase = dist * dev.Wavenumber;
            return new Drive { Phase = new Phase(phase * rad), Intensity = EmitIntensity.Max };
        });
    }
}