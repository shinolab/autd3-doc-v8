use autd3::prelude::*;
use autd3_link_soem::{SOEM, Status};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Make a controller to control AUTD

    // Configure the devices
    // The argument of AUTD3::new is position
    // Here, the device is placed at the origin
    let mut autd = Controller::builder([AUTD3::new(Vector3::zeros())])
        // Open controller with SOEM link
        // The callback specified by with_err_handler is called when error occurs
        .open(SOEM::builder().with_err_handler(|slave, status| match status {
                Status::Error => eprintln!("Error [{}]: {}", slave, status),
                Status::Lost => {
                    eprintln!("Lost [{}]: {}", slave, status);
                    // You can also wait for the link to recover, without exitting the process
                    std::process::exit(-1);
                }
                Status::StateChanged => eprintln!("StateChanged [{}]: {}", slave, status),
            })).await?;

    // Check firmware version
    // This code assumes that the version is v8.0.x
    autd.firmware_version().await?.iter().for_each(|firm_info| {
        println!("{}", firm_info);
    });

    // Enable silencer
    // Note that this is enabled by default, so it is not actually necessary
    // To disable, send Silencer::disable()
    autd.send(Silencer::default()).await?;

    // A focus at 150mm directly above the center of the device
    let center = autd.geometry.center() + Vector3::new(0., 0., 150.0 * mm);
    let g = Focus::new(center);

    // 150Hz sine wave modulation
    let m = Sine::new(150 * Hz);

    // Send data
    autd.send((m, g)).await?;

    println!("press enter to quit...");
    let mut _s = String::new();
    std::io::stdin().read_line(&mut _s)?;

    // Close controller
    autd.close().await?;

    Ok(())
}