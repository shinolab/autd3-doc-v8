from pyautd3 import Hz
from pyautd3.modulation import Sine

m = Sine(150.0 * Hz).with_intensity(0xFF).with_offset(0xFF / 2)
