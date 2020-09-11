# -*- coding: utf-8 -*-
"""Dialogo para salvar arquivo.

Para testar está sendo salvo um arquivo do tipo ``txt`` com um texto
qualquer.
"""
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./DialogSaveFile.glade')
class DialogSaveFile(Gtk.FileChooserDialog):
    __gtype_name__ = 'DialogSaveFile'

    # Definindo o diretório padrão.
    home = Path.home()

    def __init__(self):
        super().__init__()
        # Nome inicial do arquivo.
        self.set_current_name(name='novo-arquivo.txt')
        # Pasta onde o diálogo será aberto.
        self.set_current_folder(filename=str(self.home))

        # Criando e adicionando filtros.
        txt_filter = Gtk.FileFilter()
        txt_filter.set_name(name='txt')
        txt_filter.add_pattern(pattern='.txt')
        txt_filter.add_mime_type(mime_type='text/plain')
        self.add_filter(filter=txt_filter)

        py_filter = Gtk.FileFilter()
        py_filter.set_name(name='python')
        py_filter.add_pattern(pattern='.py')
        py_filter.add_mime_type(mime_type='text/x-python')
        self.add_filter(filter=py_filter)

        all_filter = Gtk.FileFilter()
        all_filter.set_name(name='todos')
        all_filter.add_pattern(pattern='*')
        self.add_filter(filter=all_filter)

        self.show_all()

    def save_file(self):
        print('Botão SALVAR pressionado')
        print(f'Caminho até o arquivo: {self.get_filename()}')
        print(f'URI até o arquivo: {self.get_uri()}')
        file = self.get_filename()
        with open(file=file, mode='w') as f:
            text = 'Olá Mundo.'
            f.write(text)
            f.close()


if __name__ == '__main__':
    dialog = DialogSaveFile()
    response = dialog.run()
    print(response)
    dialog.destroy()
