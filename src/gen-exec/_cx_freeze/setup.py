# -*- coding: utf-8 -*-
"""Python e GTK: Como criar um executável com Cx_Freeze no Windows."""

import sys

from cx_Freeze import Executable, setup

base = None

build_exe_options = {
    'excludes': ['tkinter'],
    'include_files': ['icons', 'ui'],
    'packages': ['gi'],
}

if sys.platform == 'win32':
    from windows.include_files import include_files

    build_exe_options['include_files'] += include_files
    build_exe_options['include_msvcr'] = True

    if sys.platform == 'win32':
        base = 'Win32GUI'

    if sys.platform == 'win64':
        base = 'Win64GUI'

setup(
    name='Código Ninja',
    author='Renato Cruz (natorsc@gmail.com)',
    version='0.0.1',
    description='Python e GTK: Como criar um executável com Cx_Freeze no Windows.',
    options={'build_exe': build_exe_options},
    executables=[
        Executable(
            'MainWindow.py',
            target_name='CodigoNinja',
            base=base,
            icon='icons/icon.ico',
        ),
    ],
)
