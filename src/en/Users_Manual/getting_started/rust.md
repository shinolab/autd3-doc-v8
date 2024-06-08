# Rust tutorial

First, make a new project and add `autd3` and `autd3-link-soem` libraries as dependencies.

```shell
cargo new --bin autd3-sample
cd autd3-sample
cargo add autd3
cargo add autd3-link-soem
cargo add tokio --features full
```

Next, edit `src/main.rs` file as follows.
This is the source code for generating a focus with $\SI{150}{Hz}$ AM modulation. 

```rust,should_panic,filename=main.rs,edition2021
{{#include ../../../codes/Users_Manual/Tutorial/main.rs}}
```

Then, run the program.

```shell
cargo run --release
```

## For Linux, macOS users

You may need to run with administrator privileges when using SOEM on Linux or macOS.

```shell
cargo build --release && sudo ./target/release/autd3_sample
```
