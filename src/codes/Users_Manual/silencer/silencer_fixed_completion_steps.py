~# mypy: ignore-errors
~from pyautd3 import Silencer
~from datetime import timedelta
steps_intensity = 10
steps_phase = 10
config = Silencer.from_completion_steps(steps_intensity, steps_phase)
# or
time_intensity = timedelta(microseconds=250)
time_phase = timedelta(microseconds=250)
config = Silencer.from_completion_time(time_intensity, time_phase)