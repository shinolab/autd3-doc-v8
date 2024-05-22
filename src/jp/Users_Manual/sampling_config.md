# サンプリング設定について

Modulation, FocusSTM/GainSTMのサンプリング設定について説明する.

サンプリング周波数は$\clkf/N$で, $N$は$512$以上の32-bit符号なし整数である.

また, Silencerの設定によって指定できるサンプリング周波数の最大値が決まる.
詳しくは[Silencer](./silencer.md#fixed-completion-steps-mode)を参照.

## サンプリング周波数の設定

```rust,edition2021
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_freq.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_freq.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_freq.cs}}
```

```python
{{#include ../../codes/Users_Manual/sampling_config/sampling_config_freq.py}}
```

## サンプリング周波数分周比$N$の設定

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

データはファームウェア内部において超音波周期でリサンプリングされるため, 正しくデータを出力するためにはサンプリング周波数は超音波周波数を割り切れる必要がある.
すなわち, $N$は$512$の倍数である必要がある.
上記2つの設定では, この条件を満たさない場合はエラーになる.

非整数倍のアップサンプリングが許容できる場合は, 以下のようにする.

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

