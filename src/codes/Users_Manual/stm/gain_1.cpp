//~#include<autd3.hpp>
//~#include<autd3/link/nop.hpp>
//~int main() {
auto stm = autd3::GainSTM::from_sampling_config(
    1 * autd3::Hz, {autd3::gain::Null(), autd3::gain::Null()});
//~return 0; }