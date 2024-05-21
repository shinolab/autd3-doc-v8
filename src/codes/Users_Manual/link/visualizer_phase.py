~import numpy as np
~from pyautd3 import AUTD3, Controller, Segment
~from pyautd3.gain import Focus
from pyautd3.link.visualizer import PlotConfig, Visualizer

autd: Controller[Visualizer] = (
    Controller.builder().add_device(AUTD3([0.0, 0.0, 0.0])).open(Visualizer.builder())
)

center = autd.geometry.center + np.array([0, 0, 150])
g = Focus(center)
autd.send(g)

autd.link.plot_phase(PlotConfig(fname="phase.png"), autd.geometry, Segment.S0, 0)