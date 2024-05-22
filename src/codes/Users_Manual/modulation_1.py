~from pyautd3 import Hz, SamplingConfig
~from pyautd3.modulation import Sine
m = Sine(150 * Hz).with_sampling_config(SamplingConfig.Division(5120))