# -*- coding: utf-8 -*-
"""."""

import logging
import pathlib
import subprocess
import sys


BASE_DIR = pathlib.Path(__file__).resolve().parent
PROJ_DIR = BASE_DIR.parent.joinpath('src', 'libadwaita-widgets')

LOG = BASE_DIR.joinpath('blueprint-compiler.log')
PLATFORM = sys.platform


logging.basicConfig(
    filename=LOG,
    format='%(asctime)s - %(levelname)s - %(message)s.',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


compiler = 'blueprint-compiler'
if PLATFORM == 'win32':
    compiler = 'python3 C:\\msys64\\mingw64\\bin\\blueprint-compiler'

logger.info('[!] Convertendo arquivos, aguarde... [!]')
print('[!] Convertendo arquivo, aguarde... [!]')
for file in PROJ_DIR.rglob('*.blp'):
    output = file.parent.joinpath(f'{file.stem}.ui')
    try:
        subprocess.call(args=[compiler, 'compile', file, '--output', output])
    except Exception as error:
        logging.exception(error)
    else:
        logger.info(output)

logger.info('[!] Conversão finalizada [!]')
print('[!] Conversão finalizada [!]')
