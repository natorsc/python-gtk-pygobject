# -*- coding: utf-8 -*-
"""Python e Gtk 4: Localizando dlls no Microsoft Windows."""

import pathlib
from re import compile
from subprocess import check_output
from zipfile import ZipFile

BASE_DIR = pathlib.Path(__file__).resolve().parent
SRC_DIR = BASE_DIR.parent.parent.parent

LOST_DLLS_FILE = BASE_DIR.joinpath('lost_dlls.py')
LOST_DLLS_FILE_TXT = BASE_DIR.joinpath('lost_dlls.txt')

ZIP_FILE = SRC_DIR.joinpath('data', 'ms-windows', 'listdlls', 'ListDlls.zip')
ZIP_OUTPUT = SRC_DIR.joinpath('data', 'ms-windows', 'listdlls', 'bin')

LISTDLLS_32 = ZIP_OUTPUT.joinpath('Listdlls.exe')
LISTDLLS_64 = ZIP_OUTPUT.joinpath('Listdlls64.exe')


def unzip_listdlls(zip_file, output):
    with ZipFile(file=zip_file, mode='r') as zip_obj:
        files = zip_obj.namelist()
        for file in files:
            if file.endswith('.exe'):
                zip_obj.extract(file, output)


def remove_exe_files():
    LISTDLLS_32.unlink()
    LISTDLLS_64.unlink()


def format_dlls(data):
    lines = data.splitlines()
    regex = compile(r'C:\\.*')

    dlls = []
    for line in lines:
        match = regex.search(line)
        if match:
            dll = match.group().split('\\')[-1]
            if dll.endswith('.dll') and (dll.startswith('lib') or dll.startswith('_')):
                dlls.append((match.group(), dll))
    return dlls


def save(dlls, output):
    with open(file=output, mode='w') as file:
        file.write('include_dlls = [\n')
        for dll in dlls:
            file.write(f'    {dll},\n')
        file.write(']\n')
        file.close()


def get_dlls_by_pid(pid):
    unzip_listdlls(zip_file=ZIP_FILE, output=ZIP_OUTPUT)
    output = check_output([LISTDLLS_64, f'{pid}']).decode()
    dlls = format_dlls(data=output)
    save(dlls=dlls, output=LOST_DLLS_FILE)
    remove_exe_files()


def get_dlls_by_file(file_txt):
    with open(file=file_txt, mode='r') as f:
        data = f.read()
        f.close()
    dlls = format_dlls(data=data)
    save(dlls=dlls, output=LOST_DLLS_FILE)
    remove_exe_files()


if __name__ == '__main__':
    # get_dlls_by_pid('4320')
    get_dlls_by_file(file_txt=LOST_DLLS_FILE_TXT)
