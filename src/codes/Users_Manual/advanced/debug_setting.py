~from pyautd3 import DebugSettings, GPIOOut, DebugType
~from pyautd3 import Controller, AUTD3
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder().add_device(AUTD3([0.0, 0.0, 0.0])).open(Audit.builder())
autd.send(DebugSettings(
    lambda dev, gpio: DebugType.BaseSignal if gpio == GPIOOut.O0 else DebugType.NONE
))