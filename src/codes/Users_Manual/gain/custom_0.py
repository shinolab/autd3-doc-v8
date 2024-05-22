~from pyautd3 import Drive, EmitIntensity, Phase
from pyautd3.gain import Custom

g = Custom(
    lambda dev: lambda tr: Drive(
        Phase(0x00), EmitIntensity(0x00)
    )
)