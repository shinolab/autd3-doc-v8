~from pyautd3 import EmitIntensity
~from pyautd3.gain.holo import GSPAT, EmissionConstraint, NalgebraBackend
~from pyautd3.gain.holo import Pa
~import numpy as np
backend = NalgebraBackend()
~x1 = 0.0
~y1 = 0.0
~z1 = 0.0
~x2 = 0.0
~y2 = 0.0
~z2 = 0.0
~foci = [(np.array([x1, y1, z1]), 5e3 * Pa), (np.array([x2, y2, z2]), 5e3 * Pa)]
g = GSPAT(backend, foci).with_constraint(EmissionConstraint.Uniform(EmitIntensity.maximum()))