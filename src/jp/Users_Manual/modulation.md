# Modulation

`Modulation`はAM変調を制御するための仕組みである.

Modulationは音圧振幅に掛け合わされる.
例えば, $\SI{1}{kHz}$の`Sine`変調を印加した場合の音圧振幅は以下のようになり, 音圧振幅の正の部分 (或いは, 負の部分) の包絡線が$\SI{1}{kHz}$のsin波に従う.

<figure>
  <img src="../fig/Users_Manual/sine_1k_mod.png"/>
</figure>

なお, 現在, `Modulation`には以下の制約がある.

* バッファサイズは最大で65536
* Modulationデータは内部で8-bit符号なし整数に変換され, 超音波PWM信号のDuty比と掛け合わされる
* サンプリングレートは$\clkf/N$で, $N$は32-bit符号なし整数であり, $512$以上の値である必要がある

SDKにはデフォルトでいくつかの種類のAMを生成するための`Modulation`が用意されている.

* [Static](./modulation/static.md)
* [Sine](./modulation/sine.md)
  * [Fourier](./modulation/fourier.md)
* [Square](./modulation/square.md)
* [Wav](./modulation/wav.md)
* [RawPCM](./modulation/rawpcm.md)
* [Cache](./modulation/cache.md)
* [RadiationPressure](./modulation/radiation.md)
* [Transform](./modulation/transform.md)

## Modulationの共通API

### Sampling設定

`sampling_config`でサンプリング設定を取得できる.
デフォルトのサンプリング周波数は$\SI{4}{kHz}$である.

また, 一部の`Modulation`は`with_sampling_config`でサンプリングを設定できる.
ただし, `Modulation`の制約上, 必ずしも指定した設定になるとは限らない.

```rust,edition2021
{{#include ../../codes/Users_Manual/modulation_0.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/modulation_0.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/modulation_0.cs}}
```

```python
{{#include ../../codes/Users_Manual/modulation_0.py}}
```

### 変調データサイズ

変調データサイズは以下のように取得する.

```rust,edition2021
{{#include ../../codes/Users_Manual/modulation_1.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/modulation_1.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/modulation_1.cs}}
```

```python
{{#include ../../codes/Users_Manual/modulation_1.py}}
```

### LoopBehavior

ループの挙動を`with_loop_behavior`で制御できる.
有限回ループするか, 無限ループするかを指定できる.

デフォルトは無限ループである.

```rust,edition2021
{{#include ../../codes/Users_Manual/modulation_loop.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/modulation_loop.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/modulation_loop.cs}}
```

```python
{{#include ../../codes/Users_Manual/modulation_loop.py}}
```

無限ループの場合, どのインデックスデータから再生されるかは制御できない.
有限回ループの場合, 0番目のデータから再生が始まり, 指定回数のループの後, 最終インデックスデータが出力され続ける.

**この設定は, Segmentを切り替えたときにしか効果がない. 詳しくは[Segment](./segment.md)を参照.**
