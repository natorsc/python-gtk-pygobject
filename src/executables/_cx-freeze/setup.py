# -*- coding: utf-8 -*-
"""Python e GTK 4: Como criar um executável com Cx_Freeze no Microsoft Windows.

Arquivo executado através do terminal MinGW x64 do msys2.
"""

import pathlib
import platform
import sys

from cx_Freeze import setup, Executable

BASE_DIR = pathlib.Path(__file__).resolve().parent
APP_ICON = str(BASE_DIR.joinpath('icons', 'br.com.justcode.Example.ico'))

base = None

build_exe_options = {
    'excludes': ['tkinter'],
    'include_files': ['icons', 'ui'],
    'includes': ['gi', 'cairo'],
    'packages': ['gi', 'cairo'],
}

if platform.system() == 'Windows':
    from ms_windows import lost_dlls

    build_exe_options['include_files'] += [
        ('C:/msys64/mingw64/lib/gdk-pixbuf-2.0', 'lib/gdk-pixbuf-2.0'),
        ('C:/msys64/mingw64/lib/girepository-1.0', 'lib/girepository-1.0'),
        ('C:/msys64/mingw64/lib/gtk-4.0', 'lib/gtk-4.0'),
        #
        ('C:/msys64/mingw64/share/glib-2.0', 'share/glib-2.0'),
        ('C:/msys64/mingw64/share/gtk-4.0', 'share/gtk-4.0'),
    ]
    build_exe_options['include_files'] += lost_dlls.include_dlls

    if sys.platform == 'win32':
        base = "Win32GUI"

    if sys.platform == 'win64':
        base = "Win64GUI"

setup(
    name='br.com.justcode.Example',
    author='Renato Cruz (natorsc@gmail.com)',
    version='0.0.1',
    description='Python e GTK 4: Como criar um executável com Cx_Freeze no Microsoft Windows.',
    options={'build_exe': build_exe_options},
    executables=[
        Executable(
            script='MainWindow.py',
            target_name='br.com.justcode.Example',
            base=base,
            icon=APP_ICON,
        ),
    ],
)
