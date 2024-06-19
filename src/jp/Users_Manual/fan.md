# ファン制御
  
AUTD3デバイスにはファンがついており, Auto, Off, Onの3つのファンモードが有る. 

Autoモードでは温度監視ICがICの温度を監視し, 一定温度以上になると自動でファンを起動する.
Offモードではファンは常時オフであり, Onモードでは常時オンになる. 

モードの切替は, ファン横のジャンパスイッチで行う. 少しわかりにくいが, 以下の図のようにファン側をショートするとAuto, 真ん中でOff, 右側でOnとなる.

<figure>
    <img src="../fig/Users_Manual/fan.jpg"/>
    <figcaption>AUTDファン制御用のジャンパスイッチ</figcaption>
</figure>

Autoモードの場合は温度が高くなると自動的にファンが起動する.

Autoモードの場合, `ForceFan`でファンを強制的に起動できる.

```rust,edition2021
{{#include ../../codes/Users_Manual/controller_fan.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/controller_fan.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/controller_fan.cs}}
```

```python
{{#include ../../codes/Users_Manual/controller_fan.py}}
```

`ForceFan`コンストラクタの引数は`Fn(&Device) -> bool`で, デバイス毎にファンを強制駆動するかどうかを指定する.
