using AUTD3Sharp;
using AUTD3Sharp.Modulation;

var m = new Square(150.0 * Hz)
        .WithLow(0x00)
        .WithHigh(0xFF);