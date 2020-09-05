# -*- coding: utf-8 -*-
"""Janela de dialogo do tipo salvar arquivo."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


class DialogSave(Gtk.Builder):
    def __init__(self):
        super().__init__()
        self.add_from_file(filename='./DialogSave.glade')

        self.dialog = self.get_object(name='DialogSaveFile')
        # self.dialog.set_current_name(name='NomeDoArquivo.txt')
        # self._set_filter()

        response = self.dialog.run()

        if response == Gtk.ResponseType.OK:
            print(self.dialog.get_filename())
            print(self.dialog.get_uri())

        # Acessando informações do filtro selecionado.
        dialog_filter = self.dialog.get_filter()
        print('\nInformações do filtro selecionado:')
        print(dialog_filter.get_name())
        print(dialog_filter.get_needed())
        print(dialog_filter.to_gvariant())

        self.dialog.destroy()

    def _set_filter(self):
        filter_png = self.get_object(name='filefilter')
        # filter_png.set_name(name='PNG')
        self.dialog.add_filter(filter_png)

        # filter_python = self.get_object(name='python_filter')
        # filter_python.set_name(name='Python')
        # self.dialog.add_filter(filter_python)
        #
        # filter_txt = self.get_object(name='txt_filter')
        # filter_txt.set_name(name='TXT')
        # self.dialog.add_filter(filter_txt)
        #
        # filter_any = self.get_object(name='any_filter')
        # filter_any.set_name(name='Todos')
        # self.dialog.add_filter(filter_any)


if __name__ == '__main__':
    DialogSave()
