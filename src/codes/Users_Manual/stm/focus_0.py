~import numpy as np
~from pyautd3 import Controller, AUTD3, FocusSTM, Hz
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder().add_device(AUTD3([0.0, 0.0, 0.0])).open(Audit.builder())
center = autd.geometry.center + np.array([0.0, 0.0, 150.0])
point_num = 200
radius = 30.0
stm = FocusSTM.from_freq(1.0 * Hz).add_foci_from_iter(
    map(
        lambda theta: center + radius * np.array([np.cos(theta), np.sin(theta), 0]),
        map(lambda i: 2.0 * np.pi * i / point_num, range(point_num)),
    )
)