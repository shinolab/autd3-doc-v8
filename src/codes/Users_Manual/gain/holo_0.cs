using AUTD3Sharp.Gain.Holo;

~using AUTD3Sharp.Utils;
~using static AUTD3Sharp.Units;
~var x1 = 0.0f;
~var y1 = 0.0f;
~var z1 = 0.0f;
~var x2 = 0.0f;
~var y2 = 0.0f;
~var z2 = 0.0f;
var backend = new NalgebraBackend();
var g = new GSPAT(backend, [
                        (new Vector3(x1, y1, z1), 5e3f * Pa),
                        (new Vector3(x1, y1, z1), 5e3f * Pa)
                    ]);