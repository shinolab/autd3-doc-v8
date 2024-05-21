~from pyautd3 import LoopBehavior, Hz
~from pyautd3.modulation import Sine
m = Sine(150 * Hz).with_loop_behavior(LoopBehavior.Infinite)  # infinite loop
m = Sine(150 * Hz).with_loop_behavior(LoopBehavior.Finite(10))  # 10 times loop
m = Sine(150 * Hz).with_loop_behavior(LoopBehavior.Once)  # equivalent to finite(1)