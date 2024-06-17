~from pyautd3 import Hz, SamplingConfig
~import numpy as np
from pyautd3.modulation import Custom

buf = np.array([0xFF, 0xFF])
m = Custom(buf, SamplingConfig.Freq(4000 * Hz))
