# -*- coding: utf-8 -*-
"""."""

import pathlib
import subprocess
import sys


BASE_DIR = pathlib.Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR.parent.joinpath('docs')
HTML_DIR = DOCS_DIR.joinpath('build', 'dirhtml')

subprocess.call(args=['make', 'dirhtml'], cwd=DOCS_DIR)

subprocess.call(
    args=[f'{sys.executable}', '-m', 'http.server',
          '--b', '127.0.0.1', '-d', f'{HTML_DIR}'],
)
