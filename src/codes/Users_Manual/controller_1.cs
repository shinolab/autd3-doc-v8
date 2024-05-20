~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
~using var autd = new ControllerBuilder().AddDevice(new AUTD3(Vector3d.Zero)).Open(Nop.Builder());
~var m = new Static();
~var g = new Null();
autd.Send((m, g), TimeSpan.FromMilliseconds(20));