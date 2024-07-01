~using AUTD3Sharp;
~{
ushort stepsIntensity = 10;
ushort stepsPhase = 10;
var config = Silencer.FromCompletionSteps(stepsIntensity, stepsPhase);
~}
// or
~{
var timeIntensity = TimeSpan.FromMicroseconds(250);
var timePhase = TimeSpan.FromMicroseconds(250);
var config = Silencer.FromCompletionTime(timeIntensity, timePhase);
~}