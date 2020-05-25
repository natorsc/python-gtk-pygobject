# -*- coding: utf-8 -*-
"""Script para gerar o arquivo `windows_include_files.py`.

Arquivo `windows_include_files.py` possui as DLLs que foram listadas
com o programa `ListDlls`.
"""


def remove_duplicate_paths():
    """Realiza a leitura do arquivo onde estão as DLLs que foram
    localizadas pelo programa `Listdlls.exe`.
    """
    paths = []
    with open(file='dlls.txt', mode='r') as f:
        data = f.read()
        [paths.append(path) for path in data.split('\n') if path not in paths]
        f.close()
    return paths


def remove_unnecessary_dlls(paths):
    """Removendo dlls que não precisam ser copiadas."""
    dlls = []
    for path in paths:
        dll = path.split('\\')[-1]
        if dll.endswith('.dll') and (dll.startswith('lib') or dll.startswith('_')):
            dlls.append((path.replace('\\', '/'), dll))
    return dlls


if __name__ == '__main__':
    paths = remove_duplicate_paths()
    dlls = remove_unnecessary_dlls(paths=paths)

    # Salvando o arquivo que será importado no `setup.py`.
    with open(file='windows_include_files.py', mode='w') as f:
        f.write('include_files = [\n')
        for dll in dlls:
            f.write(f'    {dll},\n')
        f.write(']')
        f.close()
