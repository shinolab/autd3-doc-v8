# Custom

`Custom`はユーザーが自由に音場を生成するための`Gain`である.

```rust,edition2021
{{#include ../../../codes/Users_Manual/gain/custom_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/gain/custom_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/gain/custom_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/gain/custom_0.py}}
```

`Custom`コンストラクタの引数は`Fn(&Device) -> Fn(&Transducer) -> Drive`である.
