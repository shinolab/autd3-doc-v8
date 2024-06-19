# Clocking

AUTD3デバイスで使用している水晶振動子 (SG-8002CE-25.6M-PCB-L2, EPSON) の周波数は$\SI{25.6}{MHz}$であり, これをFPGA内蔵のMixed-Mode Clock Manager (MMCM) で変換したものをメインクロックとして使用している.

MMCMの動的リコンフィグレーション機能 (Dynamic Reconfiguration) を使用することで, ソフトウェアからメインクロック周波数を変更できるようにしてある.
超音波周期は固定 ($=512$) なので, メインクロック周波数を変更することで超音波周波数を変更できる.

動的リコンフィグレーションを使用して周波数を変更するには, MMCM内部レジスタに特定の値を書き込む必要がある.
比較的面倒なので, これはソフトウェアで計算しておいて, その値を書き込むことにしている.
MMCMで指定できる周波数には制限がある. MMCMについては, [UG472](https://docs.amd.com/v/u/en-US/ug472_7Series_Clocking)を参照.
動的リコンフィグレーションについては, [XAPP888](https://docs.amd.com/v/u/en-US/xapp888_7Series_DynamicRecon)参照.

デフォルトのメインクロック周波数は$\SI{40}{kHz}\times 512 = \SI{20.48}{MHz}$である.
