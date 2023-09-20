# -*- coding: utf-8 -*-
"""."""

import subprocess
import sys
from pathlib import Path


# Não utilizar no Gnome Builder. Configurar via meson.
def compile_blueprint_ui(ui_dir: Path):
    operational_system = sys.platform
    if operational_system == 'linux':
        for data in ui_dir.iterdir():
            if data.is_file() and data.suffix == '.blp':
                subprocess.run(
                    args=['blueprint-compiler', 'compile', f'{data}',
                          '--output', f'{ui_dir.joinpath(data.stem)}.ui'],
                )
    elif operational_system == 'win32':
        # MSYS2 + MINGW64 terminal.
        blueprint_compiler = 'C:\\msys64\\mingw64\\bin\\blueprint-compiler'
        for data in ui_dir.iterdir():
            if data.is_file() and data.suffix == '.blp':
                subprocess.run(
                    args=['python3', blueprint_compiler, 'compile', f'{data}',
                          '--output', f'{ui_dir.joinpath(data.stem)}.ui'],
                )
