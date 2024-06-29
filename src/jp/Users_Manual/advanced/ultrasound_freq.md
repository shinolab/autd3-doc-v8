# 超音波周波数の設定

超音波周波数を変更する場合は, 環境変数`AUTD3_ULTRASOUND_FREQ`にHz単位の周波数を整数で設定すれば良い.

> NOTE: Rust版の場合は, `dynamic_freq` featureを有効にする必要がある.

なお, 同期などの制約で, 超音波周波数$f$は以下の条件を満たす必要がある.
この条件を満たさない周波数を設定した場合, エラーが発生する.

- $$
 \exist k \in \mathbb{N} \text{ s.t. }f \times 512 = k \times 2000
$$
- $$
\exist c \in [1,2,...,106], \exist m \in [16,17,...,512], \exist d \in [8,9,...,1024] \text{ s.t. }\\
\frac{3200000 \times m}{c} \in [600000000, 1600000000], f \times d = 50000 \times m
$$

これを満たす超音波周波数の例には
- $f = 40\,\mathrm{kHz}, (k = 10240, c = 1, m = 188, d = 235)$
- $f = 41\,\mathrm{kHz}, (k = 10496, c = 1, m = 205, d = 250)$

などがある.
