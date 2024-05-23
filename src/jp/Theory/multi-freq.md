# 複数周波数の応用

Author: Shun Suzuki

Date: 2024-05-24

- - -

> 最新バージョンのAUTD3ファームウェア/ソフトウェアでは, デバイス・振動子単位での超音波周波数の変更は不可能になった.
> 以下はメモのために残している.

## 時空間変調

ここでは, 周波数のみ異なる2つのアレイが同じ位置に焦点を生成したときの焦点の音圧について考察する.

焦点付近の音場はほぼ,
アレイの中心から焦点までのベクトルに平行に進む平面波で近似できるとする.
すなわち, 焦点付近の音場$p(\br)$は
$$\begin{aligned}
  p(\br) \propto \rme^{\im \bk\cdot \br}\rme^{-\im \omega t}
\end{aligned}$$
のように書くことができる.

さて, 周波数の異なる2つのアレイがx軸に対して対称に置かれている, すなわち, アレイの中心が$(\pm X, 0, 0)$で, それぞれの周波数が$f_0 \pm \Delta f$であるとする.
このとき, $(0, 0, z_f)$に焦点を生成する場合を考えよう.

波数$k$と音速$c$の関係式は$k c = \omega = 2\pi f$なので,
それぞれのアレイの波数ベクトル$\bk$は$2\pi\frac{f_0 \pm \Delta f}{c}(\mp\cos \theta, 0, \sin \theta), \theta = \arctan z_f/X$となる,
振動子の音圧が周波数に依存しないとすると, 焦点近傍の音圧は
$$\begin{aligned}
  p\left(\left.\br\right|_{y=0, z=z_f}\right) & \propto \rme^{-\im 2\pi\frac{f_0 + \Delta f}{c}\cos\theta x}\rme^{-\im 2\pi (f_0 + \Delta f) t} + \rme^{\im 2\pi\frac{f_0 - \Delta f}{c}\cos\theta x}\rme^{-\im 2\pi (f_0 - \Delta f) t} \\
                                              & \propto \rme^{-\im 2\pi\frac{f_0}{c}\cos\theta x}\rme^{-\im 2\pi \Delta f t} + \rme^{\im 2\pi\frac{f_0}{c}\cos\theta x}\rme^{\im 2\pi \Delta f t}                                        \\
                                              & = 2\cos \left( 2\pi\frac{f_0}{c}\cos\theta x + 2\pi \Delta f t\right)
\end{aligned}$$ となる. したがって,
$\left|p\left(\left.\br\right|_{y=0, z=z_f}\right)\right|$が最大となる点は
$$\begin{aligned}
  2\pi\frac{f_0}{c}\cos\theta x + 2\pi \Delta f t = 0
\end{aligned}$$ であり, この点の速度は
$$\begin{aligned}
  2\pi\frac{f_0}{c}\cos\theta \mathrm{d}x + 2\pi \Delta f \mathrm{d}t = 0 \\
  \therefore \diff{x}{t} = - \frac{\Delta f}{f_0} \frac{c}{\cos \left[\arctan\left(\frac{z_f}{X}\right)\right]}
\end{aligned}$$
となる.
**すなわち, 位相変化を行うことなく最大音圧点を移動させることができる.**
