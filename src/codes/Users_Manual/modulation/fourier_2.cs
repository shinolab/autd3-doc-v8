using AUTD3Sharp;
using AUTD3Sharp.Modulation;

var m = new Sine(100.0) + new Sine(150.0 * Hz).WithPhase(AUTD3.Pi / 2.0 * Rad);