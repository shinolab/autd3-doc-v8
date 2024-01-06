# フェーズドアレイについて

Author: Shun Suzuki

Date: 2024-01-06

- - -

ここでは, 多数の球面波音源が生成する音場について考察する.

## フェーズドアレイから放射される音場

位置$\br^\prime$にある振動子が$\br$生成する音圧場$p(\br)$は次の式で与えられる (球面波モデル).
$$\begin{align}
  p(\br) = \frac{a}{\|\br-\br^\prime\|}\rme^{\im k\|\br-\br^\prime\|}\rme^{-\im\omega t}\rme^{\im \phi}.
\end{align}$$
ここで, $a, \phi$はそれぞれ振動子の振幅, 位相パラメータであり,
$k$は波数, $\omega$は角周波数, $t$は時間である[^1].

ここで, 次の2つの関数を導入する.
$$\begin{aligned}
  g(\br, \br^\prime) & = \frac{1}{\|\br-\br^\prime\|}\rme^{\im k\|\br-\br^\prime\|}, \\
  q(a, \phi)         & = a\rme^{\im \phi}.
\end{aligned}$$
この$g$を伝達関数, $q$を振動子のゲインと呼ぶことにする.
$g$は振動子の物理的な配置で決まるのに対して,
$q$は振動子に印加する駆動信号によってプログラマブルに変更できる.

ここで, 複数の振動子からなるアレイを考える.
各振動子を添字$i$で区別することにすると, これらの振動子が生成する音場は,
全ての振動子の音場の重ね合わせになり,
$$\begin{aligned}
  p(\br) = \sum_i g(\br, \br_i)q(a_i, \phi_i) \rme^{-\im\omega t},
\end{aligned}$$
と表される[^2].

## 格子状のアレイ

以下では, フェーズドアレイは平面に格子状に並べられた振動子から構成されると仮定する.
> NOTE: 実際には, 格子状である必然性はない. 
> 例えば, [^marzo2017realization]では曲面状に振動子を配置しているし, [^marzo2017ultraino]ではさまざまな形状のアレイを生成できるようにしている.
> さらに変わったところだと, [^price2018fibonacci]ではアレイの配置をFibonacci spiralに沿って配置している.
> この論文では, Fibonacci spiral配置によりグレーティングローブ (後述) が軽減されると報告している.
> しかし, ここでは簡単のため平面上の格子配列を考える.

このとき, 振動子は間隔$d$で縦横それぞれ$N, M$個並べられているとしよう.
このとき, $p(\br)$は
$$\begin{aligned}
  p(\br) & = \sum_{n=0}^{N-1}\sum_{m=0}^{M-1} g(\br, \br_{m,n})q(a_{m,n}, \phi_{m,n}) \rme^{-\im\omega t},
\end{aligned}$$
である.
ここで, ${}_{m,n}$は$n$行$m$列の振動子を表す.

### 焦点の生成

ある, 位置$\br_f = (x_f, y_f, z_f)$に焦点を生成したいとする. つまり,
$p(\br_f)$を最大化しようとしたときに振動子に与えるべきゲインは明らかに
$$\begin{aligned}
  a_{m,n}    & = a_\text{max}              \\
  \phi_{m,n} & = -k\| \br_f - \br_{m,n} \|
\end{aligned}$$ となる. ここで, $a_\text{max}$は振動子の上限振幅である.

このときに, 焦点付近の音場がどうなるか考察しよう.
解析を簡単にするために, いくつかの近似を導入する.
まず, $0$行$0$列の振動子が$(0,0,0)$に置かれているとすると, 
$$\begin{aligned}
  \br_{n,m} = (md, nd, 0)
\end{aligned}$$
となる.
そのため, $$\begin{aligned}
  \|\br - \br_{m,n}\| & = \sqrt{(x-md)^2 + (y-nd)^2 + z^2}                                                             \\
                      & = z \left( \frac{(x-md)^2}{z^2} + \frac{(y-nd)^2}{z^2} + 1\right)^\frac{1}{2}                  \\
                      & = z \left( 1+  \frac{1}{2}\frac{(x-md)^2}{z^2} + \frac{1}{2}\frac{(y-nd)^2}{z^2}+\cdots\right)
\end{aligned}$$
となる.
ここで十分遠方を考え, $|x-md|, |y-nd| \ll z$が成り立つとしよう.
このとき, $$\begin{aligned}
  \|\br - \br_{m,n}\| & \sim z \left( 1+  \frac{1}{2}\frac{(x-md)^2}{z^2} + \frac{1}{2}\frac{(y-nd)^2}{z^2}\right) \\
                      & = z + \frac{1}{2}\frac{(x-md)^2}{z} + \frac{1}{2}\frac{(y-nd)^2}{z}                        \\
                      & = z + \frac{x^2+y^2}{2z} - \frac{xmd + ynd}{z} + \frac{(md)^2 + (nd)^2}{2z}
\end{aligned}$$
となる.
この近似をFresnel近似と呼ぶ. 
同様に, $|x_f-md|, |y_f-nd|\ll z_f$が成り立つならば
$$\begin{aligned}
  \|\br_f - \br_{m,n}\| & \sim z_f + \frac{x_f^2+y_f^2}{2z_f} - \frac{x_fmd + y_fnd}{z_f} + \frac{(md)^2 + (nd)^2}{2z_f}
\end{aligned}$$
となる.
この近似をFraunhofer近似と呼ぶ.
さらに, ここで次の近似を導入する.
$$\begin{aligned}
  \frac{1}{\|\br - \br_{m,n}\|} \sim \frac{1}{z}.
\end{aligned}$$
この近似を近軸近似と呼ぶ.

これらの近似を用いると, $$\begin{aligned}
  p(\br) & = \sum_{n=0}^{N-1}\sum_{m=0}^{M-1} \frac{a_\text{max}}{z}\rme^{\im k\|\br-\br_{m,n}\|}\rme^{-\im k\|\br_f-\br_{m,n}\|} \rme^{-\im\omega t}                                                       \\
         & \sim \frac{a_\text{max}}{z}\sum_{n=0}^{N-1}\sum_{m=0}^{M-1} \exp\left[\im k\left(z + \frac{x^2+y^2}{2z} - \frac{xmd + ynd}{z} + \frac{(md)^2 + (nd)^2}{2z}\right)\right]                \\
         & \quad\quad\times \exp\left[-\im k\left(z_f + \frac{x_f^2+y_f^2}{2z_f} - \frac{x_fmd + y_fnd}{z_f} + \frac{(md)^2 + (nd)^2}{2z_f}\right)\right] \rme^{-\im\omega t},                              \\
         & = \frac{a_\text{max}}{z}\rme^{\im\phi_0}\sum_{m=0}^{M-1} \exp\left[\im kmd\left(\frac{x_f}{z_f}-\frac{x}{z}\right) + \im k(md)^2\left(\frac{1}{2z}-\frac{1}{2z_f}\right)\right]\\
         & \quad\quad\times \sum_{n=0}^{N-1}\exp\left[\im knd\left(\frac{y_f}{z_f}-\frac{y}{z}\right) + \im k(nd)^2\left(\frac{1}{2z}-\frac{1}{2z_f}\right)\right] \rme^{-\im\omega t},\\
  \phi_0 & = kz - kz_f + k\frac{x^2+y^2}{2z} - k\frac{x_f^2+y_f^2}{2z_f},
\end{aligned}$$
となる.

ここで, 焦点を通り, アレイに平行な平面, すなわち$z=z_f$の場合を考えよう.
このとき, $$\begin{aligned}
  p(\left.\br\right|_{z=z_f}) & \sim \frac{a_\text{max}}{z_f} \rme^{\im\phi_0}\sum_{m=0}^{M-1} \exp\left[\im k\frac{md}{z_f}(x_f-x)\right]\sum_{n=0}^{N-1} \exp\left[\im k\frac{nd}{z_f}(y_f-y)\right] \rme^{-\im\omega t},
\end{aligned}$$
となる.

さてここで, $$\begin{aligned}
  \sum_{n=0}^{N-1} \exp\left(\im rn \right) = \frac{1-\exp(\im rN)}{1-\exp(\im r)}
\end{aligned}$$
であり, $$\begin{aligned}
  1-\exp(\im r) & = \exp\left(\im \frac{r}{2}\right) \left[\exp\left(-\im \frac{r}{2}\right)-\exp\left(\im \frac{r}{2}\right)\right] \\
                & = -2\im \sin \left(\frac{r}{2}\right) \exp\left(\im \frac{r}{2}\right)
\end{aligned}$$
であるから
$$\begin{aligned}
  \sum_{n=0}^{N-1} \exp\left(\im rn \right) = N \frac{\sinc\left(\frac{rN}{2}\right) }{\sinc\left(\frac{r}{2}\right)}\exp\left(\im (N-1) \frac{r}{2}\right)
\end{aligned}$$
と表される.
ここで, 
$$\begin{aligned}
  \sinc(x) = \begin{cases}
                \frac{\sin(x)}{x} & (x \ne 0) \\
                1 & (x = 0)
             \end{cases} 
\end{aligned}$$
である.

したがって, $$\begin{aligned}
  \left| p(\left.\br\right|_{z=z_f}) \right| & \sim \frac{a_\text{max}}{z_f} MN \frac{\left| \sinc\left(\frac{kMd}{2z_f}(x_f-x)\right) \right|}{\left| \sinc\left(\frac{kd}{2z_f}(x_f-x)\right) \right|}\frac{\left| \sinc\left(\frac{kNd}{2z_f}(y_f-y)\right) \right|}{\left| \sinc\left(\frac{kd}{2z_f}(y_f-y)\right) \right|}
\end{aligned}$$
となる.

ここで, sinc関数の挙動を確認しておこう.
以下に$\sinc(x)$のグラフを載せる.

<figure>
  <img src="../fig/theory/phasedarray/sinc.jpg"/>
</figure>

図からわかるように$x=\pm \pi, \pm 2\pi, \pm 3\pi,...$で$\sinc(x)=0$になる.

また, 以下に$\sinc(nx)/\sinc(x)$のグラフを載せる.

<figure>
  <img src="../fig/theory/phasedarray/sinc_i.jpg"/>
</figure>

図からわかるように,
$x=0, \pm \pi, \pm 2\pi, \pm 3\pi,...$でその絶対値が最大値の$1$をとることがわかる.

したがって, $\left| p \right|$はまず, $x=x_f, y=y_f$で最大値をとる.
その後, $x$軸方向には,
$$\begin{aligned}
  \frac{kMd}{2z_f}(x_f-x) = \pm \pi \\
  \therefore x = x_f \pm \frac{2\pi}{kMd}z_f,
\end{aligned}$$
で$\left| p \right| = 0$になる. 
同様に, $y$軸方向には
$$\begin{aligned}
  y = y_f \pm \frac{2\pi}{kNd}z_f,
\end{aligned}$$
で$\left| p \right| = 0$になる. 
従って, x,y軸方向の焦点の幅$W_x, W_y$はそれぞれ,
$$\begin{aligned}
  W_x &= \frac{4\pi}{kMd}z_f = 2\lambda \frac{z_f}{Md}, \\
  W_y &= \frac{4\pi}{kNd}z_f = 2\lambda \frac{z_f}{Nd}, \\
\end{aligned}$$
となる.
フェーズドアレイの幅が, x,y軸方向にそれぞれ$Md, Nd$であることを考えると, **波長程度に焦点を収束できるのは$z_f$ (フェーズドアレイから焦点までの距離) がフェーズドアレイの幅程度までとなる.**

また, $|p|$は
$$\begin{aligned}
  x & = x_f \pm \frac{2\pi}{kd}z_f, x_f \pm 2\frac{2\pi}{kd}z_f,... \\
  y & = y_f \pm \frac{2\pi}{kd}z_f, y_f \pm 2\frac{2\pi}{kd}z_f,...
\end{aligned}$$
でも最大値をとる.
これがグレーティングローブと呼ばれるものである.

以下に$M=18, N=14, d = 10, k=2\pi/8.5, \br_f = (0,0,200)$の場合の焦点平面のx方向の音場を載せる.
図に見られるように, 焦点周りの音場は比較的精度よく近似されている.
しかし, グレーティングローブ周りの近似はかなりずれている事がわかる. 
これは, $|x-md| \ll z$, 及び近軸近似が成り立たないためである.

<figure>
<p>
<img src="../fig/theory/phasedarray/x_narrow_x200.jpg" />
<img src="../fig/theory/phasedarray/x_wide_x200.jpg" />
</p>
<figcaption>x軸方向の音場 ($z_f=200$).
焦点付近は比較的よく近似されるが, グレーティングローブ周りは近似の精度は低く, 位置も音圧もずれている.
</figcaption>
</figure>

[^1]: より現実に近いモデルとして, さらに振動子の指向性や空気の吸収による減衰などを入れたものがある.

[^2]: 音速の変化等はとりあえず考えない. また, あくまで線形の範囲に絞る.

[^marzo2017realization]: Marzo, Asier, et al. "Realization of compact tractor beams using acoustic delay-lines." Applied Physics Letters 110.1 (2017).

[^marzo2017ultraino]: Marzo, Asier, Tom Corkett, and Bruce W. Drinkwater. "Ultraino: An open phased-array system for narrowband airborne ultrasound transmission." IEEE transactions on ultrasonics, ferroelectrics, and frequency control 65.1 (2017): 102-111.

[^price2018fibonacci]: Price, Adam, and Benjamin Long. "Fibonacci spiral arranged ultrasound phased array for mid-air haptics." 2018 IEEE International Ultrasonics Symposium (IUS). IEEE, 2018.
