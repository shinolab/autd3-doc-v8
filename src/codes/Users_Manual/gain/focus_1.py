~from pyautd3 import Focus
~x = 0.0
~y = 0.0
~z = 0.0
g = Focus([x, y, z])\
        .with_intensity(0xFF)\
        .with_phase_offset(0x00)