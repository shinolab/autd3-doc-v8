# Spatio-Temporal Modulation

SDK provides a function to switch `Gain` periodically (Spatio-Temporal Modulation, STM).
The SDK provides `FocusSTM` that supports only a single focus and `GainSTM` that support arbitrary `Gain`.
`FocusSTM` and `GainSTM` use the timer on the AUTD3 hardware, so the time accuracy is high, but there are many restrictions.

- [FocusSTM](./stm/focus.md)
- [GainSTM](./stm/gain.md)

## FocusSTM/GainSTM common API

### frequency

Get the frequency of STM.

### sampling_config

Get the sampling configuration of STM.
