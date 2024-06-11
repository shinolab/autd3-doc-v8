from collections.abc import Callable

import numpy as np
from pyautd3 import Device, Drive, EmitIntensity, Geometry, Phase, Transducer, rad
from pyautd3.gain import Gain


class Focus(Gain):
    def __init__(self, point):
        self.point = np.array(point)

    def calc(self, _: Geometry) -> Callable[[Device], Callable[[Transducer], Drive]]:
        return Gain._transform(
            lambda dev: lambda tr: Drive(
                Phase(
                    float(np.linalg.norm(tr.position - self.point))
                    * dev.wavenumber
                    * rad
                ),
                EmitIntensity.maximum(),
            ),
        )
