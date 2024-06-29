~from pyautd3 import SamplingConfig, Hz
~from datetime import timedelta
SamplingConfig.FreqNearest(4000.0 * Hz)
# or
SamplingConfig.PeriodNearest(timedelta(microseconds=250))
# or
SamplingConfig.DivisionRaw(5120)