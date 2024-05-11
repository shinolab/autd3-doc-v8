from pyautd3 import Hz
from pyautd3.modulation import Square

m = Square(150.0 * Hz).with_low(0x00).with_high(0xFF)
