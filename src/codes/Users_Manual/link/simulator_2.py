~from pyautd3 import Controller, AUTD3
~from pyautd3.link.simulator import Simulator
~autd: Controller[Simulator] = Controller.builder().add_device(AUTD3([0.0, 0.0, 0.0])).open(Simulator.builder(8080))
autd.link.update_geometry(autd.geometry)