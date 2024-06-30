# Modulation

`Modulation`はAM変調を制御するための仕組みである.

Modulationは音圧振幅に掛け合わされる.
例えば, $\SI{1}{kHz}$の`Sine`変調を印加した場合の音圧振幅は以下のようになり, 音圧振幅の正の部分 (或いは, 負の部分) の包絡線が$\SI{1}{kHz}$のsin波に従う.

<figure>
  <img src="../fig/Users_Manual/sine_1k_mod.png"/>
</figure>

なお, 現在, `Modulation`には以下の制約がある.

* バッファサイズは最大で32768
  * 拡張モードを使用すると65536
* サンプリングレートは$\clkf/N$である. ここで, $N$は$\SI{32}{bit}$符号なし整数であり, $512$の倍数である必要がある.

SDKにはデフォルトでいくつかの種類のAMを生成するための`Modulation`が用意されている.

* [Static](./modulation/static.md) - 変調なし
* [Sine](./modulation/sine.md) - 正弦波
  * [Fourier](./modulation/fourier.md) - 正弦波の重ね合わせ
  * [Mixer](./modulation/mixer.md) - 正弦波の掛け合わせ
* [Square](./modulation/square.md) - 矩形波
* [Wav](./modulation/wav.md) - Wavファイルをもとにした変調
* [Csv](./modulation/csv.md) - Csvファイルをもとにした変調
* [RawPCM](./modulation/rawpcm.md) - RawPCMデータをもとにした変調
* [Custom](./modulation/custom.md) - ユーザー定義の変調
* [Cache](./modulation/cache.md) - 他の`Modulation`の計算結果をキャッシュする
* [RadiationPressure](./modulation/radiation.md) - 放射圧に対して変調を適用する
* [Transform](./modulation/transform.md) - 他の`Modulation`の計算結果に何らかの後処理を加える

## Modulationの共通API

### Sampling設定

一部の`Modulation`は`with_sampling_config`でサンプリング周波数を設定できる.

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

サンプリング設定についての詳細は[サンプリング設定について](./sampling_config.md)を参照されたい.

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

**ループ設定は, Segmentを切り替えたときにしか効果がない. 詳しくは[Segment](./segment.md)を参照.**
