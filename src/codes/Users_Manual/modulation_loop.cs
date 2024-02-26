using AUTD3Sharp;
using AUTD3Sharp.Modulation;

var m = new Sine(150).WithLoopBehavior(LoopBehavior.Infinite); // infinite loop
var m = new Sine(150).WithLoopBehavior(LoopBehavior.Finite(10u)); // 10 times
var m = new Sine(150).WithLoopBehavior(LoopBehavior.Once); // equivalent to Finite(1u)