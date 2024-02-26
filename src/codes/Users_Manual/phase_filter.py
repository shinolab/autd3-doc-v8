from pyautd3 import ConfigurePhaseFilter, Phase

autd.send(ConfigurePhaseFilter(lambda dev, tr: Phase(0)))
