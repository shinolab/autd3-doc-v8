~from pyautd3 import EmitIntensity
~from pyautd3.gain import Plane
~nx = 1.0
~ny = 0.0
~nz = 0.0
g = Plane([nx, ny, nz]).with_intensity(EmitIntensity.maximum())
