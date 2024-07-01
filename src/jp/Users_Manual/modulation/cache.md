# Cache

`with_cache`で計算結果をキャッシュしておくための`Modulation`を生成できる.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/cache_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/cache_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/cache_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/cache_0.py}}
```

> NOTE: ほとんどの`Modulation`に対して, キャッシュするより都度計算し直したほうが速い. 使用時は必ずベンチマークを取ること.
