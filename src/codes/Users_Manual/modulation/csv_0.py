~import pathlib
~from pyautd3 import Hz
from pyautd3.modulation.audio_file import Csv

path = pathlib.Path("path/to/foo.csv")
m = Csv(path, 4000 * Hz)
