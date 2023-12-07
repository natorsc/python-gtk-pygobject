# -*- coding: utf-8 -*-
"""."""

import subprocess
import sys

from pathlib import Path

PLATFORM = sys.platform


blp_compiler = 'blueprint-compiler'
if PLATFORM == 'win32':
    blp_compiler = 'python3 C:\\msys64\\mingw64\\bin\\blueprint-compiler'


def compile_blueprint_ui(ui_dir: Path):
    for file in ui_dir.rglob('*.ui'):
        if file.is_file() and file.suffix == '.blp':
            subprocess.run(
                args=f'{blp_compiler} compile {file} --output '
                f'{ui_dir.joinpath(file.stem)}.ui',
                shell=True,
                check=True,
            )
