import sys
from os.path import join, isfile

from SCons.Script import DefaultEnvironment, SConscript

env = DefaultEnvironment()
core = env.BoardConfig().get("build.core", "arduino")
build_script = ""

# select build script as either from the Earle Philhower core or
# from the builder script contained in this platform.

if core == "ramirofd":
    build_script = join(
        env.PioPlatform().get_package_dir("framework-arduino-mbed-usb"), "tools", "platformio-build.py")
else:
    build_script = join(env.PioPlatform().get_dir(), "builder",
                        "frameworks", "arduino", "mbed-core", "arduino-core-mbed.py")

if not isfile(build_script):
    sys.stderr.write(
        "Error: Missing PlatformIO build script %s!\n" % build_script)
    env.Exit(1)

SConscript(build_script)
