# Silencer

AUTD3には出力を静音化するためのSilencerが用意されている.
Silencerは, 振動子の駆動信号の急激な変動を抑制し, 静音化する.

[[_TOC_]]

## 理論

詳細は鈴木らの論文[^suzuki2020]を参照されたい.

大まかに概要を述べると, 

* 振幅変調された超音波は可聴音を生じる
* 超音波振動子を駆動する際に, 位相変化が振幅変動を引き起こす
    * したがって, 可聴音の騒音が生じる
* 位相変化を線形に補間し, 段階的に変化させることで振幅変動を抑えられる
    * したがって, 騒音を低減できる
* 補間を細かくやると, その分だけ騒音を小さくできる

となる.

## Silencerの設定

Silencerの設定には`ConfigureSilencer`を送信する.

Silencerはデフォルトで適当な値に設定されている.
Silencerを無効化する場合は, `disable`を送信する.

```rust,edition2021
{{#include ../../codes/Users_Manual/silencer_0.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/silencer_0.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/silencer_0.cs}}
```

```python
{{#include ../../codes/Users_Manual/silencer_0.py}}
```

より細く設定する場合は, 以下2つのモードから選択する必要がある.

- [位相/振幅変化速度がすべての振動子で同一のモード (Fixed update rate mode)](#fixed-update-rate-mode)
- [位相/振幅変化が完了するまで時間がすべての振動子で同一のモード (Fixed completion steps mode)](#fixed-completion-steps-mode)

なお, デフォルトではFixed completion steps modeに設定されている.

### Fixed update rate mode

#### Fixed update rate modeにおける位相の変化

Silencerは位相$P$の変化を線形補間し, 段階的にすることで静音化を行う.
即ち, 位相$P$の時系列データを(単純)移動平均フィルタに通しているのにほとんど等しい.
ただし, 位相データが周期的であるという事を考慮している点で異なる.

例えば, 超音波の周期$T$が$T=12$の場合を考える. 即ち, $P=0$が$0\,\mathrm{rad}$, $P=12$が$2\pi\,\mathrm{rad}$に対応する. 
ここで, 時刻$t_s$で, 位相が$P=2$から$P=6$に変化したとする.
この時, Silencerによる位相変化は以下の図のようになる.

<figure>
  <img src="../fig/Users_Manual/silent/phase.svg"/>
<figcaption>位相$P$の変化</figcaption>
</figure>

一方, 時刻$t_s$で, 位相が$P=2$から$P=10$に変化したとする.
この時のSilencerによる位相変化は以下の図のようになる.
これは, $P=10$よりも, $P=-2$のほうが近いためである.

<figure>
  <img src="../fig/Users_Manual/silent/phase2.svg"/>
<figcaption>位相$P$の変化 (位相変化量が$\pi$より大きい場合)</figcaption>
</figure>

つまり, Silencerは現在の$P$と目標値$P_r$に対して
$$
    P \leftarrow \begin{cases}
        P + \mathrm{sign}(P_r - P) \min (|P_r - P|, \Delta) & \text{if } |P_r - P| \le T/2\\
        P - \mathrm{sign}(P_r - P) \min (|P_r - P|, \Delta) & \text{(otherwise)}\\
    \end{cases},
$$
として位相$P$を更新する.
ここで, $\Delta$は1ステップ当たりの更新量 (`Silencer`の`step`) を表す.
なお, 更新周波数は$\ufreq$となっている.

$\Delta$が小さいほど, 位相変化はなだらかになり騒音が抑制される.

<figure>
  <img src="../fig/Users_Manual/silent/duty.svg"/>
<figcaption>$\Delta$による変化の違い</figcaption>
</figure>

この実装の都合上, 移動平均フィルタとは異なる挙動を示す場合がある.
一つは, 上に示した位相変化量が$\pi$より大きい場合であり, もう一つが, 途中でもう一度位相が変化する場合である.
この時の位相変化の例を以下に示す.
元時系列に対する忠実度という観点では移動平均フィルタが正しいが, 位相変化量が$\pi$より大きい場合を考慮したり, $\Delta$を可変にする (即ち, フィルタ長を可変にする) のが大変なため現在のような実装となっている.

<figure>
  <img src="../fig/Users_Manual/silent/mean.svg"/>
<figcaption>移動平均フィルタとの比較</figcaption>
</figure>

#### Fixed update rate modeにおける振幅の変化

振幅変動が騒音を引き起こすので, 振幅パラメータ$D$も同等のフィルタをかけることでAMによる騒音を抑制できる.

振幅パラメータ$D$は位相とは異なり周期的ではないので, 現在の$D$と目標値$D_r$に対して
$$
    D \leftarrow D + \mathrm{sign}(D_r - D) \min (|D_r - D|, \Delta),
$$
のように更新する.

#### Fixed update rate modeの設定

Fixed update rate modeを設定するには, 以下のようにする.
引数はそれぞれ, 上述の$\Delta$に対応する.
なお, 内部では, Silencerは
- 位相は$\SI{8}{bit}$の値に$256$をかけたもの
- 振幅は変調データとかけ合わされたもの

に対して適用される.

```rust,edition2021
{{#include ../../codes/Users_Manual/silencer_fixed_update_rate.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/silencer_fixed_update_rate.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/silencer_fixed_update_rate.cs}}
```

```python
{{#include ../../codes/Users_Manual/silencer_fixed_update_rate.py}}
```

### Fixed completion steps mode

このモードでは, 位相/振幅変化が一定の時間で完了するようになる.

#### Fixed completion steps modeの設定

Fixed completion steps modeを設定するには, 以下のようにする.
なお, 引数はそれぞれ, 振幅/位相変化の完了までのステップ数に対応する.
1ステップの時間間隔は$\SI{25}{us}$である.

```rust,edition2021
{{#include ../../codes/Users_Manual/silencer_fixed_completion_steps.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/silencer_fixed_completion_steps.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/silencer_fixed_completion_steps.cs}}
```

```python
{{#include ../../codes/Users_Manual/silencer_fixed_completion_steps.py}}
```

デフォルト値は, 位相変化が$40$ステップ, 振幅変化が$10$ステップである.
なお, Silencerの無効化は, 位相/振幅変化が$1$ステップと等価である.

なお, このモードでは, `Modulation`や`FocusSTM`, `GainSTM`の位相/振幅がSilencerに指定した時間で完了できない場合にエラーが返される.
すなわち, 以下の条件が満たされる必要がある.
- Silencerの振幅変化完了ステップ $\times \SI{25}{us} \le$ `Modulation`のサンプリング周期
- Silencerの振幅変化完了ステップ $\times \SI{25}{us} \le$ `FocusSTM`/`GainSTM`のサンプリング周期
- Silencerの位相変化完了ステップ $\times \SI{25}{us} \le$ `FocusSTM`/`GainSTM`のサンプリング周期

`strict_mode`を無効にすれば, この条件を満たさない場合でもエラーを返さないようになるが, 推奨はされない.

```rust,edition2021
{{#include ../../codes/Users_Manual/silencer_fixed_completion_steps_with_strict.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/silencer_fixed_completion_steps_with_strict.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/silencer_fixed_completion_steps_with_strict.cs}}
```

```python
{{#include ../../codes/Users_Manual/silencer_fixed_completion_steps_with_strict.py}}
```

[^suzuki2020]: Suzuki, Shun, et al. "Reducing amplitude fluctuation by gradual phase shift in midair ultrasound haptics." IEEE transactions on haptics 13.1 (2020): 87-93.
