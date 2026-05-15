import subprocess

def adb(command):
    return subprocess.check_output(
        ["adb", "shell"] + command.split(),
        text=True
    ).strip()

android = adb("getprop ro.build.version.release")
model = adb("getprop ro.product.model")

print("Android version:", android)
print("Model device:", model)