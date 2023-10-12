# -*- coding: utf-8 -*-
"""."""

import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DIRHTML = BASE_DIR.joinpath('build', 'dirhtml')


def make_doc(shell: bool = True) -> None:
    subprocess.run(
        args='make dirhtml',
        cwd=BASE_DIR,
        shell=shell,
    )


def run_doc(doc_dir, shell: bool = True) -> None:
    subprocess.run(
        args=f'python3 -m http.server -d {doc_dir}',
        cwd=BASE_DIR,
        shell=shell,
    )


if __name__ == "__main__":
    make_doc()
    run_doc(doc_dir=DIRHTML)
