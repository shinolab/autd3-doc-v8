~import numpy as np
~from pyautd3 import Drive, EmitIntensity, Phase, rad, Uniform
g = Uniform(EmitIntensity.maximum()).with_transform(
    lambda dev, tr, d: Drive(
        Phase((d.phase.radian + np.pi) * rad), EmitIntensity(d.intensity.value // 2)
    )
)