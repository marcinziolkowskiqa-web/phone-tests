import pytest
from utils.device_info import get_app_version


def test_app_version():

    version = get_app_version("io.appium.android.apis")

    print("\n")
    print("Tested app version:",version)

    assert version is not None