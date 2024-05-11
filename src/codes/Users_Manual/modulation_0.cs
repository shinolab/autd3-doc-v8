using AUTD3Sharp;
using AUTD3Sharp.Modulation;

var m = new Sine(150 * Hz).WithReadsFPGAState(SamplingConfig.Freq(4000 * Hz));