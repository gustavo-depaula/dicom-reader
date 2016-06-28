import sys
from cx_Freeze import setup, Executable

setup(
    name = "Project N",
    version = "0.1",
    description = "Primeiro Prototipo",
    executables = [Executable("main.py", base = "Win32GUI")])
