~import pathlib
~from pyautd3 import Hz
from pyautd3.modulation.audio_file import RawPCM

path = pathlib.Path("path/to/foo.dat")
m = RawPCM(path, 4000 * Hz)
