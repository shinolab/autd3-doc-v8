~using AUTD3Sharp.Utils;
~using AUTD3Sharp.Gain;
~var x = 0.0f;
~var y = 0.0f;
~var z = 0.0f;
var g = new Group(dev => tr => tr.Idx <= 100 ? "null" : "focus")
          .Set("null", new Null())
          .Set("focus", new Focus(new Vector3(x, y, z)));