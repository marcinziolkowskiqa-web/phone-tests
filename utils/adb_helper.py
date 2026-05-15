import subprocess

ADB_PATH = r"C:\Users\MarcinZiółkowski\AppData\Local\Android\Sdk\platform-tools\adb.exe"


def adb(args):
    return subprocess.run(
        [ADB_PATH] + args,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )


def adb_shell(command: str) -> str:
    result = adb(["shell"] + command.split())

    if result.returncode != 0:
        raise RuntimeError(
            f"ADB shell failed\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )

    return result.stdout.strip()