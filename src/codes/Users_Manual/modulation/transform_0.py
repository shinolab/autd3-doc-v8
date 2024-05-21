~from pyautd3 import Hz, Sine
m = Sine(150 * Hz).with_transform(lambda i, d: d // 2)