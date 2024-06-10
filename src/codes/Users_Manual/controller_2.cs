~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(Nop.Builder());
~var x = 0.0f;
~var y = 0.0f;
~var z = 0.0f;
autd.Group(dev =>
    {
        return dev.Idx switch
        {
            0 => "null",
            1 => "focus",
            _ => null
        };
    })
    .Set("null", new Null())
    .Set("focus", new Focus(new Vector3(x, y, z)))
    .Send();