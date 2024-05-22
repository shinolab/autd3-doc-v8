~from pyautd3 import EmitIntensity, Plane, Phase
~nx = 1.0
~ny = 0.0
~nz = 0.0
g = Plane([nx, ny, nz])\
        .with_intensity(EmitIntensity.maximum())\
        .with_phase_offset(Phase(0x00))