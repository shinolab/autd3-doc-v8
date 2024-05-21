~from pyautd3 import Hz, Sine
~from pyautd3.modulation import Fourier
m = (
    Fourier(Sine(100 * Hz))
    .add_component(Sine(150 * Hz))
    .add_components_from_iter([Sine(200 * Hz)])
)