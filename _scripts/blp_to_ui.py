# -*- coding: utf-8 -*-
"""."""

import pathlib
import subprocess
import sys

from settings import logging

BASE_DIR = pathlib.Path(__file__).resolve().parent
PROJ_DIR = BASE_DIR.parent / 'src'
TEST_DIR = PROJ_DIR / 'gtk-widgets'

platform = sys.platform

compiler = 'blueprint-compiler'
if platform == 'win32':
    compiler = 'python3 C:\\msys64\\mingw64\\bin\\blueprint-compiler'


def blp_compile(input: pathlib = PROJ_DIR) -> None:
    logging.info('[[!] Converting (blp -> ui), please wait... [!]')
    for file in input.rglob('*.blp'):
        output = file.parent.joinpath(f'{file.stem}.ui')
        try:
            subprocess.call(
                args=[compiler, 'compile', '--output', output, file]
            )
        except Exception as error:
            logging.exception(error)
        else:
            logging.info(output)
    logging.info('[!] Conversion finished [!]')


if __name__ == '__main__':
    print('[!] Converting (blp -> ui), please wait... [!]')
    blp_compile(input=TEST_DIR)
    print('[!] Conversion finished [!]')
