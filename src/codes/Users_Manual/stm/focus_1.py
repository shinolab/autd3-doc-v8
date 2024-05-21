~from pyautd3 import Hz, SamplingConfig, FocusSTM
stm = FocusSTM.from_sampling_config(SamplingConfig.Freq(1 * Hz))