~from pyautd3 import Controller, AUTD3, ReadsFPGAState
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder().add_device(AUTD3([0.0, 0.0, 0.0])).open(Audit.builder())
autd.send(ReadsFPGAState(lambda _: True))

info = autd.fpga_state