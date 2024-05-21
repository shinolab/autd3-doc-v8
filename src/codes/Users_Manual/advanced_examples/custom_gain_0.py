import numpy as np
from pyautd3 import Drive, EmitIntensity, Geometry, Phase, rad
from pyautd3.gain import Gain


class Focus(Gain):
    def __init__(self, point):
        self.point = np.array(point)

    def calc(self, geometry: Geometry) -> dict[int, np.ndarray]:
        return Gain._transform(
            geometry,
            lambda dev: lambda tr: Drive(
                Phase(
                    float(np.linalg.norm(tr.position - self.point))
                    * dev.wavenumber
                    * rad
                ),
                EmitIntensity.maximum(),
            ),
        )
