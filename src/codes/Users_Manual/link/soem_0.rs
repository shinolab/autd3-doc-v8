use autd3::prelude::*;
use autd3_link_soem::{SOEM, TimerStrategy, Status};

# #[allow(unused_variables)]
# #[tokio::main]
# async fn main() -> Result<(), Box<dyn std::error::Error>> {
# let autd = Controller::builder([AUTD3::new(Vector3::zeros())])
#            .open(
SOEM::builder()
    .with_ifname("")
    .with_buf_size(32)
    .with_err_handler(|slave, status| match status {
        Status::Error => eprintln!("Error [{}]: {}", slave, status),
        Status::Lost => {
            eprintln!("Lost [{}]: {}", slave, status);
            // You can also wait for the link to recover, without exitting the process
            std::process::exit(-1);
        }
        Status::StateChanged => eprintln!("StateChanged [{}]: {}", slave, status),
    })
    .with_state_check_interval(std::time::Duration::from_millis(100))
    .with_sync0_cycle(2)
    .with_send_cycle(2)
    .with_timer_strategy(TimerStrategy::BusyWait)
    .with_sync_tolerance(std::time::Duration::from_micros(1))
    .with_sync_timeout(std::time::Duration::from_secs(10))
# ).await?;
# Ok(())
# }