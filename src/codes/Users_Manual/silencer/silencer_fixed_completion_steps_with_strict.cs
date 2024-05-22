~using AUTD3Sharp;
ushort stepsIntensity = 10;
ushort stepsPhase = 10;
var config = Silencer.FixedCompletionSteps(stepsIntensity, stepsPhase).WithStrictMode(false);