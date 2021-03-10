# -*- coding: utf-8 -*-
"""Python e GTK: Como criar um executável com Cx_Freeze no Windows.

Script para tratar os dados fornecidos pelo ListDLLs.
"""

from os.path import isfile
from re import compile
from subprocess import check_output
from urllib.request import urlretrieve
from zipfile import ZipFile


def extract_listdlls(filename):
    """Não utilizar.

    Falta testar.
    """
    zip_file = ZipFile(file=filename)
    zip_file.extractall(path='.')
    zip_file.close()


def config_listdlls():
    """Não utilizar.

    Falta testar.
    """
    filename = 'ListDlls.zip'
    if not isfile(filename):
        url = 'https://download.sysinternals.com/files/ListDlls.zip'
        urlretrieve(url, filename=filename)
    extract_listdlls(filename=filename)


def save(dlls: list):
    """Métudo criar o arquivo `include_files.py`.

    Depois arquivo pode ser importado no script `setup.py`.

    Args:
        dlls (list): Lista de listas ou lista de tuplas contendo o
        caminho (path) até a DLL e o nome da DLL.
    """
    with open(file='include_files.py', mode='w') as file:
        file.write('include_files = [\n')
        for dll in dlls:
            file.write(f'    {dll},\n')
        file.write(']\n')
        file.close()


def format_dlls(output: str) -> list:
    """Função faz o tratamento dos dados que são fornecidos pelo
    ListDLLs.

    Args:
        output (str): Texto contendo as informações que foram geradas
        pelo ListDLLs.

    Returns:
        list: Lista de tuplas, onde a tupla tem a seguinte formatação:
        (dll_path, dll_name).
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


def make_include_files_by_pid(pid: str):
    def format_dlls(output: str) -> list:
        """Método cria o arquivo `include_files.py` utilizando o
        ListDLLs e o PID do processo que está em execução.

        Args:
            pid (str | int): Valor faz referencia ao processo que está
            em execução e é obrigatório que o processo esteja em
            execução!
        """

    output = check_output(['Listdlls64.exe', f'{pid}']).decode()
    dlls = format_dlls(output=output)
    save(dlls=dlls)


def make_include_files_by_file(file: str):
    """Método cria o arquivo `include_files.py` utilizando um arquivo
    de texto que contenha os dados gerados pelo ListDLLs.

    Args:
        file (str): Caminho (path) até o arquivo que será lido.
    """
    file = open(file=file, mode='r')
    output = file.read()
    file.close()
    dlls = format_dlls(output=output)
    save(dlls=dlls)


if __name__ == '__main__':
    file = './dlls.txt'
    make_include_files_by_file(file=file)
    # pid = ''
    # make_include_files_by_pid(pid=pid)
