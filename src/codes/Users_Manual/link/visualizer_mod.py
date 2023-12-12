from pyautd3 import AUTD3, Controller
from pyautd3.link.visualizer import PlotConfig, Visualizer
from pyautd3.modulation import Sine

autd: Controller[Visualizer] = (
    Controller.builder()
    .add_device(AUTD3([0.0, 0.0, 0.0]))
    .open_with(Visualizer.builder())
)

m = Sine(150)
autd.send(m)

autd.link.plot_modulation(PlotConfig(fname="mod.png"))
