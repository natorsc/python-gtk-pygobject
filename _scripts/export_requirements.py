# -*- coding: utf-8 -*-
"""PDM export requirements.txt."""

import pathlib
import subprocess


BASE_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

print('[!] Gerando arquivos requirements [!]')
subprocess.call(
    args=['pdm', 'export', '--without-hashes', '-o', 'requirements.txt'],
    cwd=ROOT_DIR,
)
print('[!] Arquivos requirements gerados [!]')
