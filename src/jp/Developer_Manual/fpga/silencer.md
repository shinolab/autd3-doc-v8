# Silencer

<figure>
  <a href="../../fig/Developers_Manual/FPGA/silencer.svg" data-lightbox="image"><img src="../../fig/Developers_Manual/FPGA/silencer.svg"/></a>
  <figcaption>Silencerモジュール</figcaption>
</figure>

| Name                          | In/Out | Width | Description                                        | 
| ----------------------------- | ------ | ----- | -------------------------------------------------- | 
| CLK                           | In     | 1     | 20.48MHzクロック                                   | 
| SETTINGS                      | In     | -     |                                                    | 
| ├─ MODE                       | In     | 1     | モード                                             | 
| ├─ UPDATE_RATE_INTENSITY      | In     | 16    | 固定更新幅 (強度)                                  | 
| ├─ UPDATE_RATE_PHASE          | In     | 16    | 固定更新幅 (位相)                                  | 
| ├─ COMPLETION_STEPS_INTENSITY | In     | 16    | 固定完了ステップ (強度)                            | 
| └─ COMPLETION_STEPS_PHASE     | In     | 16    | 固定完了ステップ (位相)                            | 
| DIN_VALID                     | In     | 1     | 強度/位相データ有効フラグ                          | 
| INTENSITY_IN                  | In     | 16    | 強度                                               | 
| PHASE_IN                      | In     | 8     | 位相                                               | 
| INTENSITY_OUT                 | Out    | 16    | 強度                                               | 
| PHASE_OUT                     | Out    | 8     | 位相                                               | 
| DOUT_VALID                    | Out    | 1     | 強度/位相データ有効フラグ                          | 

このモジュールは, 強度/位相データの急激な変化を抑え, 静音化するためのモジュールである.

強度データ$D$に対しては, 現在の値$D_c$と, 目標値$D_t$に対して, 以下のように更新する.
$$
    D_c \leftarrow D_c + \mathrm{sign}(D_t - D_c) \min (|D_t - D_c|, \Delta_I).
$$
また, 位相データ$P$に対しては, 現在の値$P_c$と, 目標値$P_t$に対して, 以下のように更新する.
$$
    P_c \leftarrow \begin{cases}
        P_c + \mathrm{sign}(P_t - P_c) \min (|P_t - P_c|, \Delta_P) & (|P_t - P_c| \le T/2)\\
        P_c - \mathrm{sign}(P_t - P_c) \min (|P_t - P_c|, \Delta_P) & (\text{otherwise})\\
    \end{cases}.
$$
ここで, $\Delta_I,\Delta_P$はそれぞれ強度, 位相に対する1ステップ当たりの更新量, $T$は超音波周期である.
なお, 更新は$\ufreq$の周波数で行われる.

> NOTE: 位相データの場合分けは, 位相の周期性によるものである. 位相変化が半周期より大きい場合は, 逆方向に変化したほうが早く変化が完了する.

$\Delta$の決定方法に2つのモードがある. 
1. 固定更新幅モード: すべての振動子に対して, 強度, 位相それぞれ固定の$\Delta_I=$`UPDATE_RATE_INTENSITY`, $\Delta_P=$`UPDATE_RATE_PHASE`を用いる.
1. 固定完了ステップモード: すべての振動子に対して同一のステップで変化が完了するように$\Delta$を決定する. すなわち, 強度, 位相のステップ数$S_I=$`COMPLETION_STEPS_INTENSITY`, $S_P=$`COMPLETION_STEPS_PHASE`に対して,
    $$\begin{align}
        \Delta_I = \frac{|D_t - D_c|}{S_I}, \quad \Delta_P = \frac{|P_t - P_c|}{S_P},
    \end{align}$$
    を, 目標値が変化したタイミングでここの振動子に対して設定する.

これらのモードは`MODE`にて切り替える.

このモジュール内部では, 位相データは$256$倍されている.
これは, 強度データと位相データのスケールを揃えるためである.

> NOTE: 強度データの最大値は$255\times 255$なので, 若干異なるが, 面倒なので$256$倍にしている.

このモジュールの処理もパイプライン的に行われる.
入力として, `DIN_VALID`は249クロックの間1であり, その間`INTENSITY_IN`, `PHASE_IN`から強度/位相データが順番に流れてくることを想定している.
処理が終わったら, `DOUT_VALID`を1とし, 順次`INTENSITY_OUT`, `PHASE_OUT`から強度/位相データを流す.

## Step Calculator

このサブモジュールは, 式(1)により$\Delta$を計算する.

ただし, 整数を用いるため, 余りの処理が問題になる.
これに関しては, 例えば強度の場合, $S_I$ステップの内, 最初の$|D_t - D_c|\,\%\,S_I$ステップにおいては$\lfloor|D_t - D_c|/S_I\rfloor+1$, それ以降では$\lfloor|D_t - D_c|/S_I\rfloor$を$\Delta_I$として使用することで対処している. 位相も同様である.

なお, 固定更新幅モードの場合は, このサブモジュールの出力は使用されない.

## Interpolator

このサブモジュールは, 現在の強度/位相データに対して, 更新量$\Delta$を加算しているだけである.
ただし, 位相に関しては前述の通り, 目標値と現在地との差の大きさに応じて加算するか減算するかを決定している.
