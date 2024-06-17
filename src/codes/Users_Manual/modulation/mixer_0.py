~from pyautd3 import Hz, Sine
~from pyautd3.modulation import Mixer
m = Mixer([Sine(100 * Hz), Sine(150 * Hz)])