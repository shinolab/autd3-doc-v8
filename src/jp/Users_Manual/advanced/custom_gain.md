# Gainの自作

> NOTE: 同様の目的で, [Custom](../gain/custom.md)を使用することもできる.

ライブラリでは自前の`Gain`を作成することができる.

ここでは, `Focus`と同じように単一焦点を生成する`FocalPoint`を実際に定義してみることにする.

```rust,edition2021
{{#include ../../../codes/Users_Manual/advanced/custom_gain_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/advanced/custom_gain_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/advanced/custom_gain_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/advanced/custom_gain_0.py}}
```

`send`関数は`Gain`型を継承したクラスを引数に取ることができる.
そのため, `Gain`型を継承をしておく.

`send`関数内部では`Geometry`を引数にした`calc`メソッドが呼ばれる.
`calc`の返り値は, `Fn(&Device) -> Fn(&Transducer) -> Drive`であり, この関数を元に振幅/位相データが送信される.
