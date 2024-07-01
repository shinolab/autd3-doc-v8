~from datetime import timedelta
~from pyautd3 import Hz
~from pyautd3.modulation import Sine
m = Sine(150 * Hz).with_sampling_config(4000 * Hz)
# or
m = Sine(150 * Hz).with_sampling_config(timedelta(microseconds=250))