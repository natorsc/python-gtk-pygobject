# -*- coding: utf-8 -*-
"""Export requirements.txt."""

import pathlib
import subprocess

BASE_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

print('[!] Creating requirements.txt [!]')
subprocess.call(
    args=['poetry', 'export', '--without-hashes', '-o', 'requirements.txt'],
    cwd=ROOT_DIR,
)
print('[!] Requirements.txt created [!]')
