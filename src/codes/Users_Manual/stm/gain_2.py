from pyautd3 import Hz
from pyautd3.stm import GainSTM, GainSTMMode

stm = GainSTM.from_freq(1.0 * Hz).with_mode(GainSTMMode.PhaseFull)