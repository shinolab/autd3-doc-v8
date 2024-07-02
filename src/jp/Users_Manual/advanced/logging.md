# ロギングの有効化

## Rust

ログには[tracing](https://github.com/tokio-rs/tracing)を使用しているため, 以下のようにログ出力を有効化できる.

```rust,edition2021
tracing_subscriber::fmt()
    .with_max_level(tracing::Level::INFO)
    .init();
```

## C++/C#/Python

`RUST_LOG`環境変数に`autd3=<LEVEL>`を設定した上で, `tracing_init`を呼び出すことでログ出力を有効化できる.

`<LEVEL>`には以下のいずれかを指定することができる. 下に行くほど詳細なログが出力される.
- `ERROR`
- `WARN`
- `INFO`
- `DEBUG`
- `TRACE`

```cpp
#include <stdlib.h>

#ifdef WIN32
_putenv_s("RUST_LOG", "autd3=INFO");
#else
setenv("RUST_LOG", "autd3=INFO", false);
#endif

autd3::tracing_init();
```

```cs
System.Environment.SetEnvironmentVariable("RUST_LOG", "autd3=INFO");

AUTD3Sharp.Tracing.Init();
```

```python
from pyautd3 import tracing_init

os.environ["RUST_LOG"] = "autd3=INFO"

tracing_init()
```
