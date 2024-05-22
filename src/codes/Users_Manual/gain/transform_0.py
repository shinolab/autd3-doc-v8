~import numpy as np
~from pyautd3 import Drive, EmitIntensity, Phase, rad, Uniform
g = Uniform(EmitIntensity.maximum()).with_transform(
    lambda dev: lambda tr, d: Drive(
        Phase((d.phase.radian + np.pi) * rad), d.intensity // 2
    )
)