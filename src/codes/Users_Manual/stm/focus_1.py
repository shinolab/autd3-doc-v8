~from pyautd3 import Hz, SamplingConfig, FociSTM
~import numpy as np
~foci = [np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 0.0])]
stm = FociSTM.from_sampling_config(SamplingConfig.Freq(1 * Hz), foci)