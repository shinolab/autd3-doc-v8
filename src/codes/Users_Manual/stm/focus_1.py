from pyautd3 import Hz, SamplingConfig
from pyautd3.stm import FocusSTM

stm = FocusSTM.from_sampling_config(SamplingConfig.freq(1 * Hz))
