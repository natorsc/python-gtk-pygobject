# -*- coding: utf-8 -*-
"""Dialogo para selecionar arquivo."""
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./DialogSelectFile.glade')
class DialogSelectFile(Gtk.FileChooserDialog):
    __gtype_name__ = 'DialogSelectFile'

    # Definindo o diretório padrão.
    home = Path.home()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.select_multiple = kwargs['select_multiple']

        # Defininido se a seleção será multipla ou não
        self.set_select_multiple(select_multiple=self.select_multiple)
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

        # É obrigatório utilizar ``show_all()``.
        self.show_all()

    def show_file(self):
        if self.select_multiple:
            print('Botão SALVAR pressionado')
            print('CheckBox ESTÁ marcado')
            print(f'Caminho até os arquivos: {self.get_filenames()}')
            print(f'URI dos arquivos: {self.get_uris()}')
        else:
            print('Botão SALVAR pressionado')
            print('CheckBox NÃO está marcado')
            print(f'Caminho até o arquivo: {self.get_filename()}')
            print(f'URI do arquivo: {self.get_uri()}')


if __name__ == '__main__':
    dialog = DialogSelectFile()
    response = dialog.run()
    print(response)
    dialog.destroy()
