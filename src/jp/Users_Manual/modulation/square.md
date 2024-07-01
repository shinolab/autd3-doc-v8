# Square

矩形波状の`Modulation`.

コンストラクタには周波数$f$を指定する.

デフォルトのサンプリング周波数分周比は$N=5120$である.
(超音波周波数が$\SI{40}{kHz}$の場合, サンプリング周波数は$\SI{4}{kHz}$.)

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/square_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/square_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/square_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/square_0.py}}
```

## 振幅の指定

Low/Highレベルの振幅はそれぞれ, `with_low`, `with_high`で指定できる.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/square_1.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/square_1.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/square_1.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/square_1.py}}
```

## Duty比の指定

`with_duty`で矩形波のDuty比を指定できる.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/square_2.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/square_2.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/square_2.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/square_2.py}}
```

## 周波数制約

`Square`はデフォルトだと周波数に厳格であり, サンプリング周波数によって出力不可能な周波数が指定された場合にはエラーを返す.

その場合はサンプリング設定を変更するか, `from_freq_nearest`を使用することで, 出力可能な周波数の内で最も近い周波数で変調することができる.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/square_3.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/square_3.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/square_3.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/square_3.py}}
```
