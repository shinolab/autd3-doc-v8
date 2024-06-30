# Wav

`Wav`はWavファイルをもとに構成される`Modulation`である.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/wav_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/wav_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/wav_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/wav_0.py}}
```

> NOTE: AUTD3のサンプリング周波数に関する制約により, 出力できない可能性があるので注意されたい.
> その場合は, 元のファイルを適当な周波数で各自リサンプリングすること. **本SDKでは, リサンプリング機能は提供しない.**
> Modulationのサンプリング周波数の設定と制約は[Modulation](../modulation.md)を参照されたい.
