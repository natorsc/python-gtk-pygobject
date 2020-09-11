# -*- coding: utf-8 -*-
"""Dialogo para selecionar pasta."""
from pathlib import Path

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./DialogSelectFolder.glade')
class DialogSelectFolder(Gtk.FileChooserDialog):
    __gtype_name__ = 'DialogSelectFolder'

    # Definindo o diretório padrão.
    home = Path.home()

    def __init__(self, select_multiple):
        super().__init__()
        self.select_multiple = select_multiple

        # Defininido se a seleção será multipla ou não
        self.set_select_multiple(select_multiple=self.select_multiple)
        # Pasta onde o diálogo será aberto.
        self.set_current_folder(filename=str(self.home))

        # É obrigatório utilizar ``show_all()``.
        self.show_all()

    def show_file(self):
        if self.select_multiple:
            print('Botão SALVAR pressionado')
            print('CheckBox ESTÁ marcado')
            print(f'Caminho até as pastas: {self.get_filenames()}')
            print(f'URI das pastas: {self.get_uris()}')
        else:
            print('Botão SALVAR pressionado')
            print('CheckBox NÃO está marcado')
            print(f'Caminho até a pasta: {self.get_filename()}')
            print(f'URI da pasta: {self.get_uri()}')


if __name__ == '__main__':
    dialog = DialogSelectFolder()
    response = dialog.run()
    print(response)
    dialog.destroy()
