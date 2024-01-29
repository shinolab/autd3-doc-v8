#include "autd3/link/soem.hpp"

void error_handler(const uint32_t slave, const uint8_t status, const char* msg) {
  switch (status) {
    case autd3::link::Status::Error:
      std::cout << "Error [" << slave << "]: " << msg << std::endl;
      break;
    case autd3::link::Status::Lost:
      std::cout << "Lost [" << slave << "]: " << msg << std::endl;
      // You can also wait for the link to recover, without exiting the process
      exit(-1);
    case autd3::link::Status::StateChanged:
      std::cout << "StateChanged [" << slave << "]: " << msg << std::endl;
      break;
  }
}

autd3::link::SOEM::builder()
    .with_ifname("")
    .with_buf_size(32)
    .with_err_handler(&error_handler)
    .with_state_check_interval(std::chrono::milliseconds(100))
    .with_sync0_cycle(2)
    .with_send_cycle(2)
    .with_timer_strategy(autd3::TimerStrategy::BusyWait)
    .with_sync_mode(autd3::link::SyncMode::DC)