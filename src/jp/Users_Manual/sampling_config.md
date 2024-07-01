# サンプリング設定について

Modulation, FociSTM/GainSTMのサンプリング設定について説明する.

サンプリング周波数は$\clkf/N$で, $N$は$512$以上の32-bit符号なし整数である.

また, Silencerの設定によって指定できるサンプリング周波数の最大値が決まる.
詳しくは[Silencer](./silencer.md#fixed-completion-steps-mode)を参照.

## サンプリング周波数/周期の設定

サンプリング周波数, または, サンプリング周期を設定する場合は, 周波数, 周期をそのまま指定すれば良い.

```rust,edition2021
{{#include ../../codes/Users_Manual/sampling_config/modulation_0.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/sampling_config/modulation_0.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/sampling_config/modulation_0.cs}}
```

```python
{{#include ../../codes/Users_Manual/sampling_config/modulation_0.py}}
```

## サンプリング周波数分周比の設定

サンプリング周波数分周比$N$を設定する場合は以下のようにする.

```rust,edition2021
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_div.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_div.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_div.cs}}
```

```python
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_div.py}}
```

## サンプリング周波数制限の緩和

データはファームウェア内部において超音波周期でリサンプリングされるため, 正しくデータを出力するためにはサンプリング周波数は超音波周波数を割り切れる必要がある.
すなわち, $N$は$512$の倍数である必要がある.
上記の方法では, この条件を満たさない場合はエラーになる.

非整数倍のアップサンプリングが許容できる場合は, 以下を使用する.

```rust,edition2021
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_div_raw.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_div_raw.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_div_raw.cs}}
```

```python
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_div_raw.py}}
```

**使用は推奨されないが**, 周波数, 周期で指定することもできる.
この場合, サンプリング設定は可能なものの内で最も近いものになる.

```rust,edition2021
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.cs}}
```

```python
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_freq_nearest.py}}
```
