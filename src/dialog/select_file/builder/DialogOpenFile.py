# -*- coding: utf-8 -*-
"""Abrindo o dialogo do tipo abrir aquivo."""

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./DialogOpenFile.glade')
class DialogOpenFile(Gtk.FileChooserDialog):
    __gtype_name__ = 'DialogOpenFile'

    filter_png = Gtk.Template.Child(name='png_filter')
    filter_python = Gtk.Template.Child(name='python_filter')
    filter_txt = Gtk.Template.Child(name='txt_filter')
    filter_any = Gtk.Template.Child(name='any_filter')

    def __init__(self, select_multiple=False):
        super().__init__(select_multiple=select_multiple)
        self._set_filter()

        response = self.run()
        if select_multiple is True:
            if response == Gtk.ResponseType.OK:
                print(f'Caminho até o arquivo: {self.get_filenames()}')
                print(f'URI até o arquivo: {self.get_uris()}')
        else:
            if response == Gtk.ResponseType.OK:
                print(self.get_filename())
                print(self.get_uri())

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
    dialog = DialogOpenFile()
