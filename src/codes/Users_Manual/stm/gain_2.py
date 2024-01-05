from pyautd3.stm import GainSTM, GainSTMMode

stm = GainSTM.from_freq(1).with_mode(GainSTMMode.PhaseFull)
