~from pyautd3 import Hz
~from pyautd3.modulation import Sine
m = Sine(150 * Hz)
fs = m.sampling_config.freq # -> 4kHz