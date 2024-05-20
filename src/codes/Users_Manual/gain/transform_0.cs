~using System;
~using AUTD3Sharp;
~using AUTD3Sharp.Gain;
var g = new Uniform(EmitIntensity.Max).WithTransform((dev, tr, d) =>
{
    d.Intensity = d.Intensity / 2;
    d.Phase = Phase.FromRad(d.Phase.Radian + Math.PI);
    return d;
});