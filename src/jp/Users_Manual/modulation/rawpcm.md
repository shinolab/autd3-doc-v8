# RawPCM

`RawPCM`はraw pcmファイルをもとに構成される`Modulation`である.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/rawpcm_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/rawpcm_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/rawpcm_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/rawpcm_0.py}}
```

コンストラクタの第2引数で, このデータのサンプリング設定を指定する必要がある.

> NOTE: AUTD3のサンプリング周波数に関する制約により, 出力できない可能性があるので注意されたい.
> その場合は, 元のファイルを適当な周波数で各自リサンプリングすること. **本SDKでは, リサンプリング機能は提供しない.**
> Modulationのサンプリング周波数の設定と制約は[Modulation](../modulation.md)を参照されたい.
