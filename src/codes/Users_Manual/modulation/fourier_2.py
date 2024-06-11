~import numpy as np
~from pyautd3 import Hz, rad, Sine
~from pyautd3.modulation import Fourier
m = Fourier([Sine(100 * Hz), Sine(150 * Hz).with_phase(np.pi / 2.0 * rad)])