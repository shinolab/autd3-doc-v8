~import numpy as np
~from pyautd3 import Controller, AUTD3
~from pyautd3.link.audit import Audit
~autd: Controller[Audit] = Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Audit.builder())
dev = autd.geometry[0]
idx = dev.idx
dev.enable = False
dev.sound_speed = 340e3
dev.set_sound_speed_from_temp(15.0)
t = np.array([1.0, 0.0, 0.0])
r = np.array([1.0, 0.0, 0.0, 0.0])
dev.translate(t)
dev.rotate(r)
dev.affine(t, r)
wavelength = dev.wavelength
wavenumber = dev.wavenumber
rotation = dev.rotation
x_dir = dev.x_direction
y_dir = dev.y_direction
axial_dir = dev.axial_direction