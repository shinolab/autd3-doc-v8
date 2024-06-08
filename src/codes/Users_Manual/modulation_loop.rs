# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() {
let m = autd3::modulation::Sine::new(150. * Hz)
            .with_loop_behavior(LoopBehavior::infinite()); // infinite loop
let m = autd3::modulation::Sine::new(150. * Hz)
            .with_loop_behavior(LoopBehavior::finite(10).unwrap()); // 10 times
let m = autd3::modulation::Sine::new(150. * Hz)
            .with_loop_behavior(LoopBehavior::once()); // equivalent to finite(1).unwrap()
# } 