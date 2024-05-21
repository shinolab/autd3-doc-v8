~from pyautd3 import AUTD3, Controller
Controller.builder().add_device(AUTD3([-AUTD3.DEVICE_WIDTH, 0.0, 0.0])).add_device(
    AUTD3([0.0, 0.0, 0.0])
)
