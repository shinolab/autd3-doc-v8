~using custom;
~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~using static AUTD3Sharp.Units;
using AUTD3Sharp.Derive;

var g = new FocalPoint(new Vector3d(0, 0, 0));

namespace custom
{
    [Gain]
    public partial class FocalPoint
    {
        private readonly Vector3d _point;

        public FocalPoint(Vector3d point)
        {
            _point = point;
        }

        private Dictionary<int, Drive[]> Calc(Geometry geometry)
        {
            return Transform(geometry, (dev, tr) =>
            {
                var tp = tr.Position;
                var dist = (tp - _point).L2Norm;
                var phase = dist * dev.Wavenumber;
                return new Drive { Phase = Phase.FromRad(phase), Intensity = EmitIntensity.Max };
            });
        }
    }
}