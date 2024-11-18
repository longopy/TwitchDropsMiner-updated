import glob
import os
import sys
from setuptools import find_packages, setup


def get_py_files():
    return [
        os.path.basename(f)
        for f in glob.glob("*.py")
        if f not in ["main.py", "setup.py"]
    ]


def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


APP = ["main.py"]
DATA_FILES = [("", get_py_files()), ("lang", glob.glob("lang/*"))]
PACKAGES = ["PIL", "pystray"]
OPTIONS = {
    "iconfile": "pickaxe.icns",
    "packages": PACKAGES
}

setup(
    name="TwitchDropsMiner",
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    install_requires=read_requirements(),
)
