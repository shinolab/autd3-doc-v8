~from pyautd3 import Bessel, rad
~x = 0.0
~y = 0.0
~z = 0.0
~nx = 1.0
~ny = 0.0
~nz = 0.0
~theta = 0.0
g = Bessel([x, y, z], [nx, ny, nz], theta * rad)\
        .with_intensity(0xFF)\
        .with_phase_offset(0x00)