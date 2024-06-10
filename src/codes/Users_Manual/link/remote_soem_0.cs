~using System.Net;
~using AUTD3Sharp;
using AUTD3Sharp.Link;

~using AUTD3Sharp.Gain;
~using AUTD3Sharp.Modulation;
~using AUTD3Sharp.Utils;
~var autd = Controller.Builder([new AUTD3(Vector3.Zero)]).Open(
RemoteSOEM.Builder(new IPEndPoint(IPAddress.Parse("172.16.99.104"), 8080))
~);