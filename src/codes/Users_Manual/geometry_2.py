~import numpy as np
~from pyautd3 import AUTD3, Controller, EulerAngles, rad
Controller.builder(
    [
        AUTD3([0.0, 0.0, 0.0]),
        AUTD3([AUTD3.DEVICE_WIDTH, 0.0, 0.0]).with_rotation(
            EulerAngles.ZYZ(0 * rad, np.pi / 2 * rad, 0 * rad)
        ),
    ],
)
