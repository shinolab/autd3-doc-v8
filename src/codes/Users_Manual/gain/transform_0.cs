~using System;
~using AUTD3Sharp;
~using AUTD3Sharp.Gain;
~using static AUTD3Sharp.Units;
var g = new Uniform(EmitIntensity.Max).WithTransform(dev => (tr, d) =>
{
    d.Intensity = d.Intensity / 2;
    d.Phase = new Phase((d.Phase.Radian + MathF.PI) * rad);
    return d;
});