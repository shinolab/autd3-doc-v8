from pyautd3 import Hz
from pyautd3.modulation import Fourier, Sine

m = (
    Fourier(Sine(100.0 * Hz))
    .add_component(Sine(150.0 * Hz))
    .add_components_from_iter([Sine(200.0 * Hz)])
)
