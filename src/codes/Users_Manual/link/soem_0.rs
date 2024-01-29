# extern crate autd3;
# extern crate tokio;
# extern crate autd3_link_soem;
use autd3::prelude::*;
use autd3_link_soem::{SOEM, SyncMode, Status};

# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::builder()
#     .add_device(AUTD3::new(Vector3::zeros()))
#            .open_with(
SOEM::builder()
    .with_ifname("")
    .with_buf_size(32)
    .with_err_handler(|slave, status| match status {
        Status::Error(msg) => eprintln!("Error [{}]: {}", slave, msg),
        Status::Lost(msg) => {
            eprintln!("Lost [{}]: {}", slave, msg);
            // You can also wait for the link to recover, without exitting the process
            std::process::exit(-1);
        }
        Status::StateChanged(msg) => eprintln!("StateChanged [{}]: {}", slave, msg),
    })
    .with_state_check_interval(std::time::Duration::from_millis(100))
    .with_sync0_cycle(2)
    .with_send_cycle(2)
    .with_timer_strategy(TimerStrategy::BusyWait)
    .with_sync_mode(SyncMode::DC)
# ).await?;
# Ok(())
# }