# 半正定値緩和法

Author: Shun Suzuki

Date: 2024-01-09

- - -

ここでは, 件の行列方程式を解く方法を述べる.
ただし, 行列方程式を解くにはまず焦点の位相を決定する必要がある.

行列方程式を解いて得られた解が振動子出力の制約を満たさないのなら, 出力を一律に抑える必要がある.
そのため, 一部の振動子が突出して強いパワーで駆動するような解が得られたとしたら, 上限に合わせて全体をスケールしなければならず, 弱い場が生成されてしまう.
このような制約の下で, "良い"解を見つけるために, 焦点における位相を最適化する手法がこれまでにいくつか提案されている.

以下に, 井上らによる半正定値緩和法によるを紹介する[^inoue2014siggraph] [^inoue2014asia] [^inoue2015active].

まず, $P = \diag(|p_0|, ..., |p_{M-1}|), \bu = [\rme^{-\im \psi_0}, ..., \rme^{-\im \psi_{M-1}}]\trans$として, この問題を次のような最適化問題に書き換える.
$$\begin{aligned}
    \min_{|u_i|=1} \| G\bq - P\bu \|^2.
\end{aligned}$$
ここで$\bu$は位相成分を表すため$|u_i|=1$なる制約が付く.

ここで,
$$\begin{aligned}
    \bq               & = G^{-1}P\bu, \\
    G^{-1}GG^{-1}     & = G^{-1},     \\
    (GG^{-1})\hermite & = GG^{-1},
\end{aligned}$$
を満たすような$G^{-1}$が存在するとすると
$$\begin{aligned}
    \min_{|u_i|=1} \| G\bq - P\bu \|^2
     & = \| (GG^{-1} - \1) P\bu \|^2                                    \\
     & = \bu\hermite P\hermite(GG^{-1} - \1)\hermite (GG^{-1} - \1)P\bu \\
     & = \bu\hermite P(GG^{-1} - \1) (GG^{-1} - \1 )P\bu                \\
     & = \bu\hermite P(GG^{-1}GG^{-1} - 2GG^{-1} + \1 )P\bu             \\
     & = \bu\hermite P(\1-GG^{-1})P\bu,
\end{aligned}$$
となる.
ここで, $\cdot\hermite$はエルミート転置をあらわす.

$M= P(\1-GG^{-1})P$と置くと, 最適化問題は以下のように書き下せる.
$$\begin{aligned}
    \min_{|u_i|=1} \bu\hermite M \bu.
\end{aligned}$$

(以下の議論は文献[^phase]の2.4. Complex MaxCut.による.)
上記最適化は制約条件により凸問題ではない.
そこで, $U=uu\hermite$と置くと,
$$\begin{aligned}
    \min\                  & \mathrm{Tr}(UM),                   \\
    \mathrm{subject\ to}\  & \mathrm{diag}(U) = \1,             \\
                           & U \succeq 0, \mathrm{Rank}(U) = 1,
\end{aligned}$$
となる.
ここで, ランク制限を落とすと半正定値問題となり, 効率的に解くことができる.
$\mathrm{Rank}(U) = 1$ではない場合は$U$の最大固有値に対応する固有ベクトルが$\bu$の近似解となる.

ブロック座標降下法を用いて$U$を求めるアルゴリズムは文献[^phase] Algorithm 3を参照[^6].

あとは,
$$\begin{aligned}
    \bq               & = G^{-1}P\bu, \\
    G^{-1}GG^{-1}     & = G^{-1},     \\
    (GG^{-1})\hermite & = GG^{-1},
\end{aligned}$$
を満たす$G^{-1}$を求めればいい.
この$G^{-1}$はMoore-Penroseの擬似逆行列と呼ばれていて, $G$の特異値分解$G=U\Sigma V\hermite$から
$$\begin{aligned}
    G^{-1} = V\Sigma^{-1} U\hermite,
\end{aligned}$$
として計算できる.
ただし,
$\Sigma^{-1}$は$\Sigma=\diag(\sigma_1,...)$に対して
$$\begin{aligned}
    \Sigma^{-1} = \diag\left(\frac{1}{\sigma_1},...\right),
\end{aligned}$$
である.

井上らの方法では, ここにさらにTikhonov正則化が入る[^7].
すなわち, 最小化問題に以下の正則化項を加える.
$$\begin{aligned}
    \min_{|\bu_i|=1} \| G\bq - P\bu \|^2 + \alpha\|\bq\|^2.
\end{aligned}$$
これは, 機械学習の文脈ではリッジ回帰などと呼ばれる, L2正則化である.
この正則化には, 解の大きさを抑えるような効果がある.
この場合の解は, 以下で与えられる
$$\begin{aligned}
    \bq & = (G\hermite G + \alpha \1)^{-1}G\hermite  P\bu \\
        & = (V\Sigma\hermite U\hermite U\Sigma V\hermite + \alpha V \1 V\hermite)^{-1}V\Sigma\hermite  U\hermite P\bu \\
        & = V(\Sigma\hermite \Sigma + \alpha \1)^{-1}\Sigma\hermite U\hermite P\bu                                    \\
        & = V \diag\left(\frac{\sigma_1}{\sigma_1^2 + \alpha},...\right) U\hermite P\bu.
\end{aligned}$$

[^inoue2014siggraph]: Inoue, Seki, et al. "HORN: the hapt-optic reconstruction." ACM SIGGRAPH 2014 Emerging Technologies. 2014. 1-1.

[^inoue2014asia]: Inoue, S., et al. "HORN: Stationary airborne ultrasound 3d haptic image." Asia Haptics (2014): 18-20.

[^inoue2015active]: Inoue, Seki, Yasutoshi Makino, and Hiroyuki Shinoda. "Active touch perception produced by airborne ultrasonic haptic hologram." 2015 IEEE World Haptics Conference (WHC). IEEE, 2015.

[^phase]: Waldspurger, Irene, Alexandre d’Aspremont, and Stéphane Mallat. "Phase recovery, maxcut and complex semidefinite programming." Mathematical Programming 149 (2015): 47-81.

[^6]: なお, 実際の実装では$M_{i^c,i}$の計算において$M$の$i$番目の列を取得した後, $i$番目の行を除くのではなく単に$0$を代入している.これは, $X^k_{i^c,i^c}$のようにある行と列を除いた行列を取得するのはコストのかかる処理であると思われるからである. (少なくとも簡単にベンチマークを取った限りでは正しかった.)

[^7]: 実は論文には具体的な正則化の方法は書かれていない.
