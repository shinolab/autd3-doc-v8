# CPUボードとのインターフェース

FPGAとCPUボードとの接続は以下のようになっている.

* `[16:0] CPU_ADDR`: Input, CPUボードから書き込まれるデータのアドレス. 最下位の$\SI{1}{bit}$は使用できないため, 実質$\SI{16}{bit}$
* `[15:0] CPU_DATA`: Input/Output, CPUボードから書き込まれるデータ
* `CPU_CKIO`: Input, CPUバスクロック ($\SI{75}{MHz}$)
* `CPU_CS1_N`: Input, CPUバスイネーブル (負論理)
* `CPU_WE0_N`: Input, 書き込みイネーブル (負論理)
* `CPU_WE1_N`: Input, 書き込みイネーブル (負論理, 未使用)
* `CPU_RD_N`: Input, 読み込みイネーブル (負論理)
* `CPU_RDWR`: Input, 1でCPUからの読み込み, 0でCPUからの書き込み

CPUとの通信には, `CPU_ADDR`, `CPU_DATA`, `CPU_CKIO`, `CPU_CS1_N`, `CPU_WE0_N`, 及び, `CPU_RDWR`を使用する.
これらの信号は, XilinxのBRAM IP (Native Port) と接続できる.

CPUからの書き込みには, `CPU_ADDR`を`addr`, `CPU_DATA`を`din`, `CPU_CKIO`を`clk`, `~CPU_CS1_N`を`en`, `~CPU_WE0_N`を`we`に接続すれば良い.

CPUからの読み込みには, トライステートバッファを使用し, `~CPU_CS1_N`, かつ, `~CPU_RD_N`, かつ, `CPU_RDWR`の場合に`CPU_DATA`を`dout`に接続し, そうでないときは`CPU_DATA`をハイインピーダンス (`z`) にする.
