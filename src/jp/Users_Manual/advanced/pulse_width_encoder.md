# PulseWidthEncoder

PWM信号のDuty比と超音波出力の間には非線形な関係がある. 
この関係を補正するために, `PulseWidthEncoder`を使用できる.

ファームウェア内部には, Gain/FociSTM/GainSTMの振幅データ ($0$--$255$) とModulationの振幅データ ($0$--$255$) をかけ合わせた強度データを2で割ったもの ($0$--$32512$) をインデックスにして, PWM信号のパルス幅 ($0$--$256$) を決定するテーブルがある.
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

コンストラクタの引数は各デバイスに対して, テーブルのインデックスを引数にパルス幅を返す関数を返す関数`Fn(&Device) -> Fn(u16) -> u16`である.

テーブルのサイズは$32768$であり, パルス幅の値は$0$以上$256$以下で広義単調増加 (非減少) である必要がある.

デフォルトでは,
$$
    \text{table}[i] = \begin{cases}
        \left[\sin^{-1}\left(\frac{i}{32512}\right) \times \frac{512}{\pi}\right] & (i \le 32512) \\
        256 & (\text{otherwise})
               \end{cases}
$$
となるテーブルが書き込まれている[^1]. ここで$[\cdot]$は最も近い整数を表す.

なお, 例えば$\frac{a\times b}{2} = 257, a,b \in [0,1, ..., 255]$となるような$a,b$の組み合わせは存在しないが, Silencerの補完によって強度がこの値になる可能性があるので, 必ずすべての強度データに対応するパルス幅を設定すること.

[^1]: 実際には, $32512$を超えるインデックスの値は使用されない.
