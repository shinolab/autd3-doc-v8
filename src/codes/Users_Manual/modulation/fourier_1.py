~from pyautd3 import Hz
~from pyautd3.modulation import Fourier, Sine
m = Fourier(Sine(100 * Hz)) + Sine(150 * Hz)