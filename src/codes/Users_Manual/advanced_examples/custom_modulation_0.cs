~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~using static AUTD3Sharp.Units;
using AUTD3Sharp.Derive;

[Modulation]
public partial class Burst
{
    private readonly int _length;

    public Burst(int length)
    {
        _length = length;
        _config = SamplingConfig.Freq(4000u * Hz);
    }

    private EmitIntensity[] Calc(Geometry _)
    {
        var buf = Enumerable.Repeat<EmitIntensity>(EmitIntensity.Min, _length).ToArray();
        buf[0] = EmitIntensity.Max;
        return buf;
    }
}