# Spatio-Temporal Modulation

SDK provides a function to switch `Gain` periodically (Spatio-Temporal Modulation, STM).
The SDK provides `FociSTM` that supports 8 foci at maximum and `GainSTM` that support arbitrary `Gain`.
`FociSTM` and `GainSTM` use the timer on the AUTD3 hardware, so the time accuracy is high, but there are many restrictions.

- [FociSTM](./stm/focus.md)
- [GainSTM](./stm/gain.md)

## FociSTM/GainSTM common API

### frequency

Get the frequency of STM.

### sampling_config

Get the sampling configuration of STM.
