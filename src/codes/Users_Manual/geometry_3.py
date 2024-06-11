~from pyautd3 import Controller, AUTD3
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
num_devices = autd.geometry.num_devices
num_transducers = autd.geometry.num_transducers
center = autd.geometry.center
