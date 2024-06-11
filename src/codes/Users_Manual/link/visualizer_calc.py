~import numpy as np
~from pyautd3 import AUTD3, Controller, Segment
~from pyautd3.gain import Focus
~from pyautd3.link.visualizer import Visualizer
autd: Controller[Visualizer] = (
    Controller[Visualizer].builder([AUTD3([0.0, 0.0, 0.0])]).open(Visualizer.builder())
)

center = autd.geometry.center + np.array([0, 0, 150])
g = Focus(center)
autd.send(g)

points = [center]
p = autd.link.calc_field(points, autd.geometry, Segment.S0, 0)
print(f"Acoustic pressure at ({center[0]}, {center[1]}, {center[2]}) = {p[0]}")