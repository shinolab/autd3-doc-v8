# PWM

<figure>
  <a href="../../fig/Developers_Manual/FPGA/pwm.svg" data-lightbox="image"><img src="../../fig/Developers_Manual/FPGA/pwm.svg"/></a>
  <figcaption>PWMモジュール</figcaption>
</figure>

| Name        | In/Out | Width | Description                                        | 
| ----------- | ------ | ----- | -------------------------------------------------- | 
| CLK         | In     | 1     | 20.48MHzクロック                                   | 
| TIME_CNT    | In     | 9     | 40kHz周期カウンタ                                  | 
| UPDATE      | In     | 1     | 40kHz周期トリガ                                    | 
| DIN_VALID   | In     | 1     | パルス幅/位相データ有効フラグ                      | 
| PULSE_WIDTH | In     | 9     | パルス幅                                           | 
| PHASE       | In     | 8     | 位相                                               | 
| PWM_OUT     | Out    | 1x249 | PWM信号                                            | 
| DOUT_VALID  | Out    | 1     | 立ち上がり/立ち下がりデータ有効フラグ (デバッグ用) | 

## Preconditioner

このサブモジュールでは, 後の処理を楽にするために, パルス幅$D$/位相$P$を信号の立ち上がり時刻$R$と立ち下がり時刻$F$に変換する.

$$\begin{align*}
R &= \left[(T-2P) - \frac{D}{2}\right] \%\, T\\
F &= \left[(T-2P) + \frac{D+1}{2}\right] \%\, T
\end{align*}$$

ここで, $T(=512)$は周期である.

> NOTE: $D+1$を計算しているのは, $D$が奇数の場合を考慮するためである.

なお, Preconditionerの計算はパイプライン的に行われる.
入力として, `DIN_VALID`は249クロックの間1であり, その間`PULSE_WIDTH`, `PHASE`からパルス幅/位相データが順番に流れてくることを想定している.
出力に関して, 中間データを出力しないようにするために, 一旦バッファに格納している.

## Buffer

Bufferは, `TIME_CNT`の値が$0$になるまで$R, F$の更新を遅らせる.
すなわち, 超音波周期の途中で$R, F$が更新されることを防ぐためにある.

> NOTE: Bufferの必要性には議論の余地がある. 周期の中間でデータが更新されることに問題はあるか?

## Generator

Generatorは`TIME_CNT`の値$t$とBufferから出力された$R, F$を用いて, PWMの出力$v$を計算する.

$$\begin{align}
    v = \begin{cases}
            (R \le t) \land (t < F) & (\text{If } R \le F) \\
            (t < F) \lor (R \le t)  & (\text{Otherwise})   \\
        \end{cases}
\end{align}$$
