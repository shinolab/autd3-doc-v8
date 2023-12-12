# Visualizer

`Visualizer` link is a link for visualizing phase pattern and sound field.

> NOTE:
> Currently, this Link is not provided in the distributed C++/C#/Unity/Python libraries for linux-armv7 and linux-aarch64.

[[_TOC_]]

## Visualize phase pattern

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

## Visualize modulation data

<figure>
  <img src="../../fig/Users_Manual/mod.png"/>
</figure>

```rust,edition2021
{{#include ../../../codes/Users_Manual/link/visualizer_mod.rs}}
```

```cpp
{{#include ../../../codes/Users_Manual/link/visualizer_mod.cpp}}
```

```cs
{{#include ../../../codes/Users_Manual/link/visualizer_mod.cs}}
```

```python
{{#include ../../../codes/Users_Manual/link/visualizer_mod.py}}
```

## Visualize sound field

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

### Calculate sound field

You can calculate sound field without plotting by using `calc_field` function.

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

The first argument of `calc_field` is an iterator of positions to calculate sound field.
The return value is a `Vec` of complex acoustic pressure at the specified positions.

## Enable GPU

You can use GPU to calculate sound field.
The argument of `with_gpu` is GPU id. If you specify `-1`, the most suitable GPU is selected automatically.


```rust,edition2021
{{#include ../../../codes/Users_Manual/link/visualizer_gpu.rs}}
```

- In rust library, you need to enable `gpu` feature.

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

## Using Matplotlib

You can plot using Python and matplotlib with `PythonBackend`.

```rust,edition2021
{{#include ../../../codes/Users_Manual/link/visualizer_matplotlib.rs}}
```

- In rust library, you need to enable `python` feature.

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
