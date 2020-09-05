# -*- coding: utf-8 -*-
"""Janela de dialogo do tipo salvar arquivo."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./DialogSave.glade')
class DialogSave(Gtk.FileChooserDialog):
    __gtype_name__ = 'DialogSaveFile'

    filter_png = Gtk.Template.Child(name='png_filter')
    filter_python = Gtk.Template.Child(name='python_filter')
    filter_txt = Gtk.Template.Child(name='txt_filter')
    filter_any = Gtk.Template.Child(name='any_filter')

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.set_current_name(name='NomeDoArquivo.txt')
        self._set_filter()

        response = self.run()
        if response == Gtk.ResponseType.OK:
            print(self.get_filename())
            print(self.get_uri())

        # Acessando informações do filtro selecionado.
        dialog_filter = self.get_filter()
        print('\nInformações do filtro selecionado:')
        print(dialog_filter.get_name())
        print(dialog_filter.get_needed())
        print(dialog_filter.to_gvariant())

        self.destroy()

    def _set_filter(self):
        self.filter_png.set_name(name='PNG')
        self.add_filter(self.filter_png)

        self.filter_python.set_name(name='Python')
        self.add_filter(self.filter_python)

        self.filter_txt.set_name(name='TXT')
        self.add_filter(self.filter_txt)

        self.filter_any.set_name(name='Todos')
        self.add_filter(self.filter_any)


if __name__ == '__main__':
    DialogSave()
