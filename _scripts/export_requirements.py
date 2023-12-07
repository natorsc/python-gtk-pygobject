# -*- coding: utf-8 -*-
"""PDM."""

import subprocess

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

print('[!] Gerando arquivos requirements [!]')
subprocess.run(
    args='pdm export --without-hashes -o requirements.txt',
    cwd=ROOT_DIR,
    shell=True,
    check=True,
)
subprocess.run(
    args='pdm export --without-hashes --no-default -G docs -o requirements-docs.txt',
    cwd=ROOT_DIR,
    shell=True,
    check=True,
)
print('[!] Arquivos requirements gerados [!]')