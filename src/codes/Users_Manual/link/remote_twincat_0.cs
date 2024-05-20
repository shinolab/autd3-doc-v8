~using System.Net;
~using AUTD3Sharp;
~using AUTD3Sharp.Link;
~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
~var autd = new ControllerBuilder().AddDevice(new AUTD3(Vector3d.Zero)).Open(
RemoteTwinCAT.Builder("172.16.99.111.1.1")
        .WithServerIp(IPAddress.Parse("172.16.99.104"))
        .WithClientAmsNetId("172.16.99.62.1.1")
~);