# Sine

音圧をSin波状に変形するための`Modulation`.

コンストラクタには周波数$f$を指定する.

デフォルトのサンプリング周波数分周比は$N=5120$である.
(超音波周波数が$\SI{40}{kHz}$の場合, サンプリング周波数は$\SI{4}{kHz}$.)

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/sine_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/sine_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/sine_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/sine_0.py}}
```

## 振幅とオフセットの指定

`Sine`は音圧の波形が
$$
    \frac{amplitude}{2} \times \sin(2\pi ft) + offset
$$
となるようなAMをかける.
ここで, $amplitude$と$offset$はそれぞれ, `with_intensity`と`with_offset`にて指定できる (デフォルトはそれぞれ`u8`の最大値とその半分).

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/sine_1.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/sine_1.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/sine_1.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/sine_1.py}}
```
