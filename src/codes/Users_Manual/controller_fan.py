~from pyautd3 import ForceFan
~from pyautd3 import Controller, AUTD3
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
autd.send(ForceFan(lambda _: True))