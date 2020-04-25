# -*- coding: utf-8 -*-
"""Gerando executáveis com Cx_Freeze!"""

import sys
from platform import system

from cx_Freeze import Executable, setup

base = None

build_exe_options = {
    'excludes': ['tkinter', 'wx', 'email', 'pydoc_data', 'curses'],
    'include_files': ['icons'],
    'packages': ['gi'],
}

if system() == 'Windows':
    from windows_include_files import include_files

    if sys.platform == 'win32':
        base = 'Win32GUI'
        build_exe_options['include_files'] = include_files

    if sys.platform == 'win64':
        base = 'Win64GUI'
        build_exe_options['include_files'] = include_files

setup(
    name='MyApp',
    author='Renato Cruz (natorsc@gmail.com)',
    version='0.0.1',
    description='Criando executáveis com Cx_Freeze!',
    options={'build_exe': build_exe_options},
    executables=[
        Executable(
            'MainWindow.py',
            base=base,
            icon='icons/icon.ico',
        ),
    ],
)
