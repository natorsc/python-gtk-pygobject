# -*- coding: utf-8 -*-
"""."""

import subprocess
import sys

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR.parent.joinpath('docs')
HTML_DIR = DOCS_DIR.joinpath('build', 'dirhtml')

subprocess.run(
    args='make dirhtml',
    cwd=DOCS_DIR,
    shell=True,
    check=True,
)

subprocess.run(
    args=f'{sys.executable} -m http.server --b 127.0.0.1 -d {HTML_DIR}',
    shell=True,
    check=True,
)