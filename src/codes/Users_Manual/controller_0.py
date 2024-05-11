from pyautd3 import ReadsFPGAState

autd.send(ReadsFPGAState(lambda _: True))

info = autd.fpga_state
