#include <iostream>

#include "autd3.hpp"
#include "autd3/link/soem.hpp"

coro::task<int> main_() {
  // create and open controller
  auto autd =
      co_await autd3::ControllerBuilder()
          // The  argument is the position.
          // The position is the origin of the device in the global coordinate
          // system you set.
          .add_device(autd3::AUTD3(autd3::Vector3::Zero()))
          .open_async(autd3::link::SOEM::builder().with_err_handler(
              [](const uint16_t slave, const autd3::link::Status status,
                 const std::string& msg) {
                switch (status) {
                  case autd3::link::Status::Error:
                    std::cout << "Error [" << slave << "]: " << msg
                              << std::endl;
                    break;
                  case autd3::link::Status::Lost:
                    std::cout << "Lost [" << slave << "]: " << msg << std::endl;
                    // You can also wait for the link to recover, without
                    // exiting the process
                    exit(-1);
                  case autd3::link::Status::StateChanged:
                    std::cout << "StateChanged [" << slave << "]: " << msg
                              << std::endl;
                    break;
                }
              }));

  // check firmware version
  const auto firm_infos = co_await autd.firmware_infos_async();
  std::copy(firm_infos.begin(), firm_infos.end(),
            std::ostream_iterator<autd3::FirmwareInfo>(std::cout, "\n"));

  // Silencer is used to quiet down the transducers' noise by passing the
  // phase/amplitude parameters through a low-pass filter.
  co_await autd.send_async(autd3::ConfigureSilencer::default_());

  // focus is 150.0 mm above array center
  const autd3::Vector3 focus =
      autd.geometry().center() + autd3::Vector3(0.0, 0.0, 150.0);
  autd3::gain::Focus g(focus);

  // Amplitude Modulation of 150 Hz sine wave
  autd3::modulation::Sine m(150);

  // send data
  co_await autd.send_async(m, g);

  std::cout << "press enter to finish..." << std::endl;
  std::cin.ignore();

  // close controller
  co_await autd.close_async();

  co_return 0;
}

int main() try { return sync_wait(main_()); } catch (std::exception& ex) {
  std::cerr << ex.what() << std::endl;
}