~from pyautd3 import Hz
~from pyautd3.modulation import Sine
m = Sine(150 * Hz).with_transform(lambda i, d: d // 2)