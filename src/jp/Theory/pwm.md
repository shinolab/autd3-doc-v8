# PWMと超音波の出力

Author: Shun Suzuki

Date: 2024-01-05

- - -

まず, 周期が$T$であり, 時間$t$に対する電圧$V(t)$が
$$
  V(t) = \begin{cases}
           V & (P-\frac{D}{2} \le t < P+\frac{D}{2}) \\
           0 & (\text{otherwise})
         \end{cases},
$$
で与えられるPWM信号を考える.

この信号のフーリエ展開は
$$\begin{aligned}
  \frac{1}{T}\int_{0}^{T}\,\mathrm{d}t V(t) \rme^{-2\pi \im n \frac{t}{T}}
   & = \frac{1}{T}V\int_{P-\frac{D}{2}}^{P+\frac{D}{2}}\,\mathrm{d}t \rme^{-2\pi \im n \frac{t}{T}}                                                                        \\
   & = \frac{1}{T}V \left( -\frac{T}{2\pi\im  n} \rme^{-2\pi \im n \frac{1}{T}(P+\frac{D}{2})} + \frac{T}{2\pi\im n} \rme^{-2\pi \im n \frac{1}{T}(P-\frac{D}{2})} \right) \\
   & = \frac{V}{2\pi \im n}\left( \rme^{2\pi \im n \frac{D}{2T}} - \rme^{-2\pi \im n \frac{D}{2T}} \right) \rme^{-2\pi\im n \frac{P}{T}}                                   \\
   & = \frac{V}{\pi n}\sin\left(\pi n \frac{D}{T}\right) \rme^{-2\pi\im n \frac{P}{2T}}
\end{aligned}$$
から
$$\begin{aligned}
  V(t) & = \sum_{n=-\infty}^{\infty} \frac{V}{\pi n}\sin\left(\pi n \frac{D}{T}\right) \rme^{-2\pi\im n \frac{P}{T}} \rme^{2\pi \im n \frac{t}{T}}      \\
       & = \frac{V}{T}D + \sum_{n=1}^{\infty} \frac{2V}{\pi n}\sin\left(\pi n \frac{D}{T}\right) \cos\left(\frac{2\pi n}{T}t -2\pi n\frac{P}{T} \right)
\end{aligned}$$
となる.

周波数$f=1/T$の振動子が十分高い$Q$値を持つとすると[^1], 周波数$f=1/T$の成分だけが取り出され, 超音波として放出される.
PWM信号の周波数$f=1/T$の成分は,
$$\begin{aligned}
  \frac{2V}{\pi}\sin\left(\pi \frac{D}{T}\right) \cos\left(\frac{2\pi}{T}t -2\pi \frac{P}{T} \right)
\end{aligned}$$
であるため,
PWM信号のパタメータ$P, D$と放出される超音波の振幅$A$と位相$\phi$の関係式は
$$\begin{aligned}
  A    & \propto V\sin\left(\pi \frac{D}{T}\right)     \\
  \phi & = 2\pi \frac{P}{T}
\end{aligned}$$
と表される. すなわち, パラメータ$P, D$により,
それぞれ位相と振幅を制御できる.

[^1]: 実際, AUTD3で使用されるT4010A1/T4010B1の$Q$値は$Q=29$であり, $n=2$の成分と$n=1$の成分との比は$4.3\times 10^{-3}$となり十分無視できる.
