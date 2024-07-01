# Cache

`with_cache`によって`Gain`の計算結果をキャッシュする`Gain`を生成できる.

```rust,edition2021
{{#include ../../../codes/Users_Manual/gain/cache_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/gain/cache_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/gain/cache_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/gain/cache_0.py}}
```

> NOTE: 当然ながら, `Cache`は計算処理が重い`Gain`に対してのみ有効なため, 実際には`Null`をキャッシュする意味はない. 使用時は必ずベンチマークを取ること.
