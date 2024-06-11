~from pyautd3 import Hz, SamplingConfig, GainSTM, Null
stm = GainSTM.from_sampling_config(SamplingConfig.Freq(1 * Hz), [Null(), Null()])