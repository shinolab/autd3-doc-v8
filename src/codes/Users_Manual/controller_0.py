from pyautd3 import ConfigureReadsFPGAState

autd.send(ConfigureReadsFPGAState(lambda _: True))

info = autd.fpga_state
