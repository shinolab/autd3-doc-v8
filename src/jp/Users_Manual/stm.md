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

### LoopBehavior

ループの挙動を, [Modulation](./modulation.md#loopbehavior)と同様に`WithLoopBehavior`で制御できる.
有限回ループするか, 無限ループするかを指定できる.

デフォルトは無限ループである.

無限ループの場合, どのインデックスデータから再生されるかは制御できない.
有限回ループの場合, 0番目のデータから再生が始まり, 指定回数のループの後, 最終インデックスデータが出力され続ける.

**この設定は, Segmentを切り替えたときにしか効果がない. 詳しくは[Segment](./segment.md)を参照.**
