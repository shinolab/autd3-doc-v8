~using custom;
~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
using AUTD3Sharp.Derive;

var m = new Burst(4000);

namespace custom
{
    [Modulation]
    public partial class Burst
    {
        private readonly int _length;

        public Burst(int length)
        {
            _length = length;
        }

        private EmitIntensity[] Calc(Geometry _)
        {
            var buf = Enumerable.Repeat<EmitIntensity>(EmitIntensity.Min, _length).ToArray();
            buf[0] = EmitIntensity.Max;
            return buf;
        }
    }
}