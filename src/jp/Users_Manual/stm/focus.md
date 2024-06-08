# FociSTM

- 最大サンプリング点数は$8192$.
  - 拡張モードの場合は$16384$
- サンプリングレートは$\clkf/N$で, $N$は32-bit符号なし整数であり, $512$以上の値である必要がある

`FociSTM`の使用方法は以下のようになる.
これは, アレイの中心から直上$\SI{150}{mm}$の点を中心とした半径$\SI{30}{mm}$の円周上で焦点を回すサンプルである.
円周上を200点サンプリングし, 一周を$\SI{1}{Hz}$で回るようにしている. (すなわち, サンプリング周波数は$\SI{200}{Hz}$である.)

```rust,edition2021
{{#include ../../../codes/Users_Manual/stm/focus_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/stm/focus_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/stm/focus_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/stm/focus_0.py}}
```

`FocusSTM`のコンストラクタにはSTM周波数を指定する.

なお, サンプリング点数とサンプリング周期に関する制約によって, 指定した周波数で出力できない可能性がある.
例えば, 上記の例は200点を$\SI{1}{Hz}$で回すため, サンプリング周波数は$\SI{200}{Hz}=\clkf/102400$とすれば良い.
しかし, 例えば`point_num=199`にすると, サンプリング周波数を$\SI{199}{Hz}$にしなければならないが, $\SI{199}{Hz}=\clkf/N$を満たすような整数$N$は存在せずエラーになる.

`from_freq_nearest`を使用すると, 最も近い$N$が選択されるようになるが, 指定した周波数と実際の周波数がずれるため注意が必要である.

## サンプリング設定の指定

周波数ではなく, サンプリング周波数を指定することもできる.

```rust,edition2021
{{#include ../../../codes/Users_Manual/stm/focus_1.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/stm/focus_1.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/stm/focus_1.cs}}
```

```python
{{#include ../../../codes/Users_Manual/stm/focus_1.py}}
```

サンプリング設定についての詳細は[サンプリング設定について](./../sampling_config.md)を参照されたい.
