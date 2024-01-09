# 非線形最小二乗法

Author: Shun Suzuki

Date: 2024-01-09

- - -

件の行列方程式を次の非線形最小二乗問題として解く方法もある,
$$\begin{aligned}
    \min \|G\bq - \bp\|^2.
\end{aligned}$$
ここでのパラメータは$\bp$の位相と$\bq$である.
反復的に上式を最小化していく方法がいくつか知られている.

### Levenberg-Marquardt (LM) 法

ここでは, LM (Levenberg-Marquardt) 法 [^levenberg1944method] [^marquardt1963algorithm]を紹介する.
LM法を用いた例としては [^sakiyama2020midair] [^matsubayashi2020rendering]などがある.

後のため, 推定すべきパラメータ$\btheta$を
$$\begin{aligned}
    \bphi   & = [-\phi_0,..., -\phi_{N-1}]\trans,            \\
    \bpsi   & = [-\psi_0,..., -\psi_{M-1}]\trans,            \\
    \ba     & = [a_0,..., a_{N-1}]\trans,                    \\
    \btheta & = [\bphi\trans, \bpsi\trans, \ba\trans]\trans.
\end{aligned}$$
と置き, 最適化問題を
$$\begin{aligned}
    \min \|\bz(\btheta)\|^2,
\end{aligned}$$
$$\begin{aligned}
    \|\bz(\btheta)\|^2
     & = \|G\bq- \bp\|^2                                                        \\
     & = \|G\bq - \diag(|p_0|, ..., |p_{M-1}|)\rme^{\im\bpsi}\|^2               \\
     & = \|G\bq - P\rme^{\im\bpsi}\|^2 \quad (P = \diag(|p_0|, ..., |p_{M-1}|))
\end{aligned}$$
と書く.
ここでベクトル$\bx = [x_0, ..., x_k]\trans$に対して$\rme^{\bx}$は
$$\begin{aligned}
    \rme^{\bx} = [\rme^{x_0}, ..., \rme^{x_k}]\trans
\end{aligned}$$ を意味する.
まず, $\bz$は複素関数であることに注意する.
LM法を適用できるようにするため, 実部と虚部に分けると,
$$\begin{aligned}
    \|\bz(\btheta)\|^2 = \left\|
        \left(\begin{array}{c}
            \mathcal{R}[\bz(\btheta)] \\ \mathcal{I}[\bz(\btheta)]
        \end{array}\right)
        \right\|^2
\end{aligned}$$
となる.
ここで, $\mathcal{R}[z], \mathcal{I}[z]$はそれぞれ$z$の実部と虚部を表す.
$$\begin{aligned}
    \boldf(\btheta) = \left(\begin{array}{c}
                        \mathcal{R}[\bz(\btheta)] \\ \mathcal{I}[\bz(\btheta)]
                      \end{array}\right)
\end{aligned}$$
とおくと, $\boldf$は実関数であり
$$\begin{aligned}
    \min \|G\bq - \bp\|^2  \Leftrightarrow \min \|\boldf(\btheta)\|^2
\end{aligned}$$
となるので, LM法が適用できる.

この時, $\boldf(\btheta)$のJacobian $J(\btheta)$は
$$\begin{aligned}
    (\bz(\btheta))_k                            & = \sum_j G_{kj}a_j\rme^{\im\phi_j} - |p_k|\rme^{\im\psi_k}, \\
    \therefore \pdiff{(\bz(\btheta))_k}{\phi_j} & = \im G_{kj}a_j\rme^{\im\phi_j},                            \\
    \pdiff{(\bz(\btheta))_k}{\psi_i}            & = -\im\delta_{ki}|p_k|\rme^{\im\psi_k},                     \\
    \pdiff{(\bz(\btheta))_k}{a_j}               & = G_{kj}\rme^{\im\phi_j},
\end{aligned}$$
から,
$$\begin{aligned}
    J(\btheta) &= \pdiff{\boldf(\btheta)}{\btheta}\\
               &= \left(\begin{array}{ccc}
                        \mathcal{R}[\im G\diag(\bq)] & \mathcal{R}[-\im P\diag(\rme^{\im\bpsi})] & \mathcal{R}[G\diag(\rme^{\im\bphi})] \\
                            \mathcal{I}[\im G\diag(\bq)] & \mathcal{I}[-\im P\diag(\rme^{\im\bpsi})] & \mathcal{I}[G\diag(\rme^{\im\bphi})]
                  \end{array}\right)
\end{aligned}$$
となる.
この$J(\btheta)$を用いて, LM法では, 以下の更新式に従いパラメータを更新する.
$$\begin{aligned}
    \btheta_{t+1} = \btheta_t - (J(\btheta_t)\trans J(\btheta_t) + \lambda(t) \1)^{-1}J(\btheta_t)\trans f(\btheta).
\end{aligned}$$
$\lambda(t)$の決め方にはいくつかのバリエーションが知られている.
例えば, 文献[^madsen2004methods]を参照.

ここで, 計算量を削減するため, $J(\btheta_t)\trans J(\btheta_t)$をあらかじめ計算しておこう.
$$\begin{aligned}
    &J(\btheta_t)\trans J(\btheta_t)\\
    &= \left(\begin{array}{cc}
        \mathcal{R}[\im G\diag(\bq)]\trans              & \mathcal{I}[\im G\diag(\bq)]\trans\\
        \mathcal{R}[-\im P\diag(\rme^{\im\bpsi})]\trans & \mathcal{I}[-\im P\diag(\rme^{\im\bpsi})]\trans \\
        \mathcal{R}[G\diag(\rme^{\im\bphi})]\trans      & \mathcal{I}[G\diag(\rme^{\im\bphi})]\trans
       \end{array}\right) \\
    &\quad\times \left(\begin{array}{cc}
        \mathcal{R}[\im G\diag(\bq)] & \mathcal{R}[-\im P\diag(\rme^{\im\bpsi})] & \mathcal{R}[G\diag(\rme^{\im\bphi})] \\
                \mathcal{I}[\im G\diag(\bq)] & \mathcal{I}[-\im P\diag(\rme^{\im\bpsi})] & \mathcal{I}[G\diag(\rme^{\im\bphi})]
    \end{array}\right)
\end{aligned}$$
であるが,
$$\begin{aligned}
    \mathcal{R}[X]\trans\mathcal{R}[Y] + \mathcal{I}[X]\trans\mathcal{I}[Y] = \mathcal{R}[X^\dagger Y]
\end{aligned}$$
であるから, 結局,
$$\begin{aligned}
     & J(\btheta_t)\trans J(\btheta_t) \\
     & = \mathcal{R}\left(\begin{array}{ccc}
                        \diag(\overline{\bq}) G\hermite G \diag(\bq) & -\diag(\overline{\bq}) G\hermite P\diag(\rme^{\im\bpsi}) & -\im \diag(\overline{\bq}) G\hermite G\diag(\rme^{\im\bphi}) \\
                        *                                            & \diag(\rme^{-\im\bpsi})P\trans P \diag(\rme^{\im\bpsi})  & \im \diag(\rme^{-\im\bpsi})P\trans G\diag(\rme^{\im\bphi})   \\
                        *                                            & *                                                        & \diag(\rme^{-\im\bphi})G\hermite G \diag(\rme^{\im\bphi})
                    \end{array}\right)
\end{aligned}$$
($J(\btheta_t)\hermite J(\btheta_t)$はHermite行列なので, 一部省略した. 以下同様.)

ここで, 列ベクトル$\bx,\by$に対して,
$$\begin{aligned}
    \left(\diag(\bx) M \diag(\by)\right)_{ij} & = \sum_l \left(\sum_k \delta_{ik} x_k M_{kl} \right)\delta_{lj} y_j \\
                                              & = \sum_l \sum_k \delta_{ik}\delta_{lj} x_k M_{kl} y_j               \\
                                              & = M_{ij} x_i y_j
\end{aligned}$$
であり, したがって,
$$\begin{aligned}
    \diag(\bx) M \diag(\by) = M \circ \bx\by\trans
\end{aligned}$$
となる.
なお, $X\circ Y$は$X$と$Y$のHadamard積を意味する.
ここで,
$$\begin{aligned}
    B &= \left(\begin{array}{ccc}G & -P & -\im G\end{array}\right),          \\
    T &= \left(\begin{array}{ccc}
              \overline{\bq} \\ \rme^{-\im\bpsi} \\ \rme^{-\im\bphi}
          \end{array}\right)
\end{aligned}$$
と定義すると,
$$\begin{aligned}
     & \left(\begin{array}{ccc}
           \diag(\overline{\bq}) G\hermite G \diag(\bq) & -\diag(\overline{\bq}) G\hermite P\diag(\rme^{\im\bpsi}) & -\im \diag(\overline{\bq}) G\hermite G\diag(\rme^{\im\bphi}) \\
           *                                            & \diag(\rme^{-\im\bpsi})P\trans P \diag(\rme^{\im\bpsi})  & \im \diag(\rme^{-\im\bpsi})P\trans G\diag(\rme^{\im\bphi})   \\
           *                                            & *                                                        & \diag(\rme^{-\im\bphi})G\hermite G \diag(\rme^{\im\bphi})
        \end{array}\right) \\
     & = \left(\begin{array}{ccc}
             G\hermite G & -G\hermite P & -\im G\hermite G \\
             *           & P\trans P    & \im P\trans G    \\
             *           & *            & G\hermite G
         \end{array}\right) \circ\left(\begin{array}{ccc}
                               \overline{\bq}\bq\trans & \overline{\bq}\left(\rme^{\im\bpsi}\right)\trans   & \overline{\bq}\left(\rme^{\im\bphi}\right)\trans   \\
                               *                       & \rme^{-\im\bpsi}\left(\rme^{\im\bpsi}\right)\trans & \rme^{-\im\bpsi}\left(\rme^{\im\bphi}\right)\trans \\
                               *                       & *                                                  & \rme^{-\im\bphi}\left(\rme^{\im\bphi}\right)\trans
                           \end{array}\right)                  \\
     & = (B\hermite B) \circ TT\hermite
\end{aligned}$$
となり,
$$\begin{aligned}
    J(\btheta_t)\trans J(\btheta_t) = \mathcal{R}\left[(B\hermite B) \circ TT\hermite\right]
\end{aligned}$$
と計算できる.

次に, $J(\btheta_t)\trans f(\btheta)$を計算しよう.
$$\begin{aligned}
    J(\btheta_t)\trans f(\btheta) & = \left(\begin{array}{ccc}
                                          \mathcal{R}[\im G\diag(\bq)]\trans              & \mathcal{I}[\im G\diag(\bq)]\trans              \\
                                          \mathcal{R}[-\im P\diag(\rme^{\im\bpsi})]\trans & \mathcal{I}[-\im P\diag(\rme^{\im\bpsi})]\trans \\
                                          \mathcal{R}[G\diag(\rme^{\im\bphi})]\trans      & \mathcal{I}[G\diag(\rme^{\im\bphi})]\trans\end{array}\right)\left(\begin{array}{ccc}\mathcal{R}[\bz(\btheta)] \\ \mathcal{I}[\bz(\btheta)]\end{array}\right)  \\
                                  & = \mathcal{R}\left[\left(\begin{array}{ccc}
                                                               -\im\diag(\bq)\hermite G\hermite \bz  \\
                                                               \im\diag(\rme^{-\im\bpsi})P\trans \bz \\
                                                               \diag(\rme^{-\im\bphi}) G\hermite \bz
                                                           \end{array}\right) \right]
\end{aligned}$$ ここで, $\bz= G\bq - P\rme^{\im\bpsi}$なので,
$$\begin{aligned}
    \left(\begin{array}{ccc}
        -\im\diag(\bq)\hermite G\hermite \bz  \\
        \im\diag(\rme^{-\im\bpsi})P\trans \bz \\
        \diag(\rme^{-\im\bphi}) G\hermite \bz
    \end{array}\right)  & = \left(\begin{array}{ccc}
                          -\im\diag(\overline{\bq}) G\hermite (G\bq - P\rme^{\im\bpsi}) \\
                          \im\diag(\rme^{-\im\bpsi})P\trans (G\bq- P\rme^{\im\bpsi})    \\
                          \diag(\rme^{-\im\bphi}) G\hermite (G\bq - P\rme^{\im\bpsi})
                     \end{array}\right)                                                      \\
                                             & = -\im\left(\begin{array}{ccc}
                                                         \diag(\overline{\bq}) G\hermite G\bq - \diag(\overline{\bq}) G\hermite P\rme^{\im\bpsi} \\
                                                         -\diag(\rme^{-\im\bpsi})P\trans G\bq  + \diag(\rme^{-\im\bpsi})P\trans P\rme^{\im\bpsi} \\
                                                         \im \diag(\rme^{-\im\bphi}) G\hermite G\bq  - \im\diag(\rme^{-\im\bphi}) G\hermite P\rme^{\im\bpsi}
                                                     \end{array}\right) 
\end{aligned}$$ となる. ここで, 列ベクトル$\bx,\by$に対して,
$$\begin{aligned}
    \left(\diag(\bx) M \by\right)_{i} & = \sum_j \left(\sum_k \delta_{ik} \bx_k M_{kj} \right) \by_j \\
                                      & = \sum_j M_{ij} \bx_i \by_j                                  \\
                                      & = \sum_j \left(\diag(\bx) M \diag(\by)\right)_{ij}
\end{aligned}$$
である.
したがって,
$$\begin{aligned}
    \left(\begin{array}{ccc}
        -\im\diag(\bq)\hermite G\hermite \bz  \\
        \im\diag(\rme^{-\im\bpsi})P\trans \bz \\
        \diag(\rme^{-\im\bphi}) G\hermite \bz
    \end{array}\right)  = -\im\left(\begin{array}{ccc}
                            \diag(\overline{\bq}) G\hermite G\bq - \diag(\overline{\bq}) G\hermite P\rme^{\im\bpsi} \\
                            -\diag(\rme^{-\im\bpsi})P\trans G\bq  + \diag(\rme^{-\im\bpsi})P\trans P\rme^{\im\bpsi} \\
                            \im \diag(\rme^{-\im\bphi}) G\hermite G\bq  - \im\diag(\rme^{-\im\bphi}) G\hermite P\rme^{\im\bpsi}
                        \end{array}\right) 
\end{aligned}$$
は, $-\im(B\hermite B) \circ TT\hermite$の各行を最初の$N+M$列分だけ足したものに等しい.
したがって,
$$\begin{aligned}
    J(\btheta_t)\trans f(\btheta) = \mathrm{sumcol}(\mathcal{I}[(B\hermite B) \circ TT\hermite], N+M).
\end{aligned}$$ ここで, $\mathrm{sumcol}(X, n)$は,
$X$の各行を最初の$n$列分だけ足し合わせて得られる列ベクトルである.

なお実際にこのLM法を実装してみるとわかるが, 実は $$\begin{aligned}
    \ba & = [a_0, ..., a_{N-1}]\trans = [a, ..., a]\trans
\end{aligned}$$ という風に, 振動子の出力を(一律に)固定してしまうほうが,
再現性の意味でも, 計算量の意味でも性能がいい[^9]. このときは, 例えば,
パラメータは$\btheta = [\bphi\trans, \bpsi\trans]\trans$として,
$$\begin{aligned}
    B & = \left(\begin{array}{ccc}G & -P\end{array}\right) , \\
    T & = \left(\begin{array}{ccc}
              \overline{\bq} \\ \rme^{-\im\bpsi}
          \end{array}\right) 
\end{aligned}$$
を計算すれば良い.

#### 勾配降下法とGauss-Newton法

なお, 更新式を
$$\begin{aligned}
    \btheta_{t+1} = \btheta_t - (J(\btheta_t)\trans J(\btheta_t))^{-1}J(\btheta_t)\trans f(\btheta)
\end{aligned}$$
としたものはGauss-Newton法と呼ばれ,
$$\begin{aligned}
    \btheta_{t+1} = \btheta_t - \lambda J(\btheta_t)\trans f(\btheta)
\end{aligned}$$
としたものは勾配降下法 (Gradient-Descent), あるいは, 最急降下法 (Steepest-Descent) と呼ばれる.
LM法はこれらの間の子である.

[^levenberg1944method]: Levenberg, Kenneth. "A method for the solution of certain non-linear problems in least squares." Quarterly of applied mathematics 2.2 (1944): 164-168.

[^marquardt1963algorithm]: Marquardt, Donald W. "An algorithm for least-squares estimation of nonlinear parameters." Journal of the society for Industrial and Applied Mathematics 11.2 (1963): 431-441.

[^sakiyama2020midair]: Sakiyama, Emiri, et al. "Midair tactile reproduction of real objects." International Conference on Human Haptic Sensing and Touch Enabled Computer Applications. Cham: Springer International Publishing, 2020.

[^matsubayashi2020rendering]: Matsubayashi, Atsushi, Yasutoshi Makino, and Hiroyuki Shinoda. "Rendering ultrasound pressure distribution on hand surface in real-time." Haptics: Science, Technology, Applications: 12th International Conference, EuroHaptics 2020, Leiden, The Netherlands, September 6–9, 2020, Proceedings 12. Springer International Publishing, 2020.

[^madsen2004methods]: Madsen, Kaj & Nielsen, Hans & Tingleff, O., "Methods for Non-Linear Least Squares Problems (2nd ed.)," 60, 2004.

[^9]: 詳しいことはまだわかっていないが, 出力に対する制約が入っていないことが原因と考えられる.
