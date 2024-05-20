import multiprocessing
import pathlib
import subprocess
import sys
from functools import reduce
from glob import glob

import joblib
import requests


def get_version() -> str:
    res = requests.get("https://api.nuget.org/v3/flatcontainer/autd3sharp/index.json")
    return res.json()["versions"][-1]


if __name__ == "__main__":
    version = get_version()
    print(f"Testing with AUTD3Sharp {version}")

    base_path = pathlib.Path(__file__).parent.parent / "src" / "codes"

    n_jobs = multiprocessing.cpu_count()
    cs_srcs = list(glob(str(base_path / "**/*.cs"), recursive=True))
    N = len(cs_srcs)
    block = N // n_jobs

    base_test_dir = pathlib.Path(__file__).parent / "test-cs"
    if not base_test_dir.exists():
        base_test_dir.mkdir()

    def test(i, N):
        error_files = []
        start = i * block
        end = (i + 1) * block if i != n_jobs - 1 else N

        test_dir = base_test_dir / str(i)
        if not test_dir.exists():
            test_dir.mkdir()
        with open(test_dir / "test.csproj", "w") as f:
            f.write(
                f"""<Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <OutputType>Exe</OutputType>
        <TargetFramework>net8.0</TargetFramework>
        <ImplicitUsings>enable</ImplicitUsings>
        <Nullable>enable</Nullable>
        <AllowUnsafeBlocks>true</AllowUnsafeBlocks>
        <EmitCompilerGeneratedFiles>true</EmitCompilerGeneratedFiles>
    </PropertyGroup>

    <ItemGroup>
        <PackageReference Include="AUTD3Sharp" Version="{version}" />
        <PackageReference Include="AUTD3Sharp.Derive" Version="{version}" />
    </ItemGroup>

    </Project>"""
            )

        for cs_src in cs_srcs[start:end]:
            with open(cs_src, "r") as f:
                content = f.read()
            content = content.replace("~", "")
            with open(test_dir / "test.cs", "w") as f:
                f.write(content)

            r = subprocess.run(
                ["dotnet", "build"],
                cwd=test_dir,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            try:
                r.check_returncode()
            except subprocess.CalledProcessError:
                err = ""
                src_file = str(pathlib.Path(cs_src).absolute())
                test_file = str((test_dir / "test.cs").absolute())
                for line in r.stdout.split("\n"):
                    print(line)
                    if line.startswith(test_file):
                        err = line.replace(test_file, src_file).split("[")[0]
                        break
                error_files.append((cs_src, err))
        return error_files

    result = joblib.Parallel(n_jobs=n_jobs)(
        joblib.delayed(test)(i, len(cs_srcs)) for i in range(n_jobs)
    )
    err_files = reduce(lambda a, b: a + b, result)
    if len(err_files) == 0:
        print("All files are OK")
    else:
        print("Error files:")
        for cs_src, err in err_files:
            print(f"{cs_src}")
            print(f"\t{err}")
        sys.exit(1)
