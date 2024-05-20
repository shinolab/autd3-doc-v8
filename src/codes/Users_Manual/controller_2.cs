~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
~using var autd = new ControllerBuilder().AddDevice(new AUTD3(Vector3d.Zero)).Open(Nop.Builder());
~var x = 0.0;
~var y = 0.0;
~var z = 0.0;
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
    .Set("focus", new Focus(new Vector3d(x, y, z)))
    .Send();