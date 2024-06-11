~from pyautd3 import Hz, Sine
~from pyautd3.modulation import Fourier
m = Fourier([Sine(100 * Hz), Sine(150 * Hz)])