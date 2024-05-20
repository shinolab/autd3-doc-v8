//~#include<autd3.hpp>
//~int main() {
//~{
const auto m =
    autd3::modulation::Sine(150 * autd3::Hz)
        .with_loop_behavior(autd3::LoopBehavior::Infinite);  // infinite loop
//~}
//~{
const auto m =
    autd3::modulation::Sine(150 * autd3::Hz)
        .with_loop_behavior(autd3::LoopBehavior::Finite(10));  // 10 times loop
//~}
//~{
const auto m = autd3::modulation::Sine(150 * autd3::Hz)
                   .with_loop_behavior(
                       autd3::LoopBehavior::Once);  // equivalent to finite(1)
                                                    //~}
                                                    //~return 0; }