# DebugSettings

`DebugSettings`により, GPIOピンの出力を各デバイス・ピン毎に設定できる.

<figure>
    <img src="../../fig/Users_Manual/gpio_pin.jpg"/>
    <figcaption>GPIOピン</figcaption>
</figure>

```rust,edition2021
{{#include ../../../codes/Users_Manual/advanced/debug_setting.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/advanced/debug_setting.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/advanced/debug_setting.cs}}
```

```python
{{#include ../../../codes/Users_Manual/advanced/debug_setting.py}}
```

出力可能なデータは以下の通り.
- `None`: 出力しない
- `BaseSignal`: 基準信号 (超音波と同じ周波数のDuty比50%矩形波)
- `Thermo`: 温度センサーがアサートされているかどうか
- `ForceFan`: ForceFanフラグがアサートされているかどうか
- `Sync`: EtherCAT同期信号
- `ModSegment`: Modulationのセグメント
- `ModIdx(u16)`: Modulationのインデックスが指定した値のときにHighになる
- `StmSegment`: STMのセグメント
- `StmIdx(u16)`: STMのインデックスが指定した値のときにHighになる
- `IsStmMode`: FociSTM/GainSTMが使用されているかどうか
- `PwmOut(&Transducer)`: 指定した振動子のPWM出力
- `Direct(bool)`: 指定した値を出力する
