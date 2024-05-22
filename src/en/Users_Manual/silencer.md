# Silencer

AUTD3 has a silencer to mute the output.
The silencer suppresses the rapid change in the drive signal of the transducer and mutes the output.

## Theory

The silencer is based on the paper by Suzuki et al.[^suzuki2020].

As a rough outline,
- Amplitude modulation of ultrasound produces audible sound.
- When driving an ultrasound transducer, phase changes cause amplitude fluctuations.
  - Therefore, audible noise is generated.
- Amplitude fluctuations can be suppressed by linearly interpolating phase changes and changing them stepwise.
  - Therefore, noise can be reduced by doing fine interpolation.
- The silencer is a method to reduce noise by doing fine interpolation.

## Silencer Config

To configure the silencer, send `Silencer` to the controller.

The silencer is enabled by default.
To disable the silencer, send `Silencer::disable`.

```rust,edition2021
{{#include ../../codes/Users_Manual/silencer/silencer_0.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/silencer/silencer_0.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/silencer/silencer_0.cs}}
```

```python
{{#include ../../codes/Users_Manual/silencer/silencer_0.py}}
```

To configure the silencer more finely, you need to choose from the following two modes.

- [Fixed update rate mode](#fixed-update-rate-mode)
- [Fixed completion steps mode](#fixed-completion-steps-mode)

The default is fixed completion steps mode.

### Fixed update rate mode

#### Phase change by Silencer in Fixed update rate mode

Silencer changes the phase $P$ linearly and stepwise to mute the output.
In other words, it is almost equivalent to passing the phase $P$ time series data through a (simple) moving average filter.
However, it differs in that it takes into account the fact that the phase data is periodic.

For example, consider the case where the period $T$ of the ultrasound is $T=12$.
In other words, $P=0$ corresponds to $0\,\mathrm{rad}$ and $P=12$ corresponds to $2\pi\,\mathrm{rad}$.
Here, suppose that the phase changes from $P=2$ to $P=6$ at time $t_s$.
The phase change by Silencer is as follows.

<figure>
  <img src="../fig/Users_Manual/silent/phase.svg"/>
<figcaption>Change of phase $P$</figcaption>
</figure>

On the other hand, suppose that the phase changes from $P=2$ to $P=10$ at time $t_s$.
The phase change by Silencer is as follows.
This is because $P=-2$ is closer to $P=2$ than $P=10$ in terms of the phase.

<figure>
  <img src="../fig/Users_Manual/silent/phase2.svg"/>
<figcaption>Change of phase $P$</figcaption>
</figure>

That is, Silencer updates the phase $P$ as follows for the current $P$ and the target value $P_r$.
$$
    P \leftarrow \begin{cases}
        P + \mathrm{sign}(P_r - P) \min (|P_r - P|, \Delta) & \text{if } |P_r - P| \le T/2\\
        P - \mathrm{sign}(P_r - P) \min (|P_r - P|, \Delta) & \text{(otherwise)}\\
    \end{cases}.
$$
Where $\Delta$ is the update amount per step (`step` of `Silencer`).
And the update frequency is $\ufreq$.

Small $\Delta$ makes the phase change smoother and reduces noise.

<figure>
  <img src="../fig/Users_Manual/silent/duty.svg"/>
<figcaption>Phase change over $\Delta$</figcaption>
</figure>

According to this implementation, the behavior is different from the moving average filter.
One is when the phase change amount shown above is larger than $\pi$, and the other is when the phase changes again in the middle.
Examples of phase changes at this time are shown below.

<figure>
  <img src="../fig/Users_Manual/silent/mean.svg"/>
<figcaption>Comparison against moving average filter</figcaption>
</figure>

## Amplitude change by Silencer in Fixed update rate mode

Amplitude modulation of ultrasound produces audible sound.
So, AM noise can be reduced by applying a filter to the amplitude parameter $D$.

Unlike the phase, the amplitude parameter $D$ is not periodic with respect to the period $T$.
Therefore, the amplitude parameter $D$ is updated as follows for the current $D$ and the target value $D_r$.
$$
    D \leftarrow D + \mathrm{sign}(D_r - D) \min (|D_r - D|, \Delta),
$$

#### Configure fixed update rate mode

To configure the fixed update rate mode, do as follows.
The arguments correspond to $\Delta$ described above.
Note that internally, Silencer is applied to,
- for phase, phase parameter multiplied by $256$
- for amplitude, amplitude parameter multiplied by `Modulation` data

```rust,edition2021
{{#include ../../codes/Users_Manual/silencer/silencer_fixed_update_rate.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/silencer/silencer_fixed_update_rate.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/silencer/silencer_fixed_update_rate.cs}}
```

```python
{{#include ../../codes/Users_Manual/silencer/silencer_fixed_update_rate.py}}
```

### Fixed completion steps mode

In fixed completion steps mode, change of phase/amplitude is completed in a fixed duration.

#### Configure fixed completion steps mode

To configure the fixed completion steps mode, do as follows.
The arguments correspond to the number of steps until the completion of the amplitude/phase change, respectively, where one step correspond to $\SI{25}{us}$.

```rust,edition2021
{{#include ../../codes/Users_Manual/silencer/silencer_fixed_completion_steps.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/silencer/silencer_fixed_completion_steps.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/silencer/silencer_fixed_completion_steps.cs}}
```

```python
{{#include ../../codes/Users_Manual/silencer/silencer_fixed_completion_steps.py}}
```

The default values are $40$ steps for phase change and $10$ steps for amplitude change.
Note that disabling Silencer is equivalent to phase/amplitude change in $1$ step.

In this mode, an error is returned if the phase/amplitude change of `Modulation`, `FocusSTM`, or `GainSTM` cannot be completed in the time specified by Silencer.
That is, the following conditions must be satisfied.
- Silencer's amplitude change completion steps $\times \SI{25}{us} \le$ sampling period of `Modulation` 
- Silencer's amplitude change completion steps $\times \SI{25}{us} \le$ sampling period of `FocusSTM`/`GainSTM`
- Silencer's phase change completion steps $\times \SI{25}{us} \le$ sampling period of `FocusSTM`/`GainSTM`

If you set `strict_mode` to `false`, you can ignore these restrictions, but it's not recommended.

```rust,edition2021
{{#include ../../codes/Users_Manual/silencer/silencer_fixed_completion_steps_with_strict.rs}}
```

```cpp
{{#include ../../codes/Users_Manual/silencer/silencer_fixed_completion_steps_with_strict.cpp}}
```

```cs
{{#include ../../codes/Users_Manual/silencer/silencer_fixed_completion_steps_with_strict.cs}}
```

```python
{{#include ../../codes/Users_Manual/silencer/silencer_fixed_completion_steps_with_strict.py}}
```


[^suzuki2020]: Suzuki, Shun, et al. "Reducing amplitude fluctuation by gradual phase shift in midair ultrasound haptics." IEEE transactions on haptics 13.1 (2020): 87-93.
