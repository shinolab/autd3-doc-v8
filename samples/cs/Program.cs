using AUTD3Sharp;
using AUTD3Sharp.Utils;
using AUTD3Sharp.Link;
using AUTD3Sharp.Gain;
using AUTD3Sharp.Modulation;
using static AUTD3Sharp.Units;

using var autd = new ControllerBuilder()
        .AddDevice(new AUTD3(Vector3d.Zero))
        .Open(SOEM.Builder().WithErrHandler((slave, status, msg) =>
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
        }));

var firmList = autd.FirmwareVersionList();
foreach (var firm in firmList)
    Console.WriteLine(firm);

autd.Send(Silencer.Default());

var g = new Focus(autd.Geometry.Center + new Vector3d(0, 0, 150));
var m = new Sine(150u * Hz);
autd.Send(m, g);

Console.ReadKey(true);

autd.Close();