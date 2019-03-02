import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
      base = "Win32GUI"

setup(name="Flappy",
      version="0.1",
      description='Flappy Bird Game',
      executables=[Executable("sketch.py", base=base)])
