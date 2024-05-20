~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~var x = 0.0;
~var y = 0.0;
~var z = 0.0;
var g = new Group((dev, tr) => tr.Idx <= 100 ? "null" : "focus")
          .Set("null", new Null())
          .Set("focus", new Focus(new Vector3d(x, y, z)));