import multiprocessing
import pathlib
import subprocess
import sys
from functools import reduce
from glob import glob

import joblib
import requests


def get_version() -> str:
    res = requests.get("https://api.github.com/repos/shinolab/autd3-cpp/tags")
    return res.json()[0]["name"]


if __name__ == "__main__":
    version = get_version()
    print(f"Testing with autd3-cpp {version}")

    base_path = pathlib.Path(__file__).parent.parent / "src" / "codes"

    # n_jobs = multiprocessing.cpu_count()
    n_jobs = 4
    srcs = list(glob(str(base_path / "**/*.cpp"), recursive=True))
    N = len(srcs)
    block = N // n_jobs

    base_test_dir = pathlib.Path(__file__).parent / "test-cpp"
    if not base_test_dir.exists():
        base_test_dir.mkdir()

    def test(i, N):
        error_files = []
        start = i * block
        end = (i + 1) * block if i != n_jobs - 1 else N

        test_dir = base_test_dir / str(i)
        if not test_dir.exists():
            test_dir.mkdir()
        build_dir = test_dir / "build"
        if not build_dir.exists():
            build_dir.mkdir()
        with open(test_dir / "CMakeLists.txt", "w") as f:
            f.write(
                f"""cmake_minimum_required(VERSION 3.21)

project(autd3-doc-test)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(${{CMAKE_VERSION}} VERSION_GREATER_EQUAL "3.24.0")
  cmake_policy(SET CMP0135 NEW)
endif()

include(FetchContent)
if(WIN32)
  FetchContent_Declare(
    autd3
    URL https://github.com/shinolab/autd3-cpp/releases/download/{version}/autd3-{version}-win-x64.zip
  )
elseif(APPLE)
  FetchContent_Declare(
    autd3
    URL https://github.com/shinolab/autd3-cpp/releases/download/{version}/autd3-{version}-macos-aarch64.tar.gz
  )
else()
  FetchContent_Declare(
    autd3
    URL https://github.com/shinolab/autd3-cpp/releases/download/{version}/autd3-{version}-linux-x64.tar.gz
  )
endif()
set(USE_SYSTEM_EIGEN ON)
FetchContent_MakeAvailable(autd3)

add_executable(main main.cpp)

target_link_libraries(main PRIVATE autd3::autd3)
target_link_libraries(main PRIVATE autd3::link::soem)
target_link_libraries(main PRIVATE autd3::link::twincat)
target_link_libraries(main PRIVATE autd3::link::visualizer)
target_link_libraries(main PRIVATE autd3::link::simulator)
target_link_libraries(main PRIVATE autd3::gain::holo)
target_link_libraries(main PRIVATE autd3::modulation::audio_file)
"""
            )

        with open(test_dir / "main.cpp", "w") as f:
            f.write("""int main() { return 0; }""")
        subprocess.run(
            ["cmake", "..", "-DCMAKE_C_COMPILER=gcc-12", "-DCMAKE_CXX_COMPILER=g++-12"],
            cwd=build_dir,
        ).check_returncode()

        for src in srcs[start:end]:
            with open(src, "r") as f:
                content = f.read()
            content = content.replace("//~", "")
            with open(test_dir / "main.cpp", "w") as f:
                f.write(content)

            try:
                subprocess.run(
                    ["cmake", "--build", ".", "--config", "release"], cwd=build_dir
                ).check_returncode()
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
