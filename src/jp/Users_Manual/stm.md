# Spatio-Temporal Modulation/時空間変調

SDKでは, `Gain`を周期的に切り替えるための機能 (Spatio-Temporal Modulation, STM) が用意されている.
SDKには単一焦点のみをサポートする`FocusSTM`と, 任意の`Gain`をサポートする`GainSTM`が用意されている.
`FocusSTM`と`GainSTM`はAUTD3ハードウェア上のタイマを使用するので時間精度が高いが, 制約も多い.

- [FocusSTM](./stm/focus.md)
- [GainSTM](./stm/gain.md)

## FocusSTM/GainSTMの共通API

### frequency

STMの周波数を取得する.

### sampling_config

サンプリング設定を取得する.
