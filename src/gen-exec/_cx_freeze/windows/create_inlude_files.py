# -*- coding: utf-8 -*-
"""Script para gerar o arquivo `windows_include_files.py`.

Arquivo `windows_include_files.py` possui as DLLs que foram listadas
com o programa `ListDlls`.
"""


def remove_duplicate_paths(file: str) -> list:
    """Realiza a leitura do arquivo onde estão as bibliotecas ou DLLs e
    remove os itens que são duplicados.

    Args:
        file (str): Caminho ou nome do arquivo que será analisado.
    """
    paths = []
    with open(file=file, mode='r') as file:
        data = file.read()
        [paths.append(path) for path in data.split('\n') if path not in paths]
        file.close()
    return paths


def remove_unnecessary_dlls(paths: list) -> list:
    """Removendo bibliotecas ou Dlls que não são necessárias.

    Args:
        paths (list): Lista contendo o caminho até as bibliotecas ou DLLs.
    """
    dlls = []
    for path in paths:
        dll = path.split('\\')[-1]
        if dll.endswith('.dll') and (dll.startswith('lib') or dll.startswith('_')):
            dlls.append((path, dll))
    return dlls


def save(paths):
    """Criar o arquivo include_files.py.

    Args:
        paths (list): Lista de listas ou tuplas contendo o caminho e
        o nome do arquivo.
    """
    with open(file='include_files.py', mode='w') as file:
        file.write('include_files = [\n')
        for dll in dlls:
            file.write(f'    {dll},\n')
        file.write(']\n')
        file.close()


if __name__ == '__main__':
    path_list = remove_duplicate_paths(file='./dlls.txt')
    dlls = remove_unnecessary_dlls(paths=path_list)
    save(paths=dlls)
