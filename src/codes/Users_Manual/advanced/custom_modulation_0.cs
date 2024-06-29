~using AUTD3Sharp;
~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~using static AUTD3Sharp.Units;
using AUTD3Sharp.Derive;
~var m = new Burst(4000);

[Modulation]
public partial class Burst
{
    private readonly int _length;

    public Burst(int length)
    {
        _length = length;
        _config = 4000u * Hz;
    }

    private byte[] Calc()
    {
        var buf = Enumerable.Repeat<byte>(0x00, _length).ToArray();
        buf[0] = 0xFF;
        return buf;
    }
}