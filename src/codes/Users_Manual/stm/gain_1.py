from pyautd3 import Hz, SamplingConfig
from pyautd3.stm import GainSTM

stm = GainSTM.from_sampling_config(SamplingConfig.freq(1 * Hz))
