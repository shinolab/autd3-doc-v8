import numpy as np
from pyautd3 import Hz, rad
from pyautd3.modulation import Fourier, Sine

m = Fourier(Sine(100.0 * Hz)) + Sine(150.0 * Hz).with_phase(np.pi / 2.0 * rad)
