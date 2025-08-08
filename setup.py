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
PACKAGES = [
    "PIL", 
    "pystray", 
    "aiohttp", 
    "validators", 
    "asyncio",
    "ssl",
    "certifi",
    "pkg_resources",
    "jaraco",
    "jaraco.text",
    "setuptools",
    "platformdirs",
    "more_itertools",
    "objc",
    "Foundation",
    "AppKit",
    "Cocoa"
]
OPTIONS = {
    "iconfile": "pickaxe.icns",
    "packages": PACKAGES,
    "includes": [
        "pkg_resources.py2_warn",
        "jaraco.text",
        "jaraco.functools",
        "more_itertools.recipes",
        "importlib_resources",
        "zipp"
    ],
    "excludes": [
        "selenium",
        "seleniumwire",
        "PyQt5",
        "PyQt6",
        "PySide2",
        "PySide6",
        "tkinter",
        "test",
        "unittest"
    ],
    "arch": "universal2",
    "semi_standalone": False,
    "site_packages": True
}

setup(
    name="TwitchDropsMiner",
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    install_requires=read_requirements(),
)
