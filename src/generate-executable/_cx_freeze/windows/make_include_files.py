# -*- coding: utf-8 -*-
"""Python e GTK: Como criar um executável com Cx_Freeze no Windows.

Script para tratar os dados fornecidos pelo ListDLLs.
"""

import os
from re import compile
from subprocess import check_output
from typing import Union, List, Tuple
from urllib.request import urlretrieve
from zipfile import ZipFile


def format_dlls(output: str) -> List[Tuple[str, str]]:
    """Função faz o tratamento dos dados que são fornecidos pelo
    ``Listdlls64.exe`` ou ``Listdlls.exe``.

    Args:
        output (str): Texto contendo as informações que foram geradas
        pelo Listdlls.

    Returns:
        list: Lista de tuplas contendo o caminho (path) até a ``dll`` e
        o nome da ``dll``.
    """
    lines = output.splitlines()
    regex = compile(r'C:\\.*')

    dlls = []
    for line in lines:
        match = regex.search(line)
        if match:
            dll = match.group().split('\\')[-1]
            if dll.endswith('.dll') and (dll.startswith('lib') or dll.startswith('_')):
                dlls.append((match.group(), dll))
    return dlls


def extract_listdlls(file_path: str, path: str) -> None:
    """Método extrais os executáveis contidos no arquivvo `ListDlls.zip`.

    Args:
        file_path (str): Caminho (path) até o arquivo que será
        descompactado.
        path (str): Diretório onde o arquivo será descompactado.
    """
    zip_file = ZipFile(file=file_path)
    zip_file.extractall(path=path)
    zip_file.close()


def download_listdlls(file_path) -> None:
    """Método realiza o download do ListDlls caso o mesmo não exista.

    Args:
        file_path (str): Local onde o arquivos será salvo, o mesmo
        já inclui o nome com que o arquivo será salvo.
    """
    if not os.path.isfile(file_path):
        url = 'https://download.sysinternals.com/files/ListDlls.zip'
        urlretrieve(url, file_path)


def save(dlls: list, filename: str, path: str) -> None:
    """Método criar o arquivo ``include_files.py``.

    Posteriormente o arquivo gerado deverá ser importado no
    arquivo `setup.py`.

    Args:
        dlls (list): Lista tuplas contendo o caminho (path) até a
        ``dll`` e o nome da ``dll``.
        path (str): Diretório onde o arquivo será criado.
        filename (str): Nome do arquivo que será criado.
    """
    file_path = os.path.join(path, filename)
    with open(file=file_path, mode='w') as file:
        file.write('include_files = [\n')
        for dll in dlls:
            file.write(f'    {dll},\n')
        file.write(']\n')
        file.close()


def remove_listdlls_files(path: str, remove_files: tuple) -> None:
    """Método remove os arquivos que foram descompactados do
    arquivo ``ListDlls.zip``.

    Args:
        path (str): Diretório onde estão os arquivos.
        remove_files (tuple): Tupla contendo o nome dos arquivos que
        serão removidos.
    """
    for file in remove_files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)


def make_include_files_by_pid(
        pid: Union[int, str],
        executable: str = 'Listdlls64.exe',
        filename='include_files.py',
        path: str = '.',
        remove_files: tuple = ('Eula.txt', 'Listdlls.exe', 'Listdlls64.exe'),
        zipped_file: str = 'ListDlls.zip'):
    """Método cria o arquivo `include_files.py` utilizando o Listdlls
    e o **PID** do processo que está em execução.

    Args:
        pid (int | str): Valor do processo que está em execução.
        executable (str): Nome do executável que será utilizado.
        filename (str): Nome do arquivo que será gerado.
        path (str): Diretório onde os arquivos serão criados.
        remove_files (tuple): Tupla contendo o nome dos arquivos que
        serão removidos após gerar o arquivo ``include_files.py``.
        zipped_file (str): Nome do arquivo que será descompactado.
    """
    zipped_file_path = os.path.join(path, zipped_file)
    executable_path = os.path.join(path, executable)

    download_listdlls(file_path=zipped_file_path)
    extract_listdlls(file_path=zipped_file_path, path=path)
    output = check_output([executable_path, f'{pid}']).decode()
    dlls = format_dlls(output=output)
    save(dlls=dlls, filename=filename, path=path)
    remove_listdlls_files(path=path, remove_files=remove_files)


def make_include_files_by_file(
        filename: str = 'include_files.py',
        file_path: str = 'dlls.txt',
        path: str = '.',
        remove_files: tuple = ('Eula.txt', 'Listdlls.exe', 'Listdlls64.exe')
):
    """Método cria o arquivo `include_files.py` utilizando um arquivo
    de texto que contenha os dados gerados pelo ListDLLs.

    Args:
        filename (str): Nome do arquivo que será gerado.
        file_path (str): Caminho (path) até o arquivo que será lido.
        path (str): Diretório onde os arquivos serão criados.
        remove_files (tuple): Tupla contendo o nome dos arquivos que
        serão removidos após gerar o arquivo ``include_files.py``.
    """
    file = open(file=file_path, mode='r')
    output = file.read()
    file.close()
    dlls = format_dlls(output=output)
    save(dlls=dlls, filename=filename, path=path)
    remove_listdlls_files(path=path, remove_files=remove_files)


if __name__ == '__main__':
    # make_include_files_by_file()
    pid = ''
    make_include_files_by_pid(pid=pid)
    pass
