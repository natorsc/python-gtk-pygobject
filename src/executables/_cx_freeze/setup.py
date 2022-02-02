# -*- coding: utf-8 -*-
"""Python e GTK 4: Como criar um executável com Cx_Freeze."""

from sys import platform

from cx_Freeze import Executable, setup

base = None

build_exe_options = {
    'excludes': ['tkinter'],
    'include_files': ['icons', 'ui'],
    'packages': ['gi'],
}

if platform == 'win32':
    build_exe_options['include_files'] += [
        ('C:/msys64/mingw64/lib/girepository-1.0', 'lib/girepository-1.0'),
        ('C:/msys64/mingw64/lib/gdk-pixbuf-2.0', 'lib/gdk-pixbuf-2.0'),
        ('C:/msys64/mingw64/lib/gtk-4.0', 'lib/gtk-3.0'),
        ('C:/msys64/mingw64/share/glib-2.0', 'share/glib-2.0'),
    ]

    if platform == 'win32':
        base = 'Win32GUI'

    if platform == 'win64':
        base = 'Win64GUI'

setup(
    name='Exemplo',
    author='Renato Cruz (natorsc@gmail.com)',
    version='0.0.1',
    description='Python e GTK 4: Como criar um executável com Cx_Freeze.',
    options={'build_exe': build_exe_options},
    executables=[
        Executable(
            'MainWindow.py',
            target_name='br.natorsc.Exemplo',
            base=base,
            icon='icons/icon.ico',
        ),
    ],
)
