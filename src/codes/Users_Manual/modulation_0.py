from pyautd3 import Hz, SamplingConfig
from pyautd3.modulation import Sine

m = Sine(150.0 * Hz).with_sampling_config(SamplingConfig.frequency(4000 * Hz))
