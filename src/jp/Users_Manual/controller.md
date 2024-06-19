# Controller

ここでは, `Controller`クラスに存在するAPIを紹介する.

[[_TOC_]]

## fpga_state

FPGAの状態を取得する.
これを使用する前に, `ReadsFPGAState`で状態取得を有効化しておく必要がある.

```rust,edition2021
{{#include ../../codes/Users_Manual/controller_0.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/controller_0.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/controller_0.cs}}
```

```python
{{#include ../../codes/Users_Manual/controller_0.py}}
```

`ReadsFPGAState`コンストラクタの引数は`Fn(&Device) -> bool`で, デバイス毎に状態取得を有効化するかどうかを指定する.

有効化していないデバイスに対して`fpga_state`は`None`を返す.

FPGAの状態としては, 現在以下の情報が取得できる.

- `is_thermal_assert`: ファン制御用の温度センサがアサートされているかどうか
- `current_mod_segment`: 現在のModulation Segment
- `current_stm_segment`: 現在のFociSTM/GainSTM Segment
- `current_gain_segment`: 現在のGain Segment
- `is_gain_mode`: 現在Gainが使用されているかどうか
- `is_stm_mode`: 現在FociSTM/GainSTMが使用されているかどうか

## send

デバイスにデータを送信する.

データは単体か2つのみ同時に送信することができる.

### タイムアウト

`with_timeout`でタイムアウト時間を指定できる.
これを省略した場合は[Link](./link.md)で設定したタイムアウト時間が使用される.

```rust,edition2021
{{#include ../../codes/Users_Manual/controller_1.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/controller_1.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/controller_1.cs}}
```

```python
{{#include ../../codes/Users_Manual/controller_1.py}}
```

タイムアウトの値が0より大きい場合, 送信データがデバイスで処理されるか, 指定したタイムアウト時間が経過するまで待機する.
送信データがデバイスで処理されたのが確認できなかった場合にエラーを返す.

タイムアウトの値が0の場合, `send`関数は送信データがデバイスで処理されたかどうかのチェックを行わない.

確実にデータを送信したい場合はこれを適当な値に設定しておくことをおすすめする.

## group

`group`関数を使用すると, デバイスをグルーピングすることができる.

```rust,edition2021
{{#include ../../codes/Users_Manual/controller_2.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/controller_2.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/controller_2.cs}}
```

```python
{{#include ../../codes/Users_Manual/controller_2.py}}
```

`gain::Group`とは異なり, 通常の`send`で送信できるデータなら何でも使用できる.
ただし, デバイス単位でしかグルーピングできない.

なお, タイムアウトは, `set`したものの中で最大のものが使用される.
`set`したものの中にタイムアウトを指定したものがなければ, [Link](./link.md)で設定したタイムアウト時間が使用される.

> NOTE:
> このサンプルでは, キーとして文字列を使用しているが, HashMapのキーとして使用できるものなら何でも良い.
