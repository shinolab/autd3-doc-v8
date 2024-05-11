using AUTD3Sharp.Modulation;

var m = new Fourier(new Sine(100.0 * Hz))
        .AddComponent(new Sine(150.0 * Hz))
        .AddComponentsFromIter(new[] { new Sine(200.0 * Hz) });