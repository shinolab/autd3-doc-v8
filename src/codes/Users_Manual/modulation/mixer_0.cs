using AUTD3Sharp.Modulation;

~using static AUTD3Sharp.Units;
var m = new Mixer([new Sine(100u * Hz), new Sine(150u * Hz)]);