~using AUTD3Sharp;
~using AUTD3Sharp.Modulation;
~using static AUTD3Sharp.Units;
~{
var m = new Sine(150u * Hz).WithLoopBehavior(LoopBehavior.Infinite); // infinite loop
~}
~{
var m = new Sine(150u * Hz).WithLoopBehavior(LoopBehavior.Finite(10u)); // 10 times
~}
~{
var m = new Sine(150u * Hz).WithLoopBehavior(LoopBehavior.Once); // equivalent to Finite(1u)
~}