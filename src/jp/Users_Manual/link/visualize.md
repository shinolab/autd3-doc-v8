# Visualizer

`Visualizer`リンクは位相パターンや音場を可視化するための`Link`である.

> NOTE:
> 現在, このLinkはlinux-armv7/linux-aarch64用のC++/C#/Unity/Pythonライブラリには含まれていない. 

[[_TOC_]]

## 位相パターンの可視化

<figure>
  <img src="../../fig/Users_Manual/phase.png"/>
</figure>

```rust,edition2021
{{#include ../../../codes/Users_Manual/link/visualizer_phase.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/link/visualizer_phase.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/link/visualizer_phase.cs}}
```

```python
{{#include ../../../codes/Users_Manual/link/visualizer_phase.py}}
```

## 変調データの可視化

<figure>
  <img src="../../fig/Users_Manual/mod.png"/>
</figure>


## 音場の可視化

<figure>
  <img src="../../fig/Users_Manual/xy.png"/>
</figure>

```rust,edition2021
{{#include ../../../codes/Users_Manual/link/visualizer_field.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/link/visualizer_field.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/link/visualizer_field.cs}}
```

```python
{{#include ../../../codes/Users_Manual/link/visualizer_field.py}}
```

## 音場計算

`calc_field`関数で, プロットせずに音場の計算を行うことができる.


```rust,edition2021
{{#include ../../../codes/Users_Manual/link/visualizer_calc.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/link/visualizer_calc.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/link/visualizer_calc.cs}}
```

```python
{{#include ../../../codes/Users_Manual/link/visualizer_calc.py}}
```


第1引数に, 音場を計算する位置のイテレータを指定する.
返り値は, 指定した点における複素音圧の`Vec`である.

## GPUの有効化

`with_gpu`を使用すると, GPUを使用して音場の計算を行うことができるようになる.
`with_gpu`の引数にはGPUのIDを指定する. `-1`を指定すると, 適当なGPUが自動的に選択される.

```rust,edition2021
{{#include ../../../codes/Users_Manual/link/visualizer_gpu.rs}}
```

- Rustでは`gpu` featureを有効化する必要がある.
    ```shell
    cargo add autd3-link-visualizer --features gpu
    ```

```cpp
{{#include ../../../codes/Users_Manual/link/visualizer_gpu.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/link/visualizer_gpu.cs}}
```

```python
{{#include ../../../codes/Users_Manual/link/visualizer_gpu.py}}
```

## Matplotlibの使用

`PythonBackend`を指定することで, Pythonのmatplotlibを使用して描画することができる.
この機能を使用する場合は, Pythonとmatplotlib, 及び, numpyをインストールしておく必要がある.

```rust,edition2021
{{#include ../../../codes/Users_Manual/link/visualizer_matplotlib.rs}}
```

- Rust版では`python`featureを有効にする必要がある

    ```shell
    cagro add autd3-link-visualizer --features python
    ```

```cpp
{{#include ../../../codes/Users_Manual/link/visualizer_matplotlib.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/link/visualizer_matplotlib.cs}}
```

```python
{{#include ../../../codes/Users_Manual/link/visualizer_matplotlib.py}}
```
