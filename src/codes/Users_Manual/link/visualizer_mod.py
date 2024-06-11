~from pyautd3 import AUTD3, Controller, Segment, Hz
~from pyautd3.link.visualizer import PlotConfig, Visualizer
~from pyautd3.modulation import Sine
autd: Controller[Visualizer] = (
    Controller.builder([AUTD3([0.0, 0.0, 0.0])]).open(Visualizer.builder())
)

m = Sine(150 * Hz)
autd.send(m)

autd.link.plot_modulation(PlotConfig(fname="mod.png"), Segment.S0)