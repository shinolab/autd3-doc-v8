from pyautd3.gain.holo import GSPAT, NalgebraBackend, Pa

~import numpy as np
~x1 = 0.0
~y1 = 0.0
~z1 = 0.0
~x2 = 0.0
~y2 = 0.0
~z2 = 0.0
backend = NalgebraBackend()
g = GSPAT(backend, [(np.array([x1, y1, z1]), 5e3 * Pa), (np.array([x2, y2, z2]), 5e3 * Pa)])