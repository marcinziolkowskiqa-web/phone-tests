import pytest
from utils.adb_helper import adb_shell


@pytest.mark.smoke
def test_device_info():
    manufacturer = adb_shell("getprop ro.product.manufacturer")
    model = adb_shell("getprop ro.product.model")
    device_name = adb_shell(f"getprop ro.{manufacturer}.product.release.name")
    android = adb_shell("getprop ro.build.version.release")

    print(
        f"\nManufacturer: {manufacturer}"
        f"\nModel: {model}"
        f"\nDevice name: {device_name}"
        f"\nAndroid: {android}"
    )

    assert manufacturer != ""
    assert model != ""
    assert android != ""