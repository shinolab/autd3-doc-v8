# 固有値問題と行列方程式

Author: Shun Suzuki

Date: 2024-01-09

- - -

ここでは, 件の最適化問題の解法の1つとして, Longらによる方法 [^long2014rendering]を紹介する.
正直, この論文はお世辞にも理解しやすいとは言い難く, この節はおそらくこうだろうという自己解釈を多分に含むので注意されたい.

> NOTE: この手法は現在SDKでは実装されていない.

Longらの方法は, 単一焦点解の重ね合わせに基づく.
単一焦点解の重ね合わせとして駆動した場合, 各焦点の位相は何が最適か, を固有値問題として解く.

まずはじめに, 単一焦点を生成する解について考えよう.
ある点$\br_i$での複素音圧は
$$\begin{aligned}
    p(\br_i) = \sum_{j} G_{ij}a_j\rme^{\im (k \|\br_i - \br_j\| - \phi_j)},
\end{aligned}$$
であるため, $\br_i$に焦点を生成する解は明らかに
$$\begin{aligned}
    \phi_j = k \|\br_i - \br_j\|,
\end{aligned}$$
である.
これは, 伝搬による位相遅れを補償するように, 遠くの振動子が早めに音を出すことを意味する.

これには, 時間対称性を用いたもう1つの解釈がある.
(損失のない) 波動方程式は時間に対して対称であるため, 焦点に音源を置いたときの各振動子における音圧を記録し, これを逆再生することで焦点が生成できる.
逆再生するため,焦点から振動子への伝搬行列は$\overline{G_{ij}}$と表される.
ここで, $\overline{\cdot}$は複素共役を表す.
すなわち, $a_j\rme^{-\im \phi_j} = \overline{G_{ij}}|p(\br_i)|$[^4]とすれば, 逆に焦点が生成されるはずである.
これより,
$$\begin{aligned}
    \sum_{j} G_{ij}\rme^{\im (k \|\br_i - \br_j\|)}|p(\br_i)|\overline{G_{ij}}\rme^{-\im k \|\br_i - \br_j\|} = |p(\br_i)|\sum_{j} |G_{ij}|^2,
\end{aligned}$$
となり, 焦点での音圧$|p(\br_i)|$からずれる.
これは, 振動子の配置が離散的であることに起因する.
しかし, 今考えているのはフェーズドアレイなので, この分を補正しなくてはいけない.

したがって, 実際の振動子の駆動は
$$\begin{aligned}
    a_j\rme^{-\im \phi_j} =  \frac{|p_i|\overline{G_{ij}}}{\sum_{j} |G_{ij}|^2},
\end{aligned}$$
とすべきである(論文 [^long2014rendering]の式(8)).

ここで, 次のような行列$X$を考える,
$$\begin{aligned}
    X = \left(\begin{array}{ccc}
            \frac{|p_0|\overline{G_{00}}}{\sum_{j} |G_{0j}|^2}    & \cdots & \frac{|p_{M-1}|\overline{G_{M-1,0}}}{\sum_{j} |G_{M-1,j}|^2}   \\
            \vdots                                                & \ddots & \vdots                                                         \\
            \frac{|p_0|\overline{G_{0,N-1}}}{\sum_{j} |G_{0j}|^2} & \cdots & \frac{|p_{M-1}|\overline{G_{M-1,N-1}}}{\sum_{j} |G_{M-1,j}|^2}
        \end{array}\right).
\end{aligned}$$
少しわかりにくいが, 例えば, 第0列は$\br_0$の位置に音圧$|p_0|$の焦点を生成しようとしたときの振動子の駆動ベクトル$\bq$である.
ここで, 焦点音圧の位相 $\psi_i$から, 位相ベクトル$\bx$を,
$$\begin{aligned}
    \bx = [\rme^{-\im\psi_0}, ..., \rme^{-\im\psi_{M-1}}]\trans,
\end{aligned}$$
$$\begin{aligned}
    X\bx,
\end{aligned}$$
とすると, これは焦点に (位相込の) 複素音圧$\bp$の焦点を生成しようとしたときの振動子の各駆動ベクトルの線形重ね合わせをあらわす.
したがって, $GX\bx$は, そのような線形重ね合わせ駆動ベクトルが, 実際に焦点に生成する音圧を表す.
(行列$GX$が論文 [^long2014rendering]の行列$R$に等しい.)
これが, もともとの焦点音圧$\bp = \diag (|p_0|, ..., |p_{M-1}|) \bx$ (の定数倍) に等しくなってほしいので $$\begin{aligned}
    GX\bx = \lambda\diag (|p_0|, ..., |p_{M-1}|) \bx,
\end{aligned}$$
が解くべき問題になり, これはまさに固有値問題である.
定数倍の自由度は, 最終的に振動子の出力を$\lambda$分の1倍すればいい話なので問題にならない.

さて, 上の固有値問題の解のうち, もっとも望ましいのは$\lambda$のもっとも大きいものである.
なぜなら, $\lambda$が大きいなら, その分だけ振動子の出力を抑えることができるからである.
これは, 省電力化とアーティファクトの抑制につながる.
以上により, 焦点の位相の最適化が終わる.

焦点の位相が求まったので, 各焦点を生成する駆動ベクトルの重ね合わせである, $X\bx$を$\bq$とすれば良いような気もするが, この部分は振動子の出力可能な最大音圧を一切考慮していない.
すでに述べたように, 一部の振動子のみが突出して強い音を出すような解は望ましくない.
そこで, 振動子の出力のばらつきを抑えるためにTikhonov正則化を導入し, 最適化問題を次のように拡張したものを解く.
$$\begin{aligned}
    \left(\begin{array}{ccc}
        \bp    \\
        0      \\
        \vdots \\
        0
    \end{array}\right)
    =\left(\begin{array}{ccc}
                          & G      &                     \\
          \sigma_0^\gamma & \cdots & 0                   \\
          \vdots          & \ddots & \vdots              \\
          0               & \cdots & \sigma_{N-1}^\gamma
      \end{array}\right)\bq.
\end{aligned}$$
ここで, $$\begin{aligned}
    \sigma_j = \sqrt{\left|\sum_{i = 0}^{M-1} \frac{G_{ij}|p_i|}{M} \right|},
\end{aligned}$$
である.

> 正直に言うと, ここの解釈はいまだにきちんと理解できていない.
> おおよそは以下のような感じであろう. 
> まず, $\sigma_j$は$j$番目の振動子が持つ各焦点への"影響力"のようなものを表している.
> 連立方程式に$\sigma_j q_j = 0$のような式を追加することにより, 影響力の強い振動子の出力は弱めることにより, 振動子の出力のバランスを良くする.
> ただし, なぜ$\sigma_j$がこの表記になるのかはわからない.

なお, Longらの論文 [^long2014rendering]では,
固有値問題や逆問題の具体的な解き方は明記されていない.
また, 出力は振動子の限界を超えた場合には切り捨てるという方針を取る.

計算量は, 固有値問題を解くのに$O(M^3)$, 逆問題を解くのに, 例えばLU分解を使うと$O(N^3)$となる.
したがって, $O(\max(M, N)^3)$である[^5].

[^long2014rendering]: Long, Benjamin, et al. "Rendering volumetric haptic shapes in mid-air using ultrasound." ACM Transactions on Graphics (TOG) 33.6 (2014): 1-10.

[^4]: 焦点の位相は$0$とした.

[^5]: 普通は$M < N$
