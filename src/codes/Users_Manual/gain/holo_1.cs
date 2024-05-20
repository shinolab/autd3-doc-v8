~using AUTD3Sharp.Gain.Holo;
~using AUTD3Sharp;
var backend = new NalgebraBackend();
var g = new GSPAT<NalgebraBackend>(backend).WithConstraint(EmissionConstraint.Uniform(EmitIntensity.Max));