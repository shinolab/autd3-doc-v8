~import numpy as np
~from pyautd3 import AUTD3, Controller, FociSTM, Hz
from pyautd3 import ControlPoint, ControlPoints2
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(
~    Audit.builder()
~)
center = autd.geometry.center + np.array([0.0, 0.0, 150.0])
point_num = 200
radius = 30.0
stm = FociSTM.from_freq(
    1.0 * Hz,
    (
        ControlPoints2(
            (
                ControlPoint(center + radius * np.array([np.cos(theta), np.sin(theta), 0])).with_offset(0x00),
                ControlPoint(center - radius * np.array([np.cos(theta), np.sin(theta), 0])).with_offset(0x00),
            ),
        ).with_intensity(0xFF)
        for theta in (2.0 * np.pi * i / point_num for i in range(point_num))
    ),
)