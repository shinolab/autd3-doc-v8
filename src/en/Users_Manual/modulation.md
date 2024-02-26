# Modulation

`Modulation` is a mechanism to control AM modulation.

The modulation is applied to the amplitude of the sound pressure.
For example, if you use `Sine` with $\SI{1}{kHz}$, the sound pressure amplitude is as follows, and the envelope of the positive part (or negative part) of sound pressure follows the $\SI{1}{kHz}$ sine wave.

<figure>
  <img src="../fig/Users_Manual/sine_1k_mod.png"/>
</figure>

Currently, `Modulation` has the following restrictions.

- The buffer size is up to 32768.
- The sampling rate is $\clkf/N$, where $N$ is a 32-bit unsigned integer and must be at least 512.

The SDK has `Modulation` by default to generate several types of AM.

* [Static](./modulation/static.md)
* [Sine](./modulation/sine.md)
  * [Fourier](./modulation/fourier.md)
* [Square](./modulation/square.md)
* [Wav](./modulation/wav.md)
* [RawPCM](./modulation/rawpcm.md)
* [Cache](./modulation/cache.md)
* [RadiationPressure](./modulation/radiation.md)
* [Transform](./modulation/transform.md)

## Modulation common API

### Sampling configuration

You can get the sampling frequency with `sampling_config`.

Some `Modulation` can set the sampling configuration with `with_sampling_config`.
However, due to the constraints of `Modulation`, the sampling frequency may not be exactly the specified value.

```rust,edition2021
{{#include ../../codes/Users_Manual/modulation_0.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/modulation_0.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/modulation_0.cs}}
```

```python
{{#include ../../codes/Users_Manual/modulation_0.py}}
```

### Modulation data size

The modulation data size can be obtained as follows.

```rust,edition2021
{{#include ../../codes/Users_Manual/modulation_1.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/modulation_1.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/modulation_1.cs}}
```

```python
{{#include ../../codes/Users_Manual/modulation_1.py}}
```
