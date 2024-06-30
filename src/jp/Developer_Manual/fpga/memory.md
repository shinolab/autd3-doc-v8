# Memory

このモジュールはBRAMを集めたモジュールである.

FPGA内部のBRAMは5つに分かれている.
書き込み時は`CPU_ADDR` ($\SI{16}{bit}$) の内, 上位$\SI{2}{bit}$ (`BRAM_SELECT`) でこれを区別する.

- 0x0: Controller BRAM
- 0x1: Modulation BRAM
- 0x2: Pulse Witdth Encoder Table BRAM
- 0x3: STM BRAM

なお, STM BRAMはそのままだと書き込みアドレスが足りないので, Controller Main BRAM内の特定のアドレスに書き込まれたページ番号をアドレスの上位に付加することでアドレスを拡張している.
また, Modulation/STM BRAMは, 書き込むセグメントの選択もController Main BRAM内の特定のアドレスに書き込まれたセグメント番号により行う.

> これらのページ番号, セグメント番号データはCPUバスのクロックドメインで使用するため, BRAMに格納されたデータは使用しない.
> 代わりに, このアドレスへの書き込みを監視し, 直接レジスタに格納して使用するようにしている.
