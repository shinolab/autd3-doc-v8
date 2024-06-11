~from pyautd3 import Controller, kHz, AUTD3
Controller.builder([AUTD3([0, 0, 0])]).with_ultrasound_freq(41 * kHz)