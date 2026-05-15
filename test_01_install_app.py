import pytest
from utils.adb_helper import adb

APK_PATH = r"C:\Temp\phone_tests\ApiDemos-debug.apk"
PACKAGE_NAME = "io.appium.android.apis"

'''
drobna zmiana 2
'''

@pytest.mark.install
def test_01_install_app():
    adb(["uninstall", PACKAGE_NAME])

    result = adb(["install", "-r", APK_PATH])

    print(result.stdout)
    print(result.stderr)

    assert result.returncode == 0, (
        f"Install failed\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )

    check = adb(["shell", "pm", "list", "packages", PACKAGE_NAME])

    assert PACKAGE_NAME in check.stdout