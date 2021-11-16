import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico', 'cryptic-database-firebase-adminsdk-bv1yi-dfd68e9690.json']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "Cryptic",
    version = "1.0",
    description = "Crypto Forecasting Tool",
    author = "BDAF",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
