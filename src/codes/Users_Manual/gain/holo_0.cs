~using AUTD3Sharp.Gain.Holo;
~using AUTD3Sharp.Utils;
~using static AUTD3Sharp.Units;
~var x1 = 0.0;
~var y1 = 0.0;
~var z1 = 0.0;
~var x2 = 0.0;
~var y2 = 0.0;
~var z2 = 0.0;
var backend = new NalgebraBackend();
var g = new GSPAT<NalgebraBackend>(backend)
            .AddFocus(new Vector3d(x1, y1, z1), 5e3 * Pa)
            .AddFocus(new Vector3d(x2, y2, z2), 5e3 * Pa);