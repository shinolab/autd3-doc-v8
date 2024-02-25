using AUTD3Sharp.Derive;

[Modulation]
public partial class Burst
{
    private readonly int _length;

    public Burst(int length)
    {
        _length = length;
    }

    private EmitIntensity[] Calc()
    {
        var buf = Enumerable.Repeat<EmitIntensity>(EmitIntensity.Min, _length).ToArray();
        buf[0] = EmitIntensity.Max;
        return buf;
    }
}