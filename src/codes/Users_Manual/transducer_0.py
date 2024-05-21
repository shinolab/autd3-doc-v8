~from pyautd3 import Controller, AUTD3
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder().add_device(AUTD3([0.0, 0.0, 0.0])).open(Audit.builder())
tr = autd.geometry[0][0]
idx = tr.idx
position = tr.position
rotation = tr.rotation
x_dir = tr.x_direction
y_dir = tr.y_direction
z_dir = tr.z_direction