//~#include<autd3.hpp>
#include "autd3/link/twincat.hpp"

//~int main() {
//~auto autd = autd3::ControllerBuilder()
//~                .add_device(autd3::AUTD3(autd3::Vector3::Zero()))
//~                .open(
autd3::link::RemoteTwinCAT::builder("172.16.99.111.1.1")
    .with_server_ip("172.16.99.104")
    .with_client_ams_net_id("172.16.99.62.1.1")
    //~                    );
    //~return 0; }