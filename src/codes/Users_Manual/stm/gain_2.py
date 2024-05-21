~from pyautd3 import Hz, GainSTM, GainSTMMode
stm = GainSTM.from_freq(1.0 * Hz).with_mode(GainSTMMode.PhaseFull)