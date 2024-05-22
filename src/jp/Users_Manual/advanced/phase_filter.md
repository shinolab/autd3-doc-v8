# PhaseFilter

`PhaseFilter`により, 固定の位相オフセットを指定できる.
ここで指定した位相は, `Gain`, `GainSTM`, `FocusSTM`の位相データに加算される.

```rust,edition2021
{{#include ../../../codes/Users_Manual/advanced/phase_filter.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/advanced/phase_filter.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/advanced/phase_filter.cs}}
```

```python
{{#include ../../../codes/Users_Manual/advanced/phase_filter.py}}
```

`PhaseFilter`コンストラクタの引数は`Fn(&Device) -> Fn(&Transducer) -> Phase`である.
