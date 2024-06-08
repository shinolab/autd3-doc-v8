# Segment

`Modulation`, `Gain`, `FociSTM`, `GainSTM`のデータ領域にはそれぞれ, `Segment`が2つ用意されている.

特に指定しない限りは, `Segment::S0`が使用される.

データを書き込む`Segment`は, `with_segment`で指定する.

## Gain

```rust,edition2021
{{#include ../../codes/Users_Manual/segment/segment.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/segment/segment.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/segment/segment.cs}}
```

```python
{{#include ../../codes/Users_Manual/segment/segment.py}}
```

第二引数は, データを書き込んだ後に`Segment`を切り替えるかどうかを指定する.

### Segmentの切り替え

`Segment`を切り替えたいだけの場合は, `SwapSegment::gain`を使用する.

```rust,edition2021
{{#include ../../codes/Users_Manual/segment/segment_change.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/segment/segment_change.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/segment/segment_change.cs}}
```

```python
{{#include ../../codes/Users_Manual/segment/segment_change.py}}
```

## Modulation/GainSTM/FociSTM

```rust,edition2021
{{#include ../../codes/Users_Manual/segment/segment_transition.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/segment/segment_transition.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/segment/segment_transition.cs}}
```

```python
{{#include ../../codes/Users_Manual/segment/segment_transition.py}}
```

第2引数には`TransitionMode`を指定する.

- 遷移先セグメントが無限ループ時にのみ使用可能
    - `Immediate` : 直ちに切り替える
    - `Ext`       : 直ちに切り替え, 拡張モードにする (各`Segment`のデータを出力後, 自動で`Segment`を切り替えるモード)

- 遷移先セグメントが有限ループ時にのみ使用可能
    - `SyncIdx`               : 遷移先の`Segment`のデータインデックスが$0$になったときに切り替える
    - `SysTime(DcSysTime)`    : 指定した時刻になったときに切り替える
    - `GPIO(GPIOIn)`          : 指定したGPIOピンに信号が入力されたときに切り替える

データの書き込みのみを行い, `Segment`を切り替えたくない場合は`None`を指定する.

### Segmentの切り替え

`Segment`を切り替えたいだけの場合は, `SwapSegment::modulation,focus_stm,gain_stm`を使用する.

```rust,edition2021
{{#include ../../codes/Users_Manual/segment/segment_change_transition.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/segment/segment_change_transition.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/segment/segment_change_transition.cs}}
```

```python
{{#include ../../codes/Users_Manual/segment/segment_change_transition.py}}
```
