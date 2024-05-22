~from pyautd3 import EmitIntensity, Focus, Phase
~x = 0.0
~y = 0.0
~z = 0.0
g = Focus([x, y, z])\
        .with_intensity(EmitIntensity.maximum())\
        .with_phase_offset(Phase(0x00))