~import numpy as np
~from pyautd3 import Controller, AUTD3, PulseWidthEncoder
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder().add_device(AUTD3([0.0, 0.0, 0.0])).open(Audit.builder())
table = np.zeros(65536, dtype=np.uint16)
autd.send(PulseWidthEncoder(table))