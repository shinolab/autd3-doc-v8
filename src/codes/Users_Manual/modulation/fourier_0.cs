using AUTD3Sharp.Modulation;

~using static AUTD3Sharp.Units;
var m = new Fourier([new Sine(100u * Hz), new Sine(150u * Hz), new Sine(200u * Hz)]);