~from pyautd3 import Hz, EmitIntensity, Sine
m = Sine(150 * Hz).with_intensity(EmitIntensity(0xFF)).with_offset(EmitIntensity(0xFF) // 2)