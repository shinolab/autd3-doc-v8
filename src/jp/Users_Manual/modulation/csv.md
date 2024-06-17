# Csv

`Csv`はCsvファイルをもとに構成される`Modulation`である.

データはdeliminator (デフォルトはカンマ",", `with_deliminator`で変更可) で区切られた行データか, 列データであり, データ値は符号なし8bit整数である必要がある.

```rust,edition2021
{{#include ../../../codes/Users_Manual/modulation/csv_0.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/modulation/csv_0.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/modulation/csv_0.cs}}
```

```python
{{#include ../../../codes/Users_Manual/modulation/csv_0.py}}
```

コンストラクタの第2引数で, このデータのサンプリング周波数を指定する必要がある.

> NOTE: AUTD3のサンプリング周波数に関する制約により, 出力できない可能性があるので注意されたい.
> Modulationのサンプリング周波数の設定と制約は[Modulation](../modulation.md)を参照されたい.
