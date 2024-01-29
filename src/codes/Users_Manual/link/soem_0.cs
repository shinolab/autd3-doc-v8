using AUTD3Sharp;
using AUTD3Sharp.Link;
using AUTD3Sharp.NativeMethods;

SOEM.Builder()
    .WithIfname("")
    .WithBufSize(32)
    .WithErrHandler((slave, status, msg) =>
    {
        switch (status)
        {
            case Status.Error:
                Console.Error.WriteLine($"Error [{slave}]: {msg}");
                break;
            case Status.Lost:
                Console.Error.WriteLine($"Lost [{slave}]: {msg}");
                // You can also wait for the link to recover, without exiting the process
                Environment.Exit(-1);
                break;
            case Status.StateChanged:
                Console.Error.WriteLine($"StateChanged [{slave}]: {msg}");
                break;
        };
    })
    .WithStateCheckInterval(TimeSpan.FromMilliseconds(100))
    .WithSync0Cycle(2)
    .WithSendCycle(2)
    .WithTimerStrategy(TimerStrategy.BusyWait)
    .WithSyncMode(SyncMode.DC)