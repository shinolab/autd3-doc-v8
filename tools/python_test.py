import pathlib
import platform
import shutil
import subprocess
from glob import glob


def is_windows():
    return platform.system() == "Windows"


def is_macos():
    return platform.system() == "Darwin"


def is_linux():
    return platform.system() == "Linux"


def python_module(cmd):
    r = ["python" if is_windows() else "python3", "-m"]
    r.extend(cmd)
    return r


if __name__ == "__main__":
    base_path = pathlib.Path(__file__).parent.parent / "src" / "codes"

    srcs = list(glob(str(base_path / "**/*.py"), recursive=True))

    test_dir = pathlib.Path(__file__).parent / "test-python"
    if not test_dir.exists():
        test_dir.mkdir()

    for src in srcs:
        src = pathlib.Path(src)
        with open(src, "r") as f:
            content = f.read()
        content = content.replace("~", "")
        dst = test_dir / src.relative_to(base_path)
        if not dst.parent.exists():
            dst.parent.mkdir(parents=True)
            with open(dst.parent / "__init__.py", "w") as f:
                pass
        with open(dst, "w") as f:
            f.write(content)

    r = subprocess.run(
        python_module(["mypy", str(test_dir), "--check-untyped-defs"]),
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    try:
        r.check_returncode()
    except subprocess.CalledProcessError:
        err = r.stdout
        print(err.replace("test-python", str(base_path)))
        exit(1)

    r = subprocess.run(
        python_module(["ruff", "check", str(test_dir)]),
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    try:
        r.check_returncode()
    except subprocess.CalledProcessError:
        err = r.stdout
        print(err.replace("test-python", str(base_path)))
        exit(1)

    print("All tests passed.")
