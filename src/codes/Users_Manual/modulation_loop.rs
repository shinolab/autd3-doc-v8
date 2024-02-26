# extern crate autd3;
# use autd3::prelude::*;
use std::num::NonZeroU32;
# #[allow(unused_variables)]
# fn main() -> Result<(), Box<dyn std::error::Error>> {
let m = autd3::modulation::Sine::new(150.)
            .with_loop_behavior(LoopBehavior::Infinite); // infinite loop
let m = autd3::modulation::Sine::new(150.)
            .with_loop_behavior(LoopBehavior::Finite(NonZeroU32::new(10).unwrap())); // 10 times
let m = autd3::modulation::Sine::new(150.)
            .with_loop_behavior(LoopBehavior::once()); // equivalent to Finite(NonZeroU32::new(1).unwrap())
# Ok(())
# } 