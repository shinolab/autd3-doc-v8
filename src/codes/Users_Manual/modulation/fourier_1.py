from pyautd3 import Hz
from pyautd3.modulation import Fourier, Sine

m = Fourier(Sine(100.0 * Hz)) + Sine(150.0 * Hz)
