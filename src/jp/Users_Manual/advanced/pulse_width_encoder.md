# PulseWidthEncoder

PWM信号のDuty比と超音波出力の間には非線形な関係がある. 
この関係を補正するために, `PulseWidthEncoder`を使用できる.

ファームウェア内部には, Gain/FociSTM/GainSTMの振幅データ ($0$--$255$) とModulationの振幅データ ($0$--$255$) をかけ合わせた強度データ ($0$--$65025$) をインデックスにして, PWM信号のパルス幅 ($0$--$256$) を決定するテーブルがある.
`PulseWidthEncoder`によってこのテーブルを変更できる.

```rust,edition2021
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.cs}}
```

```python
{{#include ../../../codes/Users_Manual/advanced/pulse_width_encoder.py}}
```

指定するテーブルのサイズは$65536$, パルス幅の値は$0$以上$256$で広義単調増加 (非減少) である必要がある.

デフォルトでは,
$$
    \text{table}[i] = \begin{cases}
        \left[\sin^{-1}\left(\frac{i}{65025}\right) \times \frac{512}{\pi}\right] & (i \le 65025) \\
        256 & (\text{otherwise})
               \end{cases}
$$
となるテーブルが書き込まれている[^1]. ここで$[\cdot]$は最も近い整数を表す.

なお, 例えば$a\times b = 257, a,b \in [0,1, ..., 255]$となるような$a,b$の組み合わせは存在しないが, Silencerの補完によって強度がこの値になる可能性があるので, 必ずすべての強度データに対応するパルス幅を設定すること.

[^1]: 実際には, インデックスが$65025$を超える場合の値は使用されない.
