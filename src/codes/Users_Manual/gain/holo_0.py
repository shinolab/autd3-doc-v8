from pyautd3.gain.holo import GSPAT, NalgebraBackend, Pa

backend = NalgebraBackend()
g = GSPAT(backend).add_focus([x1, y1, z1], 5e3 * Pa).add_focus([x2, y2, z2], 5e3 * Pa)
