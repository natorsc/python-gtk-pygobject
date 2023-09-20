# -*- coding: utf-8 -*-
"""Configure project."""

import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent


def requirements_txt(shell: bool = True) -> None:
    subprocess.call(
        args='poetry export --without-hashes -f requirements.txt '
             '-o requirements.txt',
        cwd=ROOT_DIR,
        shell=shell,
    )
    subprocess.call(
        args='poetry export --with dev --without-hashes -f requirements.txt '
             '-o requirements-dev.txt',
        cwd=ROOT_DIR,
        shell=shell,
    )


if __name__ == "__main__":

    print('[!] Iniciando a configuração do projeto. [!]\n')

    requirements = str(
        input('Gerar ou atualizar o arquivo requirements.txt? (y/N): ') or 'n',
    )
    if requirements.lower() == 'y':
        requirements_txt()

    print("\n[!] Configuração inicial concluída. [!]")
