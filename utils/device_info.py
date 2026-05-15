import re
from utils.adb_helper import adb


def get_app_version(package_name: str) -> str | None:
    result = adb(["shell", "dumpsys", "package", package_name])

    if result.returncode != 0:
        raise RuntimeError(
            f"ADB failed\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )

    match = re.search(r"versionName=([^\s]+)", result.stdout)
    return match.group(1) if match else None