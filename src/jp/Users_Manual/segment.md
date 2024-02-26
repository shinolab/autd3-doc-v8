# Segment

`Modulation`, `Gain`, `FocusSTM`, `GainSTM`のデータ領域にはそれぞれ, `Segment`が2つ用意されている.

特に指定しない限りは, `Segment::S0`が使用される.

データを書き込む`Segment`は, `with_segment`で指定する.

```rust,edition2021
{{#include ../../codes/Users_Manual/segment.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/segment.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/segment.cs}}
```

```python
{{#include ../../codes/Users_Manual/segment.py}}
```

第二引数は, データを書き込んだ後に`Segment`を切り替えるかどうかを指定する.

`Segment`を切り替えたいだけの場合は, `ChangeModulationSegment`, `ChangeGainSegment`, `ChangeFocusSTMSegment`, `ChangeGainSTMSegment`をそれぞれ送信する.

```rust,edition2021
{{#include ../../codes/Users_Manual/segment_change.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/segment_change.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/segment_change.cs}}
```

```python
{{#include ../../codes/Users_Manual/segment_change.py}}
```
