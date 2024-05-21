~import numpy as np
~from pyautd3 import AUTD3, Controller, Segment
~from pyautd3.gain import Focus
~from pyautd3.link.visualizer import PlotConfig, PlotRange, Visualizer
autd: Controller[Visualizer] = (
    Controller.builder().add_device(AUTD3([0.0, 0.0, 0.0])).open(Visualizer.builder())
)

center = autd.geometry.center + np.array([0, 0, 150])
g = Focus(center)
autd.send(g)

autd.link.plot_field(
    PlotConfig(fname="xy.png"),
    PlotRange(
        x_start=center[0] - 20,
        x_end=center[0] + 20,
        y_start=center[1] - 30,
        y_end=center[1] + 30,
        z_start=center[2],
        z_end=center[2],
        resolution=1,
    ),
    autd.geometry,
    Segment.S0,
    0,
)