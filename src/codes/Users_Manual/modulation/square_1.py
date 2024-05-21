~from pyautd3 import Hz, EmitIntensity, Square
m = Square(150 * Hz).with_low(EmitIntensity(0x00)).with_high(EmitIntensity(0xFF))