from pyautd3 import Phase, PhaseFilter

autd.send(PhaseFilter(lambda dev: lambda tr: Phase(0)))
