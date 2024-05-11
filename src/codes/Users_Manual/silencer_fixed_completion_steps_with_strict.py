from pyautd3 import Silencer

steps_intensity = 10
steps_phase = 10
config = Silencer.fixed_completion_steps(steps_intensity, steps_phase).with_strict_mode(
    False
)
