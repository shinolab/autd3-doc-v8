~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Utils;
~using var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(Nop.Builder());
autd.Send(new DebugSettings(
    (dev, gpio) => gpio == GPIOOut.O0 ? DebugType.BaseSignal : DebugType.None
));