~from datetime import timedelta
~from pyautd3 import Controller, AUTD3, Static, Null
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder().add_device(AUTD3([0.0, 0.0, 0.0])).open(Audit.builder())
~m = Static()
~g = Null()
autd.send((m, g), timeout=timedelta(milliseconds=20))
