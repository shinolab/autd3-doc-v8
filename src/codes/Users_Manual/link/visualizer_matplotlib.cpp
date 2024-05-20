//~#include<autd3.hpp>
#include "autd3/link/visualizer.hpp"

//~int main() {
//~auto autd = autd3::ControllerBuilder()
//~                .add_device(autd3::AUTD3(autd3::Vector3::Zero()))
//~                .open(
autd3::link::Visualizer::builder().with_backend<autd3::link::PythonBackend>()
    //~                    );
    //~return 0; }