# extern crate autd3;
# use autd3::prelude::*;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let m = autd3::modulation::Sine::new(150. * Hz)
            .with_loop_behavior(LoopBehavior::infinite()); // infinite loop
let m = autd3::modulation::Sine::new(150. * Hz)
            .with_loop_behavior(LoopBehavior::finite(10).unwrap()); // 10 times
let m = autd3::modulation::Sine::new(150. * Hz)
            .with_loop_behavior(LoopBehavior::once()); // equivalent to finite(1).unwrap()
# Ok(())
# } 