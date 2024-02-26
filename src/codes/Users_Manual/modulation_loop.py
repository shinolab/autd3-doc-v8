from pyautd3 import LoopBehavior
from pyautd3.modulation import Sine

m = Sine(150).with_loop_behavior(LoopBehavior.infinite())  # infinite loop
m = Sine(150).with_loop_behavior(LoopBehavior.finite(10))  # 10 times loop
m = Sine(150).with_loop_behavior(LoopBehavior.once())  # equivalent to finite(1)
