~from pyautd3 import Hz
~import numpy as np
from pyautd3.modulation import Custom

buf = np.array([0xFF, 0xFF])
m = Custom(buf, 4000 * Hz)
