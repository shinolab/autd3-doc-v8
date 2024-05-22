~using System;
~using AUTD3Sharp;
~using AUTD3Sharp.Gain;
~using static AUTD3Sharp.Units;
var g = new Custom(dev => tr =>
{
    return new Drive(new Phase(0x00), new EmitIntensity(0x00));
});