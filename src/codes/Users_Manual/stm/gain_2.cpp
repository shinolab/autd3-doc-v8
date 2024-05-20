//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
auto stm = autd3::GainSTM::from_freq(1.0 * autd3::Hz)
               .with_mode(autd3::GainSTMMode::PhaseFull);
//~return 0; }