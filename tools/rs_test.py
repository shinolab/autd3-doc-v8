import multiprocessing
import pathlib
import subprocess
import sys
from functools import reduce
from glob import glob

import joblib
import requests


def get_version(crate: str) -> str:
    res = requests.get(f"https://crates.io/api/v1/crates/{crate}")
    return res.json()["crate"]["newest_version"]


if __name__ == "__main__":
    autd3_version = get_version("autd3")
    autd3_link_vis_version = get_version("autd3-link-visualizer")
    tokio_version = get_version("tokio")
    print(f"Testing with autd3-rs {autd3_version}")

    base_path = pathlib.Path(__file__).parent.parent / "src" / "codes"

    # n_jobs = multiprocessing.cpu_count()
    n_jobs = 4
    srcs = list(glob(str(base_path / "**/*.rs"), recursive=True))
    N = len(srcs)
    block = N // n_jobs

    base_test_dir = pathlib.Path(__file__).parent / "test-rs"
    if not base_test_dir.exists():
        base_test_dir.mkdir()

    def test(i, N):
        error_files = []
        start = i * block
        end = (i + 1) * block if i != n_jobs - 1 else N

        test_dir = base_test_dir / str(i)
        if not test_dir.exists():
            test_dir.mkdir()
        src_dir = test_dir / "src"
        if not src_dir.exists():
            src_dir.mkdir()
        with open(test_dir / "Cargo.toml", "w") as f:
            f.write(
                f"""[package]
name = "thirdparties"
version = "{autd3_version}"
edition = "2021"

[dependencies]
autd3 = {{ version = "{autd3_version}" }}
autd3-gain-holo = {{ version = "{autd3_version}" }}
autd3-link-simulator = {{ version = "{autd3_version}" }}
autd3-link-visualizer = {{ version = "{autd3_link_vis_version}", features = ["python", "gpu"] }}
autd3-link-soem = {{ version = "{autd3_version}", features = ["remote"] }}
autd3-link-twincat = {{ version = "{autd3_version}", features = ["remote"] }}
autd3-modulation-audio-file = {{ version = "{autd3_version}" }}
tokio = {{ version = "{tokio_version}", features = ["full"] }}
"""
            )

        for src in srcs[start:end]:
            with open(src, "r") as f:
                content = f.read()
            content = content.replace("# ", "")
            with open(src_dir / "main.rs", "w") as f:
                f.write(content)

            try:
                subprocess.run(["cargo", "build"], cwd=test_dir).check_returncode()
            except subprocess.CalledProcessError:
                error_files.append(src)

        return error_files

    result = joblib.Parallel(n_jobs=n_jobs)(
        joblib.delayed(test)(i, len(srcs)) for i in range(n_jobs)
    )
    err_files = reduce(lambda a, b: a + b, result)
    if len(err_files) == 0:
        print("All files are OK")
    else:
        print("Error files:")
        for src in err_files:
            print(f"{src}")
        sys.exit(1)
