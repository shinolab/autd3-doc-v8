from pyautd3 import Hz
from pyautd3.modulation import Square

m = Square(150).with_duty(0.5 * Hz)
